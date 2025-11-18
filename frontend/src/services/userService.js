/**
 * Low Barber - Servicio de Usuarios
 * Maneja operaciones relacionadas con usuarios
 */

import apiClient from './api.js'

export const userService = {
  /**
   * Obtener todos los usuarios
   * @returns {Promise}
   */
  async getUsers() {
    try {
      const response = await apiClient.get('/api/users')
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al obtener usuarios')
    }
  },

  /**
   * Obtener usuario por ID
   * @param {string} id - ID del usuario
   * @returns {Promise}
   */
  async getUser(id) {
    try {
      const response = await apiClient.get(`/api/users/${id}`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al obtener usuario')
    }
  },

  /**
   * Obtener perfil del usuario actual
   * @returns {Promise}
   */
  async getCurrentUser() {
    try {
      const response = await apiClient.get('/api/auth/me')
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al obtener perfil de usuario')
    }
  },

  /**
   * Actualizar perfil del usuario actual
   * @param {Object} userData - datos del usuario
   * @returns {Promise}
   */
  async updateCurrentUser(userData) {
    try {
      const response = await apiClient.put('/api/auth/me', userData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al actualizar perfil')
    }
  },

  /**
   * Actualizar usuario específico
   * @param {string} id - ID del usuario
   * @param {Object} data - datos a actualizar
   * @returns {Promise}
   */
  async updateUser(id, data) {
    try {
      const response = await apiClient.put(`/api/users/${id}`, data)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al actualizar usuario')
    }
  },

  /**
   * Eliminar usuario
   * @param {string} id - ID del usuario
   * @returns {Promise}
   */
  async deleteUser(id) {
    try {
      const response = await apiClient.delete(`/api/users/${id}`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al eliminar usuario')
    }
  },

  /**
   * Cambiar contraseña del usuario actual
   * @param {Object} passwordData - datos de contraseña actual y nueva
   * @returns {Promise}
   */
  async changePassword(passwordData) {
    try {
      const response = await apiClient.put('/api/auth/change-password', passwordData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al cambiar contraseña')
    }
  },

  // ===== MÉTODOS ADMINISTRATIVOS - FASE 8.6 =====

  /**
   * Obtener todos los usuarios desde el backend
   * @returns {Promise}
   */
  async getAll() {
    try {
      console.log('🔍 Intentando obtener usuarios desde el backend...')
      const response = await apiClient.get('/api/admin/users')
      console.log('✅ Usuarios obtenidos del backend:', response.data)
      
      // El backend devuelve diferentes formatos, transformamos a formato estándar
      let users = []
      
      if (response.data.users && Array.isArray(response.data.users)) {
        users = response.data.users
      } else if (Array.isArray(response.data)) {
        users = response.data
      } else {
        console.warn('⚠️ Formato de respuesta inesperado:', response.data)
        users = []
      }
      
      // Transformar datos del backend al formato frontend
      const transformedUsers = users.map(user => ({
        id: user.id,
        name: user.nombre,
        email: user.email,
        phone: user.telefono,
        role: this.mapBackendRole(user.rol),
        status: user.activo ? 'active' : 'inactive',
        emailVerified: user.email_verificado,
        createdAt: user.created_at,
        updatedAt: user.updated_at,
        avatar: null // No hay avatar en el modelo actual
      }))
      
      console.log('🔄 Usuarios transformados:', transformedUsers)
      return {
        data: transformedUsers,
        total: transformedUsers.length,
        isDemo: false
      }
      
    } catch (error) {
      console.error('❌ Error fetching users from backend:', error)
      console.log('🔄 Usando datos de fallback para desarrollo')
      
      // Fallback con datos transformados que coinciden con la BD
      const fallbackUsers = this.getFallbackUsersRealFormat()
      return {
        data: fallbackUsers,
        total: fallbackUsers.length,
        isDemo: true
      }
    }
  },

  /**
   * Obtener estadísticas de usuarios desde el backend
   * @returns {Promise}
   */
  async getStats() {
    try {
      console.log('📊 Intentando obtener estadísticas de usuarios...')
      const response = await apiClient.get('/api/admin/users/stats')
      console.log('✅ Estadísticas obtenidas del backend:', response.data)
      
      return response.data
      
    } catch (error) {
      console.error('❌ Error fetching user stats from backend:', error)
      console.log('🔄 Calculando estadísticas desde datos locales')
      
      // Calcular estadísticas desde los usuarios disponibles
      try {
        const usersResponse = await this.getAll()
        const users = usersResponse.data || []
        
        const clients = users.filter(u => u.role === 'cliente')
        const barbers = users.filter(u => u.role === 'barbero') 
        const admins = users.filter(u => u.role === 'admin')
        const activeUsers = users.filter(u => u.status === 'active')
        
        return {
          totalUsers: users.length,
          totalClients: clients.length,
          totalBarbers: barbers.length,
          totalAdmins: admins.length,
          activeToday: activeUsers.length,
          newThisMonth: Math.floor(users.length * 0.15), // Estimación
          totalReservations: users.length * 8, // Estimación
          isDemo: usersResponse.isDemo || true
        }
      } catch (statsError) {
        console.error('❌ Error calculando estadísticas locales:', statsError)
        
        // Fallback absoluto
        return {
          totalUsers: 0,
          totalClients: 0,
          totalBarbers: 0,
          totalAdmins: 0,
          activeToday: 0,
          newThisMonth: 0,
          totalReservations: 0,
          isDemo: true
        }
      }
    }
  },

  /**
   * Crear nuevo usuario (admin)
   * @param {Object} userData - Datos del usuario
   * @returns {Promise}
   */
  async create(userData) {
    try {
      console.log('➕ Creando nuevo usuario:', userData)
      
      // Transformar datos del frontend al formato backend
      const backendData = {
        nombre: userData.name,
        email: userData.email,
        telefono: userData.phone || null,
        password: userData.password,
        rol: this.mapFrontendRole(userData.role)
      }
      
      const response = await apiClient.post('/api/auth/register', backendData)
      console.log('✅ Usuario creado exitosamente:', response.data)
      return response.data
    } catch (error) {
      console.error('❌ Error creating user:', error)
      throw new Error(error.response?.data?.message || 'Error al crear usuario')
    }
  },

  /**
   * Actualizar usuario (admin)
   * @param {string} id - ID del usuario
   * @param {Object} userData - Datos del usuario
   * @returns {Promise}
   */
  async update(id, userData) {
    try {
      console.log(`✏️ Actualizando usuario ${id}:`, userData)
      
      // Transformar datos del frontend al formato backend
      const backendData = {
        nombre: userData.name,
        email: userData.email,
        telefono: userData.phone || null,
        rol: this.mapFrontendRole(userData.role)
      }
      
      // Si se está actualizando el estado, incluirlo
      if (userData.status !== undefined) {
        backendData.activo = userData.status === 'active'
      }
      
      const response = await apiClient.put(`/api/admin/users/${id}`, backendData)
      console.log('✅ Usuario actualizado exitosamente:', response.data)
      return response.data
    } catch (error) {
      console.error('❌ Error updating user:', error)
      throw new Error(error.response?.data?.message || 'Error al actualizar usuario')
    }
  },

  /**
   * Actualizar estado de usuario (admin)
   * @param {string} id - ID del usuario
   * @param {string} status - Nuevo estado
   * @returns {Promise}
   */
  async updateStatus(id, status) {
    try {
      console.log(`🔄 Actualizando estado del usuario ${id} a: ${status}`)
      
      const response = await apiClient.put(`/api/admin/users/${id}/status`, { 
        activo: status === 'active' 
      })
      console.log('✅ Estado actualizado exitosamente:', response.data)
      return response.data
    } catch (error) {
      console.error('❌ Error updating user status:', error)
      throw new Error(error.response?.data?.message || 'Error al actualizar estado')
    }
  },

  /**
   * Obtener historial de usuario (admin)
   * @param {string} id - ID del usuario
   * @returns {Promise}
   */
  async getUserHistory(id) {
    try {
      const response = await apiClient.get(`/api/admin/users/${id}/history`)
      return response.data
    } catch (error) {
      console.error('Error fetching user history:', error)
      // Fallback data para desarrollo
      return this.getFallbackUserHistory({ id })
    }
  },

  /**
   * Actualización masiva de estado (admin)
   * @param {Array} userIds - IDs de usuarios
   * @param {string} status - Nuevo estado
   * @returns {Promise}
   */
  async bulkUpdateStatus(userIds, status) {
    try {
      console.log(`🔄 Actualizando estado masivo de ${userIds.length} usuarios a: ${status}`)
      
      const response = await apiClient.put('/api/admin/users/bulk/status', { 
        userIds, 
        activo: status === 'active' 
      })
      console.log('✅ Estado masivo actualizado exitosamente:', response.data)
      return response.data
    } catch (error) {
      console.error('❌ Error in bulk status update:', error)
      throw new Error(error.response?.data?.message || 'Error en actualización masiva')
    }
  },

  /**
   * Actualización masiva de rol (admin)
   * @param {Array} userIds - IDs de usuarios
   * @param {string} role - Nuevo rol
   * @returns {Promise}
   */
  async bulkUpdateRole(userIds, role) {
    try {
      console.log(`👥 Actualizando rol masivo de ${userIds.length} usuarios a: ${role}`)
      
      const response = await apiClient.put('/api/admin/users/bulk/role', { 
        userIds, 
        rol: this.mapFrontendRole(role) 
      })
      console.log('✅ Rol masivo actualizado exitosamente:', response.data)
      return response.data
    } catch (error) {
      console.error('❌ Error in bulk role update:', error)
      throw new Error(error.response?.data?.message || 'Error en cambio de rol masivo')
    }
  },

  /**
   * Eliminación masiva de usuarios (admin)
   * @param {Array} userIds - IDs de usuarios
   * @returns {Promise}
   */
  async bulkDelete(userIds) {
    try {
      const response = await apiClient.delete('/api/admin/users/bulk', { data: { userIds } })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error en eliminación masiva')
    }
  },

  /**
   * Reset de contraseña por admin
   * @param {string} userId - ID del usuario
   * @param {string} newPassword - Nueva contraseña
   * @returns {Promise}
   */
  async resetPassword(userId, newPassword) {
    try {
      const response = await apiClient.put(`/api/admin/users/${userId}/reset-password`, { password: newPassword })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al reset contraseña')
    }
  },

  // ===== DATOS DE FALLBACK PARA DESARROLLO =====

  /**
   * Mapear rol del backend al frontend
   * @param {string} backendRole - Rol del backend
   * @returns {string}
   */
  mapBackendRole(backendRole) {
    const roleMap = {
      'cliente': 'cliente',
      'barbero': 'barbero', 
      'admin': 'admin'
    }
    return roleMap[backendRole] || 'cliente'
  },

  /**
   * Mapear rol del frontend al backend
   * @param {string} frontendRole - Rol del frontend
   * @returns {string}
   */
  mapFrontendRole(frontendRole) {
    const roleMap = {
      'client': 'cliente',
      'cliente': 'cliente',
      'barber': 'barbero',
      'barbero': 'barbero',
      'admin': 'admin'
    }
    return roleMap[frontendRole] || 'cliente'
  },

  /**
   * Datos de fallback que coinciden con la estructura real de la BD
   * @returns {Array}
   */
  getFallbackUsersRealFormat() {
    return [
      {
        id: 1,
        name: 'Juan Pérez González',
        email: 'juan.perez@ejemplo.com',
        phone: '+57 300 123 4567',
        role: 'cliente',
        status: 'active',
        emailVerified: true,
        avatar: null,
        createdAt: '2024-01-15T10:30:00Z',
        updatedAt: '2024-08-01T14:20:00Z'
      },
      {
        id: 2,
        name: 'Carlos Mendoza Silva',
        email: 'carlos.mendoza@lowbarber.com',
        phone: '+57 301 234 5678',
        role: 'barbero',
        status: 'active',
        emailVerified: true,
        avatar: null,
        createdAt: '2023-12-01T08:00:00Z',
        updatedAt: '2024-08-02T09:15:00Z'
      },
      {
        id: 3,
        name: 'Ana García López',
        email: 'ana.garcia@ejemplo.com',
        phone: '+57 302 345 6789',
        role: 'cliente',
        status: 'active',
        emailVerified: true,
        avatar: null,
        createdAt: '2024-02-20T16:45:00Z',
        updatedAt: '2024-07-30T11:30:00Z'
      },
      {
        id: 4,
        name: 'Miguel Rodríguez Torres',
        email: 'miguel.rodriguez@lowbarber.com',
        phone: '+57 303 456 7890',
        role: 'barbero',
        status: 'active',
        emailVerified: true,
        avatar: null,
        createdAt: '2024-01-10T12:00:00Z',
        updatedAt: '2024-08-02T08:45:00Z'
      },
      {
        id: 5,
        name: 'Administrador Sistema',
        email: 'admin@lowbarber.com',
        phone: '+57 304 567 8901',
        role: 'admin',
        status: 'active',
        emailVerified: true,
        avatar: null,
        createdAt: '2023-11-01T00:00:00Z',
        updatedAt: '2024-08-02T15:00:00Z'
      },
      {
        id: 6,
        name: 'Luis Martínez Ruiz',
        email: 'luis.martinez@ejemplo.com',
        phone: '+57 305 678 9012',
        role: 'cliente',
        status: 'inactive',
        emailVerified: false,
        avatar: null,
        createdAt: '2024-03-10T14:20:00Z',
        updatedAt: '2024-07-15T10:00:00Z'
      },
      {
        id: 7,
        name: 'María López Herrera',
        email: 'maria.lopez@ejemplo.com',
        phone: '+57 306 789 0123',
        role: 'cliente',
        status: 'inactive',
        emailVerified: false,
        avatar: null,
        createdAt: '2024-04-05T09:30:00Z',
        updatedAt: '2024-06-20T16:45:00Z'
      },
      {
        id: 8,
        name: 'Pedro Silva Castro',
        email: 'pedro.silva@ejemplo.com',
        phone: '+57 307 890 1234',
        role: 'cliente',
        status: 'active',
        emailVerified: true,
        avatar: null,
        createdAt: '2024-05-12T11:15:00Z',
        updatedAt: '2024-08-01T13:20:00Z'
      },
      {
        id: 9,
        name: 'Sofia Valencia Moreno',
        email: 'sofia.valencia@ejemplo.com',
        phone: '+57 308 901 2345',
        role: 'cliente',
        status: 'active',
        emailVerified: true,
        avatar: null,
        createdAt: '2024-06-18T15:30:00Z',
        updatedAt: '2024-08-01T12:45:00Z'
      },
      {
        id: 10,
        name: 'Roberto Jiménez Paz',
        email: 'roberto.jimenez@lowbarber.com',
        phone: '+57 309 012 3456',
        role: 'barbero',
        status: 'active',
        emailVerified: true,
        avatar: null,
        createdAt: '2024-07-02T09:00:00Z',
        updatedAt: '2024-08-02T16:30:00Z'
      }
    ]
  },

  /**
   * Datos de fallback para usuarios (formato legacy)
   * @returns {Array}
   */
  getFallbackUsers() {
    return [
      {
        id: 1,
        name: 'Juan Pérez',
        email: 'juan@ejemplo.com',
        phone: '+57 300 123 4567',
        role: 'client',
        status: 'active',
        avatar: null,
        createdAt: '2024-01-15T10:30:00Z',
        lastAccess: '2024-08-01T14:20:00Z',
        reservationsCount: 12,
        totalSpent: 360000,
        barberInfo: null
      },
      {
        id: 2,
        name: 'Carlos Mendoza',
        email: 'carlos@lowbarber.com',
        phone: '+57 301 234 5678',
        role: 'barber',
        status: 'active',
        avatar: null,
        createdAt: '2023-12-01T08:00:00Z',
        lastAccess: '2024-08-02T09:15:00Z',
        reservationsCount: 0,
        totalSpent: 0,
        barberInfo: {
          specialty: 'Cortes clásicos y barbas',
          experience: 8
        }
      },
      {
        id: 3,
        name: 'Ana García',
        email: 'ana@ejemplo.com',
        phone: '+57 302 345 6789',
        role: 'client',
        status: 'active',
        avatar: null,
        createdAt: '2024-02-20T16:45:00Z',
        lastAccess: '2024-07-30T11:30:00Z',
        reservationsCount: 8,
        totalSpent: 240000
      },
      {
        id: 4,
        name: 'Miguel Rodríguez',
        email: 'miguel@lowbarber.com',
        phone: '+57 303 456 7890',
        role: 'barber',
        status: 'active',
        avatar: null,
        createdAt: '2024-01-10T12:00:00Z',
        lastAccess: '2024-08-02T08:45:00Z',
        reservationsCount: 0,
        totalSpent: 0,
        barberInfo: {
          specialty: 'Cortes modernos y diseños',
          experience: 5
        }
      },
      {
        id: 5,
        name: 'Admin Sistema',
        email: 'admin@lowbarber.com',
        phone: '+57 304 567 8901',
        role: 'admin',
        status: 'active',
        avatar: null,
        createdAt: '2023-11-01T00:00:00Z',
        lastAccess: '2024-08-02T15:00:00Z',
        reservationsCount: 0,
        totalSpent: 0
      },
      {
        id: 6,
        name: 'Luis Martínez',
        email: 'luis@ejemplo.com',
        phone: '+57 305 678 9012',
        role: 'client',
        status: 'inactive',
        avatar: null,
        createdAt: '2024-03-10T14:20:00Z',
        lastAccess: '2024-07-15T10:00:00Z',
        reservationsCount: 3,
        totalSpent: 90000
      },
      {
        id: 7,
        name: 'María López',
        email: 'maria@ejemplo.com',
        phone: '+57 306 789 0123',
        role: 'client',
        status: 'suspended',
        avatar: null,
        createdAt: '2024-04-05T09:30:00Z',
        lastAccess: '2024-06-20T16:45:00Z',
        reservationsCount: 2,
        totalSpent: 60000
      },
      {
        id: 8,
        name: 'Pedro Silva',
        email: 'pedro@ejemplo.com',
        phone: '+57 307 890 1234',
        role: 'client',
        status: 'active',
        avatar: null,
        createdAt: '2024-05-12T11:15:00Z',
        lastAccess: '2024-08-01T13:20:00Z',
        reservationsCount: 5,
        totalSpent: 150000
      }
    ]
  },

  /**
   * Datos de fallback para historial de usuario
   * @param {Object} user - Usuario
   * @returns {Object}
   */
  getFallbackUserHistory(user) {
    return {
      id: user.id,
      name: user.name || 'Usuario Ejemplo',
      email: user.email || 'usuario@ejemplo.com',
      avatar: user.avatar,
      createdAt: user.createdAt || '2024-01-01T00:00:00Z',
      stats: {
        totalReservations: 12,
        totalSpent: 360000,
        favoriteService: 'Corte Clásico',
        avgRating: 4.8
      },
      reservations: [
        {
          id: 1,
          dateTime: '2024-08-01T10:00:00Z',
          service: 'Corte Clásico',
          barber: 'Carlos Mendoza',
          status: 'completed',
          total: 30000
        },
        {
          id: 2,
          dateTime: '2024-07-15T14:30:00Z',
          service: 'Corte + Barba',
          barber: 'Miguel Rodríguez',
          status: 'completed',
          total: 45000
        },
        {
          id: 3,
          dateTime: '2024-07-01T16:00:00Z',
          service: 'Corte Moderno',
          barber: 'Carlos Mendoza',
          status: 'completed',
          total: 35000
        },
        {
          id: 4,
          dateTime: '2024-06-20T11:30:00Z',
          service: 'Arreglo de Barba',
          barber: 'Miguel Rodríguez',
          status: 'completed',
          total: 20000
        },
        {
          id: 5,
          dateTime: '2024-08-05T15:00:00Z',
          service: 'Corte Clásico',
          barber: 'Carlos Mendoza',
          status: 'confirmed',
          total: 30000
        }
      ]
    }
  }
}

export default userService
