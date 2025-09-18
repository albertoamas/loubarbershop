<!--
  AdminReservas.vue - Gestión completa de reservas
  FASE 8.4: Integración con base de datos real
-->
<template>
  <div class="p-8 bg-gradient-to-br from-slate-50 to-slate-100 min-h-[calc(100vh-80px)]">
    <!-- Notificación de estado de conexión -->
    <div v-if="!modoDemo && reservations.length > 0" class="mb-6 p-4 bg-gradient-to-r from-emerald-100 to-emerald-50 border border-emerald-200 rounded-2xl text-emerald-800 font-semibold text-sm shadow-sm">
      ✅ Conectado a la base de datos: Mostrando reservas reales del sistema
    </div>

    <!-- Header del dashboard modernizado -->
    <div class="mb-6 bg-white rounded-2xl p-6 shadow-sm border border-gray-200">
      <div class="flex flex-col lg:flex-row lg:justify-between lg:items-start gap-6">
        <div class="flex-1">
          <h1 class="text-3xl font-extrabold bg-gradient-to-r from-black to-gray-500 bg-clip-text text-transparent mb-2">
            Gestión de Reservas
          </h1>
          <p class="text-lg text-gray-600 font-medium">
            Panel de administración y control de reservas de Low Barber Shop
          </p>
        </div>
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
          <button 
            @click="loadReservations" 
            :disabled="loadingReservations"
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-black to-gray-500 text-white border-none rounded-xl font-semibold text-sm cursor-pointer transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5 disabled:opacity-70 disabled:cursor-not-allowed disabled:transform-none"
          >
            <svg :class="{ 'animate-spin': loadingReservations }" class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            {{ loadingReservations ? 'Actualizando...' : 'Actualizar' }}
          </button>
          <button 
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white border-none rounded-xl font-semibold text-sm cursor-pointer transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5"
            @click="openCreateModal"
          >
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
            </svg>
            Nueva Reserva
          </button>
        </div>
      </div>
    </div> 

    <!-- Grid de estadísticas modernizado -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <!-- Total de reservas -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Total</h3>
            <p class="text-3xl font-black text-blue-600">{{ stats.total || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-blue-100 to-blue-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Reservas de hoy -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Hoy</h3>
            <p class="text-3xl font-black text-emerald-600">{{ stats.today || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-emerald-100 to-emerald-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Reservas pendientes -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Pendientes</h3>
            <p class="text-3xl font-black text-amber-600">{{ stats.pending || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-amber-100 to-amber-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Reservas completadas -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Completadas</h3>
            <p class="text-3xl font-black text-green-600">{{ stats.completed || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-green-100 to-green-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Filtros modernizados -->
    <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200 mb-6">
      <div class="flex flex-col sm:flex-row gap-4 items-stretch sm:items-center">
        <input
          v-model="searchTerm"
          type="text"
          placeholder="Buscar por cliente, barbero o servicio..."
          class="flex-1 min-w-0 px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:ring-2 focus:ring-violet-500 focus:border-transparent transition-all duration-200"
        />
        
        <select v-model="statusFilter" class="px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:ring-2 focus:ring-violet-500 focus:border-transparent transition-all duration-200 min-w-[180px]">
          <option value="">Todos los estados</option>
          <option value="pendiente">Pendientes</option>
          <option value="confirmada">Confirmadas</option>
          <option value="completada">Completadas</option>
          <option value="cancelada">Canceladas</option>
        </select>
        
        <select v-model="barberFilter" class="px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:ring-2 focus:ring-violet-500 focus:border-transparent transition-all duration-200 min-w-[200px]">
          <option value="">Todos los barberos</option>
          <option v-for="barber in availableBarbers" :key="barber.id" :value="barber.id">
            {{ barber.nombre }}
          </option>
        </select>
      </div>
    </div>

    <!-- Lista de reservas modernizada -->
    <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200">
      <div v-if="loadingReservations" class="flex flex-col items-center justify-center py-16 text-gray-500">
        <div class="w-12 h-12 border-3 border-gray-200 border-t-violet-500 rounded-full animate-spin mb-4"></div>
        <p class="text-lg font-medium">Cargando reservas...</p>
      </div>
      
      <div v-else-if="filteredReservations.length === 0" class="flex flex-col items-center justify-center py-16 text-gray-500 text-center">
        <svg class="w-16 h-16 text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
        </svg>
        <h3 class="text-xl font-semibold text-gray-700 mb-2">No se encontraron reservas</h3>
        <p class="text-gray-500 mb-6">No hay reservas que coincidan con los filtros aplicados.</p>
        <button @click="openCreateModal" class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white border-none rounded-xl font-semibold text-sm cursor-pointer transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5">
          Crear primera reserva
        </button>
      </div>
      
      <div v-else class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
        <div
          v-for="reservation in filteredReservations"
          :key="reservation.id"
          class="bg-slate-50 border border-slate-200 rounded-2xl p-6 transition-all duration-200 hover:border-violet-400 hover:shadow-lg hover:-translate-y-0.5"
        >
          <!-- Header de la reserva con cliente -->
          <div class="flex items-start gap-4 mb-4">
            <div class="w-12 h-12 flex-shrink-0">
              <div class="w-full h-full rounded-xl bg-gradient-to-br from-blue-500 to-blue-600 text-white flex items-center justify-center font-semibold text-sm">
                {{ getInitials(reservation.cliente_nombre || 'Usuario') }}
              </div>
            </div>
            
            <div class="flex-1 min-w-0">
              <h3 class="font-semibold text-gray-900 text-base mb-1 truncate">{{ reservation.cliente_nombre || 'Sin nombre' }}</h3>
              <p class="text-gray-500 text-sm mb-2 truncate">{{ reservation.cliente_email || 'Sin email' }}</p>
              <span :class="getStatusBadgeClass(reservation.estado)" class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold">
                <div :class="getStatusDotClass(reservation.estado)" class="w-2 h-2 rounded-full"></div>
                {{ getStatusLabel(reservation.estado) }}
              </span>
            </div>
          </div>
          
          <!-- Información de la reserva -->
          <div class="space-y-3 mb-4">
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Barbero:</span>
              <span class="text-sm text-gray-900 font-medium">
                {{ reservation.barbero_nombre || 'Sin asignar' }}
              </span>
            </div>
            
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Fecha:</span>
              <span class="text-sm text-gray-900 font-medium">{{ formatDate(reservation.fecha_reserva) }}</span>
            </div>
            
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Hora:</span>
              <span class="text-sm text-gray-900 font-medium">{{ reservation.hora_inicio || 'Sin hora' }}</span>
            </div>
            
            <div v-if="reservation.servicio_nombre" class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Servicio:</span>
              <span class="text-sm text-gray-900 font-medium">{{ reservation.servicio_nombre }}</span>
            </div>
          </div>
          
          <!-- Acciones -->
          <div class="flex gap-2 justify-end flex-wrap">
            <button @click="viewReservation(reservation)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg cursor-pointer transition-all duration-200 bg-blue-50 text-blue-700 border-blue-200 hover:bg-blue-100 hover:border-blue-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
              </svg>
              Ver
            </button>
            
            <button v-if="reservation.estado === 'pendiente'" @click="confirmReservation(reservation)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg cursor-pointer transition-all duration-200 bg-green-50 text-green-700 border-green-200 hover:bg-green-100 hover:border-green-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              Confirmar
            </button>
            
            <button @click="editReservation(reservation)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg cursor-pointer transition-all duration-200 bg-amber-50 text-amber-700 border-amber-200 hover:bg-amber-100 hover:border-amber-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
              Editar
            </button>
            
            <button @click="cancelReservation(reservation)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg cursor-pointer transition-all duration-200 bg-red-50 text-red-700 border-red-200 hover:bg-red-100 hover:border-red-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
              Cancelar
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import reservationService from '@/services/reservationService'

export default {
  name: 'AdminReservas',
  setup() {
    // Estados reactivos
    const loadingReservations = ref(true)
    const reservations = ref([])
    const selectedReservations = ref([])
    const stats = ref({
      total: 0,
      today: 0,
      pending: 0,
      confirmed: 0,
      completed: 0
    })
    const modoDemo = ref(false)
    
    // Filtros
    const searchTerm = ref('')
    const statusFilter = ref('')
    const barberFilter = ref('')
    const availableBarbers = ref([])
    
    // Configuración de tabla
    const tableColumns = [
      {
        key: 'cliente_nombre',
        label: 'Cliente',
        sortable: true
      },
      {
        key: 'barbero_nombre',
        label: 'Barbero',
        sortable: true
      },
      {
        key: 'estado',
        label: 'Estado',
        sortable: true
      },
      {
        key: 'fecha_reserva',
        label: 'Fecha y Hora',
        sortable: true
      }
    ]
    
    const filteredReservations = computed(() => {
      if (!Array.isArray(reservations.value)) {
        return []
      }

      let filtered = [...reservations.value]
      
      // Filtro por término de búsqueda
      if (searchTerm.value) {
        const term = searchTerm.value.toLowerCase()
        filtered = filtered.filter(reservation => 
          (reservation.cliente_nombre && reservation.cliente_nombre.toLowerCase().includes(term)) ||
          (reservation.cliente_email && reservation.cliente_email.toLowerCase().includes(term)) ||
          (reservation.barbero_nombre && reservation.barbero_nombre.toLowerCase().includes(term)) ||
          (reservation.servicio_nombre && reservation.servicio_nombre.toLowerCase().includes(term))
        )
      }
      
      // Filtro por estado
      if (statusFilter.value) {
        filtered = filtered.filter(reservation => reservation.estado === statusFilter.value)
      }
      
      // Filtro por barbero
      if (barberFilter.value) {
        filtered = filtered.filter(reservation => reservation.barber_id === parseInt(barberFilter.value))
      }
      
      return filtered
    })

    const paginatedReservations = computed(() => {
      return filteredReservations.value
    })
    
    // Métodos
    const loadReservations = async () => {
      try {
        loadingReservations.value = true
        const response = await reservationService.getAll()
        
        if (response && Array.isArray(response.data)) {
          reservations.value = response.data
          modoDemo.value = response.isDemo || false
          calculateStats()
        }
      } catch (error) {
        console.error('Error cargando reservas:', error)
        reservations.value = []
      } finally {
        loadingReservations.value = false
      }
    }

    const calculateStats = () => {
      const today = new Date()
      const todayStr = today.toISOString().split('T')[0]
      
      stats.value = {
        total: reservations.value.length,
        today: reservations.value.filter(r => r.fecha_reserva === todayStr).length,
        pending: reservations.value.filter(r => r.estado === 'pendiente').length,
        confirmed: reservations.value.filter(r => r.estado === 'confirmada').length,
        completed: reservations.value.filter(r => r.estado === 'completada').length
      }
    }

    const clearFilters = () => {
      searchTerm.value = ''
      statusFilter.value = ''
      barberFilter.value = ''
    }

    const openCreateModal = () => {
      console.log('Abrir modal de creación')
    }

    const viewReservation = (reservation) => {
      console.log('Ver reserva:', reservation)
    }

    const confirmReservation = async (reservation) => {
      try {
        // Aquí iría la lógica para confirmar la reserva
        console.log('Confirmar reserva:', reservation)
        // await reservationService.updateStatus(reservation.id, 'confirmada')
        // await loadReservations()
      } catch (error) {
        console.error('Error confirmando reserva:', error)
      }
    }

    const editReservation = (reservation) => {
      console.log('Editar reserva:', reservation)
      // Aquí iría la lógica para abrir el modal de edición
    }

    const cancelReservation = async (reservation) => {
      try {
        if (confirm('¿Estás seguro de que quieres cancelar esta reserva?')) {
          console.log('Cancelar reserva:', reservation)
          // await reservationService.updateStatus(reservation.id, 'cancelada')
          // await loadReservations()
        }
      } catch (error) {
        console.error('Error cancelando reserva:', error)
      }
    }
    
    // Helpers
    const getInitials = (name) => {
      if (!name) return '??'
      return name.split(' ')
        .map(word => word.charAt(0))
        .join('')
        .toUpperCase()
        .slice(0, 2)
    }

    const getStatusBadgeClass = (status) => {
      switch (status) {
        case 'pendiente': return 'bg-amber-50 text-amber-700 border border-amber-200'
        case 'confirmada': return 'bg-blue-50 text-blue-700 border border-blue-200'
        case 'completada': return 'bg-green-50 text-green-700 border border-green-200'
        case 'cancelada': return 'bg-red-50 text-red-700 border border-red-200'
        default: return 'bg-gray-50 text-gray-700 border border-gray-200'
      }
    }

    const getStatusDotClass = (status) => {
      switch (status) {
        case 'pendiente': return 'bg-amber-400'
        case 'confirmada': return 'bg-blue-400'
        case 'completada': return 'bg-green-400'
        case 'cancelada': return 'bg-red-400'
        default: return 'bg-gray-400'
      }
    }

    const getStatusLabel = (status) => {
      switch (status) {
        case 'pendiente': return 'Pendiente'
        case 'confirmada': return 'Confirmada'
        case 'completada': return 'Completada'
        case 'cancelada': return 'Cancelada'
        default: return 'Pendiente'
      }
    }

    const formatDate = (date) => {
      if (!date) return 'Sin fecha'
      return new Date(date).toLocaleDateString('es-ES')
    }
    
    // Lifecycle
    onMounted(() => {
      loadReservations()
    })

    return {
      // Estados
      loadingReservations,
      reservations,
      selectedReservations,
      stats,
      modoDemo,
      searchTerm,
      statusFilter,
      barberFilter,
      availableBarbers,
      
      // Computed
      filteredReservations,
      paginatedReservations,
      
      // Métodos
      loadReservations,
      clearFilters,
      openCreateModal,
      viewReservation,
      confirmReservation,
      editReservation,
      cancelReservation,
      
      // Helpers
      getInitials,
      getStatusBadgeClass,
      getStatusDotClass,
      getStatusLabel,
      formatDate
    }
  }
}
</script>

<style scoped>
/* Estilos esenciales para AdminReservas */

/* Animaciones necesarias */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

/* Estilos para formateo de fecha si no está disponible via utilidad */
.tiempo-actualizado {
  font-size: 0.875rem;
  color: #64748b;
}

/* Estilos de enfoque personalizados si es necesario */
.focus-ring:focus {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}

/* Transiciones suaves para elementos interactivos */
.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
</style>
