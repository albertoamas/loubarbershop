"""
Rutas para Barberos - Low Barber
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from app.models import User, Barber, UserRole, db
from app.schemas.barber_schemas import (
    barber_create_schema,
    barber_update_schema,
    barber_response_schema,
    barbers_response_schema
)
from app.utils.auth_utils import (
    get_current_user,
    format_validation_errors,
    admin_required
)

# Crear blueprint para barberos
barbers_bp = Blueprint('barbers', __name__)

@barbers_bp.route('', methods=['GET'])
def get_barbers():
    """Obtener todos los barberos activos"""
    try:
        # Parámetros opcionales
        status = request.args.get('status')  # Para filtro ?status=active
        
        # Construir query
        query = Barber.query
        
        # Filtrar por estado si se especifica
        if status == 'active':
            query = query.filter_by(disponible=True, activo=True)
        else:
            # Solo barberos disponibles para usuarios normales
            query = query.filter_by(disponible=True)
        
        barbers = query.all()
        
        # Mapear barberos con información completa
        barbers_data = []
        for barber in barbers:
            barber_dict = barber_response_schema.dump(barber)
            barbers_data.append(barber_dict)
        
        return jsonify({
            'message': 'Barberos obtenidos exitosamente',
            'data': barbers_data,
            'barbers': barbers_data,  # Para compatibilidad
            'total': len(barbers_data)
        }), 200
        
    except Exception as e:
        print(f"Error en get_barbers: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@barbers_bp.route('', methods=['POST'])
@jwt_required()
@admin_required
def create_barber():
    """Crear un nuevo barbero (solo admins)"""
    try:
        # Validar datos
        data = barber_create_schema.load(request.json)
        
        # Validar que las contraseñas coincidan
        if data['password'] != data['password_confirmation']:
            return jsonify({
                'error': 'Datos de entrada inválidos',
                'details': {'password_confirmation': ['Las contraseñas no coinciden.']}
            }), 400
        
        # Crear usuario para el barbero
        user = User(
            nombre=data['nombre'],
            email=data['email'],
            password=data['password'],
            telefono=data.get('telefono'),
            rol=UserRole.BARBERO
        )
        
        db.session.add(user)
        db.session.flush()  # Para obtener el ID del usuario
        
        # Crear barbero
        barber = Barber(
            nombre=data['nombre'],
            user_id=user.id,
            especialidad=data['especialidad'],
            disponible=data.get('disponible', True)
        )
        
        db.session.add(barber)
        db.session.commit()
        
        return jsonify({
            'message': 'Barbero creado exitosamente',
            'barber': barber_response_schema.dump(barber)
        }), 201
        
    except ValidationError as e:
        return jsonify({
            'error': 'Datos de entrada inválidos',
            'details': format_validation_errors(e.messages)
        }), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@barbers_bp.route('/<string:barber_id>', methods=['GET'])
def get_barber(barber_id):
    """Obtener un barbero específico"""
    try:
        barber = Barber.query.get_or_404(barber_id)
        
        return jsonify({
            'message': 'Barbero obtenido exitosamente',
            'barber': barber_response_schema.dump(barber)
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Barbero no encontrado',
            'message': str(e)
        }), 404

@barbers_bp.route('/<string:barber_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_barber(barber_id):
    """Actualizar un barbero (solo admins)"""
    try:
        barber = Barber.query.get_or_404(barber_id)
        
        # Validar datos
        data = barber_update_schema.load(request.json)
        
        # Actualizar campos del barbero
        if 'especialidad' in data:
            barber.especialidad = data['especialidad']
        if 'disponible' in data:
            barber.disponible = data['disponible']
        if 'activo' in data:
            barber.activo = data['activo']
            
        # Actualizar campos del usuario asociado
        if 'nombre' in data:
            barber.usuario.nombre = data['nombre']
        if 'telefono' in data:
            barber.usuario.telefono = data['telefono']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Barbero actualizado exitosamente',
            'barber': barber_response_schema.dump(barber)
        }), 200
        
    except ValidationError as e:
        return jsonify({
            'error': 'Datos de entrada inválidos',
            'details': format_validation_errors(e.messages)
        }), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@barbers_bp.route('/<string:barber_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_barber(barber_id):
    """Eliminar un barbero (solo admins)"""
    try:
        barber = Barber.query.get_or_404(barber_id)
        
        # Marcar como no disponible en lugar de eliminar
        barber.disponible = False
        barber.usuario.activo = False
        
        db.session.commit()
        
        return jsonify({
            'message': 'Barbero desactivado exitosamente'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@barbers_bp.route('/availability/<string:barber_id>', methods=['GET'])
def get_barber_availability(barber_id):
    """Obtener disponibilidad de un barbero específico"""
    try:
        barber = Barber.query.get_or_404(barber_id)
        
        if not barber.disponible:
            return jsonify({
                'error': 'Barbero no disponible',
                'message': 'Este barbero no está disponible actualmente'
            }), 400
        
        # TODO: Implementar lógica de disponibilidad basada en reservas
        # Por ahora, devolvemos disponible
        
        return jsonify({
            'message': 'Disponibilidad obtenida exitosamente',
            'barber_id': barber_id,
            'available': True,
            'next_available_slot': None  # TODO: calcular próximo slot disponible
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500
