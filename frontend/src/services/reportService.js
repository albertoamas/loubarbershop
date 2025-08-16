import api from './api.js'

/**
 * Servicio para gestionar reportes avanzados y exportación de datos
 */
const reportService = {
  // ========== REPORTES FINANCIEROS ==========
  
  /**
   * Obtener reporte financiero completo
   */
  async getFinancialReport(filters = {}) {
    try {
      const params = new URLSearchParams(filters)
      const response = await api.get(`/api/reports/financial?${params}`)
      return response.data
    } catch (error) {
      console.error('Error al obtener reporte financiero:', error)
      // Datos de fallback para desarrollo
      return this.getMockFinancialReport(filters)
    }
  },

  /**
   * Obtener análisis de rentabilidad por barbero
   */
  async getProfitabilityByBarber(period = 'month') {
    try {
      const response = await api.get(`/api/reports/profitability-barber?period=${period}`)
      return response.data
    } catch (error) {
      console.error('Error al obtener rentabilidad por barbero:', error)
      return this.getMockProfitabilityByBarber()
    }
  },

  /**
   * Obtener comparativas mensuales de ingresos
   */
  async getRevenueComparison(months = 12) {
    try {
      const response = await api.get(`/api/reports/revenue-comparison?months=${months}`)
      return response.data
    } catch (error) {
      console.error('Error al obtener comparativa de ingresos:', error)
      return this.getMockRevenueComparison()
    }
  },

  // ========== REPORTES OPERACIONALES ==========

  /**
   * Obtener reporte de ocupación por barbero
   */
  async getBarberOccupancy(filters = {}) {
    try {
      const params = new URLSearchParams(filters)
      const response = await api.get(`/api/reports/barber-occupancy?${params}`)
      return response.data
    } catch (error) {
      console.error('Error al obtener ocupación por barbero:', error)
      return this.getMockBarberOccupancy()
    }
  },

  /**
   * Obtener análisis de horarios más demandados
   */
  async getPeakHoursAnalysis(period = 'month') {
    try {
      const response = await api.get(`/api/reports/peak-hours?period=${period}`)
      return response.data
    } catch (error) {
      console.error('Error al obtener análisis de horarios:', error)
      return this.getMockPeakHoursAnalysis()
    }
  },

  /**
   * Obtener reporte de servicios más demandados
   */
  async getServiceDemandReport(filters = {}) {
    try {
      const params = new URLSearchParams(filters)
      const response = await api.get(`/api/reports/service-demand?${params}`)
      return response.data
    } catch (error) {
      console.error('Error al obtener demanda de servicios:', error)
      return this.getMockServiceDemandReport()
    }
  },

  // ========== ANALYTICS AVANZADOS ==========

  /**
   * Obtener tendencias de reservas
   */
  async getReservationTrends(period = 'year') {
    try {
      const response = await api.get(`/api/reports/reservation-trends?period=${period}`)
      return response.data
    } catch (error) {
      console.error('Error al obtener tendencias de reservas:', error)
      return this.getMockReservationTrends()
    }
  },

  /**
   * Obtener predicciones de demanda
   */
  async getDemandPredictions(months = 3) {
    try {
      const response = await api.get(`/api/reports/demand-predictions?months=${months}`)
      return response.data
    } catch (error) {
      console.error('Error al obtener predicciones de demanda:', error)
      return this.getMockDemandPredictions()
    }
  },

  /**
   * Obtener KPIs del negocio
   */
  async getBusinessKPIs(period = 'month') {
    try {
      const response = await api.get(`/api/reports/business-kpis?period=${period}`)
      return response.data
    } catch (error) {
      console.error('Error al obtener KPIs del negocio:', error)
      return this.getMockBusinessKPIs()
    }
  },

  // ========== EXPORTACIÓN DE DATOS ==========

  /**
   * Exportar reporte a PDF
   */
  async exportToPDF(reportType, filters = {}) {
    try {
      const params = new URLSearchParams({ ...filters, format: 'pdf' })
      const response = await api.get(`/api/reports/${reportType}/export?${params}`, {
        responseType: 'blob'
      })
      
      // Crear URL para descargar el archivo
      const blob = new Blob([response.data], { type: 'application/pdf' })
      const url = window.URL.createObjectURL(blob)
      
      // Crear enlace de descarga
      const link = document.createElement('a')
      link.href = url
      link.download = `reporte-${reportType}-${new Date().toISOString().split('T')[0]}.pdf`
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)
      
      return { success: true, message: 'Reporte exportado exitosamente' }
    } catch (error) {
      console.error('Error al exportar a PDF:', error)
      throw new Error('No se pudo exportar el reporte a PDF')
    }
  },

  /**
   * Exportar reporte a Excel
   */
  async exportToExcel(reportType, filters = {}) {
    try {
      const params = new URLSearchParams({ ...filters, format: 'xlsx' })
      const response = await api.get(`/api/reports/${reportType}/export?${params}`, {
        responseType: 'blob'
      })
      
      const blob = new Blob([response.data], { 
        type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' 
      })
      const url = window.URL.createObjectURL(blob)
      
      const link = document.createElement('a')
      link.href = url
      link.download = `reporte-${reportType}-${new Date().toISOString().split('T')[0]}.xlsx`
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)
      
      return { success: true, message: 'Reporte exportado exitosamente' }
    } catch (error) {
      console.error('Error al exportar a Excel:', error)
      throw new Error('No se pudo exportar el reporte a Excel')
    }
  },

  /**
   * Exportar datos a CSV
   */
  async exportToCSV(reportType, filters = {}) {
    try {
      const params = new URLSearchParams({ ...filters, format: 'csv' })
      const response = await api.get(`/api/reports/${reportType}/export?${params}`, {
        responseType: 'blob'
      })
      
      const blob = new Blob([response.data], { type: 'text/csv' })
      const url = window.URL.createObjectURL(blob)
      
      const link = document.createElement('a')
      link.href = url
      link.download = `reporte-${reportType}-${new Date().toISOString().split('T')[0]}.csv`
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)
      
      return { success: true, message: 'Reporte exportado exitosamente' }
    } catch (error) {
      console.error('Error al exportar a CSV:', error)
      throw new Error('No se pudo exportar el reporte a CSV')
    }
  },

  // ========== DATOS MOCK PARA DESARROLLO ==========

  getMockFinancialReport(filters) {
    return {
      period: filters.period || 'month',
      totalRevenue: 45780,
      totalExpenses: 15230,
      netProfit: 30550,
      profitMargin: 66.7,
      revenueByService: [
        { service: 'Corte Clásico', revenue: 18500, percentage: 40.4 },
        { service: 'Barba Completa', revenue: 12300, percentage: 26.9 },
        { service: 'Corte + Barba', revenue: 8900, percentage: 19.4 },
        { service: 'Tratamiento', revenue: 6080, percentage: 13.3 }
      ],
      revenueByBarber: [
        { barber: 'Carlos Mendoza', revenue: 15670, reservations: 89 },
        { barber: 'Miguel Torres', revenue: 14200, reservations: 82 },
        { barber: 'Jorge Ruiz', revenue: 15910, reservations: 91 }
      ],
      monthlyTrend: [
        { month: 'Ene', revenue: 42300 },
        { month: 'Feb', revenue: 39800 },
        { month: 'Mar', revenue: 45780 }
      ]
    }
  },

  getMockProfitabilityByBarber() {
    return [
      {
        barber: 'Carlos Mendoza',
        totalRevenue: 15670,
        totalReservations: 89,
        averageTicket: 176,
        efficiency: 92.5,
        profitMargin: 68.2
      },
      {
        barber: 'Miguel Torres',
        totalRevenue: 14200,
        totalReservations: 82,
        averageTicket: 173,
        efficiency: 89.3,
        profitMargin: 65.8
      },
      {
        barber: 'Jorge Ruiz',
        totalRevenue: 15910,
        totalReservations: 91,
        averageTicket: 175,
        efficiency: 94.1,
        profitMargin: 69.5
      }
    ]
  },

  getMockRevenueComparison() {
    return {
      currentYear: [
        { month: 'Ene', revenue: 42300, growth: 12.5 },
        { month: 'Feb', revenue: 39800, growth: -5.9 },
        { month: 'Mar', revenue: 45780, growth: 15.0 },
        { month: 'Abr', revenue: 47200, growth: 3.1 },
        { month: 'May', revenue: 49500, growth: 4.9 },
        { month: 'Jun', revenue: 51200, growth: 3.4 }
      ],
      previousYear: [
        { month: 'Ene', revenue: 37600 },
        { month: 'Feb', revenue: 42200 },
        { month: 'Mar', revenue: 39800 },
        { month: 'Abr', revenue: 45700 },
        { month: 'May', revenue: 47200 },
        { month: 'Jun', revenue: 49500 }
      ],
      yearOverYearGrowth: 8.7
    }
  },

  getMockBarberOccupancy() {
    return [
      {
        barber: 'Carlos Mendoza',
        totalHours: 160,
        occupiedHours: 148,
        occupancyRate: 92.5,
        idleHours: 12,
        peakDays: ['Viernes', 'Sábado']
      },
      {
        barber: 'Miguel Torres',
        totalHours: 160,
        occupiedHours: 143,
        occupancyRate: 89.3,
        idleHours: 17,
        peakDays: ['Jueves', 'Viernes']
      },
      {
        barber: 'Jorge Ruiz',
        totalHours: 160,
        occupiedHours: 150,
        occupancyRate: 93.7,
        idleHours: 10,
        peakDays: ['Viernes', 'Sábado', 'Domingo']
      }
    ]
  },

  getMockPeakHoursAnalysis() {
    return {
      hourlyDistribution: [
        { hour: '09:00', reservations: 15 },
        { hour: '10:00', reservations: 28 },
        { hour: '11:00', reservations: 42 },
        { hour: '12:00', reservations: 38 },
        { hour: '13:00', reservations: 25 },
        { hour: '14:00', reservations: 35 },
        { hour: '15:00', reservations: 47 },
        { hour: '16:00', reservations: 52 },
        { hour: '17:00', reservations: 48 },
        { hour: '18:00', reservations: 44 },
        { hour: '19:00', reservations: 32 }
      ],
      dayOfWeekDistribution: [
        { day: 'Lunes', reservations: 45 },
        { day: 'Martes', reservations: 52 },
        { day: 'Miércoles', reservations: 48 },
        { day: 'Jueves', reservations: 67 },
        { day: 'Viernes', reservations: 89 },
        { day: 'Sábado', reservations: 95 },
        { day: 'Domingo', reservations: 38 }
      ],
      peakHours: ['15:00-17:00', '16:00-18:00'],
      peakDays: ['Viernes', 'Sábado']
    }
  },

  getMockServiceDemandReport() {
    return {
      services: [
        {
          service: 'Corte Clásico',
          totalReservations: 125,
          revenue: 18500,
          averageRating: 4.8,
          demandTrend: 'up',
          growthRate: 12.5
        },
        {
          service: 'Barba Completa',
          totalReservations: 89,
          revenue: 12300,
          averageRating: 4.9,
          demandTrend: 'stable',
          growthRate: 2.1
        },
        {
          service: 'Corte + Barba',
          totalReservations: 67,
          revenue: 8900,
          averageRating: 4.7,
          demandTrend: 'up',
          growthRate: 18.3
        }
      ],
      totalDemand: 281,
      averageDemandGrowth: 10.9
    }
  },

  getMockReservationTrends() {
    return {
      monthly: [
        { month: 'Ene', reservations: 234, growth: 8.5 },
        { month: 'Feb', reservations: 218, growth: -6.8 },
        { month: 'Mar', reservations: 267, growth: 22.5 },
        { month: 'Abr', reservations: 289, growth: 8.2 },
        { month: 'May', reservations: 312, growth: 8.0 },
        { month: 'Jun', reservations: 334, growth: 7.1 }
      ],
      seasonal: {
        spring: { reservations: 868, growth: 12.8 },
        summer: { reservations: 945, growth: 8.9 },
        fall: { reservations: 823, growth: -12.9 },
        winter: { reservations: 756, growth: -8.1 }
      }
    }
  },

  getMockDemandPredictions() {
    return {
      predictions: [
        { month: 'Jul', predictedReservations: 342, confidence: 87.5 },
        { month: 'Ago', predictedReservations: 356, confidence: 85.2 },
        { month: 'Sep', predictedReservations: 329, confidence: 82.8 }
      ],
      factors: [
        'Tendencia estacional',
        'Crecimiento histórico',
        'Días festivos',
        'Promociones planificadas'
      ],
      recommendedActions: [
        'Aumentar personal en Julio y Agosto',
        'Planificar promociones para Septiembre',
        'Optimizar inventario de productos'
      ]
    }
  },

  getMockBusinessKPIs() {
    return {
      customerSatisfaction: {
        current: 4.7,
        target: 4.5,
        trend: 'up',
        improvement: 0.2
      },
      averageTicketValue: {
        current: 175,
        target: 180,
        trend: 'up',
        improvement: 8.5
      },
      customerRetention: {
        current: 78.5,
        target: 80.0,
        trend: 'stable',
        improvement: 1.2
      },
      operationalEfficiency: {
        current: 91.8,
        target: 90.0,
        trend: 'up',
        improvement: 3.4
      },
      revenuePerBarber: {
        current: 15260,
        target: 15000,
        trend: 'up',
        improvement: 5.2
      },
      noShowRate: {
        current: 8.2,
        target: 10.0,
        trend: 'down',
        improvement: -12.8
      }
    }
  }
}

export default reportService
