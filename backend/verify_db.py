#!/usr/bin/env python3
"""
Verificar estado de la base de datos
"""

import os
from sqlalchemy import create_engine, text

def get_database_url():
    """Obtener URL de la base de datos desde .env"""
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if line.startswith('DATABASE_URL='):
                    return line.split('=', 1)[1].strip()
    
    return 'postgresql://lowbarber_user:lowbarber_password@localhost/lowbarber_dev'

def main():
    """Verificar estado actual de la base de datos"""
    print("=== VERIFICACIÓN DE BASE DE DATOS ===\n")
    
    database_url = get_database_url()
    engine = create_engine(database_url)
    
    try:
        with engine.connect() as connection:
            print("✓ Conexión exitosa a la base de datos\n")
            
            # Verificar usuarios
            result = connection.execute(text("SELECT id, nombre, email, rol FROM users ORDER BY nombre"))
            users = result.fetchall()
            
            print(f"USUARIOS ({len(users)}):")
            for user in users:
                print(f"  - {user[1]} ({user[2]}) - Rol: {user[3]}")
            
            # Verificar barberos
            result = connection.execute(text("""
                SELECT b.id, b.nombre, b.especialidad, u.email 
                FROM barbers b 
                JOIN users u ON b.user_id = u.id 
                ORDER BY b.nombre
            """))
            barbers = result.fetchall()
            
            print(f"\nBARBEROS ({len(barbers)}):")
            for barber in barbers:
                print(f"  - {barber[1]} - {barber[2]} ({barber[3]})")
            
            # Verificar servicios
            result = connection.execute(text("SELECT nombre, precio, duracion FROM services ORDER BY nombre"))
            services = result.fetchall()
            
            print(f"\nSERVICIOS ({len(services)}):")
            for service in services:
                print(f"  - {service[0]} - ${service[1]} ({service[2]} min)")
            
            # Verificar productos
            result = connection.execute(text("SELECT nombre, precio, stock FROM products ORDER BY nombre"))
            products = result.fetchall()
            
            print(f"\nPRODUCTOS ({len(products)}):")
            for product in products:
                print(f"  - {product[0]} - ${product[1]} (Stock: {product[2]})")
            
            # Verificar reservas
            result = connection.execute(text("SELECT COUNT(*) FROM reservations"))
            reservations_count = result.scalar()
            print(f"\nRESERVAS: {reservations_count}")
            
            print("\n✓ Base de datos verificada correctamente")
            
    except Exception as e:
        print(f"✗ Error: {e}")

if __name__ == '__main__':
    main()
