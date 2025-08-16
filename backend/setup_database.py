#!/usr/bin/env python3
"""
SETUP BASE DE DATOS - LOW BARBER
Script único para configurar completamente la base de datos
"""

import os
import sys
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.exc import SQLAlchemyError
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash

def print_header(title):
    """Imprimir encabezado"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def print_step(step):
    """Imprimir paso"""
    print(f"\n>>> {step}")

def print_success(msg):
    """Imprimir éxito"""
    print(f"    OK - {msg}")

def print_error(msg):
    """Imprimir error"""
    print(f"    ERROR - {msg}")

def get_database_url():
    """Obtener URL de la base de datos desde .env"""
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if line.startswith('DATABASE_URL='):
                    return line.split('=', 1)[1].strip()
    
    # Valor por defecto
    return 'postgresql://lowbarber_user:lowbarber_password@localhost/lowbarber_dev'

def create_direct_connection():
    """Crear conexión directa a PostgreSQL"""
    database_url = get_database_url()
    print_step(f"Conectando a: {database_url}")
    
    try:
        engine = create_engine(database_url)
        connection = engine.connect()
        print_success("Conexión establecida")
        return engine, connection
    except Exception as e:
        print_error(f"No se pudo conectar: {e}")
        return None, None

def create_tables(connection):
    """Crear todas las tablas directamente con SQL"""
    print_step("Eliminando tablas existentes...")
    
    # Eliminar tablas en orden correcto (por dependencias)
    drop_tables = [
        "DROP TABLE IF EXISTS barber_services CASCADE;",
        "DROP TABLE IF EXISTS reservations CASCADE;", 
        "DROP TABLE IF EXISTS products CASCADE;",
        "DROP TABLE IF EXISTS services CASCADE;",
        "DROP TABLE IF EXISTS barbers CASCADE;",
        "DROP TABLE IF EXISTS users CASCADE;",
        "DROP FUNCTION IF EXISTS update_updated_at_column();",
    ]
    
    for sql in drop_tables:
        try:
            connection.execute(text(sql))
            connection.commit()
        except Exception as e:
            print(f"    Info: {e}")
    
    print_success("Tablas eliminadas")
    
    print_step("Creando nuevas tablas...")
    
    # Crear tablas
    create_tables_sql = """
    -- Función para actualizar updated_at automáticamente
    CREATE OR REPLACE FUNCTION update_updated_at_column()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated_at = CURRENT_TIMESTAMP;
        RETURN NEW;
    END;
    $$ language 'plpgsql';

    -- Tabla de usuarios
    CREATE TABLE users (
        id VARCHAR(36) PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        email VARCHAR(120) UNIQUE NOT NULL,
        telefono VARCHAR(20),
        password_hash VARCHAR(255) NOT NULL,
        rol VARCHAR(20) NOT NULL DEFAULT 'CLIENTE' CHECK (rol IN ('CLIENTE', 'BARBERO', 'ADMIN')),
        activo BOOLEAN DEFAULT TRUE,
        email_verificado BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );

    -- Tabla de barberos
    CREATE TABLE barbers (
        id VARCHAR(36) PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        especialidad VARCHAR(200),
        descripcion TEXT,
        experiencia_anos INTEGER DEFAULT 0,
        disponible BOOLEAN DEFAULT TRUE,
        activo BOOLEAN DEFAULT TRUE,
        user_id VARCHAR(36) NOT NULL,
        horario_trabajo JSON,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );

    -- Tabla de servicios
    CREATE TABLE services (
        id VARCHAR(36) PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        descripcion TEXT,
        precio DECIMAL(10, 2) NOT NULL,
        duracion INTEGER NOT NULL,
        activo BOOLEAN DEFAULT TRUE,
        popular BOOLEAN DEFAULT FALSE,
        categoria VARCHAR(50),
        imagen_url VARCHAR(255),
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );

    -- Tabla de productos
    CREATE TABLE products (
        id VARCHAR(36) PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        descripcion TEXT,
        precio DECIMAL(10, 2) NOT NULL,
        stock INTEGER DEFAULT 0,
        stock_minimo INTEGER DEFAULT 5,
        categoria VARCHAR(50),
        marca VARCHAR(50),
        activo BOOLEAN DEFAULT TRUE,
        destacado BOOLEAN DEFAULT FALSE,
        imagen_url VARCHAR(255),
        sku VARCHAR(50) UNIQUE,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );

    -- Tabla de reservas
    CREATE TABLE reservations (
        id VARCHAR(36) PRIMARY KEY,
        user_id VARCHAR(36) NOT NULL,
        barber_id VARCHAR(36) NOT NULL,
        service_id VARCHAR(36) NOT NULL,
        fecha_reserva DATE NOT NULL,
        hora_inicio TIME NOT NULL,
        hora_fin TIME,
        estado VARCHAR(20) DEFAULT 'pendiente' CHECK (estado IN ('pendiente', 'confirmada', 'en_proceso', 'completada', 'cancelada', 'no_asistio')),
        notas TEXT,
        notas_barbero TEXT,
        precio_final DECIMAL(10, 2),
        cliente_nombre VARCHAR(100) NOT NULL,
        cliente_telefono VARCHAR(20),
        cliente_email VARCHAR(120) NOT NULL,
        fecha_confirmacion TIMESTAMP WITH TIME ZONE,
        fecha_completacion TIMESTAMP WITH TIME ZONE,
        fecha_cancelacion TIMESTAMP WITH TIME ZONE,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (barber_id) REFERENCES barbers(id) ON DELETE CASCADE,
        FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
    );

    -- Tabla de relación barberos-servicios
    CREATE TABLE barber_services (
        barber_id VARCHAR(36) NOT NULL,
        service_id VARCHAR(36) NOT NULL,
        PRIMARY KEY (barber_id, service_id),
        FOREIGN KEY (barber_id) REFERENCES barbers(id) ON DELETE CASCADE,
        FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
    );

    -- Triggers para updated_at
    CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    CREATE TRIGGER update_barbers_updated_at BEFORE UPDATE ON barbers FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    CREATE TRIGGER update_services_updated_at BEFORE UPDATE ON services FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    CREATE TRIGGER update_products_updated_at BEFORE UPDATE ON products FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    CREATE TRIGGER update_reservations_updated_at BEFORE UPDATE ON reservations FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

    -- Índices
    CREATE INDEX idx_users_email ON users(email);
    CREATE INDEX idx_users_rol ON users(rol);
    CREATE INDEX idx_barbers_user_id ON barbers(user_id);
    CREATE INDEX idx_reservations_fecha ON reservations(fecha_reserva);
    CREATE INDEX idx_reservations_barber_id ON reservations(barber_id);
    """
    
    try:
        connection.execute(text(create_tables_sql))
        connection.commit()
        print_success("Tablas creadas exitosamente")
        return True
    except Exception as e:
        print_error(f"Error creando tablas: {e}")
        return False

def insert_initial_data(connection):
    """Insertar datos iniciales"""
    print_step("Insertando datos iniciales...")
    
    # Generar IDs
    admin_id = str(uuid.uuid4())
    barber_id = str(uuid.uuid4())
    
    # Servicios
    service_ids = [str(uuid.uuid4()) for _ in range(5)]
    
    # Producto
    product_id = str(uuid.uuid4())
    
    # Hash de password
    admin_password = generate_password_hash('admin123')
    
    # Insertar admin
    admin_sql = """
    INSERT INTO users (id, nombre, email, telefono, password_hash, rol, activo, email_verificado)
    VALUES (:id, :nombre, :email, :telefono, :password_hash, :rol, :activo, :email_verificado)
    """
    
    try:
        connection.execute(text(admin_sql), {
            'id': admin_id,
            'nombre': 'Administrador',
            'email': 'admin@lowbarber.com',
            'telefono': '+1234567890',
            'password_hash': admin_password,
            'rol': 'ADMIN',  # Usar valor del enum en mayúscula
            'activo': True,
            'email_verificado': True
        })
        print_success("Usuario admin creado")
        
        # Insertar barbero
        barber_sql = """
        INSERT INTO barbers (id, nombre, especialidad, descripcion, experiencia_anos, disponible, activo, user_id)
        VALUES (:id, :nombre, :especialidad, :descripcion, :experiencia_anos, :disponible, :activo, :user_id)
        """
        
        connection.execute(text(barber_sql), {
            'id': barber_id,
            'nombre': 'Pedro Martínez',
            'especialidad': 'Especialista en cortes modernos',
            'descripcion': 'Barbero profesional con 5 años de experiencia',
            'experiencia_anos': 5,
            'disponible': True,
            'activo': True,
            'user_id': admin_id
        })
        print_success("Barbero creado")
        
        # Insertar servicios
        servicios = [
            ('Corte de Cabello', 'Corte profesional adaptado a tu estilo', 50.00, 45, 'Cortes', True),
            ('Arreglo de Barba', 'Perfilado y arreglo profesional de barba', 40.00, 30, 'Barba', True),
            ('Afeitado Clásico', 'Afeitado tradicional con navaja', 60.00, 35, 'Afeitado', False),
            ('Cejas', 'Perfilado de cejas masculinas', 15.00, 20, 'Cejas', False),
            ('Servicio Completo', 'Corte + Barba + Cejas', 70.00, 90, 'Completo', False)
        ]
        
        service_sql = """
        INSERT INTO services (id, nombre, descripcion, precio, duracion, categoria, popular, activo)
        VALUES (:id, :nombre, :descripcion, :precio, :duracion, :categoria, :popular, :activo)
        """
        
        for i, (nombre, desc, precio, duracion, categoria, popular) in enumerate(servicios):
            connection.execute(text(service_sql), {
                'id': service_ids[i],
                'nombre': nombre,
                'descripcion': desc,
                'precio': precio,
                'duracion': duracion,
                'categoria': categoria,
                'popular': popular,
                'activo': True
            })
        
        print_success("Servicios creados")
        
        # Insertar producto
        product_sql = """
        INSERT INTO products (id, nombre, descripcion, precio, stock, categoria, marca, activo, destacado, sku)
        VALUES (:id, :nombre, :descripcion, :precio, :stock, :categoria, :marca, :activo, :destacado, :sku)
        """
        
        connection.execute(text(product_sql), {
            'id': product_id,
            'nombre': 'Pomada para Cabello Premium',
            'descripcion': 'Pomada de alta fijación para peinados duraderos',
            'precio': 25.00,
            'stock': 50,
            'categoria': 'Cuidado Capilar',
            'marca': 'Low Barber',
            'activo': True,
            'destacado': True,
            'sku': 'LB-POM-001'
        })
        print_success("Producto creado")
        
        # Asociar barbero con servicios
        barber_service_sql = """
        INSERT INTO barber_services (barber_id, service_id) VALUES (:barber_id, :service_id)
        """
        
        for service_id in service_ids:
            connection.execute(text(barber_service_sql), {
                'barber_id': barber_id,
                'service_id': service_id
            })
        
        print_success("Barbero asociado con servicios")
        
        connection.commit()
        return True
        
    except Exception as e:
        print_error(f"Error insertando datos: {e}")
        connection.rollback()
        return False

def verify_setup(connection):
    """Verificar que todo se creó correctamente"""
    print_step("Verificando configuración...")
    
    try:
        # Verificar tablas
        inspector = inspect(connection)
        tables = inspector.get_table_names()
        print_success(f"Tablas encontradas: {len(tables)}")
        for table in sorted(tables):
            print(f"      - {table}")
        
        # Contar registros
        counts = {}
        for table in ['users', 'barbers', 'services', 'products']:
            result = connection.execute(text(f"SELECT COUNT(*) FROM {table}"))
            count = result.scalar()
            counts[table] = count
            print_success(f"{table}: {count} registros")
        
        # Verificar admin
        result = connection.execute(text("SELECT email, rol FROM users WHERE rol = 'admin'"))
        admin = result.fetchone()
        if admin:
            print_success(f"Admin encontrado: {admin[0]}")
        
        return True
        
    except Exception as e:
        print_error(f"Error en verificación: {e}")
        return False

def main():
    """Función principal"""
    print_header("CONFIGURACIÓN DE BASE DE DATOS - LOW BARBER")
    print("Este script configurará completamente tu base de datos desde cero")
    
    # Confirmar
    respuesta = input("\nContinuar? (s/N): ").lower().strip()
    if respuesta not in ['s', 'si', 'sí', 'y', 'yes']:
        print("\nOperación cancelada")
        return
    
    # Conectar
    engine, connection = create_direct_connection()
    if not connection:
        print_error("No se pudo establecer conexión")
        return
    
    try:
        # Crear tablas
        if not create_tables(connection):
            return
        
        # Insertar datos
        if not insert_initial_data(connection):
            return
        
        # Verificar
        if not verify_setup(connection):
            return
        
        print_header("CONFIGURACIÓN COMPLETADA")
        print("\nCREDENCIALES DE ACCESO:")
        print("  Email:    admin@lowbarber.com")
        print("  Password: admin123")
        print("\nTu base de datos está lista!")
        print("Puedes probar tu aplicación con: python app.py")
        
    finally:
        connection.close()

if __name__ == '__main__':
    main()
