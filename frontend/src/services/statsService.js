import api from './api.js'

/**
 * Servicio para gestionar estadísticas
 */
const statsService = {
  /**
   * Obtener estadísticas generales del dashboard
   */
  async getDashboardStats() {
    try {
      const response = await api.get('/api/stats/dashboard')
      return response.data
    } catch (error) {
      // Si es error 401/403, el usuario no está autenticado o no tiene permisos
      if (error.response?.status === 401 || error.response?.status === 403) {
        console.warn('Usuario no autenticado o sin permisos para estadísticas')
      } else if (error.response?.status === 422) {
        console.warn('Error 422 en endpoint de estadísticas, usando datos de fallback')
      } else {
        console.warn('Backend no disponible, usando datos de fallback para dashboard stats')
      }
      
      // Datos de fallback para desarrollo
      return {
        totalReservations: 125,
        totalClients: 1247,
        totalBarbers: 6,
        monthlyRevenue: 3450.00,
        weeklyGrowth: {
          reservations: 12.5,
          clients: 8.3,
          revenue: 15.2
        },
        chartData: {
          labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
          datasets: [{
            label: 'Reservas',
            data: [65, 78, 90, 81, 95, 125],
            borderColor: 'rgb(59, 130, 246)',
            backgroundColor: 'rgba(59, 130, 246, 0.1)',
            tension: 0.4
          }]
        },
        servicesChart: {
          labels: ['Corte Clásico', 'Barba', 'Combo', 'Lavado'],
          datasets: [{
            label: 'Servicios',
            data: [45, 25, 20, 10],
            backgroundColor: [
              'rgba(59, 130, 246, 0.8)',
              'rgba(16, 185, 129, 0.8)',
              'rgba(245, 158, 11, 0.8)',
              'rgba(239, 68, 68, 0.8)'
            ]
          }]
        }
      }
    }
  },

  /**
   * Obtener estadísticas de reservas
   */
  async getReservationStats(filters = {}) {
    try {
      const params = new URLSearchParams(filters)
      const response = await api.get(`/api/stats/reservations?${params}`)
      return response.data
    } catch (error) {
      console.warn('Backend no disponible, usando datos de fallback para reservation stats')
      return {
        totalReservations: 125,
        completedReservations: 98,
        cancelledReservations: 12,
        pendingReservations: 15,
        averageServiceTime: 45,
        popularTimeSlots: [
          { time: '10:00', count: 25 },
          { time: '14:00', count: 32 },
          { time: '16:00', count: 28 },
          { time: '18:00', count: 35 }
        ]
      }
    }
  },

  /**
   * Obtener estadísticas de ingresos
   */
  async getRevenueStats(filters = {}) {
    try {
      const params = new URLSearchParams(filters)
      const response = await api.get(`/api/stats/revenue?${params}`)
      return response.data
    } catch (error) {
      console.warn('Backend no disponible, usando datos de fallback para revenue stats')
      return {
        totalRevenue: 3450.00,
        monthlyGrowth: 15.2,
        averageTicket: 27.60,
        topServices: [
          { name: 'Corte Clásico', revenue: 1200.00 },
          { name: 'Barba + Corte', revenue: 980.00 },
          { name: 'Barba', revenue: 650.00 }
        ]
      }
    }
  },

  /**
   * Obtener estadísticas de servicios más populares
   */
  async getPopularServices(limit = 10) {
    try {
      const response = await api.get(`/api/stats/popular-services?limit=${limit}`)
      return response.data
    } catch (error) {
      console.warn('Backend no disponible, usando datos de fallback para popular services')
      return [
        { name: 'Corte Clásico', count: 45, percentage: 36 },
        { name: 'Barba + Corte', count: 32, percentage: 25 },
        { name: 'Barba', count: 25, percentage: 20 },
        { name: 'Lavado + Peinado', count: 15, percentage: 12 },
        { name: 'Afeitado Completo', count: 8, percentage: 7 }
      ]
    }
  },

  /**
   * Obtener estadísticas de barberos
   */
  async getBarberStats() {
    try {
      const response = await api.get('/api/stats/barbers')
      return response.data
    } catch (error) {
      console.warn('Backend no disponible, usando datos de fallback para barber stats')
      return [
        { name: 'Carlos Mendoza', reservations: 28, revenue: 840.00, rating: 4.8 },
        { name: 'Miguel Torres', reservations: 32, revenue: 960.00, rating: 4.9 },
        { name: 'David López', reservations: 25, revenue: 750.00, rating: 4.7 },
        { name: 'Roberto Silva', reservations: 22, revenue: 660.00, rating: 4.6 }
      ]
    }
  },

  /**
   * Obtener métricas en tiempo real
   */
  async getRealTimeMetrics() {
    try {
      const response = await api.get('/api/stats/real-time')
      return response.data
    } catch (error) {
      console.warn('Backend no disponible, usando datos de fallback para real-time metrics')
      return {
        activeReservations: 3,
        todayReservations: 8,
        waitingClients: 2,
        availableBarbers: 4,
        lastUpdate: new Date().toISOString()
      }
    }
  }
}

export default statsService
