# 🧪 Guía de Pruebas - Sistema de Reservas

## 📋 **Instrucciones paso a paso para probar el sistema**

### 🔧 **1. Preparación inicial**

1. **Activar el entorno de Python:**
   ```bash
   conda activate ./env
   ```

2. **Crear datos de prueba (IMPORTANTE - Solo la primera vez):**
   ```bash
   cd backend
   python create_test_data.py
   ```
   
   Esto creará:
   - ✅ Usuario admin: `admin@lowbarber.com` / `admin123`
   - ✅ Barberos de prueba con IDs UUID válidos
   - ✅ Servicios activos con precios y duración
   - ✅ Productos de ejemplo

3. **Iniciar el backend:**
   ```bash
   cd backend
   python app.py
   ```
   
   Deberías ver:
   ```
   * Running on http://127.0.0.1:5000
   * Debug mode: on
   ```

### 🧪 **2. Ejecutar las pruebas**

1. **Abrir el archivo de prueba:**
   - Abrir `test_reservations_integration.html` en tu navegador
   - O simplemente hacer doble clic en el archivo

2. **Seguir este orden de pruebas:**

   **Paso 1: Probar Conexión**
   - Clic en "🔌 Probar Conexión"
   - Debe mostrar: ✅ Conexión exitosa

   **Paso 2: Verificar datos básicos**
   - Clic en "✂️ Servicios" - Debe mostrar 4 servicios
   - Clic en "👨‍💼 Barberos" - Debe mostrar barberos disponibles

   **Paso 3: Autenticarse**
   - Email: `admin@lowbarber.com`
   - Password: `admin123`
   - Clic en "🔑 Iniciar Sesión"
   - Debe mostrar: ✅ Login exitoso

   **Paso 4: Probar reservas**
   - Clic en "📋 Obtener Reservas" - Puede estar vacío inicialmente
   - Clic en "➕ Crear Reserva" - Debe crear una reserva exitosamente

### ❌ **3. Solución de problemas comunes**

**Error: "❌ Error de conexión"**
- ✅ Verificar que el backend esté corriendo en `http://localhost:5000`
- ✅ Verificar que no haya otros procesos usando el puerto 5000

**Error: "❌ Error en login"**
- ✅ Ejecutar `python create_test_data.py` primero
- ✅ Verificar que uses `admin@lowbarber.com` / `admin123`

**Error: "❌ No hay barberos/servicios disponibles"**
- ✅ Ejecutar `python create_test_data.py` primero
- ✅ Verificar que la base de datos esté funcionando

**Error: "❌ Error al crear reserva"**
- ✅ Asegurarse de estar autenticado primero
- ✅ Verificar que hay barberos disponibles y activos
- ✅ Verificar que hay servicios activos

### 📊 **4. Datos de prueba creados**

**Usuarios:**
- `admin@lowbarber.com` / `admin123` (Administrador)
- `barbero@lowbarber.com` / `barbero123` (Barbero)
- `cliente@lowbarber.com` / `cliente123` (Cliente)

**Servicios:**
- Corte de Cabello - Bs 25.00 (30 min)
- Arreglo de Barba - Bs 15.00 (20 min)
- Corte + Barba - Bs 35.00 (45 min)
- Lavado de Cabello - Bs 10.00 (15 min)

**Barberos:**
- Pedro Martínez (Especialista en cortes modernos)
- Carlos Rivera (Maestro de la barba clásica)
- Juan Pérez (Experto en estilos vintage)

### 🎯 **5. Próximas pruebas**

Una vez que el sistema básico funcione, puedes probar:

1. **Frontend Vue.js completo:**
   ```bash
   cd frontend
   npm run dev
   ```
   Ir a: `http://localhost:5173/reservas`

2. **Panel administrativo:**
   Ir a: `http://localhost:5173/admin`

3. **Diferentes tipos de usuario:**
   - Probar con `barbero@lowbarber.com`
   - Probar con `cliente@lowbarber.com`

### 📝 **6. Logs útiles**

**Backend logs importantes:**
- `200` - Operación exitosa
- `400` - Error en los datos enviados
- `401` - No autenticado
- `404` - Endpoint no encontrado

**Frontend logs útiles:**
- El área "📜 Log de Eventos" muestra todas las operaciones
- La consola del navegador (F12) muestra detalles técnicos

---

## 🎉 **¡Listo!**

Si todas las pruebas pasan, el sistema de reservas está funcionando correctamente y conectado al backend.

**¿Problemas?** Revisar:
1. Backend corriendo en puerto 5000
2. Datos de prueba creados con `create_test_data.py`
3. Credenciales correctas para login
4. Logs del backend para errores específicos
