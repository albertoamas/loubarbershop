<!--
  AdminDashboard.vue - Dashboard principal del panel administrativo
  Incluye estadísticas clave, gráficos y overview del negocio
-->
<template>
  <div class="admin-dashboard">
    <!-- Header del dashboard -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900 mb-2">Dashboard Administrativo</h1>
      <p class="text-gray-600">Resumen general del estado de Low Barber</p>
    </div>

    <!-- Grid de estadísticas principales -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <!-- Total de reservas del mes -->
      <AdminCard
        title="Reservas del Mes"
        :value="stats.reservationsThisMonth"
        icon="calendar"
        :change="stats.reservationsChange"
        color="blue"
        :loading="loadingStats"
      />

      <!-- Total de clientes registrados -->
      <AdminCard
        title="Clientes Registrados"
        :value="stats.totalClients"
        icon="users"
        :change="stats.clientsChange"
        color="green"
        :loading="loadingStats"
      />

      <!-- Total de barberos activos -->
      <AdminCard
        title="Barberos Activos"
        :value="stats.activeBarbersCount"
        icon="scissors"
        :change="stats.barbersChange"
        color="purple"
        :loading="loadingStats"
      />

      <!-- Ingresos del mes -->
      <AdminCard
        title="Ingresos del Mes"
        :value="stats.revenueThisMonth"
        format="currency"
        icon="euro"
        :change="stats.revenueChange"
        color="yellow"
        :loading="loadingStats"
      />
    </div>

    <!-- Grid de gráficos -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
      <!-- Gráfico de reservas por mes -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-medium text-gray-900">Reservas por Mes</h3>
          <div class="flex items-center space-x-2">
            <span class="text-sm text-gray-500">Últimos 6 meses</span>
          </div>
        </div>
        
        <div v-if="loadingCharts" class="flex justify-center items-center h-80">
          <svg class="animate-spin h-8 w-8 text-blue-600" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
        </div>

        <div v-else class="h-80">
          <Line
            :data="reservationsChartData"
            :options="reservationsChartOptions"
            class="max-h-full"
          />
        </div>
      </div>

      <!-- Gráfico de servicios populares -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-medium text-gray-900">Servicios Más Populares</h3>
          <div class="flex items-center space-x-2">
            <span class="text-sm text-gray-500">Este mes</span>
          </div>
        </div>

        <div v-if="loadingCharts" class="flex justify-center items-center h-80">
          <svg class="animate-spin h-8 w-8 text-blue-600" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
        </div>

        <div v-else class="h-80">
          <Doughnut
            :data="servicesChartData"
            :options="servicesChartOptions"
            class="max-h-full"
          />
        </div>
      </div>
    </div>

    <!-- Grid de información adicional -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Actividad reciente -->
      <div class="lg:col-span-2 bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <h3 class="text-lg font-medium text-gray-900 mb-6">Actividad Reciente</h3>
        
        <div v-if="loadingActivity" class="space-y-4">
          <div v-for="n in 5" :key="n" class="animate-pulse">
            <div class="flex items-center space-x-4">
              <div class="w-10 h-10 bg-gray-200 rounded-full"></div>
              <div class="flex-1 space-y-2">
                <div class="h-4 bg-gray-200 rounded w-3/4"></div>
                <div class="h-3 bg-gray-200 rounded w-1/2"></div>
              </div>
            </div>
          </div>
        </div>

        <div v-else-if="recentActivity.length === 0" class="text-center py-8">
          <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <h3 class="mt-2 text-sm font-medium text-gray-900">Sin actividad reciente</h3>
          <p class="mt-1 text-sm text-gray-500">No hay actividad para mostrar en este momento.</p>
        </div>

        <div v-else class="space-y-4">
          <div
            v-for="activity in recentActivity"
            :key="activity.id"
            class="flex items-center space-x-4 p-3 hover:bg-gray-50 rounded-lg transition-colors"
          >
            <div :class="[
              'w-10 h-10 rounded-full flex items-center justify-center',
              getActivityIconClass(activity.type)
            ]">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                <path v-if="activity.type === 'reservation'" fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd" />
                <path v-else-if="activity.type === 'user'" fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
                <path v-else fill-rule="evenodd" d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zM3 10a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1v-6zM14 9a1 1 0 00-1 1v6a1 1 0 001 1h2a1 1 0 001-1v-6a1 1 0 00-1-1h-2z" clip-rule="evenodd" />
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-gray-900 truncate">
                {{ activity.description }}
              </p>
              <p class="text-sm text-gray-500">{{ formatTime(activity.timestamp) }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Estadísticas rápidas -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <h3 class="text-lg font-medium text-gray-900 mb-6">Estadísticas Rápidas</h3>
        
        <div class="space-y-6">
          <!-- Reservas de hoy -->
          <div>
            <div class="flex items-center justify-between">
              <span class="text-sm font-medium text-gray-900">Reservas de Hoy</span>
              <span class="text-2xl font-bold text-blue-600">{{ stats.reservationsToday || 0 }}</span>
            </div>
            <div class="mt-2 bg-gray-200 rounded-full h-2">
              <div 
                class="bg-blue-600 h-2 rounded-full transition-all duration-500"
                :style="{ width: `${Math.min((stats.reservationsToday / 20) * 100, 100)}%` }"
              ></div>
            </div>
          </div>

          <!-- Ocupación promedio -->
          <div>
            <div class="flex items-center justify-between">
              <span class="text-sm font-medium text-gray-900">Ocupación Promedio</span>
              <span class="text-2xl font-bold text-green-600">{{ stats.averageOccupancy || 0 }}%</span>
            </div>
            <div class="mt-2 bg-gray-200 rounded-full h-2">
              <div 
                class="bg-green-600 h-2 rounded-full transition-all duration-500"
                :style="{ width: `${stats.averageOccupancy || 0}%` }"
              ></div>
            </div>
          </div>

          <!-- Satisfacción del cliente -->
          <div>
            <div class="flex items-center justify-between">
              <span class="text-sm font-medium text-gray-900">Satisfacción</span>
              <span class="text-2xl font-bold text-yellow-600">{{ stats.customerSatisfaction || 0 }}%</span>
            </div>
            <div class="mt-2 bg-gray-200 rounded-full h-2">
              <div 
                class="bg-yellow-600 h-2 rounded-full transition-all duration-500"
                :style="{ width: `${stats.customerSatisfaction || 0}%` }"
              ></div>
            </div>
          </div>

          <!-- Nuevos clientes este mes -->
          <div class="pt-4 border-t border-gray-200">
            <div class="text-center">
              <div class="text-2xl font-bold text-purple-600">{{ stats.newClientsThisMonth || 0 }}</div>
              <div class="text-sm text-gray-500">Nuevos clientes este mes</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { Line, Doughnut } from 'vue-chartjs'
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

import AdminCard from '@/components/admin/AdminCard.vue'
import statsService from '@/services/statsService'

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
  components: {
    AdminCard,
    Line,
    Doughnut
  },
  setup() {
    // Estado reactivo
    const loadingStats = ref(true)
    const loadingCharts = ref(true)
    const loadingActivity = ref(true)
    const stats = ref({})
    const chartData = ref({})
    const recentActivity = ref([])

    // Datos para gráfico de reservas
    const reservationsChartData = computed(() => {
      if (!chartData.value.reservationsByMonth) {
        return {
          labels: [],
          datasets: []
        }
      }

      return {
        labels: chartData.value.reservationsByMonth.labels,
        datasets: [
          {
            label: 'Reservas',
            data: chartData.value.reservationsByMonth.data,
            borderColor: 'rgb(59, 130, 246)',
            backgroundColor: 'rgba(59, 130, 246, 0.1)',
            borderWidth: 2,
            fill: true,
            tension: 0.4
          }
        ]
      }
    })

    // Opciones para gráfico de reservas
    const reservationsChartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          mode: 'index',
          intersect: false
        }
      },
      scales: {
        x: {
          display: true,
          grid: {
            display: false
          }
        },
        y: {
          display: true,
          beginAtZero: true,
          grid: {
            color: 'rgba(0, 0, 0, 0.1)'
          }
        }
      },
      interaction: {
        mode: 'nearest',
        axis: 'x',
        intersect: false
      }
    }

    // Datos para gráfico de servicios
    const servicesChartData = computed(() => {
      if (!chartData.value.popularServices) {
        return {
          labels: [],
          datasets: []
        }
      }

      return {
        labels: chartData.value.popularServices.labels,
        datasets: [
          {
            data: chartData.value.popularServices.data,
            backgroundColor: [
              'rgba(59, 130, 246, 0.8)',
              'rgba(16, 185, 129, 0.8)',
              'rgba(245, 158, 11, 0.8)',
              'rgba(139, 92, 246, 0.8)',
              'rgba(239, 68, 68, 0.8)'
            ],
            borderWidth: 0,
            hoverOffset: 4
          }
        ]
      }
    })

    // Opciones para gráfico de servicios
    const servicesChartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            padding: 20,
            usePointStyle: true
          }
        },
        tooltip: {
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
      }
    }

    // Métodos
    const loadDashboardData = async () => {
      try {
        loadingStats.value = true
        loadingCharts.value = true
        loadingActivity.value = true

        // Cargar estadísticas principales (esto ahora incluye chartData)
        const dashboardData = await statsService.getDashboardStats()
        
        // Mapear los datos recibidos
        stats.value = {
          reservationsThisMonth: dashboardData.totalReservations || 125,
          reservationsChange: dashboardData.weeklyGrowth?.reservations || 12.5,
          totalClients: dashboardData.totalClients || 1247,
          clientsChange: dashboardData.weeklyGrowth?.clients || 8.3,
          activeBarbersCount: dashboardData.totalBarbers || 6,
          barbersChange: 0,
          revenueThisMonth: dashboardData.monthlyRevenue || 3450,
          revenueChange: dashboardData.weeklyGrowth?.revenue || 15.2,
          reservationsToday: 8,
          averageOccupancy: 75,
          customerSatisfaction: 92,
          newClientsThisMonth: 34
        }

        // Los datos de gráficos vienen en el dashboardData
        if (dashboardData.chartData) {
          chartData.value = {
            reservationsByMonth: {
              labels: dashboardData.chartData.labels,
              data: dashboardData.chartData.datasets[0].data
            },
            popularServices: {
              labels: dashboardData.servicesChart?.labels || ['Corte Clásico', 'Barba', 'Combo', 'Lavado'],
              data: dashboardData.servicesChart?.datasets[0]?.data || [45, 25, 20, 10]
            }
          }
        }

        // Actividad reciente simulada
        recentActivity.value = [
          {
            id: 1,
            type: 'reservation',
            description: 'Nueva reserva creada por Juan Pérez',
            timestamp: new Date(Date.now() - 15 * 60 * 1000)
          },
          {
            id: 2,
            type: 'user',
            description: 'Nuevo cliente registrado: María García',
            timestamp: new Date(Date.now() - 45 * 60 * 1000)
          },
          {
            id: 3,
            type: 'reservation',
            description: 'Reserva confirmada para Carlos López',
            timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000)
          }
        ]

      } catch (error) {
        console.error('Error cargando datos del dashboard:', error)
      } finally {
        loadingStats.value = false
        loadingCharts.value = false
        loadingActivity.value = false
      }
    }

    const getActivityIconClass = (type) => {
      switch (type) {
        case 'reservation':
          return 'bg-blue-100 text-blue-600'
        case 'user':
          return 'bg-green-100 text-green-600'
        default:
          return 'bg-gray-100 text-gray-600'
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

    // Lifecycle
    onMounted(() => {
      loadDashboardData()
    })

    return {
      loadingStats,
      loadingCharts,
      loadingActivity,
      stats,
      chartData,
      recentActivity,
      reservationsChartData,
      reservationsChartOptions,
      servicesChartData,
      servicesChartOptions,
      loadDashboardData,
      getActivityIconClass,
      formatTime
    }
  }
}
</script>

<style scoped>
.admin-dashboard {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Animaciones suaves para las barras de progreso */
.transition-all {
  transition: all 0.5s ease-in-out;
}

/* Asegurar que los gráficos no se desborden */
.max-h-full {
  max-height: 100%;
}
</style>
