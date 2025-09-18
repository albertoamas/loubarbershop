"""
Utilidades para autenticación y autorización
"""

from functools import wraps
from flask import jsonify, current_app
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from app.models import User, UserRole

def token_required(f):
    """Decorador para rutas que requieren token JWT"""
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({
                'error': 'Token inválido',
                'message': 'Se requiere un token de acceso válido'
            }), 401
    return decorated

def admin_required(f):
    """Decorador para rutas que requieren rol de administrador"""
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            verify_jwt_in_request()
            current_user_id = get_jwt_identity()
            user = User.find_by_id(current_user_id)
            
            if not user or user.rol != UserRole.ADMIN:
                return jsonify({
                    'error': 'Acceso denegado',
                    'message': 'Se requieren permisos de administrador'
                }), 403
            
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({
                'error': 'Token inválido',
                'message': 'Se requiere un token de acceso válido'
            }), 401
    return decorated

def barber_or_admin_required(f):
    """Decorador para rutas que requieren rol de barbero o administrador"""
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            verify_jwt_in_request()
            current_user_id = get_jwt_identity()
            user = User.find_by_id(current_user_id)
            
            if not user or user.rol not in [UserRole.BARBERO, UserRole.ADMIN]:
                return jsonify({
                    'error': 'Acceso denegado',
                    'message': 'Se requieren permisos de barbero o administrador'
                }), 403
            
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({
                'error': 'Token inválido',
                'message': 'Se requiere un token de acceso válido'
            }), 401
    return decorated

def get_current_user():
    """Obtiene el usuario actual desde el token JWT"""
    try:
        current_user_id = get_jwt_identity()
        
        if not current_user_id:
            return None
            
        user = User.find_by_id(current_user_id)
        return user
    except Exception as e:
        return None

def check_user_permission(user_id, required_role=None):
    """Verifica si el usuario actual tiene permisos para acceder a un recurso"""
    current_user = get_current_user()
    
    if not current_user:
        return False, "Usuario no autenticado"
    
    # Los administradores pueden acceder a todo
    if current_user.rol == UserRole.ADMIN:
        return True, "Acceso autorizado"
    
    # Si se especifica un rol requerido, verificarlo
    if required_role and current_user.rol != required_role:
        return False, f"Se requiere rol de {required_role.value}"
    
    # Los usuarios solo pueden acceder a sus propios recursos
    if str(current_user.id) != str(user_id):
        return False, "Solo puedes acceder a tus propios recursos"
    
    return True, "Acceso autorizado"

def format_validation_errors(errors):
    """Formatea los errores de validación de Marshmallow"""
    formatted_errors = {}
    for field, messages in errors.items():
        if isinstance(messages, list):
            formatted_errors[field] = messages[0] if messages else "Error de validación"
        else:
            formatted_errors[field] = str(messages)
    return formatted_errors
