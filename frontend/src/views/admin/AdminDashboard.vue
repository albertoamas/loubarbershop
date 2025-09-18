<!--
  AdminDashboard.vue - Dashboard principal del panel administrativo
  Incluye estadísticas clave, gráficos y overview del negocio en tiempo real
-->
<template>
  <div class="p-8 bg-gradient-to-br from-gray-50 to-gray-100 min-h-screen font-inter">
    <!-- Header del dashboard modernizado -->
    <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-200 mb-6">
      <div class="flex flex-col lg:flex-row lg:justify-between lg:items-start gap-6">
        <div class="flex-1">
          <h1 class="text-3xl font-extrabold bg-gradient-to-r from-black to-gray-500 bg-clip-text text-transparent mb-2">
            Dashboard Administrativo
          </h1>
          <p class="text-lg text-gray-600 font-medium">Panel de control general de Low Barber Shop</p>
        </div>
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
          <button 
            @click="refreshDashboard" 
            :disabled="isRefreshing"
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-black to-gray-500 text-white border-none rounded-xl font-semibold text-sm cursor-pointer transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5 disabled:opacity-70 disabled:cursor-not-allowed disabled:transform-none"
          >
            <svg :class="{ 'animate-spin': isRefreshing }" class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            {{ isRefreshing ? 'Actualizando...' : 'Actualizar' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Grid de estadísticas principales modernizado -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <!-- Reservas del mes -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Reservas</h3>
            <p class="text-3xl font-black text-blue-600">{{ stats.totalReservations || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-blue-100 to-blue-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Clientes registrados -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Clientes</h3>
            <p class="text-3xl font-black text-emerald-600">{{ stats.totalClients || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-emerald-100 to-emerald-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Barberos activos -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Barberos</h3>
            <p class="text-3xl font-black text-amber-600">{{ stats.activeBarbersCount || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-amber-100 to-amber-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1.5a1.5 1.5 0 001.5-1.5V7a1.5 1.5 0 00-1.5-1.5H9m4.5 5H16a1 1 0 011 1v4a1 1 0 01-1 1h-2.5m-6 0H5a1 1 0 01-1-1v-4a1 1 0 011-1h2.5m0 0V9a1 1 0 011-1h1V7a1 1 0 011-1H12a1 1 0 011 1v1h1a1 1 0 011 1v1" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Ingresos del mes -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Ingresos</h3>
            <p class="text-3xl font-black text-purple-600">${{ formatPrice(stats.monthlyRevenue || 0) }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-purple-100 to-purple-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Grid de gráficos modernizado -->
    <div class="grid grid-cols-1 xl:grid-cols-2 gap-8 mb-8">
      <!-- Gráfico de reservas por mes -->
      <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
        <div class="p-6 border-b border-gray-100 bg-gray-50">
          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
            <div class="flex-1">
              <h3 class="text-xl font-bold text-slate-800 mb-1">Tendencia de Reservas</h3>
              <p class="text-sm text-slate-600">Evolución mensual de reservas</p>
            </div>
            <div class="flex items-center">
              <div class="flex bg-gray-200 rounded-lg p-1">
                <button 
                  v-for="period in timePeriods" 
                  :key="period.value"
                  @click="selectedPeriod = period.value"
                  :class="[
                    'px-4 py-2 text-sm font-medium rounded-md transition-all duration-200',
                    selectedPeriod === period.value 
                      ? 'bg-white text-blue-600 shadow-sm' 
                      : 'text-slate-600 hover:text-slate-800'
                  ]"
                >
                  {{ period.label }}
                </button>
              </div>
            </div>
          </div>
        </div>
        
        <div v-if="loadingCharts" class="flex flex-col items-center justify-center h-96 gap-4">
          <div class="w-8 h-8 border-3 border-gray-200 border-t-blue-600 rounded-full animate-spin"></div>
          <p class="text-slate-600 font-medium">Cargando datos...</p>
        </div>

        <div v-else class="p-6">
          <div class="h-80">
            <canvas ref="reservationsChart"></canvas>
          </div>
        </div>
      </div>

      <!-- Gráfico de servicios populares -->
      <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
        <div class="p-6 border-b border-gray-100 bg-gray-50">
          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
            <div class="flex-1">
              <h3 class="text-xl font-bold text-slate-800 mb-1">Servicios Populares</h3>
              <p class="text-sm text-slate-600">Distribución de servicios más solicitados</p>
            </div>
            <div class="flex items-center">
              <span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-semibold">
                Este mes
              </span>
            </div>
          </div>
        </div>

        <div v-if="loadingCharts" class="flex flex-col items-center justify-center h-96 gap-4">
          <div class="w-8 h-8 border-3 border-gray-200 border-t-blue-600 rounded-full animate-spin"></div>
          <p class="text-slate-600 font-medium">Cargando datos...</p>
        </div>

        <div v-else class="p-6">
          <div class="h-80">
            <canvas ref="servicesChart"></canvas>
          </div>
        </div>
      </div>
    </div>

    <!-- Grid inferior modernizado -->
    <div class="grid grid-cols-1 xl:grid-cols-5 gap-8">
      <!-- Actividad reciente -->
      <div class="xl:col-span-3 bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
        <div class="p-6 border-b border-gray-100 bg-gray-50">
          <div class="flex items-center justify-between">
            <h3 class="text-xl font-bold text-slate-800">Actividad Reciente</h3>
            <button @click="loadRecentActivity" class="p-2 hover:bg-gray-200 rounded-lg transition-colors duration-200">
              <svg class="w-5 h-5 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
            </button>
          </div>
        </div>
        
        <div v-if="loadingActivity" class="p-6">
          <div v-for="n in 5" :key="n" class="flex items-center gap-4 mb-4">
            <div class="w-10 h-10 bg-gray-200 rounded-full animate-pulse"></div>
            <div class="flex-1">
              <div class="h-4 bg-gray-200 rounded animate-pulse mb-2 w-3/4"></div>
              <div class="h-3 bg-gray-200 rounded animate-pulse w-1/2"></div>
            </div>
          </div>
        </div>

        <div v-else-if="recentActivity.length === 0" class="p-12 text-center">
          <div class="w-16 h-16 mx-auto mb-4 text-gray-400">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <h4 class="text-base font-semibold text-slate-700 mb-2">Sin actividad reciente</h4>
          <p class="text-sm text-slate-500">No hay actividad para mostrar en este momento.</p>
        </div>

        <div v-else class="p-6">
          <div
            v-for="activity in recentActivity"
            :key="activity.id"
            class="flex items-center gap-4 p-4 hover:bg-gray-50 rounded-xl transition-colors duration-200 mb-2 last:mb-0"
          >
            <div :class="getActivityIconClass(activity.type)" class="w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                <path v-if="activity.type === 'reservation'" fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd" />
                <path v-else-if="activity.type === 'user'" fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
                <path v-else-if="activity.type === 'payment'" fill-rule="evenodd" d="M4 4a2 2 0 00-2 2v4a2 2 0 002 2V6h10a2 2 0 00-2-2H4zm2 6a2 2 0 012-2h8a2 2 0 012 2v4a2 2 0 01-2 2H8a2 2 0 01-2-2v-4zm6 4a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
                <path v-else fill-rule="evenodd" d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zM3 10a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1v-6zM14 9a1 1 0 00-1 1v6a1 1 0 001 1h2a1 1 0 001-1v-6a1 1 0 00-1-1h-2z" clip-rule="evenodd" />
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-slate-800 truncate">{{ activity.description }}</p>
              <p class="text-xs text-slate-500">{{ formatTime(activity.timestamp) }}</p>
            </div>
            <div v-if="activity.amount" class="text-sm font-bold text-emerald-600">
              ${{ formatPrice(activity.amount) }}
            </div>
          </div>
        </div>
      </div>

      <!-- Estadísticas rápidas modernizadas -->
      <div class="xl:col-span-2 bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
        <div class="p-6 border-b border-gray-100 bg-gray-50">
          <div class="flex items-center justify-between">
            <h3 class="text-xl font-bold text-slate-800">Resumen de Hoy</h3>
            <div class="text-xs text-slate-600 font-medium capitalize">{{ todayFormatted }}</div>
          </div>
        </div>
        
        <div class="p-6 space-y-6">
          <!-- Reservas de hoy -->
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="text-sm font-medium text-slate-700">Reservas de Hoy</div>
              <div class="text-2xl font-black text-slate-800">{{ stats.reservationsToday || 0 }}</div>
            </div>
            <div class="space-y-2">
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div 
                  class="bg-gradient-to-r from-blue-500 to-blue-600 h-2 rounded-full transition-all duration-500"
                  :style="{ width: `${Math.min((stats.reservationsToday / 20) * 100, 100)}%` }"
                ></div>
              </div>
              <span class="text-xs text-slate-500 font-medium">Meta: 20</span>
            </div>
          </div>

          <!-- Satisfacción del cliente -->
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="text-sm font-medium text-slate-700">Satisfacción</div>
              <div class="text-2xl font-black text-slate-800">{{ stats.customerSatisfaction || 0 }}%</div>
            </div>
            <div class="space-y-2">
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div 
                  class="bg-gradient-to-r from-emerald-500 to-emerald-600 h-2 rounded-full transition-all duration-500"
                  :style="{ width: `${stats.customerSatisfaction || 0}%` }"
                ></div>
              </div>
              <span class="text-xs text-slate-500 font-medium">Promedio mensual</span>
            </div>
          </div>

          <!-- Ingresos de hoy -->
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="text-sm font-medium text-slate-700">Ingresos de Hoy</div>
              <div class="text-2xl font-black text-slate-800">${{ formatPrice(stats.dailyRevenue || 0) }}</div>
            </div>
            <div class="space-y-2">
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div 
                  class="bg-gradient-to-r from-amber-500 to-amber-600 h-2 rounded-full transition-all duration-500"
                  :style="{ width: `${Math.min((stats.dailyRevenue / stats.dailyGoal) * 100, 100)}%` }"
                ></div>
              </div>
              <span class="text-xs text-slate-500 font-medium">Meta: ${{ formatPrice(stats.dailyGoal || 0) }}</span>
            </div>
          </div>

          <!-- Estado del equipo -->
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="text-sm font-medium text-slate-700">Barberos Trabajando</div>
              <div class="text-2xl font-black text-slate-800">{{ stats.workingBarbers || 0 }}/{{ stats.activeBarbersCount || 0 }}</div>
            </div>
            <div class="space-y-2">
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div 
                  class="bg-gradient-to-r from-purple-500 to-purple-600 h-2 rounded-full transition-all duration-500"
                  :style="{ width: `${stats.activeBarbersCount ? (stats.workingBarbers / stats.activeBarbersCount) * 100 : 0}%` }"
                ></div>
              </div>
              <span class="text-xs text-slate-500 font-medium">Equipo activo</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed, nextTick } from 'vue'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  Filler
} from 'chart.js'

// Servicios reales
import reservationService from '@/services/reservationService'
import userService from '@/services/userService'
import barberService from '@/services/barberService'
import serviceService from '@/services/serviceService'

// Registrar componentes de Chart.js
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  Filler
)

export default {
  name: 'AdminDashboard',
  setup() {
    // Estados reactivos
    const isRefreshing = ref(false)
    const loadingCharts = ref(true)
    const loadingActivity = ref(true)
    const selectedPeriod = ref('6months')
    
    // Datos principales
    const stats = ref({
      totalReservations: 0,
      reservationsToday: 0,
      reservationsChange: 0,
      totalClients: 0,
      clientsChange: 0,
      newClientsThisMonth: 0,
      activeBarbersCount: 0,
      workingBarbers: 0,
      monthlyRevenue: 0,
      dailyRevenue: 0,
      dailyAverage: 0,
      dailyGoal: 1000,
      revenueChange: 0,
      averageOccupancy: 0,
      customerSatisfaction: 92
    })

    const recentActivity = ref([])
    const chartData = ref({
      reservations: [],
      services: []
    })

    // Referencias para gráficos
    const reservationsChart = ref(null)
    const servicesChart = ref(null)
    let reservationsChartInstance = null
    let servicesChartInstance = null

    // Configuraciones
    const timePeriods = [
      { label: '3M', value: '3months' },
      { label: '6M', value: '6months' },
      { label: '1A', value: '1year' }
    ]

    const todayFormatted = computed(() => {
      return new Date().toLocaleDateString('es-ES', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    })

    // Métodos de utilidad
    const formatPrice = (price) => {
      return new Intl.NumberFormat('es-CO', {
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
      }).format(price || 0)
    }

    const getTrendClass = (change) => {
      if (change > 0) return 'stat-trend-positive'
      if (change < 0) return 'stat-trend-negative'
      return 'stat-trend-neutral'
    }

    const getActivityIconClass = (type) => {
      switch (type) {
        case 'reservation':
          return 'activity-icon-primary'
        case 'user':
          return 'activity-icon-success'
        case 'payment':
          return 'activity-icon-warning'
        default:
          return 'activity-icon-neutral'
      }
    }

    const formatTime = (timestamp) => {
      const now = new Date()
      const time = new Date(timestamp)
      const diffInMinutes = Math.floor((now - time) / (1000 * 60))

      if (diffInMinutes < 1) {
        return 'Ahora mismo'
      } else if (diffInMinutes < 60) {
        return `Hace ${diffInMinutes} minutos`
      } else if (diffInMinutes < 1440) {
        const hours = Math.floor(diffInMinutes / 60)
        return `Hace ${hours} hora${hours !== 1 ? 's' : ''}`
      } else {
        return time.toLocaleDateString('es-ES')
      }
    }

    // Cargar estadísticas principales
    const loadDashboardStats = async () => {
      try {
        console.log('📊 Cargando estadísticas del dashboard...')

        // Cargar datos en paralelo
        const [reservations, users, barberos, servicios] = await Promise.all([
          reservationService.getReservations(),
          userService.getAll(),
          barberService.getAll(),
          serviceService.getAll()
        ])

        // Procesar reservas
        const today = new Date()
        const startOfMonth = new Date(today.getFullYear(), today.getMonth(), 1)
        const startOfToday = new Date(today.getFullYear(), today.getMonth(), today.getDate())

        const reservasDelMes = reservations.filter(r => {
          const reservaDate = new Date(r.fecha_hora)
          return reservaDate >= startOfMonth
        })

        const reservasDeHoy = reservations.filter(r => {
          const reservaDate = new Date(r.fecha_hora)
          return reservaDate >= startOfToday
        })

        const reservasCompletadas = reservations.filter(r => r.estado === 'completada')
        
        // Calcular ingresos
        const ingresosDelMes = reservasDelMes
          .filter(r => r.estado === 'completada')
          .reduce((sum, reserva) => {
            return sum + (reserva.servicios?.reduce((serviceSum, servicio) => {
              return serviceSum + (servicio.precio || 0)
            }, 0) || 0)
          }, 0)

        const ingresosDeHoy = reservasDeHoy
          .filter(r => r.estado === 'completada')
          .reduce((sum, reserva) => {
            return sum + (reserva.servicios?.reduce((serviceSum, servicio) => {
              return serviceSum + (servicio.precio || 0)
            }, 0) || 0)
          }, 0)

        const promedioIngresoDiario = ingresosDelMes / new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate()

        // Calcular clientes únicos
        const clientesUnicos = new Set(reservations.map(r => r.clienteId)).size
        const clientesDelMes = new Set(reservasDelMes.map(r => r.clienteId)).size

        // Barberos activos (que tienen reservas)
        const barberosConReservas = new Set(reservations.map(r => r.barberId)).size
        const barberosTrabajajanadoHoy = new Set(reservasDeHoy.map(r => r.barberId)).size

        // Actualizar estadísticas
        stats.value = {
          totalReservations: reservasDelMes.length,
          reservationsToday: reservasDeHoy.length,
          reservationsChange: Math.random() * 20 - 10, // Simulado por ahora
          totalClients: clientesUnicos,
          clientsChange: Math.random() * 15 - 5, // Simulado por ahora
          newClientsThisMonth: clientesDelMes,
          activeBarbersCount: barberos.data?.length || 0,
          workingBarbers: barberosTrabajajanadoHoy,
          monthlyRevenue: ingresosDelMes,
          dailyRevenue: ingresosDeHoy,
          dailyAverage: promedioIngresoDiario,
          dailyGoal: 1000,
          revenueChange: Math.random() * 25 - 5, // Simulado por ahora
          averageOccupancy: Math.min((reservasCompletadas.length / reservations.length) * 100, 100),
          customerSatisfaction: 92 // Simulado por ahora
        }

        console.log('✅ Estadísticas cargadas:', stats.value)

      } catch (error) {
        console.error('❌ Error cargando estadísticas:', error)
      }
    }

    // Cargar datos para gráficos
    const loadChartData = async () => {
      try {
        console.log('📈 Cargando datos de gráficos...')

        const [reservations, servicios] = await Promise.all([
          reservationService.getReservations(),
          serviceService.getAll()
        ])

        // Datos para gráfico de reservas (últimos 6 meses)
        const monthlyData = []
        const monthLabels = []
        
        for (let i = 5; i >= 0; i--) {
          const date = new Date()
          date.setMonth(date.getMonth() - i)
          const monthStart = new Date(date.getFullYear(), date.getMonth(), 1)
          const monthEnd = new Date(date.getFullYear(), date.getMonth() + 1, 0)
          
          const monthReservations = reservations.filter(r => {
            const reservaDate = new Date(r.fecha_hora)
            return reservaDate >= monthStart && reservaDate <= monthEnd
          })

          monthLabels.push(date.toLocaleDateString('es-ES', { month: 'short' }))
          monthlyData.push(monthReservations.length)
        }

        // Datos para gráfico de servicios
        const serviceCounts = {}
        reservations.forEach(reserva => {
          if (reserva.servicios) {
            reserva.servicios.forEach(servicio => {
              if (serviceCounts[servicio.nombre]) {
                serviceCounts[servicio.nombre]++
              } else {
                serviceCounts[servicio.nombre] = 1
              }
            })
          }
        })

        const sortedServices = Object.entries(serviceCounts)
          .sort(([,a], [,b]) => b - a)
          .slice(0, 5)

        chartData.value = {
          reservations: {
            labels: monthLabels,
            data: monthlyData
          },
          services: {
            labels: sortedServices.map(([name]) => name),
            data: sortedServices.map(([,count]) => count)
          }
        }

        console.log('✅ Datos de gráficos cargados:', chartData.value)

      } catch (error) {
        console.error('❌ Error cargando datos de gráficos:', error)
      }
    }
    // Cargar actividad reciente
    const loadRecentActivity = async () => {
      try {
        console.log('🔄 Cargando actividad reciente...')

        const reservations = await reservationService.getReservations()
        
        // Obtener las últimas 10 reservas y simular actividad
        const recentReservations = reservations
          .sort((a, b) => new Date(b.fecha_hora) - new Date(a.fecha_hora))
          .slice(0, 8)

        const activities = []

        recentReservations.forEach((reserva, index) => {
          const baseTime = new Date()
          baseTime.setMinutes(baseTime.getMinutes() - (index * 15))

          // Actividad de reserva
          activities.push({
            id: `res-${reserva.id}`,
            type: 'reservation',
            description: `Nueva reserva creada - ${reserva.servicios?.[0]?.nombre || 'Servicio'}`,
            timestamp: baseTime,
            amount: reserva.servicios?.reduce((sum, s) => sum + (s.precio || 0), 0)
          })

          // Ocasionalmente agregar actividad de pago
          if (reserva.estado === 'completada' && Math.random() > 0.5) {
            const paymentTime = new Date(baseTime)
            paymentTime.setMinutes(paymentTime.getMinutes() + 5)
            
            activities.push({
              id: `pay-${reserva.id}`,
              type: 'payment',
              description: `Pago procesado - Reserva #${reserva.id}`,
              timestamp: paymentTime,
              amount: reserva.servicios?.reduce((sum, s) => sum + (s.precio || 0), 0)
            })
          }
        })

        // Agregar algunas actividades de usuarios nuevos
        const userActivities = [
          {
            id: 'user-1',
            type: 'user',
            description: 'Nuevo cliente registrado - María García',
            timestamp: new Date(Date.now() - 45 * 60 * 1000)
          },
          {
            id: 'user-2',
            type: 'user',
            description: 'Cliente actualizado - Carlos López',
            timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000)
          }
        ]

        activities.push(...userActivities)

        // Ordenar por timestamp y tomar los más recientes
        recentActivity.value = activities
          .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp))
          .slice(0, 10)

        console.log('✅ Actividad reciente cargada:', recentActivity.value.length, 'elementos')

      } catch (error) {
        console.error('❌ Error cargando actividad reciente:', error)
        recentActivity.value = []
      }
    }

    // Crear gráfico de reservas
    const createReservationsChart = async () => {
      if (!reservationsChart.value || !chartData.value.reservations) return

      try {
        const ctx = reservationsChart.value.getContext('2d')

        if (reservationsChartInstance) {
          reservationsChartInstance.destroy()
        }

        reservationsChartInstance = new Chart(ctx, {
          type: 'line',
          data: {
            labels: chartData.value.reservations.labels,
            datasets: [{
              label: 'Reservas',
              data: chartData.value.reservations.data,
              borderColor: 'rgb(59, 130, 246)',
              backgroundColor: 'rgba(59, 130, 246, 0.1)',
              borderWidth: 3,
              fill: true,
              tension: 0.4,
              pointBackgroundColor: 'rgb(59, 130, 246)',
              pointBorderColor: 'white',
              pointBorderWidth: 2,
              pointRadius: 6,
              pointHoverRadius: 8
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                display: false
              },
              tooltip: {
                backgroundColor: 'rgba(0, 0, 0, 0.8)',
                titleColor: 'white',
                bodyColor: 'white',
                borderColor: 'rgba(59, 130, 246, 0.5)',
                borderWidth: 1,
                cornerRadius: 8,
                callbacks: {
                  label: function(context) {
                    return `Reservas: ${context.parsed.y}`
                  }
                }
              }
            },
            scales: {
              x: {
                display: true,
                grid: {
                  display: false
                },
                ticks: {
                  color: '#6b7280',
                  font: {
                    weight: '500'
                  }
                }
              },
              y: {
                display: true,
                beginAtZero: true,
                grid: {
                  color: 'rgba(0, 0, 0, 0.05)'
                },
                ticks: {
                  color: '#6b7280',
                  font: {
                    weight: '500'
                  }
                }
              }
            },
            interaction: {
              mode: 'nearest',
              axis: 'x',
              intersect: false
            },
            animation: {
              duration: 1000,
              easing: 'easeOutQuart'
            }
          }
        })

      } catch (error) {
        console.error('❌ Error creando gráfico de reservas:', error)
      }
    }

    // Crear gráfico de servicios
    const createServicesChart = async () => {
      if (!servicesChart.value || !chartData.value.services) return

      try {
        const ctx = servicesChart.value.getContext('2d')

        if (servicesChartInstance) {
          servicesChartInstance.destroy()
        }

        servicesChartInstance = new Chart(ctx, {
          type: 'doughnut',
          data: {
            labels: chartData.value.services.labels,
            datasets: [{
              data: chartData.value.services.data,
              backgroundColor: [
                'rgba(59, 130, 246, 0.8)',
                'rgba(16, 185, 129, 0.8)',
                'rgba(245, 158, 11, 0.8)',
                'rgba(139, 92, 246, 0.8)',
                'rgba(239, 68, 68, 0.8)'
              ],
              borderColor: [
                'rgb(59, 130, 246)',
                'rgb(16, 185, 129)',
                'rgb(245, 158, 11)',
                'rgb(139, 92, 246)',
                'rgb(239, 68, 68)'
              ],
              borderWidth: 2,
              hoverOffset: 6
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '60%',
            plugins: {
              legend: {
                position: 'bottom',
                labels: {
                  padding: 20,
                  usePointStyle: true,
                  color: '#374151',
                  font: {
                    weight: '500'
                  }
                }
              },
              tooltip: {
                backgroundColor: 'rgba(0, 0, 0, 0.8)',
                titleColor: 'white',
                bodyColor: 'white',
                borderColor: 'rgba(255, 255, 255, 0.1)',
                borderWidth: 1,
                cornerRadius: 8,
                callbacks: {
                  label: function(context) {
                    const label = context.label || ''
                    const value = context.parsed || 0
                    const total = context.dataset.data.reduce((a, b) => a + b, 0)
                    const percentage = ((value / total) * 100).toFixed(1)
                    return `${label}: ${value} (${percentage}%)`
                  }
                }
              }
            },
            animation: {
              duration: 1000,
              easing: 'easeOutQuart'
            }
          }
        })

      } catch (error) {
        console.error('❌ Error creando gráfico de servicios:', error)
      }
    }

    // Refrescar dashboard completo
    const refreshDashboard = async () => {
      isRefreshing.value = true
      console.log('🔄 Refrescando dashboard completo...')

      try {
        await Promise.all([
          loadDashboardStats(),
          loadChartData(),
          loadRecentActivity()
        ])

        // Recrear gráficos
        await nextTick()
        await Promise.all([
          createReservationsChart(),
          createServicesChart()
        ])

        console.log('✅ Dashboard refrescado correctamente')

      } catch (error) {
        console.error('❌ Error refrescando dashboard:', error)
      } finally {
        isRefreshing.value = false
        loadingCharts.value = false
        loadingActivity.value = false
      }
    }

    // Lifecycle
    onMounted(() => {
      console.log('🚀 AdminDashboard montado - iniciando carga de datos')
      refreshDashboard()
    })

    return {
      // Estados
      isRefreshing,
      loadingCharts,
      loadingActivity,
      selectedPeriod,
      
      // Datos
      stats,
      recentActivity,
      chartData,
      
      // Referencias
      reservationsChart,
      servicesChart,
      
      // Configuraciones
      timePeriods,
      
      // Computed
      todayFormatted,
      
      // Métodos
      refreshDashboard,
      loadRecentActivity,
      formatPrice,
      getTrendClass,
      getActivityIconClass,
      formatTime
    }
  }
}
</script>

<style scoped>
/* Solo estilos necesarios para Chart.js que no se pueden hacer con Tailwind */
.chart-container {
  position: relative;
  height: 300px;
}

/* Estilos para animaciones personalizadas */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-in-up {
  animation: fadeInUp 0.6s ease-out;
}

.animation-delay-100 {
  animation-delay: 100ms;
}

.animation-delay-200 {
  animation-delay: 200ms;
}

.animation-delay-300 {
  animation-delay: 300ms;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
</style>
