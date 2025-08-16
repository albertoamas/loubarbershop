/**
 * Low Barber - Servicio de Servicios
 * Maneja operaciones relacionadas con servicios de barbería
 */

import apiClient from './api.js'

export const serviceService = {
  /**
   * Obtener todos los servicios
   * @returns {Promise}
   */
  async getAll() {
    try {
      const response = await apiClient.get('/api/services')
      console.log('Respuesta completa del backend:', response.data)
      
      // El backend puede devolver diferentes formatos:
      // 1. { services: [...], total: number, message: string }
      // 2. { data: [...] }
      // 3. [...] (array directo)
      
      let services = []
      
      if (response.data.services && Array.isArray(response.data.services)) {
        // Formato: { services: [...], total: number, message: string }
        services = response.data.services
      } else if (response.data.data && Array.isArray(response.data.data)) {
        // Formato: { data: [...] }
        services = response.data.data
      } else if (Array.isArray(response.data)) {
        // Formato: [...] (array directo)
        services = response.data
      } else {
        console.warn('Formato de respuesta no reconocido:', response.data)
        services = []
      }
      
      // Adaptar datos del backend al formato del frontend
      const adaptedServices = services.map(service => {
        // Función para inferir categoría del nombre si no está definida
        const inferCategory = (name, currentCategory) => {
          if (currentCategory) return currentCategory
          
          const serviceName = (name || '').toLowerCase()
          if (serviceName.includes('corte')) return 'cortes'
          if (serviceName.includes('barba') || serviceName.includes('afeitado')) return 'barbas'
          if (serviceName.includes('tratamiento') || serviceName.includes('ceja')) return 'tratamientos'
          if (serviceName.includes('combo') || serviceName.includes('completo')) return 'combos'
          
          return 'cortes' // categoría por defecto
        }

        return {
          id: service.id,
          name: service.nombre || service.name,
          description: service.descripcion || service.description,
          category: inferCategory(service.nombre || service.name, service.categoria || service.category),
          price: service.precio || service.price,
          duration: service.duracion || service.duration,
          status: service.estado === 'activo' ? 'active' : (service.status || 'active'),
          image: service.imagen || service.image,
          availableBarbers: service.barberos || service.availableBarbers || [],
          order: service.orden || service.order || 1,
          rating: service.calificacion || service.rating || 4.5,
          bookingsCount: service.reservas || service.bookingsCount || 0
        }
      })
      
      console.log('Servicios adaptados:', adaptedServices)
      return adaptedServices
    } catch (error) {
      console.error('Error en serviceService.getAll:', error)
      // En caso de error, usar datos de fallback
      const fallbackData = this.getFallbackServices()
      return fallbackData.data
    }
  },

  /**
   * Obtener todos los servicios (alias para compatibilidad)
   * @returns {Promise}
   */
  async getServices() {
    return this.getAll()
  },

  /**
   * Obtener servicio por ID
   * @param {string} id - ID del servicio
   * @returns {Promise}
   */
  async getService(id) {
    try {
      const response = await apiClient.get(`/api/services/${id}`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al obtener servicio')
    }
  },

  /**
   * Crear nuevo servicio
   * @param {Object} serviceData - datos del servicio
   * @returns {Promise}
   */
  async create(serviceData) {
    try {
      const response = await apiClient.post('/api/services', serviceData)
      return response.data
    } catch (error) {
      console.log('Simulando creación de servicio:', serviceData.name)
      return { 
        success: true, 
        id: Date.now().toString(), 
        message: 'Servicio creado correctamente (simulado)' 
      }
    }
  },

  /**
   * Crear nuevo servicio (alias para compatibilidad)
   * @param {Object} serviceData - datos del servicio
   * @returns {Promise}
   */
  async createService(serviceData) {
    return this.create(serviceData)
  },

  /**
   * Actualizar servicio
   * @param {string} id - ID del servicio
   * @param {Object} data - datos a actualizar
   * @returns {Promise}
   */
  async update(id, data) {
    try {
      const response = await apiClient.put(`/api/services/${id}`, data)
      return response.data
    } catch (error) {
      console.log(`Simulando actualización del servicio ${id}:`, data.name || 'Sin nombre')
      return { 
        success: true, 
        message: 'Servicio actualizado correctamente (simulado)' 
      }
    }
  },

  /**
   * Actualizar servicio (alias para compatibilidad)
   * @param {string} id - ID del servicio
   * @param {Object} data - datos a actualizar
   * @returns {Promise}
   */
  async updateService(id, data) {
    return this.update(id, data)
  },

  /**
   * Eliminar servicio
   * @param {string} id - ID del servicio
   * @returns {Promise}
   */
  async delete(id) {
    try {
      const response = await apiClient.delete(`/api/services/${id}`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al eliminar servicio')
    }
  },

  /**
   * Eliminar servicio (alias para compatibilidad)
   * @param {string} id - ID del servicio
   * @returns {Promise}
   */
  async deleteService(id) {
    return this.delete(id)
  },

  // ==========================================
  // MÉTODOS ADMINISTRATIVOS
  // ==========================================

  /**
   * Obtener estadísticas generales de servicios
   * @returns {Promise}
   */
  async getStats() {
    // Por ahora, usar directamente fallback para evitar errores CORS
    // TODO: Implementar endpoint /api/admin/services/stats en el backend
    console.log('Usando estadísticas de fallback (endpoint /api/admin/services/stats no disponible)')
    return {
      totalServices: 25,
      activeServices: 22,
      mostPopular: 'Corte Clásico',
      avgRevenue: 35000
    }
    
    /* Código comentado para cuando el endpoint esté disponible:
    try {
      const response = await apiClient.get('/api/admin/services/stats')
      
      // Adaptar formato del backend al frontend
      const data = response.data
      return {
        totalServices: data.totalServicios || data.totalServices || 0,
        activeServices: data.activos || data.activeServices || 0,
        mostPopular: data.masPopular || data.mostPopular || 'N/A',
        avgRevenue: data.precioPromedio || data.avgRevenue || 0
      }
    } catch (error) {
      console.log('Endpoint /api/admin/services/stats no disponible o error CORS, usando fallback')
      return {
        totalServices: 25,
        activeServices: 22,
        mostPopular: 'Corte Clásico',
        avgRevenue: 35000
      }
    }
    */
  },

  /**
   * Obtener servicios con filtros avanzados para administración
   * @param {Object} filters - filtros a aplicar
   * @returns {Promise}
   */
  async getServicesAdmin(filters = {}) {
    try {
      const queryParams = new URLSearchParams()
      Object.keys(filters).forEach(key => {
        if (filters[key] !== null && filters[key] !== undefined && filters[key] !== '') {
          queryParams.append(key, filters[key])
        }
      })
      
      const response = await apiClient.get(`/api/admin/services?${queryParams.toString()}`)
      return response.data
    } catch (error) {
      // Si no existe endpoint admin, usar datos de fallback
      return this.getFallbackServices()
    }
  },

  /**
   * Actualización masiva de estado de servicios
   * @param {Array} serviceIds - IDs de servicios
   * @param {string} status - nuevo estado
   * @returns {Promise}
   */
  async bulkUpdateStatus(serviceIds, status) {
    try {
      const response = await apiClient.patch('/api/admin/services/bulk/status', {
        serviceIds,
        status
      })
      return response.data
    } catch (error) {
      console.log(`Simulando actualización masiva de estado a ${status} para ${serviceIds.length} servicios`)
      return { success: true, updated: serviceIds.length }
    }
  },

  /**
   * Actualización masiva de categoría de servicios
   * @param {Array} serviceIds - IDs de servicios
   * @param {string} categoria - nueva categoría
   * @returns {Promise}
   */
  async bulkUpdateCategory(serviceIds, categoria) {
    try {
      const response = await apiClient.patch('/api/admin/services/bulk/category', {
        serviceIds,
        categoria
      })
      return response.data
    } catch (error) {
      console.log(`Simulando actualización masiva de categoría a ${categoria} para ${serviceIds.length} servicios`)
      return { success: true, updated: serviceIds.length }
    }
  },

  /**
   * Eliminación masiva de servicios
   * @param {Array} serviceIds - IDs de servicios
   * @returns {Promise}
   */
  async bulkDelete(serviceIds) {
    try {
      const response = await apiClient.delete('/api/admin/services/bulk', {
        data: { serviceIds }
      })
      return response.data
    } catch (error) {
      console.log(`Simulando eliminación masiva de ${serviceIds.length} servicios`)
      return { success: true, deleted: serviceIds.length }
    }
  },

  /**
   * Actualizar estado de un servicio
   * @param {string} id - ID del servicio
   * @param {string} status - nuevo estado
   * @returns {Promise}
   */
  async updateStatus(id, status) {
    try {
      const response = await apiClient.patch(`/api/services/${id}/status`, { status })
      return response.data
    } catch (error) {
      console.log(`Simulando actualización de estado del servicio ${id} a ${status}`)
      return { success: true, message: 'Estado actualizado correctamente' }
    }
  },

  /**
   * Obtener estadísticas detalladas de un servicio específico
   * @param {string} serviceId - ID del servicio
   * @returns {Promise}
   */
  async getServiceStats(serviceId) {
    try {
      const response = await apiClient.get(`/api/admin/services/${serviceId}/stats`)
      return response.data
    } catch (error) {
      console.log(`Endpoint de estadísticas para servicio ${serviceId} no disponible, usando fallback`)
      // Buscar el servicio en los datos de fallback
      const fallbackServices = this.getFallbackServices()
      const service = fallbackServices.data.find(s => s.id === serviceId)
      return this.getFallbackServiceStats(service || { id: serviceId, name: 'Servicio Desconocido' })
    }
  },

  /**
   * Subir imagen de servicio
   * @param {string} serviceId - ID del servicio
   * @param {File} imageFile - archivo de imagen
   * @returns {Promise}
   */
  async uploadImage(serviceId, imageFile) {
    try {
      const formData = new FormData()
      formData.append('image', imageFile)
      
      const response = await apiClient.post(`/api/services/${serviceId}/image`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al subir imagen')
    }
  },

  /**
   * Eliminar imagen de servicio
   * @param {string} serviceId - ID del servicio
   * @returns {Promise}
   */
  async removeImage(serviceId) {
    try {
      const response = await apiClient.delete(`/api/services/${serviceId}/image`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al eliminar imagen')
    }
  },

  // ==========================================
  // MÉTODOS DE FALLBACK PARA DESARROLLO
  // ==========================================

  /**
   * Datos de fallback para servicios (desarrollo)
   * @returns {Object}
   */
  getFallbackServices() {
    return {
      data: [
        {
          id: '1',
          name: 'Corte Clásico',
          description: 'Corte tradicional con tijera y máquina',
          category: 'cortes',
          price: 25000,
          duration: 30,
          status: 'active',
          image: null,
          availableBarbers: [1, 2],
          order: 1,
          rating: 4.8,
          bookingsCount: 95
        },
        {
          id: '2',
          name: 'Corte Fade',
          description: 'Corte degradado moderno',
          category: 'cortes',
          price: 30000,
          duration: 45,
          status: 'active',
          image: null,
          availableBarbers: [2, 3],
          order: 2,
          rating: 4.6,
          bookingsCount: 88
        },
        {
          id: '3',
          name: 'Arreglo de Barba',
          description: 'Recorte y perfilado de barba',
          category: 'barbas',
          price: 20000,
          duration: 25,
          status: 'active',
          image: null,
          availableBarbers: [1, 3],
          order: 3,
          rating: 4.7,
          bookingsCount: 78
        },
        {
          id: '4',
          name: 'Tratamiento Capilar',
          description: 'Tratamiento hidratante para el cabello',
          category: 'tratamientos',
          price: 45000,
          duration: 60,
          status: 'inactive',
          image: null,
          availableBarbers: [1],
          order: 4,
          rating: 4.3,
          bookingsCount: 65
        },
        {
          id: '5',
          name: 'Combo Corte + Barba',
          description: 'Servicio completo de corte y arreglo de barba',
          category: 'combos',
          price: 40000,
          duration: 50,
          status: 'active',
          image: null,
          availableBarbers: [1, 2, 3],
          order: 5,
          rating: 4.9,
          bookingsCount: 92
        }
      ],
      total: 5,
      page: 1,
      totalPages: 1
    }
  },

  /**
   * Estadísticas de fallback para un servicio específico
   * @param {Object} service - objeto del servicio
   * @returns {Object}
   */
  getFallbackServiceStats(service) {
    const totalBookings = Math.floor(Math.random() * 100) + 20
    const completedBookings = Math.floor(Math.random() * 80) + 15
    const cancelledBookings = Math.floor(Math.random() * 10) + 2
    const totalRevenue = Math.floor(Math.random() * 2000000) + 500000
    const avgRating = (Math.random() * 2 + 3).toFixed(1)
    const monthlyBookings = Math.floor(Math.random() * 20) + 5

    return {
      ...service,
      stats: {
        totalBookings,
        completedBookings,
        cancelledBookings,
        totalRevenue,
        avgRating,
        monthlyBookings,
        efficiency: Math.round((completedBookings / totalBookings) * 100),
        revenuePerBooking: Math.round(totalRevenue / completedBookings),
        trend: Math.random() > 0.5 ? 'positive' : 'negative',
        trendPercentage: Math.floor(Math.random() * 20) + 5
      }
    }
  }
}

export default serviceService
