<!--
  AdminReservas.vue - Gestión completa de reservas
  FASE 8.4: Integración con base de datos real
-->
<template>
  <div class="admin-reservas">
    <!-- Notificación de estado de conexión -->
    <div v-if="!modoDemo && reservations.length > 0" class="success-notice">
      ✅ Conectado a la base de datos: Mostrando reservas reales del sistema
    </div>

    <!-- Header con acciones -->
    <div class="admin-header">
      <div>
        <h1 class="admin-title">Gestión de Reservas</h1>
        <p class="admin-subtitle">Panel de administración de reservas</p>
      </div>
      
      <div class="header-actions">
        <button 
          class="btn-secondary"
          @click="loadReservations"
          title="Actualizar datos"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
          </svg>
          Actualizar
        </button>
        <button 
          class="btn-primary"
          @click="openCreateModal"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
          </svg>
          Nueva Reserva
        </button>
      </div>
    </div>

    <!-- Estadísticas rápidas -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-content">
          <div class="stat-number">{{ stats.total || 0 }}</div>
          <div class="stat-label">Total Reservas</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-success">
        <div class="stat-content">
          <div class="stat-number">{{ stats.today || 0 }}</div>
          <div class="stat-label">Hoy</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-info">
        <div class="stat-content">
          <div class="stat-number">{{ stats.pending || 0 }}</div>
          <div class="stat-label">Pendientes</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-info">
        <div class="stat-content">
          <div class="stat-number">{{ stats.confirmed || 0 }}</div>
          <div class="stat-label">Confirmadas</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-purple">
        <div class="stat-content">
          <div class="stat-number">{{ stats.completed || 0 }}</div>
          <div class="stat-label">Completadas</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M5 13l4 4L19 7"/>
          </svg>
        </div>
      </div>
    </div>

    <!-- Tabla de reservas -->
    <AdminTable
      title="Lista de Reservas"
      description="Gestiona todas las reservas del sistema"
      :data="paginatedReservations"
      :columns="tableColumns"
      :loading="loadingReservations"
      :selectable="true"
      :hidePageSize="true"
      searchPlaceholder="Buscar por cliente, barbero o servicio..."
      emptyMessage="No se encontraron reservas"
      @update:selected="selectedReservations = $event"
    >
      <!-- Filtros personalizados -->
      <template #filters>
        <div class="filters-container-compact">
          <div class="filters-row">
            <select v-model="statusFilter" class="filter-select-compact">
              <option value="">Todos los estados</option>
              <option value="pendiente">Pendientes</option>
              <option value="confirmada">Confirmadas</option>
              <option value="completada">Completadas</option>
              <option value="cancelada">Canceladas</option>
            </select>
            
            <select v-model="barberFilter" class="filter-select-compact">
              <option value="">Todos los barberos</option>
              <option v-for="barber in availableBarbers" :key="barber.id" :value="barber.id">
                {{ barber.nombre }}
              </option>
            </select>
            
            <button 
              @click="clearFilters"
              class="filter-clear-btn-compact"
              title="Limpiar filtros"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
              Limpiar
            </button>
          </div>
        </div>
      </template>

      <!-- Celda personalizada para cliente -->
      <template #cell-cliente_nombre="{ item }">
        <div class="reserva-info">
          <div class="reserva-avatar">
            {{ getInitials(item.cliente_nombre || 'Usuario') }}
          </div>
          <div class="reserva-details">
            <div class="reserva-name">{{ item.cliente_nombre || 'Sin nombre' }}</div>
            <div class="reserva-meta">{{ item.cliente_email || 'Sin email' }}</div>
          </div>
        </div>
      </template>

      <!-- Celda personalizada para barbero -->
      <template #cell-barbero_nombre="{ item }">
        <div class="barbero-info">
          <span class="barbero-name">{{ item.barbero_nombre || 'Sin asignar' }}</span>
          <span v-if="item.barbero_especialidad" class="barbero-especialidad">{{ item.barbero_especialidad }}</span>
        </div>
      </template>

      <!-- Celda personalizada para estado -->
      <template #cell-estado="{ item }">
        <span :class="['status-badge', getStatusClass(item.estado)]">
          <div class="status-dot"></div>
          {{ getStatusLabel(item.estado) }}
        </span>
      </template>

      <!-- Celda personalizada para fecha y hora -->
      <template #cell-fecha_reserva="{ item }">
        <div class="fecha-info">
          <div class="fecha-date">{{ formatDate(item.fecha_reserva) }}</div>
          <div class="fecha-time">{{ item.hora_inicio }}</div>
        </div>
      </template>

      <!-- Acciones por fila -->
      <template #actions="{ item }">
        <div class="action-buttons">
          <button
            @click="viewReservation(item)"
            class="action-btn action-view"
            title="Ver detalles"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
            </svg>
          </button>
          
          <button
            v-if="item.estado === 'pendiente'"
            @click="changeReservationStatus(item, 'confirmada')"
            class="action-btn action-confirm"
            title="Confirmar reserva"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
          </button>
          
          <button
            v-if="item.estado === 'confirmada'"
            @click="changeReservationStatus(item, 'completada')"
            class="action-btn action-complete"
            title="Marcar como completada"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
          </button>
        </div>
      </template>

      <!-- Acciones masivas simplificadas -->
      <template #bulk-actions="{ selectedItems }">
        <div class="bulk-actions">
          <button
            class="bulk-btn bulk-confirm"
            @click="bulkConfirm(selectedItems)"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
            Confirmar
          </button>
          
          <button
            class="bulk-btn bulk-complete"
            @click="bulkComplete(selectedItems)"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            Completar
          </button>
        </div>
      </template>
    </AdminTable>

    <!-- Controles de paginación separados -->
    <div class="pagination-container">
      <div class="pagination-info">
        Mostrando {{ startIndex + 1 }}-{{ Math.min(endIndex, filteredReservations.length) }} de {{ filteredReservations.length }} reservas
      </div>
      <div class="pagination-buttons">
        <button 
          @click="previousPage"
          :disabled="currentPage === 1"
          class="pagination-btn"
          :class="{ 'pagination-btn-disabled': currentPage === 1 }"
          title="Página anterior"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
          </svg>
        </button>
        
        <span class="pagination-current">
          Página {{ currentPage }} de {{ totalPages }}
        </span>
        
        <button 
          @click="nextPage"
          :disabled="currentPage === totalPages"
          class="pagination-btn"
          :class="{ 'pagination-btn-disabled': currentPage === totalPages }"
          title="Página siguiente"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- Modal para ver detalles de reserva -->
    <AdminModal
      :show="showDetailsModal"
      title="Detalles de la Reserva"
      description="Información completa de la reserva"
      size="lg"
      :showActions="false"
      @close="closeDetailsModal"
    >
      <div v-if="currentReservation" class="space-y-6">
        <!-- Información del cliente -->
        <div class="bg-gray-50 rounded-lg p-4">
          <h3 class="text-lg font-medium text-gray-900 mb-3">Cliente</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700">Nombre</label>
              <p class="text-sm text-gray-900">{{ currentReservation.cliente_nombre || 'Sin nombre' }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Email</label>
              <p class="text-sm text-gray-900">{{ currentReservation.cliente_email || 'Sin email' }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Teléfono</label>
              <p class="text-sm text-gray-900">{{ currentReservation.cliente_telefono || 'Sin teléfono' }}</p>
            </div>
          </div>
        </div>

        <!-- Información de la reserva -->
        <div class="bg-blue-50 rounded-lg p-4">
          <h3 class="text-lg font-medium text-gray-900 mb-3">Reserva</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700">Fecha</label>
              <p class="text-sm text-gray-900">{{ formatDate(currentReservation.fecha_reserva) }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Hora</label>
              <p class="text-sm text-gray-900">{{ currentReservation.hora_inicio }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Estado</label>
              <span :class="[
                'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium',
                getStatusClass(currentReservation.estado)
              ]">
                {{ getStatusLabel(currentReservation.estado) }}
              </span>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Precio Total</label>
              <p class="text-sm text-gray-900 font-medium">{{ formatPrice(currentReservation.precio_final) }}</p>
            </div>
          </div>
        </div>

        <!-- Información del barbero y servicio -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-green-50 rounded-lg p-4">
            <h3 class="text-lg font-medium text-gray-900 mb-3">Barbero</h3>
            <div class="space-y-2">
              <div>
                <label class="block text-sm font-medium text-gray-700">Nombre</label>
                <p class="text-sm text-gray-900">{{ currentReservation.barbero_nombre || 'Sin asignar' }}</p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Especialidad</label>
                <p class="text-sm text-gray-900">{{ currentReservation.barbero_especialidad || '-' }}</p>
              </div>
            </div>
          </div>

          <div class="bg-purple-50 rounded-lg p-4">
            <h3 class="text-lg font-medium text-gray-900 mb-3">Servicio</h3>
            <div class="space-y-2">
              <div>
                <label class="block text-sm font-medium text-gray-700">Servicio</label>
                <p class="text-sm text-gray-900">{{ currentReservation.servicio_nombre || 'Sin servicio' }}</p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Duración</label>
                <p class="text-sm text-gray-900">{{ currentReservation.servicio_duracion || 30 }} minutos</p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Precio</label>
                <p class="text-sm text-gray-900">{{ formatPrice(currentReservation.servicio_precio) }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Notas -->
        <div v-if="currentReservation.notas" class="bg-yellow-50 rounded-lg p-4">
          <h3 class="text-lg font-medium text-gray-900 mb-3">Notas</h3>
          <p class="text-sm text-gray-700">{{ currentReservation.notas }}</p>
        </div>

        <!-- Historial de cambios -->
        <div v-if="currentReservation.history?.length" class="bg-gray-50 rounded-lg p-4">
          <h3 class="text-lg font-medium text-gray-900 mb-3">Historial de Cambios</h3>
          <div class="space-y-2">
            <div 
              v-for="change in currentReservation.history" 
              :key="change.id"
              class="flex items-center justify-between text-sm"
            >
              <span class="text-gray-700">{{ change.description }}</span>
              <span class="text-gray-500">{{ formatDateTime(change.createdAt) }}</span>
            </div>
          </div>
        </div>
      </div>
    </AdminModal>

    <!-- Modal para crear/editar reserva -->
    <AdminModal
      :show="showReservationModal"
      :title="isEditing ? 'Editar Reserva' : 'Nueva Reserva'"
      :description="isEditing ? 'Modifica los datos de la reserva' : 'Crea una nueva reserva en el sistema'"
      size="lg"
      :loading="savingReservation"
      :saveDisabled="!isReservationFormValid"
      @close="closeReservationModal"
      @save="saveReservation"
    >
      <div class="space-y-6">
        <p class="text-sm text-gray-600">
          Formulario de reserva (implementación básica para pruebas)
        </p>
        <!-- Aquí iría el formulario completo de reserva -->
        <!-- Por ahora solo un placeholder para completar la funcionalidad -->
      </div>
    </AdminModal>

    <!-- Modal de confirmación para cancelar -->
    <AdminModal
      :show="showCancelModal"
      type="confirm"
      confirmType="danger"
      title="Cancelar Reserva"
      confirmMessage="¿Estás seguro de que quieres cancelar esta reserva? Esta acción se puede revertir."
      confirmText="Cancelar Reserva"
      cancelText="Mantener"
      :loading="cancellingReservation"
      @confirm="confirmCancel"
      @cancel="closeCancelModal"
    />
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue'
import AdminCard from '@/components/admin/AdminCard.vue'
import AdminTable from '@/components/admin/AdminTable.vue'
import AdminModal from '@/components/admin/AdminModal.vue'
import AdminButton from '@/components/admin/AdminButton.vue'
import reservationService from '@/services/reservationService'
import { barberService } from '@/services/barberService'
import { serviceService } from '@/services/serviceService'

export default {
  name: 'AdminReservas',
  components: {
    AdminCard,
    AdminTable,
    AdminModal,
    AdminButton
  },
  setup() {
    // Estado reactivo
    const loadingStats = ref(true)
    const loadingReservations = ref(true)
    const savingReservation = ref(false)
    const cancellingReservation = ref(false)
    
    const reservations = ref([])
    const selectedReservations = ref([])
    const stats = ref({})
    const availableBarbers = ref([])
    const availableServices = ref([])
    const modoDemo = ref(false) // Indicador de modo demo
    
    // Filtros
    const statusFilter = ref('')
    const barberFilter = ref('')
    const serviceFilter = ref('')
    const dateFromFilter = ref('')
    const dateToFilter = ref('')
    const showAdvancedFilters = ref(false)
    
    // Paginación
    const currentPage = ref(1)
    const itemsPerPage = ref(25)
    
    // Modales
    const showDetailsModal = ref(false)
    const showReservationModal = ref(false)
    const showCancelModal = ref(false)
    const isEditing = ref(false)
    const currentReservation = ref(null)
    
    // Configuración de tabla con campos reales de la BD
    const tableColumns = [
      {
        key: 'cliente_nombre',
        label: 'Cliente',
        sortable: true,
        width: '200px'
      },
      {
        key: 'barbero_nombre', 
        label: 'Barbero',
        sortable: true,
        width: '150px'
      },
      {
        key: 'servicio_nombre',
        label: 'Servicio',
        sortable: true,
        width: '180px'
      },
      {
        key: 'fecha_reserva',
        label: 'Fecha y Hora',
        sortable: true,
        width: '160px'
      },
      {
        key: 'estado',
        label: 'Estado',
        sortable: true,
        width: '120px'
      },
      {
        key: 'precio_final',
        label: 'Precio',
        sortable: true,
        width: '100px'
      },
      {
        key: 'acciones',
        label: 'Acciones',
        sortable: false,
        width: '120px'
      }
    ]
    
    // Computed
    const filteredReservations = computed(() => {
      // Verificar que reservations.value sea un array
      if (!Array.isArray(reservations.value)) {
        console.warn('reservations.value no es un array:', reservations.value)
        return []
      }

      let filtered = [...reservations.value]
      
      if (statusFilter.value) {
        filtered = filtered.filter(reservation => reservation.estado === statusFilter.value)
      }
      
      if (barberFilter.value) {
        filtered = filtered.filter(reservation => reservation.barber_id === parseInt(barberFilter.value))
      }
      
      if (serviceFilter.value) {
        filtered = filtered.filter(reservation => reservation.service_id === parseInt(serviceFilter.value))
      }
      
      if (dateFromFilter.value) {
        filtered = filtered.filter(reservation => reservation.fecha_reserva >= dateFromFilter.value)
      }
      
      if (dateToFilter.value) {
        filtered = filtered.filter(reservation => reservation.fecha_reserva <= dateToFilter.value)
      }
      
      return filtered
    })
    
    // Paginación computed
    const totalPages = computed(() => {
      return Math.ceil(filteredReservations.value.length / itemsPerPage.value)
    })
    
    const startIndex = computed(() => {
      return (currentPage.value - 1) * itemsPerPage.value
    })
    
    const endIndex = computed(() => {
      return startIndex.value + itemsPerPage.value
    })
    
    const paginatedReservations = computed(() => {
      return filteredReservations.value.slice(startIndex.value, endIndex.value)
    })
    
    const isReservationFormValid = computed(() => {
      // Placeholder para validación del formulario
      return true
    })
    
    // Métodos
    const loadReservations = async () => {
      try {
        loadingReservations.value = true
        const response = await reservationService.getAll()
        console.log('📥 Respuesta del servicio de reservas:', response)
        
        // El servicio devuelve {data: [], total: number, isDemo: boolean}
        if (response && response.data && Array.isArray(response.data)) {
          reservations.value = response.data
          modoDemo.value = response.isDemo || false
        } else {
          console.warn('Estructura de respuesta inesperada:', response)
          reservations.value = []
          modoDemo.value = true
        }
      } catch (error) {
        console.error('Error cargando reservas:', error)
        // Usar datos de fallback del servicio que mapean a los campos reales
        const fallbackResponse = reservationService.getFallbackData()
        reservations.value = fallbackResponse.data || []
        modoDemo.value = true
      } finally {
        loadingReservations.value = false
      }
    }
    
    const loadStats = async () => {
      try {
        loadingStats.value = true
        const response = await reservationService.getStats()
        console.log('📊 Respuesta del servicio de estadísticas:', response)
        
        // El servicio puede devolver las estadísticas directamente o en un objeto
        if (response && typeof response === 'object') {
          stats.value = response.data || response
        } else {
          stats.value = {}
        }
      } catch (error) {
        console.error('Error cargando estadísticas:', error)
        // Usar estadísticas de fallback que reflejan datos reales
        const fallbackStats = reservationService.getFallbackStats()
        stats.value = fallbackStats.data || fallbackStats
      } finally {
        loadingStats.value = false
      }
    }
    
    const loadBarbers = async () => {
      try {
        const data = await barberService.getActive()
        availableBarbers.value = data
      } catch (error) {
        console.error('Error cargando barberos:', error)
        availableBarbers.value = [
          { id: 1, name: 'Carlos Martínez' },
          { id: 2, name: 'Miguel García' },
          { id: 3, name: 'Luis Rodríguez' }
        ]
      }
    }
    
    const loadServices = async () => {
      try {
        const data = await serviceService.getAll()
        availableServices.value = data
      } catch (error) {
        console.error('Error cargando servicios:', error)
        availableServices.value = [
          { id: 1, name: 'Corte Clásico' },
          { id: 2, name: 'Arreglo de Barba' },
          { id: 3, name: 'Corte + Barba' }
        ]
      }
    }
    
    const clearFilters = () => {
      statusFilter.value = ''
      barberFilter.value = ''
      serviceFilter.value = ''
      dateFromFilter.value = ''
      dateToFilter.value = ''
      currentPage.value = 1 // Reset página al limpiar filtros
    }
    
    // Funciones de paginación
    const nextPage = () => {
      if (currentPage.value < totalPages.value) {
        currentPage.value++
      }
    }
    
    const previousPage = () => {
      if (currentPage.value > 1) {
        currentPage.value--
      }
    }
    
    const goToPage = (page) => {
      if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page
      }
    }
    
    const viewReservation = (reservation) => {
      currentReservation.value = reservation
      showDetailsModal.value = true
    }
    
    const closeDetailsModal = () => {
      showDetailsModal.value = false
      currentReservation.value = null
    }
    
    const editReservation = (reservation) => {
      currentReservation.value = reservation
      isEditing.value = true
      showReservationModal.value = true
    }
    
    const openCreateModal = () => {
      currentReservation.value = null
      isEditing.value = false
      showReservationModal.value = true
    }
    
    const closeReservationModal = () => {
      showReservationModal.value = false
      currentReservation.value = null
    }
    
    const saveReservation = async () => {
      try {
        savingReservation.value = true
        // Implementar guardado de reserva
        console.log('Guardando reserva...')
        await loadReservations()
        await loadStats()
        closeReservationModal()
      } catch (error) {
        console.error('Error guardando reserva:', error)
      } finally {
        savingReservation.value = false
      }
    }
    
    const changeReservationStatus = async (reservation, newStatus) => {
      try {
        await reservationService.updateStatus(reservation.id, newStatus)
        await loadReservations()
        await loadStats()
      } catch (error) {
        console.error('Error cambiando estado:', error)
      }
    }
    
    const cancelReservation = (reservation) => {
      currentReservation.value = reservation
      showCancelModal.value = true
    }
    
    const closeCancelModal = () => {
      showCancelModal.value = false
      currentReservation.value = null
    }
    
    const confirmCancel = async () => {
      try {
        cancellingReservation.value = true
        await reservationService.updateStatus(currentReservation.value.id, 'cancelled')
        await loadReservations()
        await loadStats()
        closeCancelModal()
      } catch (error) {
        console.error('Error cancelando reserva:', error)
      } finally {
        cancellingReservation.value = false
      }
    }
    
    const exportReservations = () => {
      console.log('Exportando reservas...')
      // Implementar exportación
    }
    
    // Acciones masivas
    const bulkConfirm = async (selectedItems) => {
      try {
        const promises = selectedItems.map(item => 
          reservationService.updateStatus(item.id, 'confirmed')
        )
        await Promise.all(promises)
        await loadReservations()
        await loadStats()
      } catch (error) {
        console.error('Error confirmando reservas:', error)
      }
    }
    
    const bulkComplete = async (selectedItems) => {
      try {
        const promises = selectedItems.map(item => 
          reservationService.updateStatus(item.id, 'completed')
        )
        await Promise.all(promises)
        await loadReservations()
        await loadStats()
      } catch (error) {
        console.error('Error completando reservas:', error)
      }
    }
    
    const bulkCancel = async (selectedItems) => {
      try {
        const promises = selectedItems.map(item => 
          reservationService.updateStatus(item.id, 'cancelled')
        )
        await Promise.all(promises)
        await loadReservations()
        await loadStats()
      } catch (error) {
        console.error('Error cancelando reservas:', error)
      }
    }
    
    const bulkExport = (selectedItems) => {
      console.log('Exportando reservas seleccionadas:', selectedItems)
      // Implementar exportación de seleccionadas
    }
    
    // Helpers
    const getInitials = (name) => {
      return name.split(' ')
        .map(word => word.charAt(0))
        .join('')
        .toUpperCase()
        .slice(0, 2)
    }
    
    const getStatusClass = (status) => {
      switch (status) {
        case 'pending':
          return 'bg-yellow-100 text-yellow-800'
        case 'confirmed':
          return 'bg-blue-100 text-blue-800'
        case 'in_progress':
          return 'bg-purple-100 text-purple-800'
        case 'completed':
          return 'bg-green-100 text-green-800'
        case 'cancelled':
          return 'bg-red-100 text-red-800'
        default:
          return 'bg-gray-100 text-gray-800'
      }
    }
    
    const getStatusIconColor = (status) => {
      switch (status) {
        case 'pending':
          return 'text-yellow-400'
        case 'confirmed':
          return 'text-blue-400'
        case 'in_progress':
          return 'text-purple-400'
        case 'completed':
          return 'text-green-400'
        case 'cancelled':
          return 'text-red-400'
        default:
          return 'text-gray-400'
      }
    }
    
    const getStatusLabel = (status) => {
      switch (status) {
        case 'pending':
          return 'Pendiente'
        case 'confirmed':
          return 'Confirmada'
        case 'in_progress':
          return 'En progreso'
        case 'completed':
          return 'Completada'
        case 'cancelled':
          return 'Cancelada'
        default:
          return 'Desconocido'
      }
    }
    
    const formatDate = (date) => {
      return new Date(date).toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    }
    
    const formatDateTime = (datetime) => {
      return new Date(datetime).toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    }
    
    const formatPrice = (price) => {
      return new Intl.NumberFormat('es-ES', {
        style: 'currency',
        currency: 'EUR'
      }).format(price || 0)
    }
    
    // Lifecycle
    onMounted(() => {
      loadReservations()
      loadStats()
      loadBarbers()
      loadServices()
    })
    
    // Watchers - Reset página cuando cambien los filtros
    watch([statusFilter, barberFilter, serviceFilter, dateFromFilter, dateToFilter], () => {
      currentPage.value = 1
    })
    
    return {
      // Estado
      loadingStats,
      loadingReservations,
      savingReservation,
      cancellingReservation,
      reservations,
      selectedReservations,
      stats,
      availableBarbers,
      availableServices,
      modoDemo,
      statusFilter,
      barberFilter,
      serviceFilter,
      dateFromFilter,
      dateToFilter,
      showAdvancedFilters,
      showDetailsModal,
      showReservationModal,
      showCancelModal,
      isEditing,
      currentReservation,
      
      // Paginación
      currentPage,
      itemsPerPage,
      totalPages,
      startIndex,
      endIndex,
      
      // Configuración
      tableColumns,
      
      // Computed
      filteredReservations,
      paginatedReservations,
      isReservationFormValid,
      
      // Métodos
      loadReservations,
      loadStats,
      clearFilters,
      nextPage,
      previousPage,
      goToPage,
      viewReservation,
      closeDetailsModal,
      editReservation,
      openCreateModal,
      closeReservationModal,
      saveReservation,
      changeReservationStatus,
      cancelReservation,
      closeCancelModal,
      confirmCancel,
      exportReservations,
      bulkConfirm,
      bulkComplete,
      bulkCancel,
      bulkExport,
      
      // Helpers
      getInitials,
      getStatusClass,
      getStatusIconColor,
      getStatusLabel,
      formatDate,
      formatDateTime,
      formatPrice
    }
  }
}
</script>

<style scoped>
.admin-reservas {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  padding: 1.5rem;
  background-color: #f8fafc;
  min-height: 100vh;
}

/* Notificación de éxito */
.success-notice {
  background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
  border: 1px solid #10b981;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1.5rem;
  color: #065f46;
  font-weight: 500;
  font-size: 0.875rem;
}

/* Header */
.admin-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
}

.admin-title {
  font-size: 1.875rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.admin-subtitle {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0;
}

.header-actions {
  display: flex;
  gap: 0.75rem;
  flex-shrink: 0;
}

/* Botones */
.btn-primary {
  background: #000000;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-primary:hover {
  background: #1f2937;
}

.btn-secondary {
  background: white;
  color: #374151;
  border: 1px solid #d1d5db;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-secondary:hover {
  background: #f9fafb;
  border-color: #9ca3af;
}

/* Estadísticas */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
  border: 1px solid #e5e7eb;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.stat-content {
  flex: 1;
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  line-height: 1;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}

.stat-icon {
  flex-shrink: 0;
  width: 3rem;
  height: 3rem;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f3f4f6;
  color: #6b7280;
}

/* Variantes de color para las estadísticas */
.stat-success .stat-number { color: #059669; }
.stat-success .stat-icon {
  background: #d1fae5;
  color: #059669;
}

.stat-info .stat-number { color: #0284c7; }
.stat-info .stat-icon {
  background: #dbeafe;
  color: #0284c7;
}

.stat-purple .stat-number { color: #7c3aed; }
.stat-purple .stat-icon {
  background: #ede9fe;
  color: #7c3aed;
}

/* Filtros compactos - ultra compacto */
.filters-container-compact {
  background: white;
  border-radius: 8px;
  padding: 0.75rem 1rem;
  margin-bottom: 0.5rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
  border: 1px solid #e5e7eb;
}

.filters-row {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  flex-wrap: nowrap;
  margin: 0;
}

.filter-select-compact {
  min-width: 140px;
  padding: 0.375rem 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  background: white;
  font-size: 0.8125rem;
  color: #374151;
  transition: all 0.15s ease;
  height: 2rem;
}

.filter-select-compact:focus {
  outline: none;
  border-color: #000000;
  box-shadow: 0 0 0 1px #000000;
}

.filter-clear-btn-compact {
  background: #f3f4f6;
  color: #6b7280;
  border: 1px solid #d1d5db;
  padding: 0.375rem 0.625rem;
  border-radius: 6px;
  font-size: 0.8125rem;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 0.375rem;
  font-weight: 500;
  height: 2rem;
  white-space: nowrap;
}

.filter-clear-btn-compact:hover {
  background: #e5e7eb;
  color: #374151;
}

/* Controles de paginación separados */
.pagination-container {
  background: white;
  border-radius: 8px;
  padding: 1rem 1.5rem;
  margin-top: 1.5rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
  border: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.pagination-info {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}

.pagination-buttons {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.pagination-btn {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 6px;
  border: 1px solid #d1d5db;
  background: white;
  color: #374151;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.15s ease;
  font-weight: 500;
}

.pagination-btn:hover:not(.pagination-btn-disabled) {
  background: #f9fafb;
  border-color: #9ca3af;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.pagination-btn-disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-current {
  font-size: 0.875rem;
  color: #374151;
  font-weight: 600;
  padding: 0 1rem;
  white-space: nowrap;
}

/* Información de reserva */
.reserva-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.reserva-avatar {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 8px;
  background: #000000;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
  flex-shrink: 0;
}

.reserva-details {
  min-width: 0;
}

.reserva-name {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.875rem;
}

.reserva-meta {
  color: #6b7280;
  font-size: 0.75rem;
}

/* Información del barbero */
.barbero-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.barbero-name {
  font-weight: 500;
  color: #1f2937;
  font-size: 0.875rem;
}

.barbero-especialidad {
  color: #6b7280;
  font-size: 0.75rem;
}

/* Status badges */
.status-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
  gap: 0.5rem;
}

.status-dot {
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 50%;
}

/* Estados específicos */
.status-badge.pendiente {
  background: #fef3c7;
  color: #92400e;
  border: 1px solid #fbbf24;
}

.status-badge.pendiente .status-dot {
  background: #f59e0b;
}

.status-badge.confirmada {
  background: #dbeafe;
  color: #1e40af;
  border: 1px solid #3b82f6;
}

.status-badge.confirmada .status-dot {
  background: #2563eb;
}

.status-badge.completada {
  background: #d1fae5;
  color: #065f46;
  border: 1px solid #10b981;
}

.status-badge.completada .status-dot {
  background: #059669;
}

.status-badge.cancelada {
  background: #fee2e2;
  color: #991b1b;
  border: 1px solid #ef4444;
}

.status-badge.cancelada .status-dot {
  background: #dc2626;
}

/* Información de fecha */
.fecha-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.fecha-date {
  font-weight: 500;
  color: #1f2937;
  font-size: 0.875rem;
}

.fecha-time {
  color: #6b7280;
  font-size: 0.75rem;
}

/* Acciones */
.action-buttons {
  display: flex;
  gap: 0.5rem;
  justify-content: flex-end;
}

.action-btn {
  padding: 0.375rem 0.75rem;
  font-size: 0.75rem;
  font-weight: 500;
  border-radius: 6px;
  border: 1px solid;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.action-view {
  background: #f8fafc;
  color: #475569;
  border-color: #cbd5e1;
}

.action-view:hover {
  background: #f1f5f9;
  border-color: #94a3b8;
}

.action-confirm {
  background: #ecfdf5;
  color: #065f46;
  border-color: #10b981;
}

.action-confirm:hover {
  background: #d1fae5;
  border-color: #059669;
}

.action-complete {
  background: #dbeafe;
  color: #1e40af;
  border-color: #3b82f6;
}

.action-complete:hover {
  background: #bfdbfe;
  border-color: #2563eb;
}

/* Acciones masivas */
.bulk-actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.bulk-btn {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  font-weight: 500;
  border-radius: 6px;
  border: 1px solid;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.bulk-confirm {
  background: #ecfdf5;
  color: #065f46;
  border-color: #10b981;
}

.bulk-confirm:hover {
  background: #d1fae5;
  border-color: #059669;
}

.bulk-complete {
  background: #dbeafe;
  color: #1e40af;
  border-color: #3b82f6;
}

.bulk-complete:hover {
  background: #bfdbfe;
  border-color: #2563eb;
}

/* Responsividad */
@media (max-width: 768px) {
  .admin-reservas {
    padding: 1rem;
  }
  
  .admin-header {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .header-actions {
    justify-content: flex-end;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .filters-row {
    flex-direction: row;
    gap: 0.5rem;
    align-items: center;
    overflow-x: auto;
    flex-wrap: nowrap;
  }
  
  .filter-select-compact {
    min-width: 120px;
    flex-shrink: 0;
  }
  
  .filter-clear-btn-compact {
    flex-shrink: 0;
  }
  
  .pagination-controls {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .pagination-container {
    flex-direction: column;
    gap: 1rem;
    align-items: center;
    text-align: center;
  }
  
  .pagination-info {
    text-align: center;
  }
  
  .pagination-buttons {
    justify-content: center;
  }
  
  .action-buttons {
    flex-direction: column;
  }
  
  .bulk-actions {
    flex-direction: column;
  }
}

.btn-secondary {
  background: white;
  color: #374151;
  border: 1px solid #d1d5db;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background: #f9fafb;
  border-color: #9ca3af;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Estadísticas grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.2s ease;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.stat-content {
  flex: 1;
}

.stat-title {
  font-size: 0.875rem;
  font-weight: 600;
  color: #6b7280;
  margin: 0 0 0.5rem 0;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.stat-value {
  font-size: 2rem;
  font-weight: 800;
  color: #111827;
  margin: 0 0 0.25rem 0;
  line-height: 1;
}

.stat-description {
  font-size: 0.75rem;
  color: #9ca3af;
  margin: 0;
  font-weight: 500;
}

.stat-icon {
  flex-shrink: 0;
  width: 3rem;
  height: 3rem;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f3f4f6;
  color: #6b7280;
}

/* Variantes de color para las estadísticas */
.stat-success .stat-icon {
  background: #d1fae5;
  color: #065f46;
}

.stat-warning .stat-icon {
  background: #fef3c7;
  color: #92400e;
}

.stat-info .stat-icon {
  background: #dbeafe;
  color: #1e40af;
}

.stat-purple .stat-icon {
  background: #e9d5ff;
  color: #6b21a8;
}

/* Filtros */
.filters-container {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
}

.filters-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
  align-items: end;
}

.filter-select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 0.875rem;
  background: white;
  color: #374151;
  transition: all 0.2s ease;
}

.filter-select:focus {
  outline: none;
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.filter-clear-btn {
  background: #f3f4f6;
  color: #6b7280;
  border: 1px solid #d1d5db;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-clear-btn:hover {
  background: #e5e7eb;
  color: #374151;
}

/* Información de reservas */
.reserva-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.reserva-avatar {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  background: #f3f4f6;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
  color: #6b7280;
}

.reserva-details {
  flex: 1;
}

.reserva-name {
  font-weight: 600;
  color: #111827;
  font-size: 0.875rem;
  margin-bottom: 0.125rem;
}

.reserva-meta {
  font-size: 0.75rem;
  color: #6b7280;
}

/* Información de barbero */
.barbero-info {
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}

.barbero-name {
  font-weight: 600;
  color: #111827;
  font-size: 0.875rem;
}

.barbero-especialidad {
  font-size: 0.75rem;
  color: #6b7280;
  background: #f3f4f6;
  padding: 0.125rem 0.5rem;
  border-radius: 4px;
  display: inline-block;
}

/* Estados */
.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.375rem 0.75rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.status-dot {
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 50%;
}

.status-available {
  background: #d1fae5;
  color: #065f46;
}

.status-available .status-dot {
  background: #10b981;
}

.status-unavailable {
  background: #fee2e2;
  color: #991b1b;
}

.status-unavailable .status-dot {
  background: #ef4444;
}

.status-pending {
  background: #fef3c7;
  color: #92400e;
}

.status-pending .status-dot {
  background: #f59e0b;
}

.status-confirmed {
  background: #dbeafe;
  color: #1e40af;
}

.status-confirmed .status-dot {
  background: #3b82f6;
}

.status-completed {
  background: #d1fae5;
  color: #065f46;
}

.status-completed .status-dot {
  background: #10b981;
}

/* Información de fecha */
.fecha-info {
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}

.fecha-date {
  font-weight: 600;
  color: #111827;
  font-size: 0.875rem;
}

.fecha-time {
  font-size: 0.75rem;
  color: #6b7280;
}

/* Botones de acción */
.action-buttons {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.action-btn {
  width: 2rem;
  height: 2rem;
  border-radius: 6px;
  border: 1px solid #d1d5db;
  background: white;
  color: #6b7280;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-btn:hover {
  background: #f9fafb;
  border-color: #9ca3af;
  transform: translateY(-1px);
}

.action-view:hover {
  background: #dbeafe;
  border-color: #3b82f6;
  color: #1e40af;
}

.action-confirm:hover {
  background: #d1fae5;
  border-color: #10b981;
  color: #065f46;
}

.action-complete:hover {
  background: #e9d5ff;
  border-color: #8b5cf6;
  color: #6b21a8;
}

/* Acciones masivas */
.bulk-actions {
  display: flex;
  gap: 0.75rem;
  padding: 1rem;
  background: #f9fafb;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}

.bulk-btn {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid;
}

.bulk-confirm {
  background: #dbeafe;
  border-color: #3b82f6;
  color: #1e40af;
}

.bulk-confirm:hover {
  background: #bfdbfe;
}

.bulk-complete {
  background: #d1fae5;
  border-color: #10b981;
  color: #065f46;
}

.bulk-complete:hover {
  background: #a7f3d0;
}

/* Notificación de éxito */
.success-notice {
  background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
  border: 1px solid #10b981;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1.5rem;
  color: #065f46;
  font-weight: 500;
  font-size: 0.875rem;
}

/* Responsividad */
@media (max-width: 768px) {
  .admin-reservas {
    padding: 1rem;
  }
  
  .admin-header {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .header-actions {
    justify-content: flex-end;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .filters-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .admin-title {
    font-size: 1.5rem;
  }
  
  .stat-value {
    font-size: 1.5rem;
  }
}
</style>
