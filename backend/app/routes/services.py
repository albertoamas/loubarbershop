"""
Rutas para Servicios - Low Barber
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from app.models import Service, db
from app.schemas.service_schemas import (
    service_create_schema,
    service_update_schema,
    service_response_schema,
    services_response_schema
)
from app.utils.auth_utils import (
    get_current_user,
    format_validation_errors,
    admin_required
)

# Crear blueprint para servicios
services_bp = Blueprint('services', __name__, url_prefix='/api/services')

@services_bp.route('', methods=['GET'])
def get_services():
    """Obtener todos los servicios (activos e inactivos para admin, solo activos para clientes)"""
    try:
        # Verificar si el usuario es administrador
        from flask_jwt_extended import verify_jwt_in_request, get_jwt
        
        is_admin = False
        try:
            verify_jwt_in_request(optional=True)
            claims = get_jwt()
            is_admin = claims.get('rol') == 'admin' if claims else False
        except:
            is_admin = False
        
        # Admins ven todos los servicios, usuarios públicos solo activos
        if is_admin:
            services = Service.query.all()
        else:
            services = Service.query.filter_by(activo=True).all()
        
        return jsonify({
            'message': 'Servicios obtenidos exitosamente',
            'services': services_response_schema.dump(services),
            'total': len(services)
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@services_bp.route('', methods=['POST'])
@jwt_required()
@admin_required
def create_service():
    """Crear un nuevo servicio (solo admins)"""
    try:
        # Validar datos
        data = service_create_schema.load(request.json)
        
        # Crear servicio
        service = Service(
            nombre=data['nombre'],
            descripcion=data['descripcion'],
            precio=data['precio'],
            duracion=data['duracion'],
            activo=data.get('activo', True)
        )
        
        db.session.add(service)
        db.session.commit()
        
        return jsonify({
            'message': 'Servicio creado exitosamente',
            'service': service_response_schema.dump(service)
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

@services_bp.route('/<string:service_id>', methods=['GET'])
def get_service(service_id):
    """Obtener un servicio específico"""
    try:
        service = Service.query.get_or_404(service_id)
        
        return jsonify({
            'message': 'Servicio obtenido exitosamente',
            'service': service_response_schema.dump(service)
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Servicio no encontrado',
            'message': str(e)
        }), 404

@services_bp.route('/<string:service_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_service(service_id):
    """Actualizar un servicio (solo admins)"""
    try:
        service = Service.query.get_or_404(service_id)
        
        # Validar datos
        data = service_update_schema.load(request.json)
        
        # Actualizar campos
        if 'nombre' in data:
            service.nombre = data['nombre']
        if 'descripcion' in data:
            service.descripcion = data['descripcion']
        if 'precio' in data:
            service.precio = data['precio']
        if 'duracion' in data:
            service.duracion = data['duracion']
        if 'activo' in data:
            service.activo = data['activo']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Servicio actualizado exitosamente',
            'service': service_response_schema.dump(service)
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

@services_bp.route('/<string:service_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_service(service_id):
    """Eliminar un servicio (solo admins)"""
    try:
        service = Service.query.get_or_404(service_id)
        
        # Marcar como inactivo en lugar de eliminar
        service.activo = False
        
        db.session.commit()
        
        return jsonify({
            'message': 'Servicio desactivado exitosamente'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@services_bp.route('/popular', methods=['GET'])
def get_popular_services():
    """Obtener servicios más populares"""
    try:
        # TODO: Implementar lógica basada en reservas
        # Por ahora, devolvemos todos los servicios activos
        services = Service.query.filter_by(activo=True).limit(5).all()
        
        return jsonify({
            'message': 'Servicios populares obtenidos exitosamente',
            'services': services_response_schema.dump(services),
            'total': len(services)
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500
