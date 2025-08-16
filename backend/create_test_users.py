#!/usr/bin/env python3
"""
Script para crear datos de prueba para desarrollo
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.models import db, User, UserRole, Barber, Service, Reservation
from datetime import datetime, timedelta
import uuid

def create_test_data():
    """Crear datos de prueba para desarrollo"""
    print("🌱 Creando datos de prueba...")
    
    # Crear usuarios de prueba
    users_data = [
        {
            'nombre': 'Admin Sistema',
            'email': 'admin@lowbarber.com',
            'password': 'admin123',
            'telefono': '+57 300 000 0001',
            'rol': UserRole.ADMIN
        },
        {
            'nombre': 'Carlos Mendoza Silva',
            'email': 'carlos.mendoza@lowbarber.com',
            'password': 'barber123',
            'telefono': '+57 301 234 5678',
            'rol': UserRole.BARBERO
        },
        {
            'nombre': 'Miguel Rodríguez Torres',
            'email': 'miguel.rodriguez@lowbarber.com',
            'password': 'barber123',
            'telefono': '+57 303 456 7890',
            'rol': UserRole.BARBERO
        },
        {
            'nombre': 'Roberto Jiménez Paz',
            'email': 'roberto.jimenez@lowbarber.com',
            'password': 'barber123',
            'telefono': '+57 309 012 3456',
            'rol': UserRole.BARBERO
        },
        {
            'nombre': 'Juan Pérez González',
            'email': 'juan.perez@ejemplo.com',
            'password': 'cliente123',
            'telefono': '+57 300 123 4567',
            'rol': UserRole.CLIENTE
        },
        {
            'nombre': 'Ana García López',
            'email': 'ana.garcia@ejemplo.com',
            'password': 'cliente123',
            'telefono': '+57 302 345 6789',
            'rol': UserRole.CLIENTE
        },
        {
            'nombre': 'Luis Martínez Ruiz',
            'email': 'luis.martinez@ejemplo.com',
            'password': 'cliente123',
            'telefono': '+57 305 678 9012',
            'rol': UserRole.CLIENTE
        },
        {
            'nombre': 'María López Herrera',
            'email': 'maria.lopez@ejemplo.com',
            'password': 'cliente123',
            'telefono': '+57 306 789 0123',
            'rol': UserRole.CLIENTE
        },
        {
            'nombre': 'Pedro Silva Castro',
            'email': 'pedro.silva@ejemplo.com',
            'password': 'cliente123',
            'telefono': '+57 307 890 1234',
            'rol': UserRole.CLIENTE
        },
        {
            'nombre': 'Sofia Valencia Moreno',
            'email': 'sofia.valencia@ejemplo.com',
            'password': 'cliente123',
            'telefono': '+57 308 901 2345',
            'rol': UserRole.CLIENTE
        }
    ]
    
    created_users = []
    for user_data in users_data:
        # Verificar si el usuario ya existe
        existing_user = User.query.filter_by(email=user_data['email']).first()
        if existing_user:
            print(f"⚠️ Usuario {user_data['email']} ya existe, omitiendo...")
            created_users.append(existing_user)
            continue
            
        user = User(
            nombre=user_data['nombre'],
            email=user_data['email'],
            password=user_data['password'],
            telefono=user_data['telefono'],
            rol=user_data['rol']
        )
        user.email_verificado = True  # Para pruebas
        user.activo = True
        
        # Desactivar algunos usuarios para pruebas
        if user_data['email'] in ['luis.martinez@ejemplo.com', 'maria.lopez@ejemplo.com']:
            user.activo = False
        
        db.session.add(user)
        created_users.append(user)
        print(f"✅ Usuario creado: {user_data['nombre']} ({user_data['rol'].value})")
    
    # Commit para obtener IDs
    db.session.commit()
    
    # Crear perfiles de barberos
    barberos_data = [
        {
            'nombre': 'Carlos Mendoza Silva',
            'especialidad': 'Cortes clásicos y barbas tradicionales',
            'descripcion': 'Especialista en cortes clásicos con más de 8 años de experiencia. Maestro en técnicas de barbería tradicional.',
            'experiencia_anos': 8
        },
        {
            'nombre': 'Miguel Rodríguez Torres',
            'especialidad': 'Cortes modernos y diseños creativos',
            'descripcion': 'Experto en tendencias modernas y diseños únicos. Especializado en fade cuts y estilos contemporáneos.',
            'experiencia_anos': 5
        },
        {
            'nombre': 'Roberto Jiménez Paz',
            'especialidad': 'Cortes premium y tratamientos especializados',
            'descripcion': 'Barbero premium con enfoque en servicios exclusivos y tratamientos capilares especializados.',
            'experiencia_anos': 12
        }
    ]
    
    for barber_data in barberos_data:
        # Buscar el usuario correspondiente
        user = User.query.filter_by(nombre=barber_data['nombre']).first()
        if not user:
            print(f"⚠️ Usuario {barber_data['nombre']} no encontrado para crear perfil de barbero")
            continue
            
        # Verificar si ya existe el perfil
        existing_barber = Barber.query.filter_by(user_id=user.id).first()
        if existing_barber:
            print(f"⚠️ Perfil de barbero para {barber_data['nombre']} ya existe")
            continue
        
        barber = Barber(
            nombre=barber_data['nombre'],
            especialidad=barber_data['especialidad'],
            descripcion=barber_data['descripcion'],
            experiencia_anos=barber_data['experiencia_anos'],
            user_id=user.id,
            disponible=True,
            activo=True,
            horario_trabajo={
                'lunes': {'inicio': '08:00', 'fin': '18:00'},
                'martes': {'inicio': '08:00', 'fin': '18:00'},
                'miercoles': {'inicio': '08:00', 'fin': '18:00'},
                'jueves': {'inicio': '08:00', 'fin': '18:00'},
                'viernes': {'inicio': '08:00', 'fin': '20:00'},
                'sabado': {'inicio': '08:00', 'fin': '16:00'},
                'domingo': 'cerrado'
            }
        )
        db.session.add(barber)
        print(f"✅ Perfil de barbero creado: {barber_data['nombre']}")
    
    # Crear servicios básicos
    servicios_data = [
        {
            'nombre': 'Corte Clásico',
            'descripcion': 'Corte tradicional de cabello con técnicas clásicas de barbería',
            'precio': 30000,
            'duracion': 30,
            'categoria': 'cortes',
            'popular': True
        },
        {
            'nombre': 'Corte Moderno',
            'descripcion': 'Cortes contemporáneos siguiendo las últimas tendencias',
            'precio': 35000,
            'duracion': 40,
            'categoria': 'cortes',
            'popular': True
        },
        {
            'nombre': 'Corte + Barba',
            'descripcion': 'Servicio completo de corte de cabello y arreglo de barba',
            'precio': 45000,
            'duracion': 60,
            'categoria': 'completos',
            'popular': True
        },
        {
            'nombre': 'Arreglo de Barba',
            'descripcion': 'Perfilado y arreglo profesional de barba',
            'precio': 20000,
            'duracion': 25,
            'categoria': 'barba'
        },
        {
            'nombre': 'Afeitado Clásico',
            'descripcion': 'Afeitado tradicional con navaja y toallas calientes',
            'precio': 25000,
            'duracion': 30,
            'categoria': 'afeitado'
        },
        {
            'nombre': 'Lavado y Peinado',
            'descripcion': 'Lavado profesional con productos premium y peinado',
            'precio': 15000,
            'duracion': 20,
            'categoria': 'cuidado'
        }
    ]
    
    for servicio_data in servicios_data:
        # Verificar si el servicio ya existe
        existing_service = Service.query.filter_by(nombre=servicio_data['nombre']).first()
        if existing_service:
            print(f"⚠️ Servicio {servicio_data['nombre']} ya existe")
            continue
            
        service = Service(
            nombre=servicio_data['nombre'],
            descripcion=servicio_data['descripcion'],
            precio=servicio_data['precio'],
            duracion=servicio_data['duracion'],
            categoria=servicio_data['categoria'],
            popular=servicio_data.get('popular', False),
            activo=True
        )
        db.session.add(service)
        print(f"✅ Servicio creado: {servicio_data['nombre']} - ${servicio_data['precio']:,}")
    
    # Commit final
    db.session.commit()
    print("🎉 ¡Datos de prueba creados exitosamente!")
    
    # Mostrar resumen
    total_users = User.query.count()
    total_barbers = Barber.query.count()
    total_services = Service.query.count()
    
    print(f"\n📊 Resumen de datos creados:")
    print(f"   👥 Usuarios: {total_users}")
    print(f"   ✂️ Barberos: {total_barbers}")
    print(f"   🔧 Servicios: {total_services}")
    
    # Mostrar credenciales de acceso
    print(f"\n🔑 Credenciales de acceso:")
    print(f"   Admin: admin@lowbarber.com / admin123")
    print(f"   Barbero: carlos.mendoza@lowbarber.com / barber123")
    print(f"   Cliente: juan.perez@ejemplo.com / cliente123")

if __name__ == '__main__':
    app = create_app('development')
    with app.app_context():
        try:
            create_test_data()
        except Exception as e:
            print(f"❌ Error creando datos de prueba: {e}")
            db.session.rollback()
