// reservationService.js - Manejo de reservas con estructura real de BD
import apiClient from './api.js'

const reservationService = {
  /**
   * Obtener todas las reservas (alias para getAll)
   */
  async getReservations(filters = {}) {
    return this.getAll(filters)
  },

  /**
   * Obtener todas las reservas con datos reales
   */
  async getAll(filters = {}) {
    try {
      const response = await apiClient.get('/api/reservations', { params: filters })
      console.log('✅ Reservas obtenidas del backend:', response.data)
      
      // El backend devuelve { reservas: [...], total: number }
      const reservas = response.data.reservas || []
      
      // Transformar datos para que coincidan con el frontend
      const reservasTransformadas = reservas.map(reserva => ({
        id: reserva.id,
        // Datos del cliente
        cliente_nombre: reserva.cliente_nombre,
        cliente_email: reserva.cliente_email,
        cliente_telefono: reserva.cliente_telefono,
        user_id: reserva.user_id,
        
        // Datos del barbero
        barber_id: reserva.barber_id,
        barbero_nombre: reserva.barbero?.nombre || 'Sin asignar',
        barbero_especialidad: reserva.barbero?.especialidad || '',
        
        // Datos del servicio
        service_id: reserva.service_id,
        servicio_nombre: reserva.servicio?.nombre || 'Servicio eliminado',
        servicio_precio: reserva.servicio?.precio || reserva.precio_final || 0,
        servicio_duracion: reserva.servicio?.duracion || 60,
        
        // Información de la reserva
        fecha_reserva: reserva.fecha_reserva,
        hora_inicio: reserva.hora_inicio,
        hora_fin: reserva.hora_fin,
        estado: reserva.estado,
        notas: reserva.notas,
        precio_final: reserva.precio_final,
        
        // Timestamps
        created_at: reserva.created_at,
        updated_at: reserva.updated_at,
        fecha_confirmacion: reserva.fecha_confirmacion,
        fecha_completacion: reserva.fecha_completacion,
        fecha_cancelacion: reserva.fecha_cancelacion
      }))
      
      return {
        data: reservasTransformadas,
        total: response.data.total || reservasTransformadas.length,
        isDemo: false
      }
    } catch (error) {
      console.error('❌ Error al obtener reservas del backend:', error)
      console.log('🔄 Usando datos de fallback')
      // Fallback data con estructura correcta
      return this.getFallbackReservations()
    }
  },

  /**
   * Crear nueva reserva (alias para create)
   */
  async createReservation(reservationData) {
    return this.create(reservationData)
  },

  /**
   * Crear nueva reserva
   */
  async create(reservationData) {
    try {
      const response = await apiClient.post('/api/reservations', reservationData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al crear la reserva')
    }
  },

  /**
   * Actualizar reserva
   */
  async update(id, reservationData) {
    try {
      const response = await apiClient.put(`/api/reservations/${id}`, reservationData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al actualizar la reserva')
    }
  },

  /**
   * Eliminar reserva
   */
  async delete(id) {
    try {
      const response = await apiClient.delete(`/api/reservations/${id}`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al eliminar la reserva')
    }
  },

  /**
   * Obtener reserva por ID
   */
  async getById(id) {
    try {
      const response = await apiClient.get(`/api/reservations/${id}`)
      return response.data.reserva
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al obtener la reserva')
    }
  },

  /**
   * Actualizar estado de reserva
   */
  async updateStatus(id, estado, notas_barbero = null, precio_final = null) {
    try {
      const data = { estado }
      if (notas_barbero) data.notas_barbero = notas_barbero
      if (precio_final) data.precio_final = precio_final
      
      const response = await apiClient.patch(`/api/reservations/${id}/status`, data)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al actualizar el estado')
    }
  },

  /**
   * Obtener estadísticas de reservas
   */
  async getStats() {
    try {
      const response = await apiClient.get('/api/stats/reservations')
      return response.data
    } catch (error) {
      console.error('Error fetching reservation stats:', error)
      // Calcular estadísticas de los datos disponibles
      const reservasData = await this.getAll()
      const reservas = reservasData.data || []
      const today = new Date().toISOString().split('T')[0]
      
      return {
        total: reservas.length,
        hoy: reservas.filter(r => r.fecha_reserva === today).length,
        pendientes: reservas.filter(r => r.estado === 'pendiente').length,
        confirmadas: reservas.filter(r => r.estado === 'confirmada').length,
        completadas: reservas.filter(r => r.estado === 'completada').length,
        canceladas: reservas.filter(r => r.estado === 'cancelada').length,
        en_proceso: reservas.filter(r => r.estado === 'en_proceso').length,
        no_asistio: reservas.filter(r => r.estado === 'no_asistio').length,
        ingresos_mes: reservas
          .filter(r => r.estado === 'completada' && r.precio_final)
          .reduce((total, r) => total + parseFloat(r.precio_final || 0), 0),
        isDemo: reservasData.isDemo || false
      }
    }
  },

  /**
   * Operaciones masivas
   */
  async bulkUpdateStatus(reservationIds, estado) {
    try {
      const response = await apiClient.post('/api/reservations/bulk-status', { 
        reservation_ids: reservationIds,
        estado 
      })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error en operación masiva')
    }
  },

  /**
   * Datos de fallback para desarrollo
   */
  getFallbackReservations() {
    const today = new Date()
    const tomorrow = new Date(today.getTime() + 24 * 60 * 60 * 1000)
    const dayAfter = new Date(today.getTime() + 2 * 24 * 60 * 60 * 1000)

    const reservas = [
      {
        id: '1',
        cliente_nombre: 'Juan Pérez',
        cliente_email: 'juan@email.com',
        cliente_telefono: '+57 300 123 4567',
        user_id: 'user-1',
        barber_id: 'barber-1',
        barbero_nombre: 'Carlos Martínez',
        barbero_especialidad: 'Cortes clásicos',
        service_id: 'service-1',
        servicio_nombre: 'Corte Clásico',
        servicio_precio: 25000,
        servicio_duracion: 30,
        fecha_reserva: today.toISOString().split('T')[0],
        hora_inicio: '10:00',
        hora_fin: '10:30',
        estado: 'confirmada',
        notas: 'Cliente regular, prefiere corte corto',
        precio_final: 25000,
        created_at: today.toISOString(),
        updated_at: today.toISOString(),
        fecha_confirmacion: today.toISOString()
      },
      {
        id: '2',
        cliente_nombre: 'María García',
        cliente_email: 'maria@email.com',
        cliente_telefono: '+57 310 987 6543',
        user_id: 'user-2',
        barber_id: 'barber-2',
        barbero_nombre: 'Miguel Rodríguez',
        barbero_especialidad: 'Barba y bigote',
        service_id: 'service-2',
        servicio_nombre: 'Barba + Bigote',
        servicio_precio: 20000,
        servicio_duracion: 45,
        fecha_reserva: tomorrow.toISOString().split('T')[0],
        hora_inicio: '14:30',
        hora_fin: '15:15',
        estado: 'pendiente',
        notas: '',
        precio_final: null,
        created_at: tomorrow.toISOString(),
        updated_at: tomorrow.toISOString()
      },
      {
        id: '3',
        cliente_nombre: 'Pedro López',
        cliente_email: 'pedro@email.com',
        cliente_telefono: '+57 320 555 7890',
        user_id: 'user-3',
        barber_id: 'barber-1',
        barbero_nombre: 'Carlos Martínez',
        barbero_especialidad: 'Cortes clásicos',
        service_id: 'service-3',
        servicio_nombre: 'Corte + Barba Premium',
        servicio_precio: 35000,
        servicio_duracion: 60,
        fecha_reserva: dayAfter.toISOString().split('T')[0],
        hora_inicio: '16:00',
        hora_fin: '17:00',
        estado: 'en_proceso',
        notas: 'Corte degradado, barba con estilo',
        precio_final: 35000,
        created_at: dayAfter.toISOString(),
        updated_at: dayAfter.toISOString(),
        fecha_confirmacion: dayAfter.toISOString()
      },
      {
        id: '4',
        cliente_nombre: 'Ana Morales',
        cliente_email: 'ana@email.com',
        cliente_telefono: '+57 315 444 3333',
        user_id: 'user-4',
        barber_id: 'barber-3',
        barbero_nombre: 'Ana García',
        barbero_especialidad: 'Cortes modernos',
        service_id: 'service-4',
        servicio_nombre: 'Corte Moderno',
        servicio_precio: 30000,
        servicio_duracion: 45,
        fecha_reserva: new Date(today.getTime() - 24 * 60 * 60 * 1000).toISOString().split('T')[0],
        hora_inicio: '11:00',
        hora_fin: '11:45',
        estado: 'completada',
        notas: 'Muy satisfecha con el resultado',
        precio_final: 30000,
        created_at: new Date(today.getTime() - 24 * 60 * 60 * 1000).toISOString(),
        updated_at: new Date(today.getTime() - 24 * 60 * 60 * 1000).toISOString(),
        fecha_confirmacion: new Date(today.getTime() - 24 * 60 * 60 * 1000).toISOString(),
        fecha_completacion: new Date(today.getTime() - 24 * 60 * 60 * 1000).toISOString()
      },
      {
        id: '5',
        cliente_nombre: 'Roberto Silva',
        cliente_email: 'roberto@email.com',
        cliente_telefono: '+57 301 222 1111',
        user_id: 'user-5',
        barber_id: 'barber-2',
        barbero_nombre: 'Miguel Rodríguez',
        barbero_especialidad: 'Barba y bigote',
        service_id: 'service-1',
        servicio_nombre: 'Corte Clásico',
        servicio_precio: 25000,
        servicio_duracion: 30,
        fecha_reserva: new Date(today.getTime() - 48 * 60 * 60 * 1000).toISOString().split('T')[0],
        hora_inicio: '15:30',
        hora_fin: '16:00',
        estado: 'cancelada',
        notas: 'Cancelada por el cliente',
        precio_final: null,
        created_at: new Date(today.getTime() - 48 * 60 * 60 * 1000).toISOString(),
        updated_at: new Date(today.getTime() - 48 * 60 * 60 * 1000).toISOString(),
        fecha_cancelacion: new Date(today.getTime() - 47 * 60 * 60 * 1000).toISOString()
      }
    ]

    return {
      data: reservas,
      total: reservas.length,
      isDemo: true
    }
  },

  /**
   * Obtener las reservas del usuario actual
   */
  async getMyReservations() {
    try {
      const response = await apiClient.get('/api/user/reservations')
      console.log('✅ Mis reservas obtenidas del backend:', response.data)
      
      return {
        success: true,
        data: response.data.reservas || response.data || [],
        message: 'Reservas obtenidas exitosamente'
      }
    } catch (error) {
      console.error('❌ Error al obtener mis reservas:', error)
      
      // Fallback con datos de ejemplo
      return this.getMockUserReservations()
    }
  },

  /**
   * Cancelar una reserva
   */
  async cancelReservation(reservationId) {
    try {
      const response = await apiClient.put(`/api/reservations/${reservationId}/cancel`)
      console.log('✅ Reserva cancelada:', response.data)
      
      return {
        success: true,
        data: response.data,
        message: 'Reserva cancelada exitosamente'
      }
    } catch (error) {
      console.error('❌ Error al cancelar reserva:', error)
      return {
        success: false,
        message: error.response?.data?.message || 'Error al cancelar la reserva'
      }
    }
  },

  /**
   * Obtener datos mock para las reservas del usuario
   */
  getMockUserReservations() {
    const today = new Date()
    const dayAfter = new Date(today.getTime() + 24 * 60 * 60 * 1000)
    const weekAfter = new Date(today.getTime() + 7 * 24 * 60 * 60 * 1000)
    
    const reservas = [
      {
        id: 1,
        servicio: 'Corte de Cabello Premium',
        service_name: 'Corte de Cabello Premium',
        fecha: weekAfter.toISOString().split('T')[0],
        date: weekAfter.toISOString().split('T')[0],
        hora: '10:00',
        time: '10:00',
        estado: 'confirmada',
        status: 'confirmed',
        barbero: 'Carlos López',
        barber_name: 'Carlos López',
        precio: 50.00,
        price: 50.00,
        notas: 'Corte moderno con degradado en los laterales',
        notes: 'Corte moderno con degradado en los laterales',
        created_at: new Date().toISOString()
      },
      {
        id: 2,
        servicio: 'Barba + Bigote',
        service_name: 'Barba + Bigote',
        fecha: dayAfter.toISOString().split('T')[0],
        date: dayAfter.toISOString().split('T')[0],
        hora: '14:30',
        time: '14:30',
        estado: 'pendiente',
        status: 'pending',
        barbero: 'Miguel Torres',
        barber_name: 'Miguel Torres',
        precio: 40.00,
        price: 40.00,
        notas: 'Mantener longitud actual, solo perfilar',
        notes: 'Mantener longitud actual, solo perfilar',
        created_at: new Date().toISOString()
      },
      {
        id: 3,
        servicio: 'Servicio Completo',
        service_name: 'Servicio Completo',
        fecha: '2024-12-28',
        date: '2024-12-28',
        hora: '16:00',
        time: '16:00',
        estado: 'completada',
        status: 'completed',
        barbero: 'Carlos López',
        barber_name: 'Carlos López',
        precio: 80.00,
        price: 80.00,
        notas: 'Excelente servicio como siempre',
        notes: 'Excelente servicio como siempre',
        created_at: new Date('2024-12-28').toISOString()
      },
      {
        id: 4,
        servicio: 'Corte Clásico',
        service_name: 'Corte Clásico',
        fecha: '2024-12-15',
        date: '2024-12-15',
        hora: '09:00',
        time: '09:00',
        estado: 'cancelada',
        status: 'cancelled',
        barbero: 'Miguel Torres',
        barber_name: 'Miguel Torres',
        precio: 45.00,
        price: 45.00,
        notas: 'Cancelada por cambio de planes',
        notes: 'Cancelada por cambio de planes',
        created_at: new Date('2024-12-15').toISOString()
      }
    ]

    return {
      success: true,
      data: reservas,
      message: 'Reservas de ejemplo cargadas',
      isDemo: true
    }
  }
}

export default reservationService
