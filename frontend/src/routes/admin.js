// routes/admin.js - Rutas del panel administrativo
import { requireAdmin } from '@/middleware/adminAuth'

// Importaciones lazy para optimizar la carga
const AdminLayout = () => import('@/views/admin/AdminLayout.vue')

// Vistas administrativas (se crearán en las siguientes fases)
const AdminDashboard = () => import('@/views/admin/AdminDashboard.vue')
const AdminReservas = () => import('@/views/admin/AdminReservas.vue')
const AdminBarberos = () => import('@/views/admin/AdminBarberos.vue')
const AdminUsuarios = () => import('@/views/admin/AdminUsuarios.vue')
const AdminServicios = () => import('@/views/admin/AdminServicios.vue')
const AdminProductos = () => import('@/views/admin/AdminProductos.vue')
const AdminCalendario = () => import('@/views/admin/AdminCalendario.vue')
const AdminReportes = () => import('@/views/admin/AdminReportes.vue')
const AdminConfiguracion = () => import('@/views/admin/AdminConfiguracion.vue')

export const adminRoutes = [
  {
    path: '/admin',
    component: AdminLayout,
    beforeEnter: requireAdmin,
    meta: {
      requiresAuth: true,
      requiresAdmin: true,
      title: 'Panel Administrativo'
    },
    children: [
      {
        path: '',
        name: 'admin-dashboard',
        component: AdminDashboard,
        meta: {
          title: 'Dashboard Administrativo',
          breadcrumb: 'Dashboard'
        }
      },
      {
        path: 'reservas',
        name: 'admin-reservas',
        component: AdminReservas,
        meta: {
          title: 'Gestión de Reservas',
          breadcrumb: 'Reservas'
        }
      },
      {
        path: 'barberos',
        name: 'admin-barberos',
        component: AdminBarberos,
        meta: {
          title: 'Gestión de Barberos',
          breadcrumb: 'Barberos'
        }
      },
      {
        path: 'usuarios',
        name: 'admin-usuarios',
        component: AdminUsuarios,
        meta: {
          title: 'Gestión de Usuarios',
          breadcrumb: 'Usuarios'
        }
      },
      {
        path: 'servicios',
        name: 'admin-servicios',
        component: AdminServicios,
        meta: {
          title: 'Gestión de Servicios',
          breadcrumb: 'Servicios'
        }
      },
      {
        path: 'productos',
        name: 'admin-productos',
        component: AdminProductos,
        meta: {
          title: 'Gestión de Productos',
          breadcrumb: 'Productos'
        }
      },
      {
        path: 'calendario',
        name: 'admin-calendario',
        component: AdminCalendario,
        meta: {
          title: 'Calendario Administrativo',
          breadcrumb: 'Calendario'
        }
      },
      {
        path: 'reportes',
        name: 'admin-reportes',
        component: AdminReportes,
        meta: {
          title: 'Reportes y Análisis',
          breadcrumb: 'Reportes'
        }
      },
      {
        path: 'configuracion',
        name: 'admin-configuracion',
        component: AdminConfiguracion,
        meta: {
          title: 'Configuración del Sistema',
          breadcrumb: 'Configuración'
        }
      }
    ]
  }
]

// Rutas de acceso denegado y errores
export const accessRoutes = [
  {
    path: '/access-denied',
    name: 'access-denied',
    component: () => import('@/views/errors/AccessDenied.vue'),
    meta: {
      title: 'Acceso Denegado'
    }
  },
  {
    path: '/admin-login',
    name: 'admin-login',
    component: () => import('@/views/auth/AdminLogin.vue'),
    meta: {
      title: 'Acceso Administrativo',
      requiresGuest: true
    }
  }
]
