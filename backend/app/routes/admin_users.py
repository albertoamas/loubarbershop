"""
Rutas administrativas para gestión de usuarios
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from app.models import User, UserRole, db
from app.schemas.auth_schemas import user_profile_schema
from app.utils.auth_utils import admin_required
from sqlalchemy import func, or_

# Crear blueprint para administración de usuarios
admin_users_bp = Blueprint('admin_users', __name__, url_prefix='/api/admin/users')

@admin_users_bp.route('', methods=['GET'])
@jwt_required()
@admin_required
def get_all_users():
    """Obtener todos los usuarios (solo admins)"""
    try:
        # Parámetros de filtro opcionales
        role_filter = request.args.get('role')
        status_filter = request.args.get('status')  # active/inactive
        search = request.args.get('search')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 25))
        
        # Construir query base
        query = User.query
        
        # Aplicar filtros
        if role_filter:
            try:
                role_enum = UserRole(role_filter)
                query = query.filter(User.rol == role_enum)
            except ValueError:
                pass  # Ignorar valores de rol inválidos
        
        if status_filter:
            if status_filter == 'active':
                query = query.filter(User.activo == True)
            elif status_filter == 'inactive':
                query = query.filter(User.activo == False)
        
        if search:
            query = query.filter(
                or_(
                    User.nombre.ilike(f'%{search}%'),
                    User.email.ilike(f'%{search}%'),
                    User.telefono.ilike(f'%{search}%')
                )
            )
        
        # Ordenar por fecha de creación (más recientes primero)
        query = query.order_by(User.created_at.desc())
        
        # Paginación
        paginated = query.paginate(page=page, per_page=per_page, error_out=False)
        
        # Convertir a diccionarios
        users_data = []
        for user in paginated.items:
            user_dict = user.to_dict()
            # Agregar información adicional
            user_dict['reservations_count'] = len(user.get_reservas()) if hasattr(user, 'get_reservas') else 0
            users_data.append(user_dict)
        
        return jsonify({
            'users': users_data,
            'total': paginated.total,
            'page': page,
            'per_page': per_page,
            'pages': paginated.pages,
            'has_next': paginated.has_next,
            'has_prev': paginated.has_prev,
            'message': 'Usuarios obtenidos exitosamente'
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error al obtener usuarios',
            'message': str(e)
        }), 500

@admin_users_bp.route('/stats', methods=['GET'])
@jwt_required()
@admin_required
def get_users_stats():
    """Obtener estadísticas de usuarios"""
    try:
        # Contar usuarios por rol
        total_users = User.query.count()
        total_clients = User.query.filter(User.rol == UserRole.CLIENTE).count()
        total_barbers = User.query.filter(User.rol == UserRole.BARBERO).count()
        total_admins = User.query.filter(User.rol == UserRole.ADMIN).count()
        
        # Usuarios activos
        active_users = User.query.filter(User.activo == True).count()
        
        # Usuarios nuevos este mes
        from datetime import datetime
        current_month = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        new_this_month = User.query.filter(User.created_at >= current_month).count()
        
        # Usuarios con email verificado
        verified_emails = User.query.filter(User.email_verificado == True).count()
        
        return jsonify({
            'totalUsers': total_users,
            'totalClients': total_clients,
            'totalBarbers': total_barbers,
            'totalAdmins': total_admins,
            'activeToday': active_users,  # Por simplicidad, usamos usuarios activos
            'activeUsers': active_users,
            'newThisMonth': new_this_month,
            'verifiedEmails': verified_emails,
            'message': 'Estadísticas obtenidas exitosamente'
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error al obtener estadísticas',
            'message': str(e)
        }), 500

@admin_users_bp.route('/<user_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_user(user_id):
    """Actualizar usuario (solo admins)"""
    try:
        # Buscar usuario
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        data = request.json
        
        # Actualizar campos permitidos
        if 'nombre' in data:
            user.nombre = data['nombre']
        
        if 'email' in data:
            # Verificar que el email no esté en uso por otro usuario
            existing_user = User.query.filter(User.email == data['email'], User.id != user_id).first()
            if existing_user:
                return jsonify({'error': 'El email ya está en uso'}), 400
            user.email = data['email']
        
        if 'telefono' in data:
            user.telefono = data['telefono']
        
        if 'rol' in data:
            try:
                user.rol = UserRole(data['rol'])
            except ValueError:
                return jsonify({'error': 'Rol inválido'}), 400
        
        # Guardar cambios
        db.session.commit()
        
        return jsonify({
            'user': user.to_dict(),
            'message': 'Usuario actualizado exitosamente'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error al actualizar usuario',
            'message': str(e)
        }), 500

@admin_users_bp.route('/<user_id>/status', methods=['PUT'])
@jwt_required()
@admin_required
def update_user_status(user_id):
    """Actualizar estado de usuario"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        data = request.json
        if 'activo' not in data:
            return jsonify({'error': 'Campo activo requerido'}), 400
        
        user.activo = bool(data['activo'])
        db.session.commit()
        
        return jsonify({
            'user': user.to_dict(),
            'message': f'Usuario {"activado" if user.activo else "desactivado"} exitosamente'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error al actualizar estado',
            'message': str(e)
        }), 500

@admin_users_bp.route('/bulk/status', methods=['PUT'])
@jwt_required()
@admin_required
def bulk_update_status():
    """Actualización masiva de estado"""
    try:
        data = request.json
        user_ids = data.get('userIds', [])
        activo = data.get('activo', True)
        
        if not user_ids:
            return jsonify({'error': 'Lista de IDs de usuarios requerida'}), 400
        
        # Actualizar usuarios
        updated_count = User.query.filter(User.id.in_(user_ids)).update(
            {User.activo: activo},
            synchronize_session=False
        )
        
        db.session.commit()
        
        return jsonify({
            'updated_count': updated_count,
            'message': f'{updated_count} usuarios {"activados" if activo else "desactivados"} exitosamente'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error en actualización masiva de estado',
            'message': str(e)
        }), 500

@admin_users_bp.route('/bulk/role', methods=['PUT'])
@jwt_required()
@admin_required
def bulk_update_role():
    """Actualización masiva de rol"""
    try:
        data = request.json
        user_ids = data.get('userIds', [])
        new_role = data.get('rol')
        
        if not user_ids:
            return jsonify({'error': 'Lista de IDs de usuarios requerida'}), 400
        
        if not new_role:
            return jsonify({'error': 'Nuevo rol requerido'}), 400
        
        # Validar rol
        try:
            role_enum = UserRole(new_role)
        except ValueError:
            return jsonify({'error': 'Rol inválido'}), 400
        
        # Actualizar usuarios
        updated_count = User.query.filter(User.id.in_(user_ids)).update(
            {User.rol: role_enum},
            synchronize_session=False
        )
        
        db.session.commit()
        
        return jsonify({
            'updated_count': updated_count,
            'message': f'{updated_count} usuarios actualizados a rol {new_role} exitosamente'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error en actualización masiva de rol',
            'message': str(e)
        }), 500

@admin_users_bp.route('/<user_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_user(user_id):
    """Eliminar usuario (solo admins)"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        # No permitir eliminar al usuario actual
        current_user_id = get_jwt_identity()
        if str(user.id) == str(current_user_id):
            return jsonify({'error': 'No puedes eliminar tu propia cuenta'}), 400
        
        # No permitir eliminar el último admin
        if user.rol == UserRole.ADMIN:
            admin_count = User.query.filter(User.rol == UserRole.ADMIN).count()
            if admin_count <= 1:
                return jsonify({'error': 'No se puede eliminar el último administrador'}), 400
        
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({
            'message': 'Usuario eliminado exitosamente'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error al eliminar usuario',
            'message': str(e)
        }), 500
