<!--
  AdminReportes.vue - FASE 8.8: Reportes y Estadísticas Avanzadas
-->
<template>
  <div class="admin-reportes">
    <!-- Header -->
    <div class="mb-8">
      <div class="flex items-center justify-between">
        <div>
          <h1 class="text-3xl font-bold text-gray-900 mb-2">Reportes y Estadísticas</h1>
          <p class="text-gray-600">Análisis avanzado y reportes del negocio</p>
        </div>
        
        <!-- Controles globales -->
        <div class="flex items-center space-x-4">
          <select
            v-model="globalPeriod"
            @change="updateAllReports"
            class="border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring-blue-500"
          >
            <option value="week">Última semana</option>
            <option value="month">Último mes</option>
            <option value="quarter">Último trimestre</option>
            <option value="year">Último año</option>
          </select>
          
          <button
            @click="refreshAllReports"
            :disabled="isRefreshing"
            class="flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
          >
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            {{ isRefreshing ? 'Actualizando...' : 'Actualizar Todo' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Pestañas de navegación -->
    <div class="mb-8">
      <nav class="flex space-x-8" aria-label="Tabs">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          :class="[
            'whitespace-nowrap py-2 px-1 border-b-2 font-medium text-sm',
            activeTab === tab.id
              ? 'border-blue-500 text-blue-600'
              : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
          ]"
        >
          {{ tab.name }}
        </button>
      </nav>
    </div>

    <!-- Contenido de las pestañas -->
    <div class="space-y-8">
      
      <!-- TAB: KPIs y Métricas Principales -->
      <div v-show="activeTab === 'kpis'">
        <h2 class="text-xl font-semibold text-gray-900 mb-6">KPIs y Métricas Principales</h2>
        
        <!-- KPI Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6 mb-8">
          <div v-for="kpi in businessKPIs" :key="kpi.name" class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-gray-600">{{ kpi.name }}</p>
                <p class="text-2xl font-bold text-gray-900">{{ kpi.current }}</p>
                <p class="text-sm text-gray-500">Meta: {{ kpi.target }}</p>
              </div>
              <div class="flex flex-col items-end">
                <div :class="[
                  'flex items-center text-sm font-medium',
                  kpi.trend === 'up' ? 'text-green-600' : kpi.trend === 'down' ? 'text-red-600' : 'text-gray-600'
                ]">
                  <svg v-if="kpi.trend === 'up'" class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M3.293 9.707a1 1 0 010-1.414l6-6a1 1 0 011.414 0l6 6a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L4.707 9.707a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                  </svg>
                  <svg v-else-if="kpi.trend === 'down'" class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 10.293a1 1 0 010 1.414l-6 6a1 1 0 01-1.414 0l-6-6a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l4.293-4.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                  </svg>
                  <svg v-else class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd" />
                  </svg>
                  {{ Math.abs(kpi.improvement) }}%
                </div>
                <div :class="[
                  'w-16 h-2 rounded-full mt-2',
                  kpi.current >= kpi.target ? 'bg-green-200' : 'bg-red-200'
                ]">
                  <div 
                    :class="[
                      'h-2 rounded-full',
                      kpi.current >= kpi.target ? 'bg-green-500' : 'bg-red-500'
                    ]"
                    :style="{ width: `${Math.min((kpi.current / kpi.target) * 100, 100)}%` }"
                  ></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Gráfico de tendencias de KPIs -->
        <ReportCard
          title="Tendencia de KPIs"
          description="Evolución de métricas clave en el tiempo"
          icon="trending-up"
          icon-color="blue"
          :loading="loadingKPIs"
          :error="errorKPIs"
          :show-period-selector="true"
          :show-export-menu="true"
          export-type="kpi-trends"
          @refresh="loadBusinessKPIs"
          @export="handleExport"
          @period-change="updateKPIsPeriod"
        >
          <template #default="{ data }">
            <AdvancedChart
              type="line"
              :data="kpiTrendsChartData"
              :height="300"
              :chart-types="[
                { value: 'line', label: 'Líneas' },
                { value: 'bar', label: 'Barras' }
              ]"
            />
          </template>
        </ReportCard>
      </div>

      <!-- TAB: Reportes Financieros -->
      <div v-show="activeTab === 'financieros'">
        <h2 class="text-xl font-semibold text-gray-900 mb-6">Reportes Financieros</h2>
        
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-8">
          <!-- Reporte Financiero General -->
          <ReportCard
            title="Análisis Financiero"
            description="Resumen de ingresos, gastos y rentabilidad"
            icon="currency-dollar"
            icon-color="green"
            :loading="loadingFinancial"
            :error="errorFinancial"
            :show-period-selector="true"
            :show-export-menu="true"
            export-type="financial"
            @refresh="loadFinancialReport"
            @export="handleExport"
            @period-change="updateFinancialPeriod"
          >
            <template #default="{ data }">
              <div class="space-y-6">
                <!-- Métricas principales -->
                <div class="grid grid-cols-2 gap-4">
                  <div class="text-center p-4 bg-green-50 rounded-lg">
                    <p class="text-sm text-green-600 font-medium">Ingresos Totales</p>
                    <p class="text-2xl font-bold text-green-900">${{ financialReport.totalRevenue?.toLocaleString() }}</p>
                  </div>
                  <div class="text-center p-4 bg-blue-50 rounded-lg">
                    <p class="text-sm text-blue-600 font-medium">Ganancia Neta</p>
                    <p class="text-2xl font-bold text-blue-900">${{ financialReport.netProfit?.toLocaleString() }}</p>
                  </div>
                </div>
                
                <!-- Gráfico de ingresos por servicio -->
                <AdvancedChart
                  type="doughnut"
                  :data="revenueByServiceChartData"
                  :height="250"
                />
              </div>
            </template>
          </ReportCard>
          
          <!-- Rentabilidad por Barbero -->
          <ReportCard
            title="Rentabilidad por Barbero"
            description="Análisis de desempeño financiero por barbero"
            icon="users"
            icon-color="purple"
            :loading="loadingProfitability"
            :error="errorProfitability"
            :show-export-menu="true"
            export-type="profitability"
            @refresh="loadProfitabilityReport"
            @export="handleExport"
          >
            <template #default="{ data }">
              <div class="overflow-x-auto">
                <table class="min-w-full divide-y divide-gray-200">
                  <thead class="bg-gray-50">
                    <tr>
                      <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Barbero</th>
                      <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Ingresos</th>
                      <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Ticket Promedio</th>
                      <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Eficiencia</th>
                    </tr>
                  </thead>
                  <tbody class="bg-white divide-y divide-gray-200">
                    <tr v-for="barber in profitabilityData" :key="barber.barber">
                      <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ barber.barber }}</td>
                      <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${{ barber.totalRevenue?.toLocaleString() }}</td>
                      <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${{ barber.averageTicket }}</td>
                      <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ barber.efficiency }}%</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </template>
          </ReportCard>
        </div>
        
        <!-- Comparativa de Ingresos -->
        <div class="mt-8">
          <ReportCard
            title="Comparativa de Ingresos"
            description="Comparación mensual de ingresos año actual vs anterior"
            icon="chart-bar"
            icon-color="indigo"
            :loading="loadingComparison"
            :error="errorComparison"
            :show-export-menu="true"
            export-type="revenue-comparison"
            @refresh="loadRevenueComparison"
            @export="handleExport"
          >
            <template #default="{ data }">
              <AdvancedChart
                type="bar"
                :data="revenueComparisonChartData"
                :height="350"
                :chart-types="[
                  { value: 'bar', label: 'Barras' },
                  { value: 'line', label: 'Líneas' }
                ]"
              />
            </template>
          </ReportCard>
        </div>
      </div>

      <!-- TAB: Reportes Operacionales -->
      <div v-show="activeTab === 'operacionales'">
        <h2 class="text-xl font-semibold text-gray-900 mb-6">Reportes Operacionales</h2>
        
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-8">
          <!-- Ocupación por Barbero -->
          <ReportCard
            title="Ocupación por Barbero"
            description="Análisis de utilización y eficiencia"
            icon="clock"
            icon-color="yellow"
            :loading="loadingOccupancy"
            :error="errorOccupancy"
            :show-export-menu="true"
            export-type="barber-occupancy"
            @refresh="loadBarberOccupancy"
            @export="handleExport"
          >
            <template #default="{ data }">
              <div class="space-y-4">
                <div v-for="barber in occupancyData" :key="barber.barber" class="border border-gray-200 rounded-lg p-4">
                  <div class="flex items-center justify-between mb-2">
                    <h4 class="font-medium text-gray-900">{{ barber.barber }}</h4>
                    <span class="text-sm font-medium text-gray-600">{{ barber.occupancyRate }}%</span>
                  </div>
                  <div class="w-full bg-gray-200 rounded-full h-2 mb-2">
                    <div 
                      class="bg-yellow-500 h-2 rounded-full"
                      :style="{ width: `${barber.occupancyRate}%` }"
                    ></div>
                  </div>
                  <div class="flex justify-between text-xs text-gray-500">
                    <span>{{ barber.occupiedHours }}h ocupadas</span>
                    <span>{{ barber.idleHours }}h libres</span>
                  </div>
                </div>
              </div>
            </template>
          </ReportCard>
          
          <!-- Horarios Pico -->
          <ReportCard
            title="Análisis de Horarios Pico"
            description="Horarios y días con mayor demanda"
            icon="calendar"
            icon-color="red"
            :loading="loadingPeakHours"
            :error="errorPeakHours"
            :show-export-menu="true"
            export-type="peak-hours"
            @refresh="loadPeakHoursAnalysis"
            @export="handleExport"
          >
            <template #default="{ data }">
              <AdvancedChart
                type="bar"
                :data="peakHoursChartData"
                :height="300"
              />
            </template>
          </ReportCard>
        </div>
        
        <!-- Demanda de Servicios -->
        <div class="mt-8">
          <ReportCard
            title="Demanda de Servicios"
            description="Servicios más solicitados y tendencias"
            icon="trending-up"
            icon-color="green"
            :loading="loadingServiceDemand"
            :error="errorServiceDemand"
            :show-export-menu="true"
            export-type="service-demand"
            @refresh="loadServiceDemandReport"
            @export="handleExport"
          >
            <template #default="{ data }">
              <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <div>
                  <AdvancedChart
                    type="doughnut"
                    :data="serviceDemandChartData"
                    :height="300"
                  />
                </div>
                <div class="space-y-4">
                  <div v-for="service in serviceDemandData.services" :key="service.service" class="border border-gray-200 rounded-lg p-4">
                    <div class="flex items-center justify-between mb-2">
                      <h4 class="font-medium text-gray-900">{{ service.service }}</h4>
                      <div class="flex items-center">
                        <svg v-if="service.demandTrend === 'up'" class="w-4 h-4 text-green-500 mr-1" fill="currentColor" viewBox="0 0 20 20">
                          <path fill-rule="evenodd" d="M3.293 9.707a1 1 0 010-1.414l6-6a1 1 0 011.414 0l6 6a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L4.707 9.707a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                        </svg>
                        <span :class="[
                          'text-sm font-medium',
                          service.demandTrend === 'up' ? 'text-green-600' : 'text-gray-600'
                        ]">{{ service.growthRate }}%</span>
                      </div>
                    </div>
                    <div class="text-sm text-gray-600">
                      <p>Reservas: {{ service.totalReservations }}</p>
                      <p>Ingresos: ${{ service.revenue?.toLocaleString() }}</p>
                      <p>Rating: {{ service.averageRating }}/5</p>
                    </div>
                  </div>
                </div>
              </div>
            </template>
          </ReportCard>
        </div>
      </div>

      <!-- TAB: Analytics Avanzados -->
      <div v-show="activeTab === 'analytics'">
        <h2 class="text-xl font-semibold text-gray-900 mb-6">Analytics Avanzados</h2>
        
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-8">
          <!-- Tendencias de Reservas -->
          <ReportCard
            title="Tendencias de Reservas"
            description="Análisis de patrones y estacionalidad"
            icon="trending-up"
            icon-color="blue"
            :loading="loadingTrends"
            :error="errorTrends"
            :show-export-menu="true"
            export-type="reservation-trends"
            @refresh="loadReservationTrends"
            @export="handleExport"
          >
            <template #default="{ data }">
              <AdvancedChart
                type="line"
                :data="reservationTrendsChartData"
                :height="300"
              />
            </template>
          </ReportCard>
          
          <!-- Predicciones de Demanda -->
          <ReportCard
            title="Predicciones de Demanda"
            description="Proyecciones para los próximos meses"
            icon="chart-bar"
            icon-color="purple"
            :loading="loadingPredictions"
            :error="errorPredictions"
            :show-export-menu="true"
            export-type="demand-predictions"
            @refresh="loadDemandPredictions"
            @export="handleExport"
          >
            <template #default="{ data }">
              <div class="space-y-4">
                <AdvancedChart
                  type="line"
                  :data="demandPredictionsChartData"
                  :height="250"
                />
                
                <div class="mt-4">
                  <h4 class="font-medium text-gray-900 mb-3">Recomendaciones</h4>
                  <ul class="space-y-2">
                    <li v-for="recommendation in demandPredictionsData.recommendedActions" :key="recommendation" class="flex items-start">
                      <svg class="w-4 h-4 text-blue-500 mt-0.5 mr-2 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                      </svg>
                      <span class="text-sm text-gray-700">{{ recommendation }}</span>
                    </li>
                  </ul>
                </div>
              </div>
            </template>
          </ReportCard>
        </div>
      </div>
      
    </div>

    <!-- Botón flotante para generar reporte completo -->
    <div class="fixed bottom-6 right-6">
      <button
        @click="generateCompleteReport"
        class="flex items-center px-6 py-3 bg-blue-600 text-white rounded-full shadow-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
      >
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
        </svg>
        Reporte Completo
      </button>
    </div>
  </div>
</template>

<script>
import { ref, reactive, onMounted, computed } from 'vue'
import ReportCard from '@/components/ReportCard.vue'
import AdvancedChart from '@/components/AdvancedChart.vue'
import reportService from '@/services/reportService.js'
import ExportService from '@/services/ExportService.js'

export default {
  name: 'AdminReportes',
  components: {
    ReportCard,
    AdvancedChart
  },
  setup() {
    // Estados reactivos
    const activeTab = ref('kpis')
    const globalPeriod = ref('month')
    const isRefreshing = ref(false)

    // Datos de reportes
    const businessKPIs = ref([])
    const financialReport = ref({})
    const profitabilityData = ref([])
    const revenueComparisonData = ref({})
    const occupancyData = ref([])
    const peakHoursData = ref({})
    const serviceDemandData = ref({})
    const reservationTrendsData = ref({})
    const demandPredictionsData = ref({})

    // Estados de carga
    const loadingKPIs = ref(false)
    const loadingFinancial = ref(false)
    const loadingProfitability = ref(false)
    const loadingComparison = ref(false)
    const loadingOccupancy = ref(false)
    const loadingPeakHours = ref(false)
    const loadingServiceDemand = ref(false)
    const loadingTrends = ref(false)
    const loadingPredictions = ref(false)

    // Estados de error
    const errorKPIs = ref(null)
    const errorFinancial = ref(null)
    const errorProfitability = ref(null)
    const errorComparison = ref(null)
    const errorOccupancy = ref(null)
    const errorPeakHours = ref(null)
    const errorServiceDemand = ref(null)
    const errorTrends = ref(null)
    const errorPredictions = ref(null)

    // Configuración de pestañas
    const tabs = [
      { id: 'kpis', name: 'KPIs y Métricas' },
      { id: 'financieros', name: 'Reportes Financieros' },
      { id: 'operacionales', name: 'Reportes Operacionales' },
      { id: 'analytics', name: 'Analytics Avanzados' }
    ]

    // Datos computados para gráficos
    const kpiTrendsChartData = computed(() => ({
      labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
      datasets: [
        {
          label: 'Satisfacción del Cliente',
          data: [4.5, 4.6, 4.7, 4.6, 4.8, 4.7],
          borderColor: 'rgb(59, 130, 246)',
          backgroundColor: 'rgba(59, 130, 246, 0.1)',
          tension: 0.1
        },
        {
          label: 'Retención de Clientes (%)',
          data: [75, 78, 76, 79, 77, 78.5],
          borderColor: 'rgb(34, 197, 94)',
          backgroundColor: 'rgba(34, 197, 94, 0.1)',
          tension: 0.1
        }
      ]
    }))

    const revenueByServiceChartData = computed(() => ({
      labels: financialReport.value.revenueByService?.map(item => item.service) || [],
      datasets: [{
        data: financialReport.value.revenueByService?.map(item => item.revenue) || [],
        backgroundColor: [
          '#3B82F6',
          '#10B981',
          '#F59E0B',
          '#EF4444',
          '#8B5CF6'
        ]
      }]
    }))

    const revenueComparisonChartData = computed(() => ({
      labels: revenueComparisonData.value.currentYear?.map(item => item.month) || [],
      datasets: [
        {
          label: 'Año Actual',
          data: revenueComparisonData.value.currentYear?.map(item => item.revenue) || [],
          backgroundColor: 'rgba(59, 130, 246, 0.8)'
        },
        {
          label: 'Año Anterior',
          data: revenueComparisonData.value.previousYear?.map(item => item.revenue) || [],
          backgroundColor: 'rgba(156, 163, 175, 0.8)'
        }
      ]
    }))

    const peakHoursChartData = computed(() => ({
      labels: peakHoursData.value.hourlyDistribution?.map(item => item.hour) || [],
      datasets: [{
        label: 'Reservas por Hora',
        data: peakHoursData.value.hourlyDistribution?.map(item => item.reservations) || [],
        backgroundColor: 'rgba(249, 115, 22, 0.8)'
      }]
    }))

    const serviceDemandChartData = computed(() => ({
      labels: serviceDemandData.value.services?.map(item => item.service) || [],
      datasets: [{
        data: serviceDemandData.value.services?.map(item => item.totalReservations) || [],
        backgroundColor: [
          '#10B981',
          '#3B82F6',
          '#F59E0B',
          '#EF4444'
        ]
      }]
    }))

    const reservationTrendsChartData = computed(() => ({
      labels: reservationTrendsData.value.monthly?.map(item => item.month) || [],
      datasets: [{
        label: 'Reservas',
        data: reservationTrendsData.value.monthly?.map(item => item.reservations) || [],
        borderColor: 'rgb(59, 130, 246)',
        backgroundColor: 'rgba(59, 130, 246, 0.1)',
        tension: 0.1
      }]
    }))

    const demandPredictionsChartData = computed(() => ({
      labels: demandPredictionsData.value.predictions?.map(item => item.month) || [],
      datasets: [{
        label: 'Reservas Predichas',
        data: demandPredictionsData.value.predictions?.map(item => item.predictedReservations) || [],
        borderColor: 'rgb(139, 92, 246)',
        backgroundColor: 'rgba(139, 92, 246, 0.1)',
        tension: 0.1
      }]
    }))

    // Métodos para cargar datos
    const loadBusinessKPIs = async () => {
      loadingKPIs.value = true
      errorKPIs.value = null
      try {
        const data = await reportService.getBusinessKPIs(globalPeriod.value)
        businessKPIs.value = [
          {
            name: 'Satisfacción del Cliente',
            current: data.customerSatisfaction.current,
            target: data.customerSatisfaction.target,
            trend: data.customerSatisfaction.trend,
            improvement: data.customerSatisfaction.improvement
          },
          {
            name: 'Ticket Promedio',
            current: `$${data.averageTicketValue.current}`,
            target: `$${data.averageTicketValue.target}`,
            trend: data.averageTicketValue.trend,
            improvement: data.averageTicketValue.improvement
          },
          {
            name: 'Retención de Clientes',
            current: `${data.customerRetention.current}%`,
            target: `${data.customerRetention.target}%`,
            trend: data.customerRetention.trend,
            improvement: data.customerRetention.improvement
          },
          {
            name: 'Eficiencia Operacional',
            current: `${data.operationalEfficiency.current}%`,
            target: `${data.operationalEfficiency.target}%`,
            trend: data.operationalEfficiency.trend,
            improvement: data.operationalEfficiency.improvement
          },
          {
            name: 'Ingresos por Barbero',
            current: `$${data.revenuePerBarber.current}`,
            target: `$${data.revenuePerBarber.target}`,
            trend: data.revenuePerBarber.trend,
            improvement: data.revenuePerBarber.improvement
          },
          {
            name: 'Tasa de No-Show',
            current: `${data.noShowRate.current}%`,
            target: `${data.noShowRate.target}%`,
            trend: data.noShowRate.trend,
            improvement: data.noShowRate.improvement
          }
        ]
      } catch (error) {
        errorKPIs.value = error.message
      } finally {
        loadingKPIs.value = false
      }
    }

    const loadFinancialReport = async () => {
      loadingFinancial.value = true
      errorFinancial.value = null
      try {
        const data = await reportService.getFinancialReport({ period: globalPeriod.value })
        financialReport.value = data
      } catch (error) {
        errorFinancial.value = error.message
      } finally {
        loadingFinancial.value = false
      }
    }

    const loadProfitabilityReport = async () => {
      loadingProfitability.value = true
      errorProfitability.value = null
      try {
        const data = await reportService.getProfitabilityByBarber(globalPeriod.value)
        profitabilityData.value = data
      } catch (error) {
        errorProfitability.value = error.message
      } finally {
        loadingProfitability.value = false
      }
    }

    const loadRevenueComparison = async () => {
      loadingComparison.value = true
      errorComparison.value = null
      try {
        const data = await reportService.getRevenueComparison()
        revenueComparisonData.value = data
      } catch (error) {
        errorComparison.value = error.message
      } finally {
        loadingComparison.value = false
      }
    }

    const loadBarberOccupancy = async () => {
      loadingOccupancy.value = true
      errorOccupancy.value = null
      try {
        const data = await reportService.getBarberOccupancy({ period: globalPeriod.value })
        occupancyData.value = data
      } catch (error) {
        errorOccupancy.value = error.message
      } finally {
        loadingOccupancy.value = false
      }
    }

    const loadPeakHoursAnalysis = async () => {
      loadingPeakHours.value = true
      errorPeakHours.value = null
      try {
        const data = await reportService.getPeakHoursAnalysis(globalPeriod.value)
        peakHoursData.value = data
      } catch (error) {
        errorPeakHours.value = error.message
      } finally {
        loadingPeakHours.value = false
      }
    }

    const loadServiceDemandReport = async () => {
      loadingServiceDemand.value = true
      errorServiceDemand.value = null
      try {
        const data = await reportService.getServiceDemandReport({ period: globalPeriod.value })
        serviceDemandData.value = data
      } catch (error) {
        errorServiceDemand.value = error.message
      } finally {
        loadingServiceDemand.value = false
      }
    }

    const loadReservationTrends = async () => {
      loadingTrends.value = true
      errorTrends.value = null
      try {
        const data = await reportService.getReservationTrends(globalPeriod.value)
        reservationTrendsData.value = data
      } catch (error) {
        errorTrends.value = error.message
      } finally {
        loadingTrends.value = false
      }
    }

    const loadDemandPredictions = async () => {
      loadingPredictions.value = true
      errorPredictions.value = null
      try {
        const data = await reportService.getDemandPredictions(3)
        demandPredictionsData.value = data
      } catch (error) {
        errorPredictions.value = error.message
      } finally {
        loadingPredictions.value = false
      }
    }

    // Métodos de utilidad
    const updateAllReports = () => {
      refreshAllReports()
    }

    const refreshAllReports = async () => {
      isRefreshing.value = true
      
      const promises = [
        loadBusinessKPIs(),
        loadFinancialReport(),
        loadProfitabilityReport(),
        loadRevenueComparison(),
        loadBarberOccupancy(),
        loadPeakHoursAnalysis(),
        loadServiceDemandReport(),
        loadReservationTrends(),
        loadDemandPredictions()
      ]

      await Promise.allSettled(promises)
      isRefreshing.value = false
    }

    const updateKPIsPeriod = (period) => {
      globalPeriod.value = period
      loadBusinessKPIs()
    }

    const updateFinancialPeriod = (period) => {
      globalPeriod.value = period
      loadFinancialReport()
    }

    const handleExport = async (exportData) => {
      try {
        const { type, format, period } = exportData
        
        if (format === 'pdf') {
          await generatePDFReport(type)
        } else {
          await reportService.exportToCSV(type, { period })
        }
      } catch (error) {
        console.error('Error al exportar:', error)
        // Aquí podrías mostrar una notificación de error
      }
    }

    const generatePDFReport = (reportType) => {
      const reportDataMap = {
        'kpi-trends': businessKPIs.value,
        'financial': financialReport.value,
        'profitability': profitabilityData.value,
        'revenue-comparison': revenueComparisonData.value,
        'barber-occupancy': occupancyData.value,
        'peak-hours': peakHoursData.value,
        'service-demand': serviceDemandData.value,
        'reservation-trends': reservationTrendsData.value,
        'demand-predictions': demandPredictionsData.value
      }

      const data = reportDataMap[reportType]
      const title = `Reporte ${reportType.replace('-', ' ').toUpperCase()}`
      
      ExportService.generatePDFReport(data, title)
    }

    const generateCompleteReport = () => {
      const completeData = {
        'KPIs del Negocio': businessKPIs.value,
        'Reporte Financiero': financialReport.value,
        'Rentabilidad por Barbero': profitabilityData.value,
        'Ocupación por Barbero': occupancyData.value,
        'Demanda de Servicios': serviceDemandData.value
      }
      
      ExportService.generatePDFReport(completeData, 'Reporte Completo del Negocio')
    }

    // Lifecycle
    onMounted(() => {
      refreshAllReports()
    })

    return {
      // Estados
      activeTab,
      globalPeriod,
      isRefreshing,
      tabs,
      
      // Datos
      businessKPIs,
      financialReport,
      profitabilityData,
      revenueComparisonData,
      occupancyData,
      peakHoursData,
      serviceDemandData,
      reservationTrendsData,
      demandPredictionsData,
      
      // Estados de carga
      loadingKPIs,
      loadingFinancial,
      loadingProfitability,
      loadingComparison,
      loadingOccupancy,
      loadingPeakHours,
      loadingServiceDemand,
      loadingTrends,
      loadingPredictions,
      
      // Estados de error
      errorKPIs,
      errorFinancial,
      errorProfitability,
      errorComparison,
      errorOccupancy,
      errorPeakHours,
      errorServiceDemand,
      errorTrends,
      errorPredictions,
      
      // Datos computados para gráficos
      kpiTrendsChartData,
      revenueByServiceChartData,
      revenueComparisonChartData,
      peakHoursChartData,
      serviceDemandChartData,
      reservationTrendsChartData,
      demandPredictionsChartData,
      
      // Métodos
      updateAllReports,
      refreshAllReports,
      updateKPIsPeriod,
      updateFinancialPeriod,
      loadBusinessKPIs,
      loadFinancialReport,
      loadProfitabilityReport,
      loadRevenueComparison,
      loadBarberOccupancy,
      loadPeakHoursAnalysis,
      loadServiceDemandReport,
      loadReservationTrends,
      loadDemandPredictions,
      handleExport,
      generateCompleteReport
    }
  }
}
</script>

<style scoped>
/* Estilos específicos para reportes */
.admin-reportes {
  min-height: calc(100vh - 200px);
}

/* Animación para cambio de pestañas */
.tab-content {
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Estilos para el botón flotante */
.fixed {
  z-index: 40;
}

/* Responsive para tablas */
@media (max-width: 640px) {
  .overflow-x-auto {
    font-size: 0.875rem;
  }
}
</style>
