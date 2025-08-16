#!/usr/bin/env python3
"""
Verificar estructura de tablas - Low Barber
"""

import os
from sqlalchemy import create_engine, text, inspect

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
    """Verificar estructura completa de las tablas"""
    print("=== VERIFICACIÓN DE ESTRUCTURA DE TABLAS ===\n")
    
    database_url = get_database_url()
    engine = create_engine(database_url)
    
    try:
        with engine.connect() as connection:
            inspector = inspect(connection)
            tables = ['users', 'barbers', 'services', 'products', 'reservations', 'barber_services']
            
            for table_name in tables:
                print(f"\n📋 TABLA: {table_name.upper()}")
                print("="*50)
                
                # Obtener columnas
                columns = inspector.get_columns(table_name)
                for col in columns:
                    nullable = "NULL" if col['nullable'] else "NOT NULL"
                    default = f"DEFAULT: {col['default']}" if col['default'] else ""
                    print(f"  {col['name']:<20} {str(col['type']):<20} {nullable:<10} {default}")
                
                # Obtener foreign keys
                fks = inspector.get_foreign_keys(table_name)
                if fks:
                    print("\n  🔗 FOREIGN KEYS:")
                    for fk in fks:
                        print(f"    {fk['constrained_columns']} -> {fk['referred_table']}.{fk['referred_columns']}")
                
                # Obtener índices
                indexes = inspector.get_indexes(table_name)
                if indexes:
                    print("\n  🔍 ÍNDICES:")
                    for idx in indexes:
                        unique = " (UNIQUE)" if idx['unique'] else ""
                        print(f"    {idx['name']}: {idx['column_names']}{unique}")
            
            print("\n" + "="*70)
            print("✅ VERIFICACIÓN COMPLETADA")
            print("="*70)
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
