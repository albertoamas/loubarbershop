<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-slate-100 to-slate-200 p-4 md:p-8 font-inter">
    <!-- Header modernizado -->
    <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 rounded-3xl shadow-2xl p-8 mb-8 text-white">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
        <div class="flex-1">
          <h1 class="text-3xl md:text-4xl font-black mb-2 bg-gradient-to-r from-white to-slate-300 bg-clip-text text-transparent">
            Calendario de Reservas
          </h1>
          <p class="text-slate-300 text-lg font-medium">Gestiona y visualiza todas las citas programadas</p>
        </div>
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
          <button 
            @click="mostrarModalNuevaReserva = true"
            class="px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl font-bold text-sm hover:from-blue-600 hover:to-blue-700 transition-all duration-200 hover:transform hover:-translate-y-1 shadow-lg hover:shadow-xl"
          >
            <svg class="w-5 h-5 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
            </svg>
            Nueva Reserva
          </button>
          <button 
            @click="cargarDatos" 
            :disabled="loading"
            class="px-6 py-3 bg-white/10 border border-white/20 text-white rounded-xl font-bold text-sm hover:bg-white/20 transition-all duration-200 hover:transform hover:-translate-y-1 backdrop-blur-sm"
            :class="{ 'opacity-50 cursor-not-allowed': loading }"
          >
            <svg class="w-5 h-5 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            {{ loading ? 'Cargando...' : 'Actualizar' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Grid de estadísticas modernizado -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Hoy</h3>
            <p class="text-3xl font-black text-green-600">{{ stats.hoy || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-green-100 to-green-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Esta Semana</h3>
            <p class="text-3xl font-black text-purple-600">{{ stats.semana || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-purple-100 to-purple-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Pendientes</h3>
            <p class="text-3xl font-black text-orange-600">{{ stats.pendientes || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-orange-100 to-orange-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Canceladas</h3>
            <p class="text-3xl font-black text-red-600">{{ stats.canceladas || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-red-100 to-red-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Filtros modernizados -->
    <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-8 mb-8">
      <!-- Selector de vista -->
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6 mb-6">
        <div class="flex items-center gap-4">
          <label class="text-sm font-bold text-slate-700 uppercase tracking-wider">Vista:</label>
          <div class="flex bg-slate-100 rounded-xl p-1 border border-slate-200">
            <button
              v-for="view in viewTypes"
              :key="view.value"
              @click="cambiarVista(view.value)"
              :class="[
                'px-4 py-2 rounded-lg text-sm font-semibold transition-all duration-200',
                currentView === view.value 
                  ? 'bg-gradient-to-r from-slate-800 to-slate-700 text-white shadow-md transform -translate-y-0.5' 
                  : 'text-slate-600 hover:text-slate-800 hover:bg-white/80'
              ]"
            >
              {{ view.label }}
            </button>
          </div>
        </div>
      </div>
      
      <!-- Filtros principales -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="flex flex-col gap-2">
          <label class="text-sm font-bold text-slate-700 uppercase tracking-wider">Barbero:</label>
          <select 
            v-model="filters.barbero" 
            @change="aplicarFiltros" 
            class="w-full px-4 py-3 border-2 border-slate-200 rounded-xl bg-white text-slate-700 font-medium focus:border-black focus:ring-4 focus:ring-black/10 transition-all duration-200 outline-none"
          >
            <option value="">Todos los barberos</option>
            <option 
              v-for="barbero in barberos.filter(b => b.activo)" 
              :key="barbero.id" 
              :value="barbero.id"
            >
              {{ barbero.nombre }}
            </option>
          </select>
        </div>

        <div class="flex flex-col gap-2">
          <label class="text-sm font-bold text-slate-700 uppercase tracking-wider">Estado:</label>
          <select 
            v-model="filters.estado" 
            @change="aplicarFiltros" 
            class="w-full px-4 py-3 border-2 border-slate-200 rounded-xl bg-white text-slate-700 font-medium focus:border-black focus:ring-4 focus:ring-black/10 transition-all duration-200 outline-none"
          >
            <option value="">Todos los estados</option>
            <option value="pendiente">Pendiente</option>
            <option value="confirmada">Confirmada</option>
            <option value="en_proceso">En proceso</option>
            <option value="completada">Completada</option>
            <option value="cancelada">Cancelada</option>
            <option value="no_asistio">No asistió</option>
          </select>
        </div>

        <div class="flex flex-col gap-2">
          <label class="text-sm font-bold text-slate-700 uppercase tracking-wider">Servicio:</label>
          <select 
            v-model="filters.servicio" 
            @change="aplicarFiltros" 
            class="w-full px-4 py-3 border-2 border-slate-200 rounded-xl bg-white text-slate-700 font-medium focus:border-black focus:ring-4 focus:ring-black/10 transition-all duration-200 outline-none"
          >
            <option value="">Todos los servicios</option>
            <option 
              v-for="servicio in servicios.filter(s => s.status === 'active' || s.activo)" 
              :key="servicio.id" 
              :value="servicio.id"
            >
              {{ servicio.name || servicio.nombre }}
            </option>
          </select>
        </div>

        <div class="flex flex-col gap-2">
          <label class="text-sm font-bold text-slate-700 uppercase tracking-wider opacity-0">Acción:</label>
          <button 
            @click="limpiarFiltros" 
            class="w-full px-4 py-3 bg-white border-2 border-slate-200 text-slate-600 rounded-xl font-semibold text-sm hover:bg-slate-50 hover:border-slate-800 hover:text-slate-800 transition-all duration-200 hover:transform hover:-translate-y-0.5"
          >
            Limpiar Filtros
          </button>
        </div>
      </div>
    </div>

    <!-- Contenedor del calendario modernizado -->
    <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
      <div id="calendar" ref="calendarEl" class="p-6"></div>
    </div>

    <!-- Modal de detalles modernizado -->
    <Teleport to="body">
      <div 
        v-if="mostrarModalDetalles" 
        class="fixed inset-0 bg-black/70 backdrop-blur-md flex items-center justify-center z-50 p-4"
        @click="mostrarModalDetalles = false"
      >
        <div 
          class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-hidden transform"
          @click.stop
        >
          <!-- Header del modal -->
          <div class="flex items-center justify-between p-6 border-b border-slate-100 bg-gradient-to-r from-slate-50 to-slate-100">
            <h3 class="text-xl font-bold text-slate-800">Detalles de la Reserva</h3>
            <button 
              @click="mostrarModalDetalles = false"
              class="w-8 h-8 flex items-center justify-center rounded-full text-slate-400 hover:text-slate-600 hover:bg-slate-200 transition-all duration-200"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          <div v-if="reservaSeleccionada" class="p-6 overflow-y-auto max-h-[calc(90vh-180px)]">
            <!-- Estado de la reserva -->
            <div class="mb-6">
              <span 
                :class="[
                  'inline-flex items-center px-3 py-1.5 rounded-full text-sm font-bold uppercase tracking-wider',
                  reservaSeleccionada.estado === 'pendiente' && 'bg-yellow-100 text-yellow-800',
                  reservaSeleccionada.estado === 'confirmada' && 'bg-blue-100 text-blue-800',
                  reservaSeleccionada.estado === 'en_proceso' && 'bg-purple-100 text-purple-800',
                  reservaSeleccionada.estado === 'completada' && 'bg-green-100 text-green-800',
                  reservaSeleccionada.estado === 'cancelada' && 'bg-red-100 text-red-800',
                  reservaSeleccionada.estado === 'no_asistio' && 'bg-gray-100 text-gray-800'
                ]"
              >
                {{ getEstadoTexto(reservaSeleccionada.estado) }}
              </span>
            </div>

            <!-- Información del cliente -->
            <div class="bg-blue-50 rounded-xl p-6 mb-6 border border-blue-100">
              <h4 class="text-lg font-bold text-blue-800 mb-4 flex items-center gap-2">
                <span>👤</span> Información del Cliente
              </h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="text-sm font-bold text-blue-700 uppercase tracking-wider block mb-1">Nombre:</label>
                  <p class="text-blue-800 font-medium">{{ reservaSeleccionada.cliente?.nombre }}</p>
                </div>
                <div>
                  <label class="text-sm font-bold text-blue-700 uppercase tracking-wider block mb-1">Teléfono:</label>
                  <p class="text-blue-800 font-medium">{{ reservaSeleccionada.cliente?.telefono }}</p>
                </div>
                <div class="md:col-span-2">
                  <label class="text-sm font-bold text-blue-700 uppercase tracking-wider block mb-1">Email:</label>
                  <p class="text-blue-800 font-medium">{{ reservaSeleccionada.cliente?.email }}</p>
                </div>
              </div>
            </div>

            <!-- Información del servicio -->
            <div class="bg-emerald-50 rounded-xl p-6 mb-6 border border-emerald-100">
              <h4 class="text-lg font-bold text-emerald-800 mb-4 flex items-center gap-2">
                <span>✂️</span> Detalles del Servicio
              </h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="text-sm font-bold text-emerald-700 uppercase tracking-wider block mb-1">Servicio:</label>
                  <p class="text-emerald-800 font-medium">{{ reservaSeleccionada.servicio?.nombre }}</p>
                </div>
                <div>
                  <label class="text-sm font-bold text-emerald-700 uppercase tracking-wider block mb-1">Barbero:</label>
                  <p class="text-emerald-800 font-medium">{{ reservaSeleccionada.barbero?.nombre }}</p>
                </div>
                <div>
                  <label class="text-sm font-bold text-emerald-700 uppercase tracking-wider block mb-1">Fecha:</label>
                  <p class="text-emerald-800 font-medium">{{ formatearFecha(reservaSeleccionada.fecha) }}</p>
                </div>
                <div>
                  <label class="text-sm font-bold text-emerald-700 uppercase tracking-wider block mb-1">Hora:</label>
                  <p class="text-emerald-800 font-medium">{{ reservaSeleccionada.hora }}</p>
                </div>
                <div>
                  <label class="text-sm font-bold text-emerald-700 uppercase tracking-wider block mb-1">Duración:</label>
                  <p class="text-emerald-800 font-medium">{{ reservaSeleccionada.servicio?.duracion }} min</p>
                </div>
                <div>
                  <label class="text-sm font-bold text-emerald-700 uppercase tracking-wider block mb-1">Precio:</label>
                  <p class="text-emerald-800 font-bold text-lg">{{ formatPrice(reservaSeleccionada.servicio?.precio) }}</p>
                </div>
              </div>
            </div>

            <!-- Notas adicionales -->
            <div v-if="reservaSeleccionada.notas" class="bg-amber-50 rounded-xl p-6 border border-amber-100">
              <h4 class="text-lg font-bold text-amber-800 mb-4 flex items-center gap-2">
                <span>📋</span> Notas Adicionales
              </h4>
              <p class="text-amber-800">{{ reservaSeleccionada.notas }}</p>
            </div>
          </div>

          <div class="flex items-center justify-end gap-3 p-6 border-t border-slate-100 bg-slate-50">
            <button 
              @click="editarReserva" 
              class="px-6 py-2.5 bg-white border border-slate-200 text-slate-600 rounded-xl font-semibold hover:bg-slate-50 hover:border-slate-800 hover:text-slate-800 transition-all duration-200"
            >
              Editar
            </button>
            <button
              v-if="['pendiente'].includes(reservaSeleccionada?.estado)"
              @click="confirmarReserva"
              class="px-6 py-2.5 bg-gradient-to-r from-green-500 to-green-600 text-white rounded-xl font-semibold hover:from-green-600 hover:to-green-700 transition-all duration-200 hover:transform hover:-translate-y-0.5 shadow-lg"
            >
              Confirmar
            </button>
            <button
              v-if="['pendiente', 'confirmada', 'en_proceso'].includes(reservaSeleccionada?.estado)"
              @click="cancelarReserva"
              class="px-6 py-2.5 bg-gradient-to-r from-red-500 to-red-600 text-white rounded-xl font-semibold hover:from-red-600 hover:to-red-700 transition-all duration-200 hover:transform hover:-translate-y-0.5 shadow-lg"
            >
              Cancelar
            </button>
          </div>
        </div>
      </div>
    </Teleport>

    <!-- Modal nueva reserva modernizado -->
    <Teleport to="body">
      <div 
        v-if="mostrarModalNuevaReserva" 
        class="fixed inset-0 bg-black/70 backdrop-blur-md flex items-center justify-center z-50 p-4"
        @click="mostrarModalNuevaReserva = false"
      >
        <div 
          class="bg-white rounded-2xl shadow-2xl max-w-md w-full overflow-hidden transform"
          @click.stop
        >
          <!-- Header -->
          <div class="flex items-center justify-between p-6 border-b border-slate-100 bg-gradient-to-r from-slate-50 to-slate-100">
            <h3 class="text-xl font-bold text-slate-800">Nueva Reserva</h3>
            <button 
              @click="mostrarModalNuevaReserva = false"
              class="w-8 h-8 flex items-center justify-center rounded-full text-slate-400 hover:text-slate-600 hover:bg-slate-200 transition-all duration-200"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          <!-- Contenido -->
          <div class="p-8 text-center">
            <div class="bg-blue-50 rounded-2xl p-8 border border-blue-100">
              <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                </svg>
              </div>
              <h4 class="text-lg font-bold text-blue-800 mb-2">Funcionalidad en desarrollo</h4>
              <p class="text-blue-700">Esta función redirigirá al formulario de reservas del sistema principal.</p>
            </div>
          </div>

          <!-- Footer -->
          <div class="flex items-center justify-end gap-3 p-6 border-t border-slate-100 bg-slate-50">
            <button 
              @click="mostrarModalNuevaReserva = false"
              class="px-6 py-2.5 bg-white border border-slate-200 text-slate-600 rounded-xl font-semibold hover:bg-slate-50 hover:border-slate-800 hover:text-slate-800 transition-all duration-200"
            >
              Cerrar
            </button>
            <button 
              @click="irAReservas"
              class="px-6 py-2.5 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl font-semibold hover:from-blue-600 hover:to-blue-700 transition-all duration-200 hover:transform hover:-translate-y-0.5 shadow-lg"
            >
              Ir a Reservas
            </button>
          </div>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, nextTick, watch } from 'vue'
import { Calendar } from '@fullcalendar/core'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import listPlugin from '@fullcalendar/list'
import interactionPlugin from '@fullcalendar/interaction'
import esLocale from '@fullcalendar/core/locales/es'

// Services imports
import reservationService from '@/services/reservationService'
import barberService from '@/services/barberService'
import serviceService from '@/services/serviceService'

// Reactive state
const loading = ref(false)
const calendarEl = ref(null)
const calendar = ref(null)
const currentView = ref('dayGridMonth')

// Modal states
const mostrarModalDetalles = ref(false)
const mostrarModalNuevaReserva = ref(false)
const reservaSeleccionada = ref(null)

// Data arrays
const reservas = ref([])
const barberos = ref([])
const servicios = ref([])

// Statistics
const stats = reactive({
  hoy: 0,
  semana: 0,
  pendientes: 0,
  canceladas: 0
})

// Filters
const filters = reactive({
  barbero: '',
  estado: '',
  servicio: ''
})

// View types for calendar
const viewTypes = [
  { value: 'dayGridMonth', label: 'Mes' },
  { value: 'timeGridWeek', label: 'Semana' },
  { value: 'timeGridDay', label: 'Día' },
  { value: 'listWeek', label: 'Lista' }
]

// Computed properties functions
const getEstadoTexto = (estado) => {
  const estados = {
    'pendiente': 'Pendiente',
    'confirmada': 'Confirmada',
    'en_proceso': 'En Proceso',
    'completada': 'Completada',
    'cancelada': 'Cancelada',
    'no_asistio': 'No Asistió'
  }
  return estados[estado] || estado
}

const formatPrice = (price) => {
  if (!price) return '$0'
  return new Intl.NumberFormat('es-CO', {
    style: 'currency',
    currency: 'COP',
    minimumFractionDigits: 0
  }).format(price)
}

const formatearFecha = (fecha) => {
  if (!fecha) return ''
  return new Date(fecha).toLocaleDateString('es-ES', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

// Calendar initialization
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
    height: 'auto',
    editable: false,
    selectable: true,
    selectMirror: true,
    dayMaxEvents: true,
    weekends: true,
    events: [],
    eventClick: (info) => {
      const reserva = reservas.value.find(r => r.id == info.event.id)
      if (reserva) {
        reservaSeleccionada.value = reserva
        mostrarModalDetalles.value = true
      }
    },
    dateClick: (info) => {
      // Handle date click if needed
      console.log('Fecha clickeada:', info.dateStr)
    },
    eventDidMount: (info) => {
      // Add custom classes based on event properties
      if (info.event.extendedProps.estado) {
        info.el.classList.add(info.event.extendedProps.estado)
      }
    }
  })

  calendar.value.render()
}

// Data loading functions
const cargarDatos = async () => {
  loading.value = true
  try {
    await Promise.all([
      cargarReservas(),
      cargarBarberos(),
      cargarServicios()
    ])
    actualizarEventosCalendario()
    calcularEstadisticas()
  } catch (error) {
    console.error('Error al cargar datos:', error)
  } finally {
    loading.value = false
  }
}

const cargarReservas = async () => {
  try {
    const response = await reservationService.getAll()
    reservas.value = response.data || response || []
  } catch (error) {
    console.error('Error al cargar reservas:', error)
    reservas.value = []
  }
}

const cargarBarberos = async () => {
  try {
    const response = await barberService.getAll()
    barberos.value = response.data || response || []
  } catch (error) {
    console.error('Error al cargar barberos:', error)
    barberos.value = []
  }
}

const cargarServicios = async () => {
  try {
    const response = await serviceService.getAll()
    servicios.value = response.data || response || []
  } catch (error) {
    console.error('Error al cargar servicios:', error)
    servicios.value = []
  }
}

// Calendar event management
const actualizarEventosCalendario = () => {
  if (!calendar.value) return

  const reservasFiltradas = aplicarFiltrosReservas()
  const eventos = reservasFiltradas.map(reserva => ({
    id: reserva.id,
    title: `${reserva.cliente?.nombre || 'Cliente'} - ${reserva.servicio?.nombre || reserva.servicio?.name || 'Servicio'}`,
    start: `${reserva.fecha}T${reserva.hora}`,
    end: calcularHoraFin(reserva.fecha, reserva.hora, reserva.servicio?.duracion || 30),
    backgroundColor: getColorEstado(reserva.estado).bg,
    borderColor: getColorEstado(reserva.estado).border,
    textColor: getColorEstado(reserva.estado).text,
    extendedProps: {
      estado: reserva.estado,
      reserva: reserva
    }
  }))

  calendar.value.removeAllEvents()
  calendar.value.addEventSource(eventos)
}

const calcularHoraFin = (fecha, horaInicio, duracion) => {
  const inicio = new Date(`${fecha}T${horaInicio}`)
  const fin = new Date(inicio.getTime() + (duracion * 60000))
  return fin.toISOString()
}

const getColorEstado = (estado) => {
  const colores = {
    'pendiente': { bg: '#fef3c7', border: '#f59e0b', text: '#92400e' },
    'confirmada': { bg: '#dbeafe', border: '#3b82f6', text: '#1e40af' },
    'en_proceso': { bg: '#ede9fe', border: '#8b5cf6', text: '#6d28d9' },
    'completada': { bg: '#d1fae5', border: '#10b981', text: '#065f46' },
    'cancelada': { bg: '#fee2e2', border: '#ef4444', text: '#991b1b' },
    'no_asistio': { bg: '#f3f4f6', border: '#6b7280', text: '#374151' }
  }
  return colores[estado] || colores['pendiente']
}

// Filter functions
const aplicarFiltrosReservas = () => {
  let reservasFiltradas = [...reservas.value]

  if (filters.barbero) {
    reservasFiltradas = reservasFiltradas.filter(r => 
      r.barbero?.id == filters.barbero || r.barbero_id == filters.barbero
    )
  }

  if (filters.estado) {
    reservasFiltradas = reservasFiltradas.filter(r => r.estado === filters.estado)
  }

  if (filters.servicio) {
    reservasFiltradas = reservasFiltradas.filter(r => 
      r.servicio?.id == filters.servicio || r.servicio_id == filters.servicio
    )
  }

  return reservasFiltradas
}

const aplicarFiltros = () => {
  actualizarEventosCalendario()
}

const limpiarFiltros = () => {
  filters.barbero = ''
  filters.estado = ''
  filters.servicio = ''
  actualizarEventosCalendario()
}

// Statistics calculation
const calcularEstadisticas = () => {
  const hoy = new Date()
  const inicioSemana = new Date(hoy)
  inicioSemana.setDate(hoy.getDate() - hoy.getDay())
  
  const finSemana = new Date(inicioSemana)
  finSemana.setDate(inicioSemana.getDate() + 6)

  const hoyStr = hoy.toISOString().split('T')[0]

  stats.hoy = reservas.value.filter(r => r.fecha === hoyStr).length
  stats.semana = reservas.value.filter(r => {
    const fechaReserva = new Date(r.fecha)
    return fechaReserva >= inicioSemana && fechaReserva <= finSemana
  }).length
  stats.pendientes = reservas.value.filter(r => r.estado === 'pendiente').length
  stats.canceladas = reservas.value.filter(r => r.estado === 'cancelada').length
}

// Calendar view management
const cambiarVista = (vista) => {
  currentView.value = vista
  if (calendar.value) {
    calendar.value.changeView(vista)
  }
}

// Modal actions
const editarReserva = () => {
  // Implementation for editing reservation
  console.log('Editar reserva:', reservaSeleccionada.value)
  mostrarModalDetalles.value = false
}

const confirmarReserva = async () => {
  if (reservaSeleccionada.value) {
    try {
      await reservationService.updateStatus(
        reservaSeleccionada.value.id, 
        'confirmada'
      )
      
      // Update local state
      reservaSeleccionada.value.estado = 'confirmada'
      
      // Reload calendar data
      await cargarDatos()
      
      mostrarModalDetalles.value = false
    } catch (error) {
      console.error('Error al confirmar reserva:', error)
      alert('Error al confirmar la reserva')
    }
  }
}

const cancelarReserva = async () => {
  if (reservaSeleccionada.value) {
    try {
      await reservationService.updateStatus(
        reservaSeleccionada.value.id, 
        'cancelada'
      )
      
      // Update local state
      reservaSeleccionada.value.estado = 'cancelada'
      
      // Reload calendar data
      await cargarDatos()
      
      mostrarModalDetalles.value = false
    } catch (error) {
      console.error('Error al cancelar reserva:', error)
      alert('Error al cancelar la reserva')
    }
  }
}

const irAReservas = () => {
  mostrarModalNuevaReserva.value = false
  // Here would redirect to reservations component
  console.log('Redirigir a reservas')
}

// Lifecycle
onMounted(async () => {
  await cargarDatos()
  await nextTick()
  inicializarCalendario()
})

// Return all reactive data and methods for template
// (This section would contain all the returns needed for the template)
</script>

<style scoped>
/* Estilos mínimos para FullCalendar */
:deep(.fc) {
  font-family: inherit;
}

:deep(.fc-toolbar) {
  margin-bottom: 1.5rem;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

:deep(.fc-toolbar-title) {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
  text-transform: capitalize;
}

:deep(.fc-button-group .fc-button) {
  background: white !important;
  border: 2px solid #e2e8f0 !important;
  color: #64748b !important;
  padding: 0.5rem 1rem !important;
  border-radius: 0.5rem !important;
  font-weight: 600 !important;
  transition: all 0.2s ease !important;
}

:deep(.fc-button-group .fc-button:hover) {
  background: #f8fafc !important;
  border-color: #1e293b !important;
  color: #1e293b !important;
}

:deep(.fc-button-primary:not(:disabled):active),
:deep(.fc-button-primary:not(:disabled).fc-button-active) {
  background: linear-gradient(to right, #1e293b, #0f172a) !important;
  border-color: #1e293b !important;
  color: white !important;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
}

:deep(.fc-event) {
  border: none !important;
  border-radius: 0.5rem !important;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1) !important;
  transition: all 0.2s ease !important;
  cursor: pointer !important;
}

:deep(.fc-event:hover) {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
}

:deep(.fc-event.pendiente) {
  background: #fef3c7 !important;
  color: #92400e !important;
  border-left: 3px solid #f59e0b !important;
}

:deep(.fc-event.confirmada) {
  background: #dbeafe !important;
  color: #1e40af !important;
  border-left: 3px solid #3b82f6 !important;
}

:deep(.fc-event.en_proceso) {
  background: #ede9fe !important;
  color: #6d28d9 !important;
  border-left: 3px solid #8b5cf6 !important;
}

:deep(.fc-event.completada) {
  background: #d1fae5 !important;
  color: #065f46 !important;
  border-left: 3px solid #10b981 !important;
}

:deep(.fc-event.cancelada) {
  background: #fee2e2 !important;
  color: #991b1b !important;
  border-left: 3px solid #ef4444 !important;
}

:deep(.fc-event.no_asistio) {
  background: #f3f4f6 !important;
  color: #374151 !important;
  border-left: 3px solid #6b7280 !important;
}

:deep(.fc-daygrid-day:hover) {
  background: #f8fafc !important;
}

:deep(.fc-today) {
  background: rgba(248, 250, 252, 0.5) !important;
}

:deep(.fc-col-header-cell) {
  background: #f1f5f9 !important;
  border-color: #e2e8f0 !important;
  font-weight: 700 !important;
  color: #374151 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
  font-size: 0.75rem !important;
}

:deep(.fc-daygrid-day-number) {
  font-weight: 600 !important;
  color: #374151 !important;
}

:deep(.fc-today .fc-daygrid-day-number) {
  background: #1e293b !important;
  color: white !important;
  border-radius: 50% !important;
  width: 2rem !important;
  height: 2rem !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}
</style>
