#!/usr/bin/env python3
"""
Script para verificar usuarios en la base de datos
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.models import User, UserRole, db

def check_users():
    """Verificar usuarios en la base de datos"""
    print("🔍 Verificando usuarios en la base de datos...")
    app = create_app('development')
    with app.app_context():
        # Verificar admin
        admin_user = User.query.filter_by(email='admin@lowbarber.com').first()
        if admin_user:
            print(f'✅ Usuario admin encontrado: {admin_user.nombre} ({admin_user.email})')
            print(f'   ID: {admin_user.id}')
            print(f'   Rol: {admin_user.rol.value}')
            print(f'   Activo: {admin_user.activo}')
            print(f'   Password hash: {admin_user.password_hash[:20]}...')
        else:
            print('❌ No se encontró usuario admin')
            
        # Mostrar todos los usuarios para debug
        all_users = User.query.all()
        print(f'\n📋 Total de usuarios en la BD: {len(all_users)}')
        for user in all_users:
            print(f'   - {user.nombre} ({user.email}) - {user.rol.value} - Activo: {user.activo}')

if __name__ == '__main__':
    check_users()