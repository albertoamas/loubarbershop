"""
Rutas de autenticación para la aplicación Low Barber
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token,
    get_jwt_identity,
    jwt_required
)
from marshmallow import ValidationError
from app.models import User, UserRole, db
from app.schemas.auth_schemas import (
    user_registration_schema,
    user_login_schema,
    user_profile_schema,
    user_update_schema,
    change_password_schema
)
from app.utils.auth_utils import (
    token_required,
    get_current_user,
    format_validation_errors
)

# Crear blueprint para autenticación
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    """Registro de nuevos usuarios"""
    try:
        # Validar datos de entrada
        data = user_registration_schema.load(request.json)
        
        # Verificar que el email no esté en uso
        if User.find_by_email(data['email']):
            return jsonify({
                'error': 'Email ya registrado',
                'message': 'Este email ya está en uso'
            }), 400
        
        # Crear nuevo usuario
        user = User(
            nombre=data['nombre'],
            email=data['email'],
            password=data['password'],
            telefono=data.get('telefono'),
            rol=UserRole(data.get('rol', UserRole.CLIENTE.value))
        )
        
        # Guardar en la base de datos
        user.save()
        
        # Crear tokens con el rol incluido
        additional_claims = {'rol': user.rol.value}
        access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
        refresh_token = create_refresh_token(identity=str(user.id))
        
        return jsonify({
            'message': 'Usuario registrado exitosamente',
            'user': user_profile_schema.dump(user),
            'access_token': access_token,
            'refresh_token': refresh_token
        }), 201
        
    except ValidationError as e:
        return jsonify({
            'error': 'Datos inválidos',
            'validation_errors': format_validation_errors(e.messages)
        }), 400
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    """Inicio de sesión de usuarios"""
    try:
        # Validar datos de entrada
        data = user_login_schema.load(request.json)
        
        # Buscar usuario por email
        user = User.find_by_email(data['email'])
        
        if not user or not user.check_password(data['password']):
            return jsonify({
                'error': 'Credenciales inválidas',
                'message': 'Email o contraseña incorrectos'
            }), 401
        
        # Verificar que el usuario esté activo
        if not user.activo:
            return jsonify({
                'error': 'Cuenta desactivada',
                'message': 'Tu cuenta ha sido desactivada. Contacta al administrador.'
            }), 401
        
        # Crear tokens con el rol incluido
        additional_claims = {'rol': user.rol.value}
        access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
        refresh_token = create_refresh_token(identity=str(user.id))
        
        return jsonify({
            'message': 'Inicio de sesión exitoso',
            'user': user_profile_schema.dump(user),
            'access_token': access_token,
            'refresh_token': refresh_token
        }), 200
        
    except ValidationError as e:
        return jsonify({
            'error': 'Datos inválidos',
            'validation_errors': format_validation_errors(e.messages)
        }), 400
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """Renovar token de acceso"""
    try:
        current_user_id = get_jwt_identity()
        user = User.find_by_id(current_user_id)
        
        if not user or not user.activo:
            return jsonify({
                'error': 'Usuario no válido',
                'message': 'No se puede renovar el token'
            }), 401
        
        # Crear nuevo token de acceso con el rol incluido
        additional_claims = {'rol': user.rol.value}
        access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
        
        return jsonify({
            'access_token': access_token
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@auth_bp.route('/profile', methods=['GET'])
@token_required
def get_profile():
    """Obtener perfil del usuario actual"""
    try:
        user = get_current_user()
        
        if not user:
            return jsonify({
                'error': 'Usuario no encontrado',
                'message': 'No se pudo obtener el perfil del usuario'
            }), 404
        
        return jsonify({
            'user': user_profile_schema.dump(user)
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@auth_bp.route('/profile', methods=['PUT'])
@token_required
def update_profile():
    """Actualizar perfil del usuario actual"""
    try:
        user = get_current_user()
        
        if not user:
            return jsonify({
                'error': 'Usuario no encontrado',
                'message': 'No se pudo encontrar el usuario'
            }), 404
        
        # Validar datos de entrada
        data = user_update_schema.load(request.json)
        
        # Actualizar campos
        if 'nombre' in data:
            user.nombre = data['nombre']
        if 'telefono' in data:
            user.telefono = data['telefono']
        
        # Guardar cambios
        user.save()
        
        return jsonify({
            'message': 'Perfil actualizado exitosamente',
            'user': user_profile_schema.dump(user)
        }), 200
        
    except ValidationError as e:
        return jsonify({
            'error': 'Datos inválidos',
            'validation_errors': format_validation_errors(e.messages)
        }), 400
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@auth_bp.route('/change-password', methods=['POST'])
@token_required
def change_password():
    """Cambiar contraseña del usuario actual"""
    try:
        user = get_current_user()
        
        if not user:
            return jsonify({
                'error': 'Usuario no encontrado',
                'message': 'No se pudo encontrar el usuario'
            }), 404
        
        # Validar datos de entrada
        data = change_password_schema.load(request.json)
        
        # Verificar contraseña actual
        if not user.check_password(data['current_password']):
            return jsonify({
                'error': 'Contraseña incorrecta',
                'message': 'La contraseña actual es incorrecta'
            }), 400
        
        # Actualizar contraseña
        user.set_password(data['new_password'])
        user.save()
        
        return jsonify({
            'message': 'Contraseña actualizada exitosamente'
        }), 200
        
    except ValidationError as e:
        return jsonify({
            'error': 'Datos inválidos',
            'validation_errors': format_validation_errors(e.messages)
        }), 400
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@auth_bp.route('/logout', methods=['POST'])
@token_required
def logout():
    """Cerrar sesión (placeholder - JWT es stateless)"""
    return jsonify({
        'message': 'Sesión cerrada exitosamente'
    }), 200

@auth_bp.route('/test', methods=['GET'])
def test_auth():
    """Endpoint de prueba para autenticación"""
    return jsonify({
        'message': 'Sistema de autenticación funcionando',
        'endpoints': {
            'register': 'POST /api/auth/register',
            'login': 'POST /api/auth/login',
            'profile': 'GET /api/auth/profile (requiere token)',
            'refresh': 'POST /api/auth/refresh (requiere refresh token)',
            'make-admin': 'POST /api/auth/make-admin (requiere token)'
        },
        'test_data': {
            'register_example': {
                'nombre': 'Juan Pérez',
                'email': 'juan@test.com',
                'password': '123456',
                'password_confirmation': '123456',
                'rol': 'cliente'
            },
            'login_example': {
                'email': 'juan@test.com',
                'password': '123456'
            }
        }
    }), 200

@auth_bp.route('/make-admin', methods=['POST'])
@jwt_required()
def make_admin():
    """Convertir el usuario actual en administrador (solo para desarrollo)"""
    try:
        current_user_id = get_jwt_identity()
        user = User.find_by_id(current_user_id)
        
        if not user:
            return jsonify({
                'error': 'Usuario no encontrado',
                'message': 'El usuario actual no existe'
            }), 404
        
        # Cambiar rol a admin
        user.rol = UserRole.ADMIN
        db.session.commit()
        
        return jsonify({
            'message': 'Usuario convertido a administrador exitosamente',
            'user': {
                'id': str(user.id),
                'nombre': user.nombre,
                'email': user.email,
                'rol': user.rol.value
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@auth_bp.route('/create-admin', methods=['POST'])
def create_admin():
    """Crear administrador de prueba para desarrollo"""
    try:
        # Verificar si ya existe un admin
        existing_admin = User.query.filter_by(email='admin@lowbarber.com').first()
        if existing_admin:
            return jsonify({
                'message': 'Administrador ya existe',
                'user': {
                    'id': str(existing_admin.id),
                    'nombre': existing_admin.nombre,
                    'email': existing_admin.email,
                    'rol': existing_admin.rol.value
                }
            }), 200
        
        # Crear nuevo administrador
        admin_user = User(
            nombre='Administrador',
            email='admin@lowbarber.com',
            password='admin123',  # En producción usar hash seguro
            telefono='+1234567890',
            rol=UserRole.ADMIN,
            activo=True
        )
        
        db.session.add(admin_user)
        db.session.commit()
        
        # Crear token de acceso con el rol incluido
        additional_claims = {'rol': admin_user.rol.value}
        access_token = create_access_token(identity=str(admin_user.id), additional_claims=additional_claims)
        refresh_token = create_refresh_token(identity=str(admin_user.id))
        
        return jsonify({
            'message': 'Administrador creado exitosamente',
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': {
                'id': str(admin_user.id),
                'nombre': admin_user.nombre,
                'email': admin_user.email,
                'telefono': admin_user.telefono,
                'rol': admin_user.rol.value,
                'activo': admin_user.activo
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error creando administrador',
            'message': str(e)
        }), 500

@auth_bp.route('/force-admin-login', methods=['POST'])
def force_admin_login():
    """Forzar creación y login de admin para debug"""
    try:
        # Eliminar admin existente si hay uno
        existing_admin = User.query.filter_by(email='admin@lowbarber.com').first()
        if existing_admin:
            db.session.delete(existing_admin)
            db.session.commit()
            
        # Crear nuevo administrador
        admin_user = User(
            nombre='Admin Sistema',
            email='admin@lowbarber.com',
            password='admin123',
            telefono='+57 300 000 0001',
            rol=UserRole.ADMIN
        )
        admin_user.activo = True
        admin_user.email_verificado = True
        
        db.session.add(admin_user)
        db.session.commit()
        
        # Crear token de acceso con el rol incluido
        additional_claims = {'rol': admin_user.rol.value}
        access_token = create_access_token(identity=str(admin_user.id), additional_claims=additional_claims)
        refresh_token = create_refresh_token(identity=str(admin_user.id))
        
        return jsonify({
            'message': 'Admin creado y autenticado',
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': {
                'id': str(admin_user.id),
                'nombre': admin_user.nombre,
                'email': admin_user.email,
                'telefono': admin_user.telefono,
                'rol': admin_user.rol.value,
                'activo': admin_user.activo,
                'email_verificado': admin_user.email_verificado
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error forzando admin login',
            'message': str(e)
        }), 500
