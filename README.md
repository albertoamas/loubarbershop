# 🪒 LOW BARBER - Sistema Web Completo

## 🔍 Descripción General

Sistema web completo y responsivo para la barbería Low Barber, que incluye:
- 🌐 **Sitio web público** con información de servicios y productos
- 📅 **Sistema de reservas en línea** con calendario interactivo
- 👑 **Panel administrativo completo** con estadísticas, reportes y gestión integral
- 📊 **Analytics avanzados** con exportación de datos y predicciones

## ⚖️ Stack Tecnológico

### Frontend:
- **Vue.js 3** + Vite (Composition API)
- **Tailwind CSS V4** (CSS-First Configuration)
- **Vue Router 4** + Guards de autenticación
- **Axios** + Interceptores JWT
- **FullCalendar.js** para calendario interactivo
- **Chart.js** + Vue-ChartJS para gráficos

### Backend:
- **Python 3.11** + Flask
- **Flask-RESTful** para API REST
- **Flask-JWT-Extended** para autenticación
- **Flask-CORS** para comunicación frontend-backend
- **SQLAlchemy** + PostgreSQL
- **Marshmallow** para validación y serialización

### Base de Datos:
- **PostgreSQL** con esquema completo
- Scripts de inicialización y datos de prueba

### Herramientas de Desarrollo:
- VS Code + GitHub Copilot
- Git + GitHub
- Miniconda para gestión de entornos

## 🚀 Guía de Instalación Rápida

### 📋 Prerrequisitos

1. **Git**: https://git-scm.com/download/win
2. **Node.js**: https://nodejs.org/ (versión LTS)
3. **Miniconda**: https://docs.conda.io/en/latest/miniconda.html
4. **PostgreSQL**: https://www.postgresql.org/download/windows/ (v15+)

### 📁 Paso 1: Clonar el Proyecto
```powershell
git clone https://github.com/albertoamas/loubarbershop.git
cd loubarbershop
```

### 🗄️ Paso 2: Configurar Base de Datos
```sql
# En psql como postgres:
CREATE DATABASE lowbarber_dev;
CREATE USER lowbarber_user WITH PASSWORD 'lowbarber_password';
GRANT ALL PRIVILEGES ON DATABASE lowbarber_dev TO lowbarber_user;
```

### 🐍 Paso 3: Configurar Backend
```powershell
# Crear y activar entorno virtual
conda create --prefix ./env python=3.11
conda activate ./env

# Instalar dependencias
cd backend
pip install -r requirements.txt

# Configurar variables de entorno
copy .env.example .env
# Editar .env con tus credenciales

# ¡COMANDO MÁGICO! - Configura toda la BD automáticamente
python setup_database.py
```

### 🎨 Paso 4: Configurar Frontend
```powershell
cd frontend
npm install
```

### ▶️ Paso 5: Ejecutar el Proyecto
```powershell
# Terminal 1 - Backend
cd backend
conda activate ../env
python app.py

# Terminal 2 - Frontend  
cd frontend
npm run dev
```

**¡Listo!** 🎉
- **Frontend**: http://localhost:5173/
- **Backend API**: http://127.0.0.1:5000/
- **Admin Panel**: http://localhost:5173/admin

## 🔐 Credenciales de Prueba

Después de ejecutar `python setup_database.py`:

### 👑 Administrador:
- **Email:** admin@lowbarber.com
- **Password:** admin123

### ✂️ Barberos:
- **Email:** carlos.mendoza@lowbarber.com / **Password:** barber123
- **Email:** miguel.rodriguez@lowbarber.com / **Password:** barber123

### 👤 Clientes:
- **Email:** juan.perez@example.com / **Password:** cliente123
- **Email:** maria.garcia@example.com / **Password:** cliente123

## 🎯 Funcionalidades del Sistema

### 🌐 **Sitio Web Público:**
- Página principal con información de la barbería
- Catálogo de servicios con precios y descripciones
- Catálogo de productos con sistema de búsqueda
- Sistema de reservas en línea
- Formulario de contacto

### 📅 **Sistema de Reservas:**
- Calendario interactivo con disponibilidad en tiempo real
- Selección de barbero, servicio y horario
- Gestión de estados (pendiente → confirmada → completada)
- Notificaciones y confirmaciones automáticas

### 👑 **Panel Administrativo Completo:**
- **Dashboard Principal**: Estadísticas en tiempo real con gráficos
- **Gestión de Reservas**: CRUD completo, cambio de estados, filtros avanzados
- **Gestión de Barberos**: Control de disponibilidad, horarios, especialidades
- **Gestión de Usuarios**: Roles, permisos, historiales detallados
- **Gestión de Servicios**: CRUD completo, categorías, precios
- **Gestión de Productos**: Inventario, stock, categorías, proveedores
- **Calendario Administrativo**: Vista interactiva con FullCalendar
- **Reportes y Analytics**: Exportación PDF/Excel, predicciones, KPIs

## 🛠️ Comandos Útiles

### Backend:
```powershell
# Configurar base de datos completa
python setup_database.py

# Verificar estructura de BD
python verify_structure.py

# Verificar conexión
python verify_db.py

# Crear datos adicionales
python create_test_data.py
```

### Frontend:
```powershell
# Desarrollo
npm run dev

# Producción
npm run build
npm run preview

# Linting
npm run lint
npm run format
```

## � Solución de Problemas Comunes

### ❌ Error: "psycopg2 no se instala"
```powershell
conda install psycopg2
```

### ❌ Error: "Puerto 5000 en uso" 
```powershell
# Cambiar puerto en backend/app.py
app.run(host='0.0.0.0', port=5001, debug=True)
```

### ❌ Error: "Base de datos no conecta"
```powershell
# Verificar que PostgreSQL esté corriendo
# Verificar credenciales en .env
# Verificar que la base de datos existe
```

### ❌ Error: "CORS en desarrollo"
```powershell
pip install flask-cors
```

## 📊 Estado del Proyecto

### ✅ **COMPLETADO:**
- ✅ Estructura base del proyecto
- ✅ Sistema de autenticación JWT completo
- ✅ API REST completa con validaciones
- ✅ Sitio web público responsive
- ✅ Sistema de reservas funcional
- ✅ Conexión Frontend-Backend
- ✅ **Panel Administrativo Completo:**
  - ✅ Dashboard con estadísticas y gráficos
  - ✅ Gestión de Barberos (CRUD + horarios)
  - ✅ Gestión de Reservas (estados + filtros)
  - ✅ Gestión de Usuarios (roles + permisos)
  - ✅ Gestión de Servicios (CRUD + categorías)
  - ✅ Gestión de Productos (inventario + stock)
  - ✅ Calendario Administrativo (FullCalendar)
  - ✅ Reportes y Analytics (exportación)

### 🎯 **PRÓXIMAS MEJORAS:**
- 🔄 Optimización de performance
- 🔔 Sistema de notificaciones por email
- 📱 App móvil con capacidades offline
- 🎨 Temas personalizables
- 🌍 Despliegue en producción

## 📁 Estructura del Proyecto

```
loubarbershop/
├── 📁 frontend/           # Vue.js 3 + Vite + Tailwind CSS V4
│   ├── src/
│   │   ├── components/    # Componentes reutilizables
│   │   ├── views/         # Páginas principales
│   │   │   ├── public/    # Sitio web público
│   │   │   └── admin/     # Panel administrativo
│   │   ├── router/        # Configuración de rutas
│   │   ├── services/      # Servicios API (Axios)
│   │   └── styles/        # Tailwind CSS personalizado
│   └── package.json
├── 📁 backend/            # Python + Flask + SQLAlchemy
│   ├── app/
│   │   ├── models/        # Modelos de base de datos
│   │   └── routes/        # Rutas de la API
│   ├── app.py            # Aplicación principal
│   ├── setup_database.py # Script de configuración automática
│   └── requirements.txt
└── 📁 database/          # PostgreSQL
    ├── schema.sql        # Estructura de tablas
    └── seed_data.sql     # Datos de prueba
```

## 📧 Contacto y Soporte

- **Desarrollador**: Alberto Amas
- **GitHub**: https://github.com/albertoamas/loubarbershop
- **Email**: [Tu email aquí]

---

**🎉 ¡Sistema completo y funcional!** El proyecto Low Barber está listo para producción con todas las funcionalidades implementadas y probadas.
