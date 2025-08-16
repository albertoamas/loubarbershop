import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { authService } from '../services/index.js'
import { adminRoutes } from '../routes/admin.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    // Si hay una posición guardada (como el botón atrás), la usamos
    if (savedPosition) {
      return savedPosition
    }
    // Si no, siempre vamos al top de la página
    return { top: 0 }
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { title: 'Inicio - Low Barber' }
    },
    {
      path: '/servicios',
      name: 'services',
      component: () => import('../views/ServicesView.vue'),
      meta: { title: 'Servicios - Low Barber' }
    },
    {
      path: '/productos',
      name: 'products',
      component: () => import('../views/ProductsView.vue'),
      meta: { title: 'Productos - Low Barber' }
    },
    {
      path: '/reservas',
      name: 'reservations',
      component: () => import('../views/ReservationsView.vue'),
      meta: { title: 'Reservas - Low Barber' }
    },
    {
      path: '/contacto',
      name: 'contact',
      component: () => import('../views/ContactView.vue'),
      meta: { title: 'Contacto - Low Barber' }
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
      meta: { title: 'Acerca de Nosotros - Low Barber' }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
      meta: { title: 'Iniciar Sesión - Low Barber' }
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue'),
      meta: { title: 'Registrarse - Low Barber' }
    },
    // Rutas administrativas
    ...adminRoutes,
    {
      path: '/:pathMatch(.*)*',
      name: 'notfound',
      component: () => import('../views/NotFoundView.vue'),
      meta: { title: 'Página no encontrada - Low Barber' }
    }
  ],
})

// Guard de navegación para proteger rutas que requieren autenticación
router.beforeEach(async (to, from, next) => {
  // Verificar si la ruta requiere autenticación
  if (to.meta.requiresAuth) {
    const isAuthenticated = authService.isAuthenticated()
    
    if (!isAuthenticated) {
      // Redirigir al login si no está autenticado
      next({ 
        name: 'login', 
        query: { redirect: to.fullPath } 
      })
      return
    }

    // Verificar si la ruta requiere permisos de administrador
    if (to.meta.requiresAdmin) {
      const user = authService.getCurrentUser()
      // Verificar tanto 'rol' (backend) como 'role' (legacy)
      const userRole = user?.rol || user?.role
      
      if (!user || (userRole !== 'admin' && userRole !== 'ADMIN')) {
        // Redirigir a acceso denegado si no es admin
        next({ 
          name: 'home',
          replace: true
        })
        return
      }
    }
  }
  
  next()
})

// Cambiar el título de la página según la ruta
router.afterEach((to) => {
  document.title = to.meta.title || 'Low Barber - Barbería Moderna'
})

export default router
