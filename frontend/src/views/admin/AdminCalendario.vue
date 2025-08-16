<!--
  AdminCalendario.vue - Gestión de calendario de reservas  
  FASE 8.8: Calendario administrativo con vista de reservas
-->
<template>
  <div class="admin-calendario">
    <!-- Header -->
    <div class="admin-header">
      <div>
        <h1 class="admin-title">
          📅 Calendario de Reservas
        </h1>
        <p class="admin-subtitle">Visualiza y gestiona las reservas en calendario</p>
      </div>
      <AdminButton
        @click="mostrarModalNuevaReserva = true"
        leftIcon="➕"
        variant="primary"
      >
        Nueva Reserva
      </AdminButton>
    </div>

    <!-- Filtros y Controles -->
    <AdminCard class="filters-card">
      <div class="calendar-controls">
        <!-- Vista del calendario -->
        <div class="view-controls">
          <label>Vista:</label>
          <div class="view-buttons">
            <AdminButton
              v-for="view in viewTypes"
              :key="view.value"
              @click="cambiarVista(view.value)"
              :variant="currentView === view.value ? 'primary' : 'outline-secondary'"
              size="sm"
            >
              {{ view.label }}
            </AdminButton>
          </div>
        </div>

        <!-- Filtros -->
        <div class="filters-section">
          <div class="filter-group">
            <label>Barbero:</label>
            <select v-model="filters.barbero" @change="aplicarFiltros" class="filter-select">
              <option value="">Todos los barberos</option>
              <option v-for="barbero in barberos" :key="barbero.id" :value="barbero.id">
                {{ barbero.nombre }}
              </option>
            </select>
          </div>

          <div class="filter-group">
            <label>Estado:</label>
            <select v-model="filters.estado" @change="aplicarFiltros" class="filter-select">
              <option value="">Todos los estados</option>
              <option value="confirmada">Confirmada</option>
              <option value="pendiente">Pendiente</option>
              <option value="cancelada">Cancelada</option>
              <option value="completada">Completada</option>
            </select>
          </div>

          <div class="filter-group">
            <label>Servicio:</label>
            <select v-model="filters.servicio" @change="aplicarFiltros" class="filter-select">
              <option value="">Todos los servicios</option>
              <option v-for="servicio in servicios" :key="servicio.id" :value="servicio.id">
                {{ servicio.nombre }}
              </option>
            </select>
          </div>

          <AdminButton
            @click="limpiarFiltros"
            variant="outline-secondary"
            leftIcon="❌"
            size="sm"
          >
            Limpiar
          </AdminButton>
        </div>
      </div>
    </AdminCard>

    <!-- Estadísticas rápidas -->
    <div class="stats-grid">
      <AdminCard 
        title="Hoy" 
        :value="stats.hoy" 
        icon="📅"
        color="blue"
      />
      <AdminCard 
        title="Esta Semana" 
        :value="stats.semana" 
        icon="📊"
        color="green"
      />
      <AdminCard 
        title="Pendientes" 
        :value="stats.pendientes" 
        icon="⏳"
        color="orange"
      />
      <AdminCard 
        title="Canceladas" 
        :value="stats.canceladas" 
        icon="❌"
        color="red"
      />
    </div>

    <!-- Calendario -->
    <AdminCard class="calendar-container">
      <div id="calendar" ref="calendarEl" class="calendar-wrapper"></div>
    </AdminCard>

    <!-- Modal Detalles de Reserva -->
    <AdminModal
      :show="mostrarModalDetalles"
      title="Detalles de la Reserva"
      @close="mostrarModalDetalles = false"
    >
      <div v-if="reservaSeleccionada" class="reservation-details">
        <div class="detail-section">
          <h3>👤 Información del Cliente</h3>
          <div class="detail-info">
            <p><strong>Nombre:</strong> {{ reservaSeleccionada.cliente?.nombre }}</p>
            <p><strong>Teléfono:</strong> {{ reservaSeleccionada.cliente?.telefono }}</p>
            <p><strong>Email:</strong> {{ reservaSeleccionada.cliente?.email }}</p>
          </div>
        </div>

        <div class="detail-section">
          <h3>✂️ Detalles del Servicio</h3>
          <div class="detail-info">
            <p><strong>Servicio:</strong> {{ reservaSeleccionada.servicio?.nombre }}</p>
            <p><strong>Barbero:</strong> {{ reservaSeleccionada.barbero?.nombre }}</p>
            <p><strong>Fecha:</strong> {{ formatearFecha(reservaSeleccionada.fecha) }}</p>
            <p><strong>Hora:</strong> {{ reservaSeleccionada.hora }}</p>
            <p><strong>Duración:</strong> {{ reservaSeleccionada.servicio?.duracion }} min</p>
            <p><strong>Precio:</strong> {{ formatPrice(reservaSeleccionada.servicio?.precio) }}</p>
          </div>
        </div>

        <div class="detail-section">
          <h3>📋 Estado de la Reserva</h3>
          <div class="detail-info">
            <p><strong>Estado:</strong> 
              <span class="status-badge" :class="reservaSeleccionada.estado">
                {{ getEstadoTexto(reservaSeleccionada.estado) }}
              </span>
            </p>
            <p v-if="reservaSeleccionada.notas"><strong>Notas:</strong> {{ reservaSeleccionada.notas }}</p>
          </div>
        </div>

        <div class="modal-actions">
          <AdminButton
            @click="editarReserva"
            variant="outline-secondary"
            leftIcon="✏️"
          >
            Editar
          </AdminButton>
          <AdminButton
            v-if="reservaSeleccionada.estado === 'pendiente'"
            @click="confirmarReserva"
            variant="success"
            leftIcon="✅"
          >
            Confirmar
          </AdminButton>
          <AdminButton
            v-if="['pendiente', 'confirmada'].includes(reservaSeleccionada.estado)"
            @click="cancelarReserva"
            variant="danger"
            leftIcon="❌"
          >
            Cancelar
          </AdminButton>
        </div>
      </div>
    </AdminModal>

    <!-- Modal Nueva Reserva -->
    <AdminModal
      :show="mostrarModalNuevaReserva"
      title="Nueva Reserva"
      size="lg"
      @close="mostrarModalNuevaReserva = false"
    >
      <div class="nueva-reserva">
        <p>🚧 Funcionalidad en desarrollo</p>
        <p>Esta función redirigirá al formulario de reservas del sistema principal.</p>
        
        <div class="modal-actions">
          <AdminButton
            @click="mostrarModalNuevaReserva = false"
            variant="outline-secondary"
          >
            Cerrar
          </AdminButton>
          <AdminButton
            @click="irAReservas"
            variant="primary"
            leftIcon="🔗"
          >
            Ir a Reservas
          </AdminButton>
        </div>
      </div>
    </AdminModal>
  </div>
</template>

<script>
import { ref, reactive, onMounted, nextTick } from 'vue'
import AdminCard from '@/components/admin/AdminCard.vue'
import AdminModal from '@/components/admin/AdminModal.vue'
import AdminButton from '@/components/admin/AdminButton.vue'
import { Calendar } from '@fullcalendar/core'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import listPlugin from '@fullcalendar/list'
import interactionPlugin from '@fullcalendar/interaction'
import esLocale from '@fullcalendar/core/locales/es'

export default {
  name: 'AdminCalendario',
  components: {
    AdminCard,
    AdminModal,
    AdminButton
  },
  setup() {
    // Estado reactivo
    const calendarEl = ref(null)
    const calendar = ref(null)
    const loading = ref(false)
    const currentView = ref('dayGridMonth')
    
    // Modales
    const mostrarModalDetalles = ref(false)
    const mostrarModalNuevaReserva = ref(false)
    
    // Datos
    const reservas = ref([])
    const barberos = ref([])
    const servicios = ref([])
    const reservaSeleccionada = ref(null)
    
    // Filtros
    const filters = reactive({
      barbero: '',
      estado: '',
      servicio: ''
    })
    
    // Estadísticas
    const stats = ref({
      hoy: 0,
      semana: 0,
      pendientes: 0,
      canceladas: 0
    })
    
    // Configuración de vistas
    const viewTypes = [
      { value: 'dayGridMonth', label: 'Mes' },
      { value: 'timeGridWeek', label: 'Semana' },
      { value: 'timeGridDay', label: 'Día' },
      { value: 'listWeek', label: 'Lista' }
    ]
    
    // Métodos
    const inicializarCalendario = () => {
      if (!calendarEl.value) return
      
      calendar.value = new Calendar(calendarEl.value, {
        plugins: [dayGridPlugin, timeGridPlugin, listPlugin, interactionPlugin],
        initialView: currentView.value,
        locale: esLocale,
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
        },
        events: reservas.value,
        eventClick: (info) => {
          const reserva = reservas.value.find(r => r.id === info.event.id)
          if (reserva) {
            reservaSeleccionada.value = reserva
            mostrarModalDetalles.value = true
          }
        },
        dateClick: (info) => {
          console.log('Fecha seleccionada:', info.dateStr)
        },
        height: 'auto',
        aspectRatio: 1.35,
        slotMinTime: '08:00:00',
        slotMaxTime: '20:00:00',
        businessHours: {
          daysOfWeek: [1, 2, 3, 4, 5, 6],
          startTime: '09:00',
          endTime: '19:00'
        },
        eventClassNames: (arg) => {
          return [`event-${arg.event.extendedProps.estado}`]
        }
      })
      
      calendar.value.render()
    }
    
    const cargarDatos = async () => {
      try {
        loading.value = true
        
        // Datos de ejemplo para demostración
        reservas.value = [
          {
            id: '1',
            title: 'Corte Clásico - Juan Pérez',
            start: '2025-08-02T10:00:00',
            end: '2025-08-02T10:30:00',
            backgroundColor: '#3b82f6',
            borderColor: '#2563eb',
            estado: 'confirmada',
            cliente: {
              nombre: 'Juan Pérez',
              telefono: '+57 300 123 4567',
              email: 'juan@email.com'
            },
            barbero: {
              id: '1',
              nombre: 'Carlos Martínez'
            },
            servicio: {
              id: '1',
              nombre: 'Corte Clásico',
              duracion: 30,
              precio: 15000
            },
            fecha: '2025-08-02',
            hora: '10:00',
            notas: 'Cliente regular'
          },
          {
            id: '2',
            title: 'Barba + Bigote - Pedro López',
            start: '2025-08-02T14:00:00',
            end: '2025-08-02T14:45:00',
            backgroundColor: '#f59e0b',
            borderColor: '#d97706',
            estado: 'pendiente',
            cliente: {
              nombre: 'Pedro López',
              telefono: '+57 310 987 6543',
              email: 'pedro@email.com'
            },
            barbero: {
              id: '2',
              nombre: 'Miguel Rodríguez'
            },
            servicio: {
              id: '2',
              nombre: 'Barba + Bigote',
              duracion: 45,
              precio: 20000
            },
            fecha: '2025-08-02',
            hora: '14:00'
          }
        ]
        
        barberos.value = [
          { id: '1', nombre: 'Carlos Martínez' },
          { id: '2', nombre: 'Miguel Rodríguez' },
          { id: '3', nombre: 'Ana García' }
        ]
        
        servicios.value = [
          { id: '1', nombre: 'Corte Clásico' },
          { id: '2', nombre: 'Barba + Bigote' },
          { id: '3', nombre: 'Corte Moderno' }
        ]
        
        calcularEstadisticas()
        
      } catch (error) {
        console.error('Error al cargar datos:', error)
      } finally {
        loading.value = false
      }
    }
    
    const calcularEstadisticas = () => {
      const hoy = new Date().toISOString().split('T')[0]
      const inicioSemana = new Date()
      inicioSemana.setDate(inicioSemana.getDate() - inicioSemana.getDay())
      
      stats.value = {
        hoy: reservas.value.filter(r => r.fecha === hoy).length,
        semana: reservas.value.filter(r => {
          const fechaReserva = new Date(r.fecha)
          return fechaReserva >= inicioSemana
        }).length,
        pendientes: reservas.value.filter(r => r.estado === 'pendiente').length,
        canceladas: reservas.value.filter(r => r.estado === 'cancelada').length
      }
    }
    
    const cambiarVista = (vista) => {
      currentView.value = vista
      if (calendar.value) {
        calendar.value.changeView(vista)
      }
    }
    
    const aplicarFiltros = () => {
      let reservasFiltradas = [...reservas.value]
      
      if (filters.barbero) {
        reservasFiltradas = reservasFiltradas.filter(r => r.barbero.id === filters.barbero)
      }
      
      if (filters.estado) {
        reservasFiltradas = reservasFiltradas.filter(r => r.estado === filters.estado)
      }
      
      if (filters.servicio) {
        reservasFiltradas = reservasFiltradas.filter(r => r.servicio.id === filters.servicio)
      }
      
      if (calendar.value) {
        calendar.value.removeAllEvents()
        calendar.value.addEventSource(reservasFiltradas)
      }
    }
    
    const limpiarFiltros = () => {
      Object.keys(filters).forEach(key => {
        filters[key] = ''
      })
      aplicarFiltros()
    }
    
    const formatearFecha = (fecha) => {
      return new Date(fecha).toLocaleDateString('es-ES', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }
    
    const formatPrice = (price) => {
      return new Intl.NumberFormat('es-CO', {
        style: 'currency',
        currency: 'COP',
        minimumFractionDigits: 0
      }).format(price)
    }
    
    const getEstadoTexto = (estado) => {
      const estados = {
        'confirmada': 'Confirmada',
        'pendiente': 'Pendiente',
        'cancelada': 'Cancelada',
        'completada': 'Completada'
      }
      return estados[estado] || estado
    }
    
    const editarReserva = () => {
      console.log('Editar reserva:', reservaSeleccionada.value)
      mostrarModalDetalles.value = false
    }
    
    const confirmarReserva = () => {
      if (reservaSeleccionada.value) {
        reservaSeleccionada.value.estado = 'confirmada'
        mostrarModalDetalles.value = false
        aplicarFiltros()
      }
    }
    
    const cancelarReserva = () => {
      if (reservaSeleccionada.value) {
        reservaSeleccionada.value.estado = 'cancelada'
        mostrarModalDetalles.value = false
        aplicarFiltros()
      }
    }
    
    const irAReservas = () => {
      mostrarModalNuevaReserva.value = false
      // Aquí se redirigiría al componente de reservas
      console.log('Redirigir a reservas')
    }
    
    // Lifecycle
    onMounted(async () => {
      await cargarDatos()
      await nextTick()
      inicializarCalendario()
    })
    
    return {
      // Referencias
      calendarEl,
      
      // Estado
      loading,
      currentView,
      
      // Modales
      mostrarModalDetalles,
      mostrarModalNuevaReserva,
      
      // Datos
      reservas,
      barberos,
      servicios,
      reservaSeleccionada,
      filters,
      stats,
      viewTypes,
      
      // Métodos
      cambiarVista,
      aplicarFiltros,
      limpiarFiltros,
      formatearFecha,
      formatPrice,
      getEstadoTexto,
      editarReserva,
      confirmarReserva,
      cancelarReserva,
      irAReservas
    }
  }
}
</script>

<style scoped>
/* Componente principal */
.admin-calendario {
  padding: 1.5rem;
  max-width: 1400px;
  margin: 0 auto;
}

/* Header */
.admin-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  gap: 1rem;
}

.admin-title {
  font-size: 2rem;
  font-weight: 700;
  color: var(--color-text-primary);
  margin: 0 0 0.5rem 0;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.admin-subtitle {
  color: var(--color-text-secondary);
  margin: 0;
  font-size: 1rem;
}

/* Controles del calendario */
.filters-card {
  margin-bottom: 1.5rem;
}

.calendar-controls {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.view-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.view-controls label {
  font-weight: 600;
  color: var(--color-text-primary);
  min-width: 60px;
}

.view-buttons {
  display: flex;
  gap: 0.5rem;
}

.filters-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  align-items: end;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.filter-group label {
  font-weight: 600;
  color: var(--color-text-primary);
  font-size: 0.875rem;
}

.filter-select {
  padding: 0.5rem;
  border: 2px solid var(--color-border);
  border-radius: 8px;
  font-size: 0.875rem;
  transition: all 0.2s ease;
}

.filter-select:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px var(--color-primary-alpha);
}

/* Estadísticas */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

/* Calendario */
.calendar-container {
  margin-bottom: 2rem;
}

.calendar-wrapper {
  min-height: 600px;
}

/* Estilos para FullCalendar */
:deep(.fc) {
  font-family: inherit;
}

:deep(.fc-toolbar) {
  margin-bottom: 1rem;
  flex-wrap: wrap;
  gap: 1rem;
}

:deep(.fc-toolbar-title) {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--color-text-primary);
}

:deep(.fc-button) {
  background: var(--color-primary);
  border: 2px solid var(--color-primary);
  color: white;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  transition: all 0.2s ease;
}

:deep(.fc-button:hover) {
  background: var(--color-primary-dark);
  border-color: var(--color-primary-dark);
}

:deep(.fc-button:focus) {
  box-shadow: 0 0 0 3px var(--color-primary-alpha);
}

:deep(.fc-button-active) {
  background: var(--color-primary-dark);
  border-color: var(--color-primary-dark);
}

:deep(.fc-event) {
  cursor: pointer;
  border-radius: 6px;
  border: none;
  font-weight: 500;
  transition: all 0.2s ease;
}

:deep(.fc-event:hover) {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

:deep(.fc-day-today) {
  background: var(--color-primary-light) !important;
}

:deep(.fc-daygrid-event) {
  font-size: 0.75rem;
  padding: 2px 4px;
}

:deep(.fc-timegrid-event) {
  font-size: 0.8rem;
  padding: 4px 6px;
}

:deep(.fc-list-event-title) {
  font-weight: 600;
}

:deep(.fc-list-event-time) {
  color: var(--color-text-secondary);
}

:deep(.fc-more-link) {
  color: var(--color-primary);
  font-weight: 600;
  text-decoration: none;
}

:deep(.fc-more-link:hover) {
  color: var(--color-primary-dark);
}

/* Estados de eventos */
:deep(.event-confirmada) {
  background: #10b981 !important;
  border-color: #059669 !important;
}

:deep(.event-pendiente) {
  background: #f59e0b !important;
  border-color: #d97706 !important;
}

:deep(.event-cancelada) {
  background: #ef4444 !important;
  border-color: #dc2626 !important;
}

:deep(.event-completada) {
  background: #6366f1 !important;
  border-color: #4f46e5 !important;
}

/* Modal de detalles */
.reservation-details {
  padding: 1rem;
}

.detail-section {
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid var(--color-border);
}

.detail-section:last-child {
  border-bottom: none;
  margin-bottom: 0;
}

.detail-section h3 {
  margin: 0 0 1rem 0;
  color: var(--color-text-primary);
  font-size: 1.125rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.detail-info p {
  margin: 0.5rem 0;
  color: var(--color-text-primary);
}

.detail-info strong {
  color: var(--color-text-primary);
  font-weight: 600;
}

/* Badge de estado */
.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

.status-badge.confirmada {
  background: #d1fae5;
  color: #065f46;
}

.status-badge.pendiente {
  background: #fef3c7;
  color: #92400e;
}

.status-badge.cancelada {
  background: #fee2e2;
  color: #991b1b;
}

.status-badge.completada {
  background: #e0e7ff;
  color: #3730a3;
}

/* Acciones de modal */
.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 2px solid var(--color-border);
}

/* Modal nueva reserva */
.nueva-reserva {
  text-align: center;
  padding: 2rem;
}

.nueva-reserva p {
  margin: 1rem 0;
  color: var(--color-text-secondary);
}

/* Responsive */
@media (max-width: 768px) {
  .admin-header {
    flex-direction: column;
    align-items: stretch;
  }

  .calendar-controls {
    gap: 1rem;
  }

  .view-controls {
    flex-direction: column;
    align-items: stretch;
    gap: 0.5rem;
  }

  .view-buttons {
    justify-content: center;
  }

  .filters-section {
    grid-template-columns: 1fr;
  }

  .stats-grid {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  }

  .modal-actions {
    flex-direction: column-reverse;
  }

  :deep(.fc-toolbar) {
    flex-direction: column;
    align-items: center;
  }

  :deep(.fc-toolbar-chunk) {
    display: flex;
    justify-content: center;
    margin: 0.25rem 0;
  }
}

@media (max-width: 480px) {
  .admin-calendario {
    padding: 1rem;
  }

  .admin-title {
    font-size: 1.5rem;
  }

  .stats-grid {
    grid-template-columns: 1fr 1fr;
  }
}
</style>
