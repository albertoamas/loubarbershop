<!--
  MyReservationsView - Vista de mis reservas
  Página donde el cliente puede ver todas sus reservaciones
-->
<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Hero Section -->
    <section class="bg-[var(--color-barber-primary)] py-16 md:py-20 relative overflow-hidden">
      <!-- Elementos decorativos de fondo -->
      <div class="absolute inset-0">
        <div class="absolute top-10 left-10 w-32 h-32 bg-[var(--color-barber-gold)]/10 rounded-full blur-xl"></div>
        <div class="absolute bottom-10 right-10 w-48 h-48 bg-[var(--color-barber-gold)]/5 rounded-full blur-2xl"></div>
        <div class="absolute top-1/2 left-1/4 w-16 h-16 bg-white/10 rounded-full blur-lg"></div>
      </div>
      
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <div class="text-center">
          <!-- Logo/Nombre con estilo mejorado -->
          <div class="mb-6">
            <div class="inline-flex items-center justify-center px-4 py-2 bg-[var(--color-barber-gold)] text-[var(--color-barber-primary)] rounded-full text-sm font-bold mb-4 shadow-lg">
              📅 Low BarberShop
            </div>
            <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold text-white mb-4 leading-tight">
              Mis 
              <span class="bg-gradient-to-r from-[var(--color-barber-gold)] to-yellow-300 bg-clip-text text-transparent">
                Reservas
              </span>
            </h1>
          </div>
          
          <!-- Descripción mejorada -->
          <p class="text-gray-300 max-w-3xl mx-auto text-lg md:text-xl leading-relaxed">
            Consulta el estado de todas tus reservaciones y historial de citas
          </p>
        </div>
      </div>
    </section>

    <!-- Loading State -->
    <div v-if="loading" class="flex flex-col justify-center items-center py-24">
      <div class="relative">
        <div class="animate-spin rounded-full h-16 w-16 border-4 border-gray-200"></div>
        <div class="animate-spin rounded-full h-16 w-16 border-4 border-[var(--color-barber-primary)] border-t-transparent absolute inset-0"></div>
      </div>
      <p class="text-gray-600 text-lg font-medium mt-6">Cargando tus reservas...</p>
    </div>

    <!-- Error State -->
    <div v-if="error" class="text-center py-24">
      <div class="max-w-md mx-auto">
        <div class="w-16 h-16 bg-yellow-100 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-3">Error al cargar reservas</h3>
        <p class="text-gray-600 mb-6">{{ error }}</p>
        <button 
          @click="loadReservations" 
          class="bg-[var(--color-barber-primary)] text-white px-8 py-3 rounded-lg hover:bg-[var(--color-barber-gold)] transition-all duration-200 transform hover:scale-105 shadow-lg"
        >
          Reintentar
        </button>
      </div>
    </div>

    <!-- Content Section -->
    <section v-if="!loading && !error" class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Estadísticas rápidas -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-12">
          <div class="bg-white rounded-3xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 border border-gray-100">
            <div class="flex items-center">
              <div class="w-12 h-12 bg-gradient-to-br from-[var(--color-barber-primary)] to-gray-700 rounded-2xl flex items-center justify-center mr-4">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                </svg>
              </div>
              <div>
                <div class="text-2xl font-bold text-gray-900">{{ totalReservations }}</div>
                <div class="text-sm text-gray-600">Total Reservas</div>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-3xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 border border-gray-100">
            <div class="flex items-center">
              <div class="w-12 h-12 bg-gradient-to-br from-green-500 to-emerald-600 rounded-2xl flex items-center justify-center mr-4">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
              </div>
              <div>
                <div class="text-2xl font-bold text-gray-900">{{ confirmedReservations }}</div>
                <div class="text-sm text-gray-600">Confirmadas</div>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-3xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 border border-gray-100">
            <div class="flex items-center">
              <div class="w-12 h-12 bg-gradient-to-br from-yellow-500 to-orange-500 rounded-2xl flex items-center justify-center mr-4">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div>
                <div class="text-2xl font-bold text-gray-900">{{ pendingReservations }}</div>
                <div class="text-sm text-gray-600">Pendientes</div>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-3xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 border border-gray-100">
            <div class="flex items-center">
              <div class="w-12 h-12 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center mr-4">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
              </div>
              <div>
                <div class="text-2xl font-bold text-gray-900">{{ upcomingReservations }}</div>
                <div class="text-sm text-gray-600">Próximas</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Filtros -->
        <div class="bg-white rounded-3xl shadow-lg border border-gray-100 p-6 mb-8">
          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
          <div class="flex flex-wrap gap-3">
            <button 
              v-for="filter in filters"
              :key="filter.key"
              @click="changeFilter(filter.key)"
              :class="activeFilter === filter.key 
                ? 'bg-[var(--color-barber-primary)] text-white shadow-lg' 
                : 'bg-gray-50 text-gray-700 hover:bg-gray-100'"
              class="px-6 py-2 rounded-xl font-medium transition-all duration-200 hover:shadow-md"
            >
              {{ filter.label }}
            </button>
          </div>            <!-- Botón nueva reserva -->
            <RouterLink 
              to="/reservas"
              class="bg-[var(--color-barber-gold)] text-[var(--color-barber-primary)] px-6 py-3 rounded-xl font-bold hover:bg-yellow-300 transition-all duration-200 transform hover:scale-105 shadow-lg whitespace-nowrap text-center"
            >
              + Nueva Reserva
            </RouterLink>
          </div>
        </div>

        <!-- Lista de reservas -->
        <div v-if="filteredReservations.length === 0" class="text-center py-20">
          <div class="max-w-md mx-auto">
            <div class="w-24 h-24 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-8">
              <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-gray-900 mb-4">No tienes reservas</h3>
            <p class="text-gray-600 mb-8 leading-relaxed">
              Aún no has realizado ninguna reserva.<br>
              ¡Agenda tu primera cita ahora!
            </p>
            <RouterLink 
              to="/reservas"
              class="bg-[var(--color-barber-primary)] text-white px-8 py-3 rounded-lg font-medium hover:bg-[var(--color-barber-gold)] transition-all duration-200 shadow-lg"
            >
              Hacer mi Primera Reserva
            </RouterLink>
          </div>
        </div>

        <!-- Grid de reservas -->
        <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div 
            v-for="reservation in filteredReservations"
            :key="reservation.id"
            class="bg-white rounded-3xl shadow-lg hover:shadow-xl transition-all duration-300 p-6 border border-gray-100 group"
          >
            <!-- Header de la reserva -->
            <div class="flex items-start justify-between mb-4">
              <div class="flex-1">
                <h3 class="text-xl font-bold text-gray-900 mb-2">
                  {{ reservation.servicio || reservation.service_name }}
                </h3>
                <div class="flex items-center text-sm text-gray-600 mb-2">
                  <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                  </svg>
                  {{ formatDate(reservation.fecha || reservation.date) }}
                </div>
                <div class="flex items-center text-sm text-gray-600">
                  <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                  {{ reservation.hora || reservation.time }}
                </div>
              </div>
              
              <!-- Estado badge -->
              <div 
                :class="getStatusClass(reservation.estado || reservation.status)"
                class="px-3 py-1 rounded-full text-xs font-bold tracking-wide"
              >
                {{ getStatusText(reservation.estado || reservation.status) }}
              </div>
            </div>

            <!-- Información adicional -->
            <div class="grid grid-cols-2 gap-4 mb-4 p-4 bg-gray-50 rounded-2xl">
              <div>
                <div class="text-sm text-gray-500 mb-1">Barbero</div>
                <div class="font-semibold text-gray-900">{{ reservation.barbero || reservation.barber_name || 'Por asignar' }}</div>
              </div>
              <div>
                <div class="text-sm text-gray-500 mb-1">Precio</div>
                <div class="font-bold text-lg text-black">Bs {{ formatPrice(reservation.precio || reservation.price) }}</div>
              </div>
            </div>

            <!-- Notas si las hay -->
            <div v-if="reservation.notas || reservation.notes" class="mb-4">
              <div class="text-sm text-gray-500 mb-1">Notas</div>
              <div class="text-gray-700 bg-blue-50 p-3 rounded-lg text-sm">
                {{ reservation.notas || reservation.notes }}
              </div>
            </div>

            <!-- Acciones -->
            <div class="flex gap-3 pt-4 border-t border-gray-100">
              <button 
                v-if="canCancel(reservation)"
                @click="cancelReservation(reservation)"
                class="flex-1 bg-red-50 text-red-600 px-4 py-2 rounded-lg font-medium hover:bg-red-100 transition-all duration-200 text-sm"
              >
                Cancelar
              </button>
              <button 
                v-if="canReschedule(reservation)"
                @click="rescheduleReservation(reservation)"
                class="flex-1 bg-blue-50 text-blue-600 px-4 py-2 rounded-lg font-medium hover:bg-blue-100 transition-all duration-200 text-sm"
              >
                Reprogramar
              </button>
              <button 
                class="flex-1 bg-gray-50 text-gray-600 px-4 py-2 rounded-lg font-medium hover:bg-gray-100 transition-all duration-200 text-sm"
                @click="viewDetails(reservation)"
              >
                Ver Detalles
              </button>
            </div>
          </div>
        </div>

        <!-- Botón "Ver más" -->
        <div v-if="!showAllReservations && hasMoreReservations" class="text-center mt-12">
          <button
            @click="showAllReservations = true"
            class="bg-[var(--color-barber-primary)] text-white px-8 py-3 rounded-xl font-medium hover:bg-[var(--color-barber-gold)] transition-all duration-200 transform hover:scale-105 shadow-lg"
          >
            Ver Más Reservas
          </button>
          <p class="text-gray-500 text-sm mt-2">
            Mostrando las {{ filteredReservations.length }} más recientes
          </p>
        </div>

        <!-- Botón "Ver menos" cuando se muestran todas -->
        <div v-if="showAllReservations && hasMoreReservations" class="text-center mt-12">
          <button
            @click="showAllReservations = false"
            class="bg-gray-500 text-white px-8 py-3 rounded-xl font-medium hover:bg-gray-600 transition-all duration-200 transform hover:scale-105 shadow-lg"
          >
            Ver Menos
          </button>
          <p class="text-gray-500 text-sm mt-2">
            Mostrando todas las {{ filteredReservations.length }} reservas
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { reservationService } from '@/services'

export default {
  name: 'MyReservationsView',
  data() {
    return {
      loading: true,
      error: null,
      reservations: [],
      activeFilter: 'all',
      showAllReservations: false, // Nueva propiedad para controlar mostrar todas
      filters: [
        { key: 'all', label: 'Todas' },
        { key: 'pending', label: 'Pendientes' },
        { key: 'confirmed', label: 'Confirmadas' },
        { key: 'completed', label: 'Completadas' },
        { key: 'cancelled', label: 'Canceladas' }
      ]
    }
  },
  
  computed: {
    totalReservations() {
      return this.reservations.length
    },
    
    confirmedReservations() {
      return this.reservations.filter(r => 
        (r.estado || r.status) === 'confirmada' || (r.estado || r.status) === 'confirmed'
      ).length
    },
    
    pendingReservations() {
      return this.reservations.filter(r => 
        (r.estado || r.status) === 'pendiente' || (r.estado || r.status) === 'pending'
      ).length
    },
    
    upcomingReservations() {
      const today = new Date()
      return this.reservations.filter(r => {
        const reservationDate = new Date(r.fecha || r.date)
        return reservationDate >= today && 
               ((r.estado || r.status) === 'confirmada' || (r.estado || r.status) === 'confirmed')
      }).length
    },
    
    filteredReservations() {
      let filtered = []
      
      if (this.activeFilter === 'all') {
        filtered = this.reservations
      } else {
        filtered = this.reservations.filter(reservation => {
          const status = reservation.estado || reservation.status
          
          switch (this.activeFilter) {
            case 'pending':
              return status === 'pendiente' || status === 'pending'
            case 'confirmed':
              return status === 'confirmada' || status === 'confirmed'
            case 'completed':
              return status === 'completada' || status === 'completed'
            case 'cancelled':
              return status === 'cancelada' || status === 'cancelled'
            default:
              return true
          }
        })
      }
      
      // Ordenar por fecha, más reciente primero
      filtered = filtered.sort((a, b) => {
        const dateA = new Date(a.fecha || a.date)
        const dateB = new Date(b.fecha || b.date)
        return dateB - dateA
      })
      
      // Limitar a 6 reservas si no se muestran todas
      if (!this.showAllReservations) {
        return filtered.slice(0, 6)
      }
      
      return filtered
    },
    
    hasMoreReservations() {
      // Verificar si hay más de 6 reservas para mostrar el botón "Ver más"
      let totalFiltered = []
      
      if (this.activeFilter === 'all') {
        totalFiltered = this.reservations
      } else {
        totalFiltered = this.reservations.filter(reservation => {
          const status = reservation.estado || reservation.status
          
          switch (this.activeFilter) {
            case 'pending':
              return status === 'pendiente' || status === 'pending'
            case 'confirmed':
              return status === 'confirmada' || status === 'confirmed'
            case 'completed':
              return status === 'completada' || status === 'completed'
            case 'cancelled':
              return status === 'cancelada' || status === 'cancelled'
            default:
              return true
          }
        })
      }
      
      return totalFiltered.length > 6
    }
  },
  
  async mounted() {
    await this.loadReservations()
  },
  
  methods: {
    async loadReservations() {
      this.loading = true
      this.error = null
      
      try {
        const response = await reservationService.getMyReservations()
        
        if (response.success) {
          this.reservations = response.data
        } else {
          // Cargar datos de ejemplo si no hay servicio
          this.loadMockReservations()
        }
      } catch (error) {
        console.error('Error al cargar reservas:', error)
        // Cargar datos de ejemplo en caso de error
        this.loadMockReservations()
      } finally {
        this.loading = false
      }
    },
    
    loadMockReservations() {
      // Datos de ejemplo para desarrollo (más de 6 para probar la funcionalidad)
      this.reservations = [
        {
          id: 1,
          servicio: 'Corte de Cabello Premium',
          fecha: '2025-01-15',
          hora: '10:00',
          estado: 'confirmada',
          barbero: 'Carlos López',
          precio: 50.00,
          notas: 'Corte moderno, laterales degradados'
        },
        {
          id: 2,
          servicio: 'Barba + Bigote',
          fecha: '2025-01-20',
          hora: '14:30',
          estado: 'pendiente',
          barbero: 'Miguel Torres',
          precio: 40.00,
          notas: 'Mantener longitud actual, solo perfilar'
        },
        {
          id: 3,
          servicio: 'Servicio Completo',
          fecha: '2024-12-28',
          hora: '16:00',
          estado: 'completada',
          barbero: 'Carlos López',
          precio: 80.00,
          notas: 'Excelente servicio como siempre'
        },
        {
          id: 4,
          servicio: 'Corte Clásico',
          fecha: '2024-12-20',
          hora: '11:30',
          estado: 'completada',
          barbero: 'Ana García',
          precio: 45.00,
          notas: 'Corte tradicional, muy satisfecho'
        },
        {
          id: 5,
          servicio: 'Arreglo de Barba',
          fecha: '2024-12-15',
          hora: '15:00',
          estado: 'completada',
          barbero: 'Miguel Torres',
          precio: 35.00,
          notas: 'Perfilado perfecto'
        },
        {
          id: 6,
          servicio: 'Lavado + Peinado',
          fecha: '2024-12-10',
          hora: '09:00',
          estado: 'completada',
          barbero: 'Carlos López',
          precio: 25.00,
          notas: 'Servicio rápido y eficiente'
        },
        {
          id: 7,
          servicio: 'Corte + Barba Premium',
          fecha: '2024-11-30',
          hora: '17:30',
          estado: 'completada',
          barbero: 'Ana García',
          precio: 70.00,
          notas: 'Transformación completa del look'
        },
        {
          id: 8,
          servicio: 'Corte de Cabello',
          fecha: '2024-11-22',
          hora: '13:00',
          estado: 'cancelada',
          barbero: 'Miguel Torres',
          precio: 50.00,
          notas: 'Cancelada por enfermedad'
        },
        {
          id: 9,
          servicio: 'Servicio Express',
          fecha: '2024-11-15',
          hora: '12:15',
          estado: 'completada',
          barbero: 'Carlos López',
          precio: 30.00,
          notas: 'Retoque rápido antes de evento'
        }
      ]
    },
    
    formatDate(dateString) {
      const date = new Date(dateString)
      return date.toLocaleDateString('es-ES', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    },
    
    formatPrice(price) {
      if (!price && price !== 0) return '0.00'
      return parseFloat(price).toFixed(2)
    },
    
    getStatusClass(status) {
      const statusMap = {
        'pendiente': 'bg-yellow-100 text-yellow-800',
        'pending': 'bg-yellow-100 text-yellow-800',
        'confirmada': 'bg-green-100 text-green-800',
        'confirmed': 'bg-green-100 text-green-800',
        'completada': 'bg-blue-100 text-blue-800',
        'completed': 'bg-blue-100 text-blue-800',
        'cancelada': 'bg-red-100 text-red-800',
        'cancelled': 'bg-red-100 text-red-800'
      }
      return statusMap[status] || 'bg-gray-100 text-gray-800'
    },
    
    getStatusText(status) {
      const statusMap = {
        'pendiente': 'PENDIENTE',
        'pending': 'PENDIENTE',
        'confirmada': 'CONFIRMADA',
        'confirmed': 'CONFIRMADA',
        'completada': 'COMPLETADA',
        'completed': 'COMPLETADA',
        'cancelada': 'CANCELADA',
        'cancelled': 'CANCELADA'
      }
      return statusMap[status] || status?.toUpperCase() || 'DESCONOCIDO'
    },
    
    canCancel(reservation) {
      const status = reservation.estado || reservation.status
      const reservationDate = new Date(reservation.fecha || reservation.date)
      const now = new Date()
      
      // Solo se puede cancelar si está pendiente o confirmada y es futura
      return (status === 'pendiente' || status === 'pending' || 
              status === 'confirmada' || status === 'confirmed') &&
             reservationDate > now
    },
    
    canReschedule(reservation) {
      const status = reservation.estado || reservation.status
      const reservationDate = new Date(reservation.fecha || reservation.date)
      const now = new Date()
      
      // Solo se puede reprogramar si está confirmada y es futura
      return (status === 'confirmada' || status === 'confirmed') &&
             reservationDate > now
    },
    
    changeFilter(filterKey) {
      this.activeFilter = filterKey
      // Resetear a mostrar solo las primeras 6 cuando se cambie de filtro
      this.showAllReservations = false
    },
    
    async cancelReservation(reservation) {
      if (!confirm('¿Estás seguro de que deseas cancelar esta reserva?')) {
        return
      }
      
      try {
        const response = await reservationService.cancelReservation(reservation.id)
        
        if (response.success) {
          // Actualizar el estado local
          const index = this.reservations.findIndex(r => r.id === reservation.id)
          if (index !== -1) {
            this.reservations[index].estado = 'cancelada'
          }
          alert('Reserva cancelada exitosamente')
        } else {
          alert('Error al cancelar la reserva')
        }
      } catch (error) {
        console.error('Error al cancelar reserva:', error)
        alert('Error al cancelar la reserva')
      }
    },
    
    rescheduleReservation(reservation) {
      // Redirigir a la página de reservas con los datos pre-llenados
      this.$router.push({
        name: 'reservations',
        query: {
          reschedule: reservation.id,
          service: reservation.servicio || reservation.service_name
        }
      })
    },
    
    viewDetails(reservation) {
      // Por ahora solo mostrar un alert con los detalles
      // En el futuro podrías abrir un modal o ir a una página de detalles
      alert(`Detalles de la Reserva #${reservation.id}
      
Servicio: ${reservation.servicio || reservation.service_name}
Fecha: ${this.formatDate(reservation.fecha || reservation.date)}
Hora: ${reservation.hora || reservation.time}
Barbero: ${reservation.barbero || reservation.barber_name || 'Por asignar'}
Estado: ${this.getStatusText(reservation.estado || reservation.status)}
Precio: Bs ${this.formatPrice(reservation.precio || reservation.price)}
${reservation.notas || reservation.notes ? `\nNotas: ${reservation.notas || reservation.notes}` : ''}`)
    }
  }
}
</script>
