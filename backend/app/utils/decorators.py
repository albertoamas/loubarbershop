"""
Decoradores de autenticación y utilidades - Low Barber
"""

from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from app.models import User, UserRole

def admin_required(f):
    """Decorador que requiere rol de administrador"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = User.query.get(current_user_id)
        
        if not current_user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        if current_user.rol != UserRole.ADMIN:
            return jsonify({'error': 'Se requieren permisos de administrador'}), 403
        
        return f(*args, **kwargs)
    return decorated_function

def barbero_required(f):
    """Decorador que requiere rol de barbero o admin"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = User.query.get(current_user_id)
        
        if not current_user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        if current_user.rol not in [UserRole.BARBERO, UserRole.ADMIN]:
            return jsonify({'error': 'Se requieren permisos de barbero o administrador'}), 403
        
        return f(*args, **kwargs)
    return decorated_function

def get_current_user():
    """Obtiene el usuario actual basado en el JWT"""
    current_user_id = get_jwt_identity()
    if not current_user_id:
        return None
    
    return User.query.get(current_user_id)
