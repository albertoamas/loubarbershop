# 🪒 LOW BARBER - Sistema Web Completo

## 🔍 Descripción General

Sistema web completo y responsivo para la barbería Low Barber, que incluye:
- Sitio web público con información de servicios y productos
- Sistema de reservas en línea
- Panel administrativo con estadísticas, control de reservas, barberos y productos

## ⚖️ Stack Tecnológico

### Frontend:
- Vue.js 3 + Vite
- Tailwind CSS V4 (CSS-First Configuration)
- Vue Router
- Axios
- FullCalendar.js
- Chart.js

### Backend:
- Python + Flask
- Flask-RESTful
- Flask-JWT-Extended
- Flask-CORS
- SQLAlchemy
- Marshmallow

### Base de Datos:
- PostgreSQL

### Herramientas:
- VS Code + GitHub Copilot
- Git + GitHub
- Postman o Insomnia
- Miniconda

## 🚀 Instalación y Configuración

### Prerrequisitos:
```bash
# Instalar Miniconda si no lo tienes
# Descargar desde: https://docs.conda.io/en/latest/miniconda.html

# Instalar Node.js (para Vue.js)
# Descargar desde: https://nodejs.org/
```

### Configuración Backend (Python + Flask):
```bash
# Crear entorno virtual con miniconda
conda create --prefix ./env python=3.11

# Activar entorno
conda activate ./env

# Instalar dependencias base
pip install flask
pip install "psycopg[binary,pool]"

# Instalar dependencias adicionales (ejecutar después de Fase 3)
pip install flask-restful flask-jwt-extended flask-cors sqlalchemy marshmallow flask-marshmallow marshmallow-sqlalchemy python-dotenv
```

### Configuración Frontend (Vue.js + Vite):
```bash
# Navegar a la carpeta frontend (ejecutar después de Fase 1)
cd frontend

# Instalar dependencias
npm install

# Ejecutar en modo desarrollo
npm run dev
```

### Ejecución en modo desarrollo:
```bash
# Terminal 1 - Backend
conda activate ./env
flask --app app run
python app.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

## 🔐 Roles del Sistema

- **Cliente:** Puede registrarse y realizar reservas
- **Barbero:** Ve y gestiona sus propias reservas
- **Admin:** Gestiona todo (usuarios, reservas, productos, barberos, estadísticas)

## 📋 Plan de Desarrollo por Fases

### ▶️ FASE 1: Estructura Inicial del Proyecto
**Objetivo:** Crear la estructura base y configurar las herramientas

**Tareas:**
1. Crear estructura de carpetas:
   ```
   /frontend (Vue.js + Vite)
   /backend (Flask)
   /database (PostgreSQL scripts)
   ```

2. **Backend inicial:**
   - Crear `app.py` (archivo principal Flask)
   - Crear `requirements.txt`
   - Configurar estructura con Blueprints:
     ```
     /backend
       /app
         /models
         /routes
         /utils
         /static
         /templates
       app.py
       config.py
       requirements.txt
     ```

3. **Frontend inicial:**
   - Inicializar proyecto Vue 3 con Vite
   - Configurar Tailwind CSS V4 (CSS-First)
   - Crear estructura base:
     ```
     /frontend
       /src
         /components
         /views
         /router
         /services
         /utils
         /assets
         /styles
           app.css (con @theme)
       package.json
       vite.config.js
     ```

4. **Database:**
   - Crear `schema.sql`
   - Configurar scripts de inicialización

**Entregables:**
- Estructura completa de carpetas
- Proyecto Vue funcional con Tailwind
- Flask app básica ejecutándose

---

### ▶️ FASE 2: Sitio Web Público
**Objetivo:** Desarrollar la interfaz pública del sitio web

**Tareas:**
1. **Configurar Vue Router:**
   - Rutas: `/`, `/servicios`, `/productos`, `/reservas`, `/contacto`

2. **Crear componentes base:**
   - `Navbar.vue` - Navegación principal
   - `Footer.vue` - Pie de página
   - `Hero.vue` - Sección principal
   - `ServiceCard.vue` - Tarjeta de servicio
   - `ProductCard.vue` - Tarjeta de producto

3. **Desarrollar vistas:**
   - `Home.vue` - Página de inicio
   - `Services.vue` - Lista de servicios
   - `Products.vue` - Catálogo de productos
   - `Reservations.vue` - Formulario de reservas
   - `Contact.vue` - Información de contacto

4. **Implementar diseño responsivo:**
   - Mobile-first design
   - Breakpoints: sm, md, lg, xl
   - Componentes adaptativos

5. **Formulario de reservas inicial:**
   - Campos: nombre, email, teléfono, servicio, fecha, hora, barbero
   - Validaciones básicas
   - Diseño atractivo

**Entregables:**
- Sitio web público completamente funcional
- Navegación fluida entre páginas
- Diseño responsivo en todos los dispositivos
- Formulario de reservas (sin backend aún)

---

### ▶️ FASE 3: Backend Base + Base de Datos
**Objetivo:** Crear la estructura backend y modelos de datos

**Tareas:**
1. **Configurar Flask con SQLAlchemy:**
   - Archivo `config.py` con configuraciones
   - Conexión a PostgreSQL
   - Configuración de entornos (dev, prod)

2. **Crear modelos de datos:**
   ```python
   # models/user.py
   class User:
       - id, nombre, email, teléfono, password_hash, rol, created_at
   
   # models/barber.py
   class Barber:
       - id, nombre, especialidad, disponible, user_id, created_at
   
   # models/service.py
   class Service:
       - id, nombre, descripción, precio, duración, activo
   
   # models/product.py
   class Product:
       - id, nombre, descripción, precio, stock, imagen, activo
   
   # models/reservation.py
   class Reservation:
       - id, user_id, barber_id, service_id, fecha, hora, estado, notas
   ```

3. **Configurar Blueprints:**
   - `routes/auth.py` - Autenticación
   - `routes/reservations.py` - Gestión de reservas
   - `routes/users.py` - Gestión de usuarios
   - `routes/products.py` - Gestión de productos
   - `routes/admin.py` - Panel administrativo

4. **Database setup:**
   - Crear `schema.sql` con todas las tablas
   - Script de migración inicial
   - Datos de prueba (seeders)

5. **Configurar Flask-CORS:**
   - Permitir peticiones desde frontend
   - Configurar headers apropiados

**Entregables:**
- Base de datos PostgreSQL configurada
- Modelos SQLAlchemy funcionales
- Estructura de Blueprints
- Conexión backend-database operativa

---

### ▶️ FASE 4: Sistema de Autenticación y Roles
**Objetivo:** Implementar autenticación JWT y sistema de permisos

**Tareas:**
1. **Configurar Flask-JWT-Extended:**
   - Configuración de tokens
   - Tiempos de expiración
   - Refresh tokens

2. **Crear sistema de autenticación:**
   - Endpoint `/auth/register`
   - Endpoint `/auth/login`
   - Endpoint `/auth/logout`
   - Endpoint `/auth/refresh`

3. **Implementar roles y permisos:**
   - Decoradores para proteger rutas
   - Middleware de autorización
   - Validación de roles por endpoint

4. **Validaciones con Marshmallow:**
   - Schemas para registro/login
   - Validación de datos de entrada
   - Serialización de respuestas

5. **Manejo de errores:**
   - Respuestas JSON estandarizadas
   - Códigos de error apropiados
   - Logging de errores

**Entregables:**
- Sistema de autenticación JWT completo
- Roles y permisos funcionando
- Validaciones robustas
- Manejo de errores profesional

---

### ▶️ FASE 5: API REST Completa
**Objetivo:** Desarrollar todos los endpoints de la API

**Tareas:**
1. **Endpoints de Usuarios:**
   - `GET /api/users` - Listar usuarios (admin)
   - `GET /api/users/profile` - Perfil del usuario
   - `PUT /api/users/profile` - Actualizar perfil
   - `DELETE /api/users/:id` - Eliminar usuario (admin)

2. **Endpoints de Reservas:**
   - `GET /api/reservations` - Listar reservas
   - `POST /api/reservations` - Crear reserva
   - `PUT /api/reservations/:id` - Actualizar reserva
   - `DELETE /api/reservations/:id` - Cancelar reserva
   - `GET /api/reservations/availability` - Consultar disponibilidad

3. **Endpoints de Barberos:**
   - `GET /api/barbers` - Listar barberos
   - `POST /api/barbers` - Crear barbero (admin)
   - `PUT /api/barbers/:id` - Actualizar barbero
   - `DELETE /api/barbers/:id` - Eliminar barbero

4. **Endpoints de Productos:**
   - `GET /api/products` - Listar productos
   - `POST /api/products` - Crear producto (admin)
   - `PUT /api/products/:id` - Actualizar producto
   - `DELETE /api/products/:id` - Eliminar producto

5. **Endpoints de Servicios:**
   - `GET /api/services` - Listar servicios
   - `POST /api/services` - Crear servicio (admin)
   - `PUT /api/services/:id` - Actualizar servicio
   - `DELETE /api/services/:id` - Eliminar servicio

6. **Endpoints de Estadísticas:**
   - `GET /api/stats/dashboard` - Estadísticas generales
   - `GET /api/stats/reservations` - Estadísticas de reservas
   - `GET /api/stats/revenue` - Estadísticas de ingresos

**Entregables:**
- API REST completa y documentada
- Todas las operaciones CRUD
- Validaciones y permisos por endpoint
- Respuestas JSON estandarizadas

---

### ▶️ FASE 6: Sistema de Reservas
**Objetivo:** Implementar el sistema completo de reservas y gestión de horarios

**Tareas:**
1. **Crear modelo de Reserva:**
   - Estados: pendiente, confirmada, en_proceso, completada, cancelada
   - Relaciones con User, Barber, Service
   - Validaciones de fecha/hora
   - Notas adicionales

2. **Sistema de disponibilidad:**
   - Horarios de trabajo por barbero
   - Bloqueo de horarios ocupados
   - Validación de solapamientos
   - Consulta de horarios disponibles

3. **API REST de Reservas:**
   - `GET /api/reservations` - Listar reservas (filtros por usuario/barbero/fecha)
   - `POST /api/reservations` - Crear nueva reserva
   - `PUT /api/reservations/:id` - Actualizar reserva
   - `DELETE /api/reservations/:id` - Cancelar reserva
   - `GET /api/reservations/availability` - Consultar disponibilidad por barbero/fecha
   - `POST /api/reservations/:id/confirm` - Confirmar reserva
   - `POST /api/reservations/:id/complete` - Marcar como completada

4. **Validaciones avanzadas:**
   - Horario de trabajo del barbero
   - No permitir reservas en el pasado
   - Duración del servicio
   - Límite de reservas por cliente
   - Tiempo mínimo de anticipación

5. **Notificaciones básicas:**
   - Logs de cambios de estado
   - Preparación para emails futuros

**Entregables:**
- Sistema de reservas completamente funcional
- API REST con todas las validaciones
- Gestión de estados y disponibilidad
- Base sólida para el frontend

---

### ▶️ FASE 7: Conexión Frontend-Backend
**Objetivo:** Integrar Vue.js con la API usando Axios

**Tareas:**
1. **Configurar Axios:**
   - Instancia base de Axios
   - Interceptores para tokens JWT
   - Manejo de errores globales

2. **Crear servicios API:**
   - `services/authService.js` - Autenticación
   - `services/reservationService.js` - Reservas
   - `services/userService.js` - Usuarios
   - `services/productService.js` - Productos
   - `services/barberService.js` - Barberos

3. **Gestión de estado global:**
   - Store para autenticación
   - Store para datos del usuario
   - Store para reservas

4. **Implementar autenticación en frontend:**
   - Componentes de login/registro
   - Protección de rutas
   - Manejo de tokens

5. **Conectar formularios:**
   - Formulario de reservas funcional
   - Formulario de contacto
   - Validaciones en tiempo real

6. **Manejo de errores y loading:**
   - Spinner de carga
   - Mensajes de error
   - Notificaciones de éxito

**Entregables:**
- Frontend completamente conectado al backend
- Autenticación funcional
- Formularios operativos
- Manejo de estados profesional

---

### ▶️ FASE 8: Panel Administrativo - Desarrollo Modular
**Objetivo:** Desarrollar el panel administrativo de forma incremental y sólida

---

### ▶️ FASE 8.1: Base del Panel Administrativo
**Objetivo:** Crear la infraestructura base y layout del panel admin

**Tareas:**
1. **Layout Administrativo Base:**
   - `AdminLayout.vue` con sidebar responsivo
   - Header con información del usuario y logout
   - Navegación lateral con iconos y rutas
   - Diseño responsive para móvil/desktop

2. **Protección de Rutas:**
   - Guards de autenticación para rutas admin
   - Verificación de rol de administrador
   - Redirección automática si no autorizado

3. **Componentes Base Administrativos:**
   - `AdminCard.vue` - Tarjetas para estadísticas
   - `AdminTable.vue` - Tabla reutilizable con filtros
   - `AdminModal.vue` - Modal para formularios
   - `AdminButton.vue` - Botones con estilos admin

4. **Tema Visual Administrativo:**
   - Variables CSS específicas para admin
   - Paleta de colores profesional
   - Tipografía y espaciado consistente

**Entregables:**
- Layout administrativo funcional
- Protección de rutas implementada
- Componentes base reutilizables
- Navegación entre secciones admin

**Tiempo estimado:** 1-2 días

---

### ▶️ FASE 8.2: Dashboard Principal y Estadísticas
**Objetivo:** Crear el dashboard principal con métricas clave

**Tareas:**
1. **Vista Dashboard Principal:**
   - `AdminDashboard.vue` como página principal
   - Grid responsivo para cards de estadísticas
   - Overview de métricas importantes

2. **Estadísticas Básicas:**
   - Total de reservas del mes
   - Total de clientes registrados
   - Total de barberos activos
   - Ingresos del mes actual

3. **Gráficos con Chart.js:**
   - Gráfico de reservas por mes (últimos 6 meses)
   - Gráfico de servicios más populares
   - Gráfico de ingresos por mes

4. **API de Estadísticas:**
   - Conectar con `statsService.js`
   - Manejo de estados de carga
   - Cache de datos por tiempo determinado

**Entregables:**
- Dashboard principal funcional
- Estadísticas visuales implementadas
- Gráficos interactivos con Chart.js
- Conexión con API de estadísticas

**Tiempo estimado:** 2-3 días

---

### ▶️ FASE 8.3: Gestión de Barberos
**Objetivo:** CRUD completo para gestionar barberos

**Tareas:**
1. **Vista AdminBarbers:**
   - Lista/tabla de barberos con información clave
   - Búsqueda y filtros (activo/inactivo)
   - Paginación para listas grandes

2. **Formularios de Barbero:**
   - Modal para crear nuevo barbero
   - Modal para editar barbero existente
   - Validaciones del lado cliente

3. **Funcionalidades CRUD:**
   - Crear barbero (con asignación de usuario)
   - Editar información del barbero
   - Activar/desactivar barbero
   - Eliminar barbero (con confirmación)

4. **Gestión de Disponibilidad:**
   - Configurar horarios de trabajo
   - Días de trabajo por barbero
   - Estados: disponible/no disponible

**Entregables:**
- Gestión completa de barberos
- Formularios de creación/edición
- Sistema de disponibilidad
- Validaciones robustas

**Tiempo estimado:** 3-4 días

---

### ▶️ FASE 8.4: Gestión de Reservas
**Objetivo:** Panel completo para administrar reservas

**Tareas:**
1. **Vista AdminReservations:**
   - Tabla de reservas con toda la información
   - Filtros avanzados (fecha, barbero, estado, cliente)
   - Búsqueda por nombre de cliente o barbero

2. **Estados de Reserva:**
   - Cambio de estados: pendiente → confirmada → completada
   - Cancelación de reservas con motivo
   - Historial de cambios de estado

3. **Acciones Masivas:**
   - Selección múltiple de reservas
   - Cambio de estado en lote
   - Exportar reservas a CSV

4. **Detalles de Reserva:**
   - Modal con información completa
   - Edición de datos de la reserva
   - Notas administrativas

**Entregables:**
- Sistema completo de gestión de reservas
- Estados y flujos de trabajo
- Acciones masivas implementadas
- Interfaz intuitiva para administradores

**Tiempo estimado:** 4-5 días

---

### ▶️ FASE 8.5: Calendario Administrativo
**Objetivo:** Vista de calendario interactiva con FullCalendar

**Tareas:**
1. **Integración FullCalendar:**
   - Vista mensual, semanal y diaria
   - Eventos de reservas por barbero
   - Colores distintivos por barbero

2. **Interactividad del Calendario:**
   - Click en evento para ver detalles
   - Arrastrar y soltar para reprogramar
   - Crear nueva reserva desde calendario

3. **Filtros del Calendario:**
   - Mostrar/ocultar barberos específicos
   - Filtrar por tipo de servicio
   - Vista de reservas por estado

4. **Navegación Temporal:**
   - Navegación entre meses/semanas
   - Salto rápido a fecha específica
   - Vista de disponibilidad en tiempo real

**Entregables:**
- Calendario interactivo funcional
- Gestión visual de reservas
- Reprogramación mediante drag & drop
- Filtros y vistas personalizables

**Tiempo estimado:** 3-4 días

---

### ▶️ FASE 8.6: Gestión de Usuarios y Clientes
**Objetivo:** Administración completa de usuarios del sistema

**Tareas:**
1. **Vista AdminUsers:**
   - Lista de todos los usuarios registrados
   - Información detallada por usuario
   - Filtros por rol (cliente, barbero, admin)

2. **Gestión de Roles:**
   - Cambio de roles de usuario
   - Promoción cliente → barbero → admin
   - Permisos y restricciones por rol

3. **Historial de Cliente:**
   - Reservas históricas por cliente
   - Servicios más utilizados
   - Estadísticas de cada cliente

4. **Acciones de Usuario:**
   - Activar/desactivar cuentas
   - Reset de contraseñas
   - Eliminación de cuentas (con confirmación)

**Entregables:**
- Gestión completa de usuarios
- Sistema de roles funcional
- Historiales detallados por cliente
- Herramientas de administración de cuentas

**Tiempo estimado:** 3-4 días

---

### ✅ FASE 8.7: Gestión de Servicios y Productos (Admin) - COMPLETADA
**Objetivo:** CRUD administrativo para servicios y productos

**Tareas:**
1. **AdminServices:**
   - CRUD completo de servicios
   - Gestión de precios y duración
   - Activar/desactivar servicios

2. **AdminProducts:**
   - CRUD completo de productos
   - Gestión de stock e inventario
   - Subida y gestión de imágenes

3. **Categorización:**
   - Categorías para productos
   - Agrupación de servicios
   - Organización del catálogo

4. **Reportes:**
   - Servicios más populares
   - Productos más vendidos
   - Análisis de rentabilidad

**Entregables:**
- Gestión completa de servicios
- Administración de productos con inventario
- Sistema de categorías
- Reportes de popularidad y ventas

**Tiempo estimado:** 4-5 días

**COMPLETADO:**
- ✅ AdminServicios.vue implementado con CRUD completo
- ✅ serviceService.js extendido con métodos administrativos y estadísticas
- ✅ AdminProductos.vue implementado con gestión completa de inventario
- ✅ productService.js creado con CRUD, stock y operaciones masivas
- ✅ Sistema de categorías para servicios (Cortes, Barbas, Tratamientos, Combos)
- ✅ Sistema de categorías para productos (Cuidado Capilar, Styling, etc.)
- ✅ Gestión de imágenes con upload y preview
- ✅ Control de stock con alertas de stock bajo y agotado
- ✅ Cálculo automático de márgenes de ganancia
- ✅ Estadísticas de ventas y rotación de productos
- ✅ Operaciones masivas (actualizar stock, cambiar estado, eliminar)
- ✅ Filtros avanzados por categoría, estado, stock y proveedor

---

### ✅ FASE 8.8: Reportes y Estadísticas Avanzadas - COMPLETADA
**Objetivo:** Sistema completo de reportes y analytics

**Tareas:**
1. **Reportes Financieros:**
   - Ingresos por período
   - Análisis de rentabilidad por barbero
   - Comparativas mes a mes

2. **Reportes Operacionales:**
   - Ocupación por barbero
   - Horarios más demandados
   - Servicios con mayor demanda

3. **Exportación de Datos:**
   - Reportes en PDF
   - Exportación a Excel/CSV
   - Gráficos imprimibles

4. **Analytics Avanzados:**
   - Tendencias de reservas
   - Predicciones de demanda
   - KPIs del negocio

**Entregables:**
- Sistema completo de reportes
- Exportación en múltiples formatos
- Analytics avanzados
- Herramientas de toma de decisiones

**Tiempo estimado:** 3-4 días

**COMPLETADO:**
- ✅ reportService.js implementado con todas las APIs de reportes avanzados
- ✅ ReportCard.vue componente reutilizable para tarjetas de reportes
- ✅ AdvancedChart.vue componente para gráficos interactivos con Chart.js
- ✅ ExportService.js servicio completo para exportación en múltiples formatos
- ✅ AdminReportes.vue vista completa con 4 pestañas principales:
  - ✅ KPIs y Métricas (6 indicadores clave con tendencias)
  - ✅ Reportes Financieros (análisis completo de ingresos y rentabilidad)
  - ✅ Reportes Operacionales (ocupación, horarios pico, demanda)
  - ✅ Analytics Avanzados (tendencias y predicciones)
- ✅ Sistema de exportación a PDF, Excel y CSV funcional
- ✅ Gráficos interactivos con Chart.js (líneas, barras, donut, radar)
- ✅ Controles de período temporal para todos los reportes
- ✅ Datos de fallback completos para desarrollo sin backend
- ✅ Interfaz responsiva y profesional para análisis de datos
- ✅ KPIs visuales con indicadores de progreso y tendencias
- ✅ Botón de reporte completo para generar PDFs consolidados

---

**Resumen FASE 8 - Panel Administrativo Completo:**
- **Total estimado:** 23-31 días de desarrollo
- **8 sub-fases modulares** y bien definidas
- **Desarrollo incremental** con entregables por fase
- **Base sólida** para futuras expansiones
- **Testing** incluido en cada sub-fase

---

### ▶️ FASE 9: Módulo de Productos
**Objetivo:** Completar la funcionalidad de productos

**Tareas:**
1. **Catálogo público:**
   - Grid de productos responsivo
   - Filtros por categoría
   - Búsqueda de productos
   - Detalles de producto

2. **CRUD administrativo:**
   - Gestión completa de productos
   - Subida de imágenes
   - Gestión de stock
   - Categorías de productos

3. **Integración con reservas:**
   - Venta de productos en reservas
   - Inventory management
   - Reportes de ventas

**Entregables:**
- Catálogo de productos funcional
- Administración completa
- Integración con el sistema

---

### ▶️ FASE 10: Pulido y Despliegue
**Objetivo:** Optimizar, testear y desplegar la aplicación

**Tareas:**
1. **Optimización Frontend:**
   - Optimización de imágenes
   - Lazy loading
   - Code splitting
   - Build para producción

2. **Optimización Backend:**
   - Optimización de consultas
   - Caching
   - Compresión de respuestas
   - Rate limiting

3. **Testing:**
   - Tests unitarios (backend)
   - Tests de integración
   - Tests E2E (frontend)

4. **Seguridad:**
   - Validación de inputs
   - Sanitización de datos
   - Headers de seguridad
   - Configuración HTTPS

5. **Despliegue:**
   - **Backend:** Render, Railway, o Heroku
   - **Frontend:** Vercel, Netlify, o Firebase Hosting
   - **Base de datos:** PostgreSQL en la nube
   - Variables de entorno
   - CI/CD pipeline

6. **Documentación:**
   - Documentación de API
   - Guía de usuario
   - Guía de administrador

**Entregables:**
- Aplicación optimizada y segura
- Despliegue en producción
- Documentación completa
- Sistema listo para usuarios

---

## 🎯 Comandos Pendientes de Ejecutar

**Después de la Fase 1:**
```bash
# Instalar dependencias adicionales del backend
pip install flask-restful flask-jwt-extended flask-cors sqlalchemy marshmallow flask-marshmallow marshmallow-sqlalchemy python-dotenv

# Crear proyecto Vue en frontend
npm create vue@latest frontend
cd frontend
npm install

# Instalar Tailwind CSS V4 (nueva sintaxis)
npm install tailwindcss @tailwindcss/vite

# Instalar otras dependencias
npm install axios vue-router@4
npm install @fullcalendar/vue3 @fullcalendar/core @fullcalendar/daygrid @fullcalendar/timegrid @fullcalendar/interaction
npm install chart.js vue-chartjs
```

## 📝 Notas Importantes

- Mantener siempre el entorno conda activado al trabajar con backend
- Usar GitHub para control de versiones desde la Fase 1
- Realizar commits frecuentes y descriptivos
- Seguir el flujo de trabajo por fases estrictamente
- Mantener separación clara entre frontend y backend
- Aplicar buenas prácticas de seguridad desde el inicio
- **IMPORTANTE:** Tailwind CSS V4 usa configuración CSS-First (no tailwind.config.js)
- **NUEVO:** Personalización con @theme en archivos CSS
- **NUEVO:** Instalación con @tailwindcss/vite plugin

---

## 🎨 Configuración Tailwind CSS V4

### **Archivo vite.config.js:**
```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    vue(),
    tailwindcss()
  ]
})
```

### **Archivo src/styles/app.css:**
```css
@import "tailwindcss";

@theme {
  /* Colores de la barbería */
  --color-barber-primary: oklch(0.2 0.1 240);
  --color-barber-secondary: oklch(0.8 0.15 60);
  --color-barber-accent: oklch(0.6 0.2 30);
  
  /* Fuentes */
  --font-display: "Playfair Display", serif;
  --font-body: "Inter", sans-serif;
  
  /* Espaciado personalizado */
  --spacing-section: 5rem;
  --spacing-card: 1.5rem;
  
  /* Breakpoints personalizados */
  --breakpoint-tablet: 768px;
  --breakpoint-desktop: 1024px;
}
```

---

**Estado actual:** ✅ FASE 7 COMPLETADA - Frontend-Backend integración completa funcionando
                ✅ FASE 8.1 COMPLETADA - Base del Panel Administrativo implementada
                ✅ FASE 8.2 COMPLETADA - Dashboard Principal y Estadísticas implementado
                ✅ FASE 8.3 COMPLETADA - Gestión de Barberos (CRUD completo, disponibilidad)
                ✅ FASE 8.4 COMPLETADA - Gestión de Reservas (estados, filtros, acciones masivas)
                ✅ FASE 8.5 COMPLETADA - Calendario Administrativo (FullCalendar, drag & drop)
                ✅ FASE 8.6 COMPLETADA - Gestión de Usuarios y Clientes (roles, historiales)
                ✅ FASE 8.7 COMPLETADA - Gestión de Servicios y Productos (CRUD, inventario)
                ✅ FASE 8.8 COMPLETADA - Reportes y Estadísticas Avanzadas (analytics, exportación)

🎯 **ANÁLISIS DEL FRONTEND EXISTENTE:**
- ✅ Vue.js 3 + Vite configurado
- ✅ Tailwind CSS v4 (CSS-First) implementado
- ✅ Vue Router con rutas completas + rutas administrativas
- ✅ Axios + interceptores JWT configurados
- ✅ authService, reservationService, barberService, serviceService, userService implementados
- ✅ productService creado y conectado
- ✅ statsService para panel administrativo creado
- ✅ FullCalendar.js integrado para calendario administrativo
- ✅ Componentes base (Navbar, Footer, Cards)
- ✅ Vistas completas (Home, Services, Products, Reservations)
- ✅ ServicesView conectado con backend real + fallback
- ✅ ProductsView conectado con backend real + fallback
- ✅ Sistema de autenticación preparado

**NUEVO PLAN FASE 8 - Desarrollo Modular del Panel Admin:**
- ✅ **FASE 8.1:** Base del Panel Administrativo (Layout, rutas, componentes base)
- ✅ **FASE 8.2:** Dashboard Principal y Estadísticas (métricas, Chart.js)
- ✅ **FASE 8.3:** Gestión de Barberos (CRUD completo, disponibilidad)
- ✅ **FASE 8.4:** Gestión de Reservas (estados, filtros, acciones masivas)
- ✅ **FASE 8.5:** Calendario Administrativo (FullCalendar, drag & drop)
- ✅ **FASE 8.6:** Gestión de Usuarios y Clientes (roles, historiales)
- ✅ **FASE 8.7:** Gestión de Servicios y Productos Admin (CRUD, inventario)
- ✅ **FASE 8.8:** Reportes y Estadísticas Avanzadas (analytics, exportación)
- ⏳ **PRÓXIMA FASE:** FASE 9 - Módulo de Productos (catálogo público)

**PROGRESO FASE 8.1 COMPLETADO:**
- ✅ AdminLayout.vue con sidebar responsivo y navegación completa
- ✅ AdminCard.vue para estadísticas y métricas
- ✅ AdminTable.vue con filtros, paginación y selección múltiple
- ✅ AdminModal.vue para formularios y confirmaciones
- ✅ AdminButton.vue con múltiples variantes
- ✅ Middleware de protección de rutas (adminAuth.js)
- ✅ Configuración de rutas administrativas completas
- ✅ Tema administrativo profesional (adminTheme.js)

**PROGRESO FASE 8.2 COMPLETADO:**
- ✅ Chart.js y vue-chartjs instalados
- ✅ AdminDashboard.vue implementado con estadísticas y gráficos
- ✅ Vistas placeholder para todas las secciones admin
- ✅ Router actualizado con rutas administrativas
- ✅ Dashboard principal funcional con métricas visuales y Chart.js

**PROGRESO FASE 8.3 COMPLETADO:**
- ✅ AdminBarberos.vue implementado con CRUD completo
- ✅ barberService actualizado con métodos completos (estadísticas, disponibilidad, horarios)
- ✅ Formularios de creación y edición de barberos
- ✅ Gestión de disponibilidad y horarios de trabajo
- ✅ Tabla con filtros avanzados y acciones masivas
- ✅ Sistema de validaciones y confirmaciones

**PROGRESO FASE 8.4 COMPLETADO:**
- ✅ AdminReservas.vue implementado con gestión completa de estados
- ✅ reservationService actualizado con métodos de estadísticas y acciones masivas
- ✅ Filtros avanzados por estado, barbero, servicio y fechas
- ✅ Modal de detalles con información completa y historial de cambios
- ✅ Flujo de estados (pendiente → confirmada → en progreso → completada)
- ✅ Acciones masivas (confirmar, completar, cancelar, exportar)
- ✅ Sistema de exportación y búsqueda avanzada

**PROGRESO FASE 8.6 COMPLETADO:**
- ✅ AdminUsuarios.vue implementado con gestión completa de usuarios y clientes
- ✅ Sistema de roles y permisos (cliente, barbero, administrador)
- ✅ Filtros avanzados por rol, estado, fecha de registro y búsqueda
- ✅ Modal de historial detallado por cliente con estadísticas y reservas
- ✅ Acciones de usuario (activar/desactivar, editar, eliminar)
- ✅ Acciones masivas (cambio de estado, cambio de rol, eliminación)
- ✅ userService extendido con métodos administrativos completos
- ✅ Sistema de creación/edición con información específica por rol
- ✅ Gestión de barberos con especialidades y experiencia
- ✅ Tabla con avatar, información detallada y estadísticas por usuario
- ✅ Paginación completa con navegación y resumen de resultados
- ✅ Reset de contraseñas y gestión de cuentas administrativas
- ✅ Datos de fallback para desarrollo sin backend
- ✅ Integración con componentes base AdminCard, AdminTable, AdminModal

**PROGRESO FASE 8.8 COMPLETADO:**
- ✅ reportService.js implementado con APIs completas para todos los tipos de reportes
- ✅ ReportCard.vue componente reutilizable con controles de exportación y períodos
- ✅ AdvancedChart.vue componente para gráficos interactivos con Chart.js avanzado
- ✅ ExportService.js servicio completo para exportación (PDF, Excel, CSV, imágenes)
- ✅ AdminReportes.vue vista completa con sistema de pestañas profesional
- ✅ KPIs y Métricas: 6 indicadores clave con visualización de progreso y tendencias
- ✅ Reportes Financieros: análisis completo de ingresos, gastos, rentabilidad por barbero
- ✅ Reportes Operacionales: ocupación por barbero, análisis de horarios pico, demanda de servicios
- ✅ Analytics Avanzados: tendencias de reservas, predicciones de demanda con recomendaciones
- ✅ Sistema de exportación completo (PDF, Excel, CSV) con generación automática de nombres
- ✅ Gráficos interactivos con controles (tipos, leyenda, descarga, pantalla completa)
- ✅ Datos de fallback profesionales para desarrollo sin backend
- ✅ Controles globales de período temporal para todos los reportes
- ✅ Botón flotante para generar reporte completo consolidado
- ✅ Interfaz completamente responsiva y optimizada para móviles
- ✅ Integración perfecta con componentes administrativos existentes

**RESUMEN FASE 8 - Panel Administrativo Completo:**
- **Total implementado:** 8 sub-fases completadas exitosamente
- **Desarrollo modular:** Cada sub-fase completamente funcional e independiente
- **Componentes creados:** 15+ componentes reutilizables de alta calidad
- **Servicios implementados:** 8 servicios completos con datos de fallback
- **Funcionalidades:** CRUD completo, estadísticas, reportes, exportación, analytics
- **Calidad de código:** Arquitectura profesional lista para producción
- **Escalabilidad:** Base sólida para futuras expansiones y mejoras

**VENTAJAS DEL NUEVO PLAN MODULAR:**
- 🎯 **Desarrollo incremental:** Cada sub-fase es completamente funcional
- 🔧 **Testing por módulos:** Cada parte se prueba antes de continuar
- 📈 **Entregas frecuentes:** Se puede mostrar progreso real cada 2-4 días
- 🛠️ **Mejor arquitectura:** Componentes reutilizables y código mantenible
- 🚀 **Escalabilidad:** Fácil agregar nuevas funcionalidades

**MEJORAS RECIENTES:**
- ✅ productService.js implementado con CRUD completo
- ✅ ServicesView ya tenía conexión con backend
- ✅ ProductsView actualizado con conexión real al backend
- ✅ Sistema de fallback para datos cuando falla la API
- ✅ Estados de loading y error en ambas vistas
- ✅ Búsqueda y filtros funcionales para productos
- ✅ Plan modular creado para desarrollo sostenible del panel admin
- ✅ Dashboard administrativo con gráficos Chart.js implementado
- ✅ Sistema completo de componentes administrativos reutilizables
