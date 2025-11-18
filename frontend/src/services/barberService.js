/**
 * Low Barber - Servicio de Barberos
 * Maneja operaciones relacionadas con barberos
 */

import apiClient from './api.js'

export const barberService = {
  /**
   * Obtener todos los barberos
   * @param {boolean} showAll - Si es true, obtiene todos los barberos (incluso desactivados)
   * @returns {Promise}
   */
  async getAll(showAll = false) {
    try {
      const params = showAll ? { show_all: 'true' } : {}
      const response = await apiClient.get('/api/barbers', { params })
      console.log('🔍 Respuesta completa del backend:', response)
      console.log('🔍 response.data:', response.data)
      console.log('🔍 response.data.barbers:', response.data.barbers)
      console.log('🔍 response.data.data:', response.data.data)
      
      // El backend puede devolver en diferentes formatos
      // Intentar diferentes estructuras de respuesta
      const barbers = response.data.barbers || response.data.data || response.data || []
      console.log('✅ Barberos extraídos:', barbers)
      
      return barbers
    } catch (error) {
      console.error('Error fetching barbers:', error)
      // Fallback data
      return this.getFallbackBarbers()
    }
  },

  /**
   * Obtener todos los barberos (alias para compatibilidad)
   * @returns {Promise}
   */
  async getBarbers() {
    return this.getAll()
  },

  /**
   * Obtener barbero por ID
   * @param {string} id - ID del barbero
   * @returns {Promise}
   */
  async getBarber(id) {
    try {
      const response = await apiClient.get(`/api/barbers/${id}`)
      return response.data.barber || response.data
    } catch (error) {
      console.error('Error fetching barber:', error)
      // Fallback: buscar en datos locales
      const allBarbers = await this.getAll()
      const barber = allBarbers.find(b => b.id == id)
      if (!barber) {
        throw new Error('Barbero no encontrado')
      }
      return barber
    }
  },

  /**
   * Obtener barbero por ID (alias para compatibilidad)
   * @param {string} id - ID del barbero
   * @returns {Promise}
   */
  async getById(id) {
    return this.getBarber(id)
  },

  /**
   * Crear nuevo barbero
   * @param {Object} barberData - datos del barbero
   * @returns {Promise}
   */
  async create(barberData) {
    try {
      const response = await apiClient.post('/api/barbers', barberData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al crear barbero')
    }
  },

  /**
   * Crear nuevo barbero (alias para compatibilidad)
   * @param {Object} barberData - datos del barbero
   * @returns {Promise}
   */
  async createBarber(barberData) {
    return this.create(barberData)
  },

  /**
   * Actualizar barbero
   * @param {string} id - ID del barbero
   * @param {Object} data - datos a actualizar
   * @returns {Promise}
   */
  async update(id, data) {
    try {
      const response = await apiClient.put(`/api/barbers/${id}`, data)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al actualizar barbero')
    }
  },

  /**
   * Actualizar barbero (alias para compatibilidad)
   * @param {string} id - ID del barbero
   * @param {Object} data - datos a actualizar
   * @returns {Promise}
   */
  async updateBarber(id, data) {
    return this.update(id, data)
  },

  /**
   * Eliminar barbero
   * @param {string} id - ID del barbero
   * @returns {Promise}
   */
  async delete(id) {
    try {
      const response = await apiClient.delete(`/api/barbers/${id}`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al eliminar barbero')
    }
  },

  /**
   * Eliminar barbero (alias para compatibilidad)
   * @param {string} id - ID del barbero
   * @returns {Promise}
   */
  async deleteBarber(id) {
    return this.delete(id)
  },

  /**
   * Obtener estadísticas de barberos
   * @returns {Promise}
   */
  async getStats() {
    try {
      const response = await apiClient.get('/api/stats/barbers')
      console.log('Respuesta del backend de stats:', response.data)
      
      // Si el backend devuelve un array de barberos en lugar de stats
      if (Array.isArray(response.data)) {
        console.log('Backend devolvió array, calculando estadísticas...')
        const barbersFromStats = response.data
        const activeBarberos = barbersFromStats.filter(b => b.disponible).length
        
        return {
          total: barbersFromStats.length,
          activos: activeBarberos,
          inactivos: barbersFromStats.length - activeBarberos,
          disponibles_hoy: activeBarberos,
          promedio_reservas: 12,
          total_reservas: barbersFromStats.reduce((sum, b) => sum + (b.total_reservas || 0), 0)
        }
      }
      
      // Si el backend devuelve el objeto correcto
      return response.data
    } catch (error) {
      console.error('Error fetching barber stats:', error)
      
      // Obtener barberos para calcular estadísticas reales
      const allBarbers = this.getFallbackBarbers()
      const activeBarberos = allBarbers.filter(b => b.disponible).length
      
      // Fallback stats con campos necesarios para el componente
      return {
        total: allBarbers.length,
        activos: activeBarberos,
        inactivos: allBarbers.length - activeBarberos,
        disponibles_hoy: activeBarberos,
        promedio_reservas: 12,
        total_reservas: 156,
        ocupacion_promedio: 75.5,
        ingresos_mes: 2450000,
        especialidades: [
          { nombre: 'Cortes Clásicos', barberos: 3 },
          { nombre: 'Barba y Bigote', barberos: 4 },
          { nombre: 'Tratamientos', barberos: 2 }
        ]
      }
    }
  },

  /**
   * Obtener barberos activos
   * @returns {Promise}
   */
  async getActive() {
    try {
      const response = await apiClient.get('/api/barbers', {
        params: { status: 'active' }
      })
      // El backend devuelve { barbers: [...], total: number }
      return response.data.barbers || []
    } catch (error) {
      console.error('Error fetching active barbers:', error)
      // Fallback: filtrar barberos activos
      const allBarbers = await this.getAll()
      return allBarbers.filter(barber => barber.disponible === true)
    }
  },

  /**
   * Obtener disponibilidad de un barbero
   * @param {string} barberId - ID del barbero
   * @param {string} date - Fecha en formato YYYY-MM-DD
   * @returns {Promise}
   */
  async getAvailability(barberId, date) {
    try {
      const response = await apiClient.get(`/api/barbers/${barberId}/availability`, {
        params: { date }
      })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al obtener disponibilidad')
    }
  },

  /**
   * Actualizar disponibilidad de un barbero
   * @param {string} barberId - ID del barbero
   * @param {Object} availabilityData - Datos de disponibilidad
   * @returns {Promise}
   */
  async updateAvailability(barberId, availabilityData) {
    try {
      const response = await apiClient.put(`/api/barbers/${barberId}/availability`, availabilityData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al actualizar disponibilidad')
    }
  },

  /**
   * Obtener horario de trabajo de un barbero
   * @param {string} barberId - ID del barbero
   * @returns {Promise}
   */
  async getSchedule(barberId) {
    try {
      const response = await apiClient.get(`/api/barbers/${barberId}/schedule`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al obtener horario')
    }
  },

  /**
   * Actualizar horario de trabajo de un barbero
   * @param {string} barberId - ID del barbero
   * @param {Object} scheduleData - Datos del horario
   * @returns {Promise}
   */
  async updateSchedule(barberId, scheduleData) {
    try {
      const response = await apiClient.put(`/api/barbers/${barberId}/schedule`, scheduleData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al actualizar horario')
    }
  },

  /**
   * Cambiar estado de un barbero
   * @param {string} barberId - ID del barbero
   * @param {string} status - Nuevo estado (active/inactive)
   * @returns {Promise}
   */
  async changeStatus(barberId, status) {
    try {
      const response = await apiClient.patch(`/api/barbers/${barberId}/status`, { status })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al cambiar estado del barbero')
    }
  },

  /**
   * Obtener slots de tiempo disponibles
   * @param {string} barberId - ID del barbero
   * @param {string} date - Fecha en formato YYYY-MM-DD
   * @param {number} duration - Duración del servicio en minutos
   * @returns {Promise}
   */
  async getAvailableSlots(barberId, date, duration = 30) {
    try {
      const response = await apiClient.get(`/api/barbers/${barberId}/available-slots`, {
        params: { date, duration }
      })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al obtener slots disponibles')
    }
  },

  /**
   * Datos de fallback para desarrollo
   */
  getFallbackBarbers() {
    return [
      {
        id: 1,
        nombre: 'Carlos Mendoza',
        especialidad: 'Cortes Clásicos y Modernos',
        disponible: true,
        telefono: '123-456-7890',
        email: 'carlos@lowbarber.com',
        experiencia: '8 años',
        horario_inicio: '09:00',
        horario_fin: '18:00',
        dias_trabajo: ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'],
        avatar: '/avatars/carlos.jpg',
        rating: 4.8,
        total_reservas: 245,
        created_at: '2023-01-15T10:00:00Z'
      },
      {
        id: 2,
        nombre: 'Luis Rodríguez',
        especialidad: 'Barba y Bigote Especializado',
        disponible: true,
        telefono: '098-765-4321',
        email: 'luis@lowbarber.com',
        experiencia: '6 años',
        horario_inicio: '10:00',
        horario_fin: '19:00',
        dias_trabajo: ['martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'],
        avatar: '/avatars/luis.jpg',
        rating: 4.9,
        total_reservas: 198,
        created_at: '2023-02-20T10:00:00Z'
      },
      {
        id: 3,
        nombre: 'Miguel Ángel Torres',
        especialidad: 'Tratamientos Capilares',
        disponible: true,
        telefono: '555-123-4567',
        email: 'miguel@lowbarber.com',
        experiencia: '5 años',
        horario_inicio: '08:00',
        horario_fin: '17:00',
        dias_trabajo: ['lunes', 'martes', 'miércoles', 'jueves', 'viernes'],
        avatar: '/avatars/miguel.jpg',
        rating: 4.7,
        total_reservas: 167,
        created_at: '2023-03-10T10:00:00Z'
      },
      {
        id: 4,
        nombre: 'Andrés López',
        especialidad: 'Cortes Modernos y Degradados',
        disponible: false,
        telefono: '777-888-9999',
        email: 'andres@lowbarber.com',
        experiencia: '4 años',
        horario_inicio: '12:00',
        horario_fin: '20:00',
        dias_trabajo: ['miércoles', 'jueves', 'viernes', 'sábado', 'domingo'],
        avatar: '/avatars/andres.jpg',
        rating: 4.6,
        total_reservas: 134,
        created_at: '2023-04-05T10:00:00Z'
      }
    ]
  }
}

export default barberService
