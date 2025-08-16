#!/usr/bin/env python3
"""
Script de depuración específico para el endpoint de registro
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000/api"

def test_registration_debug():
    """Test detallado del endpoint de registro"""
    print("🔍 Depurando endpoint de registro...")
    
    # Datos de prueba
    test_data = {
        "nombre": "Test Usuario",
        "email": f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}@test.com",
        "telefono": "1234567890",
        "password": "test123",
        "password_confirmation": "test123"
    }
    
    print(f"📤 Enviando datos: {json.dumps(test_data, indent=2)}")
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register", json=test_data)
        
        print(f"📡 Status Code: {response.status_code}")
        print(f"📡 Headers: {dict(response.headers)}")
        print(f"📡 Response: {response.text}")
        
        if response.status_code == 201:
            print("✅ Registro exitoso!")
            return True
        else:
            print(f"❌ Error en registro")
            try:
                error_data = response.json()
                print(f"🔍 Error details: {json.dumps(error_data, indent=2)}")
            except:
                print(f"🔍 Raw error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def test_login_debug():
    """Test detallado del endpoint de login"""
    print("\n🔍 Depurando endpoint de login...")
    
    # Primero crear un usuario
    reg_data = {
        "nombre": "Login Test",
        "email": f"login_{datetime.now().strftime('%Y%m%d_%H%M%S')}@test.com",
        "telefono": "1234567890",
        "password": "test123",
        "password_confirmation": "test123"
    }
    
    try:
        # Registro
        reg_response = requests.post(f"{BASE_URL}/auth/register", json=reg_data)
        print(f"📤 Registro status: {reg_response.status_code}")
        
        if reg_response.status_code == 201:
            # Intentar login
            login_data = {
                "email": reg_data["email"],
                "password": reg_data["password"]
            }
            
            print(f"📤 Enviando login: {json.dumps(login_data, indent=2)}")
            
            login_response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
            
            print(f"📡 Login Status Code: {login_response.status_code}")
            print(f"📡 Login Response: {login_response.text}")
            
            if login_response.status_code == 200:
                print("✅ Login exitoso!")
                token_data = login_response.json()
                return token_data.get("access_token")
            else:
                print("❌ Error en login")
                return None
        else:
            print("❌ No se pudo crear usuario para test de login")
            return None
            
    except Exception as e:
        print(f"❌ Exception en login test: {e}")
        return None

if __name__ == "__main__":
    print("🛠️  DEPURACIÓN DE ENDPOINTS DE AUTENTICACIÓN")
    print("=" * 50)
    
    # Test registro
    reg_success = test_registration_debug()
    
    # Test login
    token = test_login_debug()
    
    print("\n" + "=" * 50)
    print("📊 RESUMEN:")
    print(f"   Registro: {'✅ OK' if reg_success else '❌ FAIL'}")
    print(f"   Login: {'✅ OK' if token else '❌ FAIL'}")
