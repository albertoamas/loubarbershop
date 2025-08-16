// middleware/adminAuth.js - Middleware para proteger rutas administrativas
import { authService } from '@/services/authService'

export function requireAdmin(to, from, next) {
  // Verificar si el usuario está autenticado
  const isAuthenticated = authService.isAuthenticated()
  
  if (!isAuthenticated) {
    // Redirigir al login y recordar la ruta destino
    next({
      name: 'login',
      query: { redirect: to.fullPath }
    })
    return
  }

  // Obtener información del usuario actual
  const user = authService.getCurrentUser()
  
  // Verificar si el usuario tiene permisos de administrador
  // Verificar tanto 'rol' (backend) como 'role' (legacy)
  const userRole = user?.rol || user?.role
  
  if (!user || (userRole !== 'admin' && userRole !== 'ADMIN')) {
    // Redirigir a página principal con mensaje
    alert('Acceso denegado: Se requieren permisos de administrador')
    next({
      name: 'home',
      replace: true
    })
    return
  }

  // Usuario autenticado y autorizado, continuar
  next()
}

export function requireAuth(to, from, next) {
  if (!authService.isAuthenticated()) {
    next({
      name: 'login',
      query: { redirect: to.fullPath }
    })
    return
  }
  
  next()
}

export function redirectIfAuthenticated(to, from, next) {
  if (authService.isAuthenticated()) {
    const user = authService.getCurrentUser()
    
    // Redirigir según el rol del usuario
    if (user?.role === 'admin') {
      next({ name: 'admin-dashboard' })
    } else {
      next({ name: 'dashboard' })
    }
    return
  }
  
  next()
}
