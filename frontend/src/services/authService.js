/**
 * Low Barber - Servicio de Autenticación
 * Maneja login, registro y gestión de tokens
 */

import apiClient from './api.js'

export const authService = {
  /**
   * Iniciar sesión
   * @param {Object} credentials - { email, password }
   * @returns {Promise}
   */
  async login(credentials) {
    try {
      const response = await apiClient.post('/api/auth/login', credentials)
      
      if (response.data.access_token) {
        localStorage.setItem('authToken', response.data.access_token)
        localStorage.setItem('user', JSON.stringify(response.data.user))
      }
      
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al iniciar sesión')
    }
  },

  /**
   * Registrar nuevo usuario
   * @param {Object} userData - { name, email, password, phone }
   * @returns {Promise}
   */
  async register(userData) {
    try {
      // Asegurar que se incluya password_confirmation
      const registrationData = {
        ...userData,
        password_confirmation: userData.password_confirmation || userData.password
      }
      
      const response = await apiClient.post('/api/auth/register', registrationData)
      
      // Si el registro es exitoso y se devuelve un token, guardarlo
      if (response.data.access_token) {
        this.setToken(response.data.access_token)
        if (response.data.user) {
          this.setUser(response.data.user)
        }
      }
      
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al registrar usuario')
    }
  },

  /**
   * Cerrar sesión
   */
  logout() {
    localStorage.removeItem('authToken')
    localStorage.removeItem('user')
  },

  /**
   * Obtener usuario actual
   * @returns {Object|null}
   */
  getCurrentUser() {
    const user = localStorage.getItem('user')
    return user ? JSON.parse(user) : null
  },

  /**
   * Verificar si el usuario está autenticado
   * @returns {boolean}
   */
  isAuthenticated() {
    return !!localStorage.getItem('authToken')
  },

  /**
   * Obtener perfil del usuario
   * @returns {Promise}
   */
  async getProfile() {
    try {
      const response = await apiClient.get('/api/auth/profile')
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al obtener perfil')
    }
  },

  /**
   * Métodos de utilidad para desarrollo y pruebas
   */
  
  /**
   * Crear y autenticar administrador para pruebas
   */
  async loginAsAdmin() {
    try {
      // Usar el endpoint que fuerza la creación y login del admin
      console.log('🔐 Forzando creación y login de admin...')
      const response = await apiClient.post('/api/auth/force-admin-login')
      
      if (response.data.access_token) {
        localStorage.setItem('authToken', response.data.access_token)
        localStorage.setItem('user', JSON.stringify(response.data.user))
        console.log('✅ Admin creado y autenticado exitosamente:', response.data.user)
        return response.data
      } else {
        throw new Error('No se recibió token de acceso')
      }
      
    } catch (error) {
      console.error('❌ Error forzando admin login:', error)
      throw new Error('No se pudo autenticar como administrador: ' + error.message)
    }
  },

  /**
   * Simular login de barbero para pruebas
   */
  loginAsBarber() {
    const barberUser = {
      id: 2,
      nombre: 'Carlos Mendoza',
      email: 'carlos@lowbarber.com',
      telefono: '+1234567891',
      role: 'barbero',
      especialidad: 'Cortes clásicos y modernos',
      created_at: new Date().toISOString()
    }
    
    const fakeToken = 'fake-barber-token-' + Date.now()
    
    localStorage.setItem('authToken', fakeToken)
    localStorage.setItem('user', JSON.stringify(barberUser))
    
    window.dispatchEvent(new Event('authStateChanged'))
    
    return {
      access_token: fakeToken,
      user: barberUser
    }
  },

  /**
   * Simular login de cliente para pruebas
   */
  loginAsClient() {
    const clientUser = {
      id: 3,
      nombre: 'Juan Pérez',
      email: 'juan@cliente.com',
      telefono: '+1234567892',
      role: 'cliente',
      created_at: new Date().toISOString()
    }
    
    const fakeToken = 'fake-client-token-' + Date.now()
    
    localStorage.setItem('authToken', fakeToken)
    localStorage.setItem('user', JSON.stringify(clientUser))
    
    window.dispatchEvent(new Event('authStateChanged'))
    
    return {
      access_token: fakeToken,
      user: clientUser
    }
  },

  /**
   * Verificar si el usuario actual es administrador
   */
  isAdmin() {
    const user = this.getCurrentUser()
    return user && (user.role === 'admin' || user.rol === 'admin')
  },

  /**
   * Verificar si el usuario actual es barbero
   */
  isBarber() {
    const user = this.getCurrentUser()
    return user && (user.role === 'barbero' || user.rol === 'barbero')
  },

  /**
   * Verificar si el usuario actual es cliente
   */
  isClient() {
    const user = this.getCurrentUser()
    return user && (user.role === 'cliente' || user.rol === 'cliente')
  }
}

export default authService
