#!/usr/bin/env python3
"""
Script para crear datos de prueba para el sistema de reservas
"""

# Renombrar el archivo app.py para evitar conflictos de nombres
import importlib.util
import sys
import os

# Cargar el archivo app.py directamente
spec = importlib.util.spec_from_file_location("main_app", "app.py")
main_app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(main_app)

from app.models import db
from app.models.user import User, UserRole
from app.models.barber import Barber
from app.models.service import Service
from app.models.product import Product
from datetime import datetime

def create_test_data():
    """Crea datos de prueba"""
    application = main_app.create_app()
    with application.app_context():
        print("🔧 Creando datos de prueba...")
        
        # Crear tablas si no existen
        db.create_all()
        
        # 1. Crear usuarios
        print("👥 Creando usuarios...")
        
        # Usuario administrador
        admin = User.find_by_email('admin@lowbarber.com')
        if not admin:
            admin = User(
                nombre='Administrador',
                email='admin@lowbarber.com',
                password='admin123',
                telefono='555-0001',
                rol=UserRole.ADMIN
            )
            admin.save()
            print(f"✅ Admin creado: {admin.email}")
        else:
            print(f"ℹ️  Admin ya existe: {admin.email}")
        
        # Usuario barbero
        barbero_user = User.find_by_email('barbero@test.com')
        if not barbero_user:
            barbero_user = User(
                nombre='Pedro Barbero',
                email='barbero@test.com',
                password='123456',
                telefono='555-0002',
                rol=UserRole.BARBERO
            )
            barbero_user.save()
            print(f"✅ Barbero user creado: {barbero_user.email}")
        else:
            print(f"ℹ️  Barbero user ya existe: {barbero_user.email}")
        
        # Usuario cliente
        cliente_user = User.find_by_email('cliente@test.com')
        if not cliente_user:
            cliente_user = User(
                nombre='Juan Cliente',
                email='cliente@test.com',
                password='123456',
                telefono='555-0003',
                rol=UserRole.CLIENTE
            )
            cliente_user.save()
            print(f"✅ Cliente creado: {cliente_user.email}")
        else:
            print(f"ℹ️  Cliente ya existe: {cliente_user.email}")
        
        # 2. Crear perfiles de barberos
        print("💈 Creando perfiles de barberos...")
        
        barberos_data = [
            {
                'nombre': 'Pedro Martínez',
                'user_id': barbero_user.id,
                'especialidad': 'Especialista en cortes modernos',
                'descripcion': 'Barbero con 5 años de experiencia en cortes modernos y técnicas avanzadas',
                'experiencia_anos': 5
            },
            {
                'nombre': 'Carlos Rivera',
                'user_id': admin.id,  # Usar admin como segundo barbero para tener más opciones
                'especialidad': 'Maestro de la barba clásica',
                'descripcion': 'Experto en arreglo de barbas y estilos clásicos con 8 años de experiencia',
                'experiencia_anos': 8
            },
            {
                'nombre': 'Juan Pérez',
                'user_id': cliente_user.id,  # Usar cliente como tercer barbero
                'especialidad': 'Experto en estilos vintage',
                'descripcion': 'Especialista en cortes vintage y retro con técnicas tradicionales',
                'experiencia_anos': 10
            }
        ]
        
        barberos_creados = []
        for barbero_data in barberos_data:
            # Verificar si el barbero ya existe por nombre
            barbero_existente = Barber.query.filter_by(nombre=barbero_data['nombre']).first()
            if not barbero_existente:
                barbero = Barber(
                    nombre=barbero_data['nombre'],
                    user_id=barbero_data['user_id'],
                    especialidad=barbero_data['especialidad'],
                    descripcion=barbero_data['descripcion'],
                    experiencia_anos=barbero_data['experiencia_anos'],
                    disponible=True  # Asegurar que estén disponibles
                )
                # Asegurar que estén activos (el campo activo se establece por defecto en True)
                barbero.activo = True
                barbero.save()
                barberos_creados.append(barbero)
                print(f"✅ Barbero creado: {barbero.nombre} - {barbero.especialidad}")
            else:
                # Actualizar barbero existente para asegurar que esté disponible y activo
                barbero_existente.disponible = True
                barbero_existente.activo = True
                barbero_existente.save()
                barberos_creados.append(barbero_existente)
                print(f"ℹ️  Barbero ya existe (actualizado): {barbero_existente.nombre}")
        
        print(f"✅ Total de barberos disponibles: {len(barberos_creados)}")
        
        # 3. Crear servicios
        print("✂️ Creando servicios...")
        
        servicios_data = [
            {
                'nombre': 'Corte de Cabello',
                'descripcion': 'Corte de cabello profesional con estilo moderno',
                'precio': 25.00,
                'duracion': 30,
                'categoria': 'Cabello',
                'popular': True
            },
            {
                'nombre': 'Arreglo de Barba',
                'descripcion': 'Recorte y arreglo profesional de barba',
                'precio': 15.00,
                'duracion': 20,
                'categoria': 'Barba',
                'popular': True
            },
            {
                'nombre': 'Corte + Barba',
                'descripcion': 'Paquete completo: corte de cabello y arreglo de barba',
                'precio': 35.00,
                'duracion': 45,
                'categoria': 'Paquete',
                'popular': True
            },
            {
                'nombre': 'Lavado de Cabello',
                'descripcion': 'Lavado profundo con productos premium',
                'precio': 10.00,
                'duracion': 15,
                'categoria': 'Cabello',
                'popular': False
            }
        ]
        
        servicios_creados = []
        for servicio_data in servicios_data:
            # Verificar si el servicio ya existe
            servicio_existente = Service.query.filter_by(nombre=servicio_data['nombre']).first()
            if not servicio_existente:
                # Crear servicio con los parámetros que acepta el constructor
                servicio = Service(
                    nombre=servicio_data['nombre'],
                    precio=servicio_data['precio'],
                    duracion=servicio_data['duracion'],
                    descripcion=servicio_data['descripcion'],
                    categoria=servicio_data['categoria']
                )
                # Establecer el campo popular después de crear el objeto
                servicio.popular = servicio_data['popular']
                servicio.save()
                servicios_creados.append(servicio)
                print(f"✅ Servicio creado: {servicio.nombre} - ${servicio.precio}")
            else:
                servicios_creados.append(servicio_existente)
                print(f"ℹ️  Servicio ya existe: {servicio_existente.nombre}")
        
        # 4. Asociar servicios a todos los barberos
        print("🔗 Asociando servicios a los barberos...")
        for barbero in barberos_creados:
            for servicio in servicios_creados:
                if servicio not in barbero.servicios:
                    barbero.servicios.append(servicio)
            barbero.save()
            print(f"✅ {len(servicios_creados)} servicios asociados a {barbero.nombre}")
        
        # 5. Crear productos
        print("🛍️ Creando productos...")
        
        productos_data = [
            {
                'nombre': 'Pomada Fijadora Premium',
                'descripcion': 'Pomada de alta calidad para un peinado duradero y con brillo natural. Formulada con ceras naturales.',
                'precio': 35.00,
                'marca': 'Premium Hair',
                'categoria': 'Styling',
                'stock': 15,
                'destacado': True
            },
            {
                'nombre': 'Shampoo Anticaspa Natural',
                'descripcion': 'Shampoo especializado para combatir la caspa con ingredientes 100% naturales y aceites esenciales.',
                'precio': 28.00,
                'marca': 'Natural Care',
                'categoria': 'Cuidado',
                'stock': 25
            },
            {
                'nombre': 'Aceite para Barba Orgánico',
                'descripcion': 'Aceite nutritivo orgánico que suaviza, hidrata y da brillo natural a tu barba.',
                'precio': 45.00,
                'marca': 'Beard Master',
                'categoria': 'Barba',
                'stock': 12,
                'destacado': True
            },
            {
                'nombre': 'Crema de Afeitar Hidratante',
                'descripcion': 'Crema hidratante con aloe vera para un afeitado suave sin irritaciones ni cortes.',
                'precio': 22.00,
                'marca': 'Smooth Shave',
                'categoria': 'Afeitado',
                'stock': 30
            },
            {
                'nombre': 'Gel Fijador Extra Fuerte',
                'descripcion': 'Gel de fijación extra fuerte para estilos extremos. Fórmula sin alcohol.',
                'precio': 25.00,
                'marca': 'Style Pro',
                'categoria': 'Styling',
                'stock': 20
            },
            {
                'nombre': 'Bálsamo para Barba',
                'descripcion': 'Bálsamo hidratante con manteca de karité que suaviza y protege tu barba diariamente.',
                'precio': 38.00,
                'marca': 'Beard Master',
                'categoria': 'Barba',
                'stock': 18
            },
            {
                'nombre': 'Champú Revitalizante',
                'descripcion': 'Champú fortificante con vitaminas B5 y E para cabello débil y sin vida.',
                'precio': 30.00,
                'marca': 'Vita Hair',
                'categoria': 'Cuidado',
                'stock': 22
            },
            {
                'nombre': 'Loción Aftershave Mentolada',
                'descripcion': 'Loción calmante post-afeitado con mentol y propiedades antisépticas refrescantes.',
                'precio': 22.00,
                'marca': 'Cool Fresh',
                'categoria': 'Afeitado',
                'stock': 35
            }
        ]
        
        productos_creados = []
        for producto_data in productos_data:
            # Verificar si el producto ya existe
            producto_existente = Product.query.filter_by(nombre=producto_data['nombre']).first()
            if not producto_existente:
                # Crear producto usando el constructor
                producto = Product(
                    nombre=producto_data['nombre'],
                    descripcion=producto_data['descripcion'],
                    precio=producto_data['precio'],
                    stock=producto_data['stock'],
                    categoria=producto_data.get('categoria'),
                    marca=producto_data.get('marca'),
                    activo=True
                )
                
                # Establecer campos adicionales si están presentes
                if 'destacado' in producto_data:
                    producto.destacado = producto_data['destacado']
                
                producto.save()
                productos_creados.append(producto)
                print(f"✅ Producto creado: {producto.nombre} - Bs {producto.precio}")
            else:
                productos_creados.append(producto_existente)
                print(f"ℹ️  Producto ya existe: {producto_existente.nombre}")
        
        # 6. Mostrar resumen
        print("\n📋 RESUMEN DE DATOS CREADOS:")
        print(f"👤 Admin: {admin.email} / admin123")
        print(f"💈 Barbero: {barbero_user.email} / barbero123")
        print(f"👨 Cliente: {cliente_user.email} / cliente123")
        print("\n💈 BARBEROS DISPONIBLES:")
        for barbero in barberos_creados:
            print(f"   🔹 {barbero.nombre} (ID: {barbero.id}) - {barbero.especialidad} - Disponible: {barbero.disponible} - Activo: {barbero.activo}")
        print("\n✂️ SERVICIOS DISPONIBLES:")
        for servicio in servicios_creados:
            print(f"   🔹 {servicio.nombre} (ID: {servicio.id}) - Bs {servicio.precio} - {servicio.duracion}min")
        print("\n🛍️ PRODUCTOS DISPONIBLES:")
        for producto in productos_creados:
            print(f"   🔸 {producto.nombre} (ID: {producto.id}) - Bs {producto.precio} - Stock: {producto.stock}")
        
        print(f"\n🎉 ¡Datos de prueba creados exitosamente!")
        print(f"📊 Total: {len(barberos_creados)} barberos, {len(servicios_creados)} servicios y {len(productos_creados)} productos")
        print(f"🌐 Ahora puedes probar en: http://127.0.0.1:5000")

if __name__ == '__main__':
    create_test_data()
