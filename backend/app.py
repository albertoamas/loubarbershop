#!/usr/bin/env python3
"""
Low Barber - Sistema de Gestión de Barbería
Archivo principal de la aplicación Flask
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os

# Importar configuración y modelos
from config import config
from app.models import db, User, Barber, Service, Product, Reservation

def create_app(config_name=None):
    """Factory para crear la aplicación Flask"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    
    # Inicializar extensiones
    db.init_app(app)
    
    # Configurar CORS de manera más permisiva para desarrollo
    CORS(app, 
         origins=['http://localhost:5173', 'http://127.0.0.1:5000', 'null', '*'],
         allow_headers=['Content-Type', 'Authorization'],
         methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
         supports_credentials=True)
    
    # Configurar JWT
    jwt = JWTManager(app)
    
    # Registrar blueprints
    from app.routes import auth_bp, stats_bp
    from app.routes.barbers import barbers_bp
    from app.routes.services import services_bp
    from app.routes.products import products_bp
    from app.routes.reservations import reservations_bp
    from app.routes.admin_users import admin_users_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(barbers_bp, url_prefix='/api/barbers')
    app.register_blueprint(services_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(reservations_bp, url_prefix='/api/reservations')
    app.register_blueprint(stats_bp, url_prefix='/api/stats')
    app.register_blueprint(admin_users_bp)
    
    # Crear tablas si no existen
    with app.app_context():
        db.create_all()
    
    # Servir archivos estáticos de prueba
    @app.route('/static/<path:filename>')
    def serve_static(filename):
        from flask import send_from_directory
        import os
        return send_from_directory(os.path.join(app.root_path, '..'), filename)
    
    # Rutas básicas
    @app.route('/')
    def home():
        return jsonify({
            'message': 'Low Barber API está funcionando!',
            'version': '1.0.0',
            'status': 'active',
            'environment': config_name
        })
    
    @app.route('/health')
    def health():
        try:
            # Verificar conexión a la base de datos
            from sqlalchemy import text
            db.session.execute(text('SELECT 1'))
            db_status = 'connected'
        except Exception as e:
            db_status = f'error: {str(e)}'
        
        return jsonify({
            'status': 'healthy',
            'service': 'Low Barber API',
            'database': db_status,
            'environment': config_name
        })
    
    # Endpoint de health check para la API
    @app.route('/api/health')
    def api_health():
        try:
            # Verificar conexión a la base de datos
            from sqlalchemy import text
            db.session.execute(text('SELECT 1'))
            db_status = 'connected'
        except Exception as e:
            db_status = f'error: {str(e)}'
        
        return jsonify({
            'status': 'healthy',
            'service': 'Low Barber API',
            'database': db_status,
            'environment': config_name,
            'message': 'API funcionando correctamente'
        })
    
    # Endpoint de información de la API
    @app.route('/api/info')
    def api_info():
        return jsonify({
            'api_name': 'Low Barber API',
            'version': '1.0.0',
            'description': 'Sistema de gestión para barbería',
            'endpoints': {
                'auth': '/api/auth',
                'users': '/api/users',
                'barbers': '/api/barbers',
                'services': '/api/services',
                'products': '/api/products',
                'reservations': '/api/reservations',
                'stats': '/api/stats'
            }
        })
    
    return app

# Crear la aplicación
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
