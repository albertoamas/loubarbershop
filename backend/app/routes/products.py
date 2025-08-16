"""
Rutas para Productos - Low Barber
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from app.models import Product, db
from app.schemas.product_schemas import (
    product_create_schema,
    product_update_schema,
    product_response_schema,
    products_response_schema
)
from app.utils.auth_utils import (
    get_current_user,
    format_validation_errors,
    admin_required
)

# Crear blueprint para productos
products_bp = Blueprint('products', __name__, url_prefix='/api/products')

@products_bp.route('', methods=['GET'])
def get_products():
    """Obtener todos los productos activos"""
    try:
        # Solo productos activos y con stock para usuarios normales
        products = Product.query.filter_by(activo=True).filter(Product.stock > 0).all()
        
        return jsonify({
            'message': 'Productos obtenidos exitosamente',
            'products': products_response_schema.dump(products),
            'total': len(products)
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@products_bp.route('/all', methods=['GET'])
@jwt_required()
@admin_required
def get_all_products():
    """Obtener todos los productos (incluye inactivos) - solo admins"""
    try:
        products = Product.query.all()
        
        return jsonify({
            'message': 'Todos los productos obtenidos exitosamente',
            'products': products_response_schema.dump(products),
            'total': len(products)
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@products_bp.route('', methods=['POST'])
@jwt_required()
@admin_required
def create_product():
    """Crear un nuevo producto (solo admins)"""
    try:
        # Validar datos
        data = product_create_schema.load(request.json)
        
        # Crear producto
        product = Product(
            nombre=data['nombre'],
            descripcion=data['descripcion'],
            precio=data['precio'],
            stock=data['stock'],
            imagen=data.get('imagen'),
            activo=data.get('activo', True)
        )
        
        db.session.add(product)
        db.session.commit()
        
        return jsonify({
            'message': 'Producto creado exitosamente',
            'product': product_response_schema.dump(product)
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

@products_bp.route('/<string:product_id>', methods=['GET'])
def get_product(product_id):
    """Obtener un producto específico"""
    try:
        product = Product.query.get_or_404(product_id)
        
        return jsonify({
            'message': 'Producto obtenido exitosamente',
            'product': product_response_schema.dump(product)
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Producto no encontrado',
            'message': str(e)
        }), 404

@products_bp.route('/<string:product_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_product(product_id):
    """Actualizar un producto (solo admins)"""
    try:
        product = Product.query.get_or_404(product_id)
        
        # Validar datos
        data = product_update_schema.load(request.json)
        
        # Actualizar campos
        if 'nombre' in data:
            product.nombre = data['nombre']
        if 'descripcion' in data:
            product.descripcion = data['descripcion']
        if 'precio' in data:
            product.precio = data['precio']
        if 'stock' in data:
            product.stock = data['stock']
        if 'imagen' in data:
            product.imagen = data['imagen']
        if 'activo' in data:
            product.activo = data['activo']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Producto actualizado exitosamente',
            'product': product_response_schema.dump(product)
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

@products_bp.route('/<string:product_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_product(product_id):
    """Eliminar un producto (solo admins)"""
    try:
        product = Product.query.get_or_404(product_id)
        
        # Marcar como inactivo en lugar de eliminar
        product.activo = False
        
        db.session.commit()
        
        return jsonify({
            'message': 'Producto desactivado exitosamente'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@products_bp.route('/search', methods=['GET'])
def search_products():
    """Buscar productos por nombre"""
    try:
        query = request.args.get('q', '').strip()
        
        if not query:
            return jsonify({
                'error': 'Parámetro de búsqueda requerido',
                'message': 'Proporcione el parámetro "q" para buscar productos'
            }), 400
        
        # Buscar productos activos que contengan el término de búsqueda
        products = Product.query.filter(
            Product.activo == True,
            Product.nombre.ilike(f'%{query}%')
        ).all()
        
        return jsonify({
            'message': f'Búsqueda completada para: "{query}"',
            'products': products_response_schema.dump(products),
            'total': len(products),
            'query': query
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500
