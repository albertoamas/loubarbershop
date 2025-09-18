<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 to-gray-100 p-6">
    <!-- Header del dashboard -->
    <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200 mb-6">
      <div class="flex flex-col lg:flex-row lg:items-start lg:justify-between gap-6">
        <div class="flex-1">
          <h1 class="text-3xl font-extrabold bg-gradient-to-r from-black to-gray-500 bg-clip-text text-transparent mb-2">
            Reportes y Análisis
          </h1>
          <p class="text-slate-600 text-lg leading-relaxed">
            Panel completo de análisis de negocio y reportes de Lou Barber Shop
          </p>
        </div>
        <div class="flex flex-col sm:flex-row gap-3">
          <button 
            @click="refreshAllData" 
            :disabled="isRefreshing"
            class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-black to-gray-700 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-200 disabled:opacity-70 disabled:cursor-not-allowed disabled:transform-none"
          >
            <svg :class="{ 'animate-spin': isRefreshing }" class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            {{ isRefreshing ? 'Actualizando...' : 'Actualizar' }}
          </button>
          <button 
            @click="exportCompleteReport" 
            :disabled="isExporting"
            class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-violet-600 to-purple-600 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-200 disabled:opacity-70 disabled:cursor-not-allowed disabled:transform-none"
          >
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            {{ isExporting ? 'Exportando...' : 'Exportar' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Navegación de pestañas -->
    <div class="bg-white rounded-2xl p-2 shadow-sm border border-slate-200 mb-8">
      <div class="flex flex-wrap gap-1">
        <button 
          v-for="tab in tabs" 
          :key="tab.id"
          @click="activeTab = tab.id"
          :class="[
            'inline-flex items-center px-4 py-3 rounded-xl font-semibold text-sm transition-all duration-200',
            activeTab === tab.id 
              ? 'bg-gradient-to-r from-black to-gray-700 text-white shadow-lg' 
              : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
          ]"
        >
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="tab.id === 'dashboard'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            <path v-else-if="tab.id === 'barberos'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            <path v-else-if="tab.id === 'servicios'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          {{ tab.name }}
        </button>
      </div>
    </div>

    <!-- Dashboard General -->
    <div v-show="activeTab === 'dashboard'" class="space-y-8">
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <h2 class="text-2xl font-bold text-slate-900">Dashboard General</h2>
        <div class="flex items-center gap-3">
          <select v-model="dateRange" class="px-4 py-2 bg-white border border-slate-200 rounded-lg text-slate-700 font-medium focus:ring-2 focus:ring-violet-500 focus:border-violet-500 transition-colors">
            <option value="7">Últimos 7 días</option>
            <option value="30">Últimos 30 días</option>
            <option value="90">Últimos 3 meses</option>
            <option value="365">Último año</option>
          </select>
        </div>
      </div>

      <!-- KPIs principales -->
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
        <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200 hover:shadow-lg hover:border-violet-200 transition-all duration-200 group">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 bg-gradient-to-r from-emerald-500 to-teal-500 rounded-xl flex items-center justify-center text-white shadow-lg group-hover:scale-110 transition-transform duration-200">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <h3 class="text-sm font-semibold text-slate-600 uppercase tracking-wider mb-2">Ingresos Totales</h3>
              <p class="text-2xl font-bold text-slate-900 mb-2">${{ totalRevenue.toLocaleString() }}</p>
              <span class="inline-flex items-center px-2 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-700">
                +12.5%
              </span>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200 hover:shadow-lg hover:border-violet-200 transition-all duration-200 group">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-xl flex items-center justify-center text-white shadow-lg group-hover:scale-110 transition-transform duration-200">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <h3 class="text-sm font-semibold text-slate-600 uppercase tracking-wider mb-2">Total Reservas</h3>
              <p class="text-2xl font-bold text-slate-900 mb-2">{{ totalReservations }}</p>
              <span class="inline-flex items-center px-2 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-700">
                +8.3%
              </span>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200 hover:shadow-lg hover:border-violet-200 transition-all duration-200 group">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 bg-gradient-to-r from-amber-500 to-orange-500 rounded-xl flex items-center justify-center text-white shadow-lg group-hover:scale-110 transition-transform duration-200">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <h3 class="text-sm font-semibold text-slate-600 uppercase tracking-wider mb-2">Ticket Promedio</h3>
              <p class="text-2xl font-bold text-slate-900 mb-2">${{ averageTicket.toFixed(2) }}</p>
              <span class="inline-flex items-center px-2 py-1 rounded-full text-xs font-semibold bg-red-100 text-red-700">
                -2.1%
              </span>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200 hover:shadow-lg hover:border-violet-200 transition-all duration-200 group">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 bg-gradient-to-r from-violet-500 to-purple-500 rounded-xl flex items-center justify-center text-white shadow-lg group-hover:scale-110 transition-transform duration-200">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <h3 class="text-sm font-semibold text-slate-600 uppercase tracking-wider mb-2">Conversión</h3>
              <p class="text-2xl font-bold text-slate-900 mb-2">{{ conversionRate.toFixed(1) }}%</p>
              <span class="inline-flex items-center px-2 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-700">
                +5.2%
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Gráfico de tendencias -->
      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div class="bg-slate-50 px-6 py-4 border-b border-slate-200">
          <h3 class="text-lg font-semibold text-slate-900">Tendencia de Ingresos</h3>
        </div>
        <div class="p-6 h-96">
          <canvas ref="revenueChart"></canvas>
        </div>
      </div>
    </div>

    <!-- Performance Barberos -->
    <div v-show="activeTab === 'barberos'" class="space-y-8">
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <h2 class="text-2xl font-bold text-slate-900">Performance de Barberos</h2>
        <div class="flex items-center gap-3">
          <select v-model="barberFilter" class="px-4 py-2 bg-white border border-slate-200 rounded-lg text-slate-700 font-medium focus:ring-2 focus:ring-violet-500 focus:border-violet-500 transition-colors">
            <option value="">Todos los barberos</option>
            <option v-for="barber in barbers" :key="barber.id" :value="barber.id">
              {{ barber.name }}
            </option>
          </select>
        </div>
      </div>

      <!-- Grid de barberos -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div v-for="barber in filteredBarbers" :key="barber.id" class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200 hover:shadow-lg hover:border-violet-200 transition-all duration-200">
          <div class="flex items-start justify-between mb-6">
            <div class="flex-1">
              <h4 class="text-lg font-semibold text-slate-900 mb-1">{{ barber.name }}</h4>
              <span class="text-sm text-slate-500 mb-3 block">{{ barber.specialty || 'General' }}</span>
              <span :class="[
                'inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider',
                getPerformanceBadgeClass(barber.efficiency)
              ]">
                {{ getPerformanceText(barber.efficiency) }}
              </span>
            </div>
            <div class="w-12 h-12 bg-gradient-to-r from-violet-500 to-purple-500 rounded-xl flex items-center justify-center text-white font-semibold text-lg shadow-lg">
              {{ barber.name.charAt(0) }}
            </div>
          </div>

          <div class="grid grid-cols-3 gap-4 mb-6">
            <div class="text-center p-4 bg-slate-50 rounded-xl">
              <span class="block text-xl font-bold text-slate-900">{{ barber.totalReservations }}</span>
              <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider mt-1">Reservas</span>
            </div>
            <div class="text-center p-4 bg-slate-50 rounded-xl">
              <span class="block text-xl font-bold text-slate-900">${{ barber.revenue }}</span>
              <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider mt-1">Ingresos</span>
            </div>
            <div class="text-center p-4 bg-slate-50 rounded-xl">
              <span class="block text-xl font-bold text-slate-900">{{ barber.rating }}</span>
              <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider mt-1">Rating</span>
            </div>
          </div>

          <div>
            <div class="w-full h-2 bg-slate-200 rounded-full overflow-hidden mb-2">
              <div 
                class="h-full bg-gradient-to-r from-red-500 via-yellow-500 to-emerald-500 rounded-full transition-all duration-300" 
                :style="{ width: barber.efficiency + '%' }"
              ></div>
            </div>
            <span class="text-xs text-slate-500 font-medium">{{ barber.efficiency }}% eficiencia</span>
          </div>
        </div>
      </div>

      <!-- Utilización de horarios -->
      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div class="bg-slate-50 px-6 py-4 border-b border-slate-200">
          <h3 class="text-lg font-semibold text-slate-900">Utilización por Barbero</h3>
        </div>
        <div class="p-6">
          <div class="space-y-4">
            <div v-for="barber in barberUtilization" :key="barber.id" class="flex items-center justify-between p-4 bg-slate-50 rounded-xl border border-slate-200">
              <div class="flex-1">
                <span class="font-semibold text-slate-900 block mb-1">{{ barber.name }}</span>
                <span class="text-sm text-slate-500">{{ barber.workedHours }}h trabajadas</span>
              </div>
              <div class="flex items-center gap-4 min-w-40">
                <div class="flex-1 h-2 bg-slate-200 rounded-full overflow-hidden">
                  <div 
                    class="h-full bg-gradient-to-r from-violet-500 to-purple-500 rounded-full transition-all duration-300" 
                    :style="{ width: barber.utilization + '%' }"
                  ></div>
                </div>
                <span class="text-sm font-semibold text-slate-900 min-w-12 text-right">{{ barber.utilization }}%</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Análisis Servicios -->
    <div v-show="activeTab === 'servicios'" class="space-y-8">
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <h2 class="text-2xl font-bold text-slate-900">Análisis de Servicios</h2>
        <div class="flex items-center gap-3">
          <select v-model="serviceCategory" class="px-4 py-2 bg-white border border-slate-200 rounded-lg text-slate-700 font-medium focus:ring-2 focus:ring-violet-500 focus:border-violet-500 transition-colors">
            <option value="">Todas las categorías</option>
            <option value="corte">Cortes</option>
            <option value="barba">Barba</option>
            <option value="combo">Combos</option>
          </select>
        </div>
      </div>

      <!-- Servicios populares -->
      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div class="bg-slate-50 px-6 py-4 border-b border-slate-200">
          <h3 class="text-lg font-semibold text-slate-900">Servicios Más Populares</h3>
        </div>
        <div class="p-6">
          <div class="space-y-4">
            <div v-for="service in popularServices" :key="service.id" class="flex flex-col sm:flex-row sm:items-center sm:justify-between p-4 border border-slate-200 rounded-xl hover:border-violet-200 hover:bg-slate-50 transition-all duration-200 gap-4">
              <div class="flex-1">
                <h4 class="text-lg font-semibold text-slate-900 mb-1">{{ service.name }}</h4>
                <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-slate-100 text-slate-700">
                  {{ service.category }}
                </span>
              </div>
              <div class="flex flex-col sm:flex-row gap-6">
                <div class="text-center">
                  <span class="block text-xl font-bold text-slate-900">{{ service.bookings }}</span>
                  <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Reservas</span>
                </div>
                <div class="text-center">
                  <span class="block text-xl font-bold text-slate-900">${{ service.revenue }}</span>
                  <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Ingresos</span>
                </div>
                <div class="text-center">
                  <span class="block text-xl font-bold text-slate-900">{{ service.rating }}</span>
                  <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Rating</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Gráfico de servicios -->
      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div class="bg-slate-50 px-6 py-4 border-b border-slate-200">
          <h3 class="text-lg font-semibold text-slate-900">Distribución de Servicios</h3>
        </div>
        <div class="p-6 h-96">
          <canvas ref="servicesChart"></canvas>
        </div>
      </div>
    </div>

    <!-- Análisis Temporal -->
    <div v-show="activeTab === 'temporal'" class="space-y-8">
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <h2 class="text-2xl font-bold text-slate-900">Análisis Temporal</h2>
        <div class="flex items-center gap-3">
          <select v-model="temporalView" class="px-4 py-2 bg-white border border-slate-200 rounded-lg text-slate-700 font-medium focus:ring-2 focus:ring-violet-500 focus:border-violet-500 transition-colors">
            <option value="hours">Por horas</option>
            <option value="days">Por días</option>
            <option value="months">Por meses</option>
          </select>
        </div>
      </div>

      <!-- Heatmap de demanda -->
      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div class="bg-slate-50 px-6 py-4 border-b border-slate-200">
          <h3 class="text-lg font-semibold text-slate-900">Mapa de Calor - Demanda por Horarios</h3>
        </div>
        <div class="p-6">
          <div class="bg-slate-50 rounded-xl p-4 overflow-x-auto">
            <div class="inline-block min-w-full">
              <table class="w-full border-separate border-spacing-1">
                <thead>
                  <tr>
                    <th class="w-16"></th>
                    <th v-for="day in weekDays" :key="day" class="px-3 py-2 bg-slate-200 rounded text-center text-sm font-semibold text-slate-700 min-w-16">
                      {{ day }}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="hour in workingHours" :key="hour">
                    <td class="px-3 py-2 bg-slate-200 rounded text-center text-sm font-semibold text-slate-700">
                      {{ hour }}:00
                    </td>
                    <td 
                      v-for="day in weekDays" 
                      :key="`${hour}-${day}`"
                      @click="showHourDetails(hour, day)"
                      :class="[
                        'px-3 py-2 text-center text-sm font-medium rounded cursor-pointer transition-all duration-200 hover:scale-110 hover:shadow-lg',
                        getHeatmapIntensity(hour, day) === 0 ? 'bg-slate-100 text-slate-400' :
                        getHeatmapIntensity(hour, day) === 1 ? 'bg-blue-100 text-blue-700' :
                        getHeatmapIntensity(hour, day) === 2 ? 'bg-blue-200 text-blue-800' :
                        getHeatmapIntensity(hour, day) === 3 ? 'bg-blue-300 text-blue-900' :
                        'bg-blue-500 text-white'
                      ]"
                    >
                      {{ getReservationCount(hour, day) }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- Tendencias temporales -->
      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div class="bg-slate-50 px-6 py-4 border-b border-slate-200">
          <h3 class="text-lg font-semibold text-slate-900">Tendencias por Período</h3>
        </div>
        <div class="p-6 h-96">
          <canvas ref="temporalChart"></canvas>
        </div>
      </div>
    </div>

    <!-- Botón flotante de exportar -->
    <button 
      v-if="hasDataToExport"
      @click="exportCurrentView" 
      :disabled="isExporting"
      class="fixed bottom-8 right-8 inline-flex items-center gap-2 px-6 py-4 bg-gradient-to-r from-violet-600 to-purple-600 text-white rounded-full font-semibold shadow-xl hover:shadow-2xl transform hover:-translate-y-1 transition-all duration-200 z-50 disabled:opacity-70 disabled:cursor-not-allowed disabled:transform-none"
    >
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
      </svg>
      Exportar {{ tabs.find(t => t.id === activeTab)?.name }}
    </button>
  </div>
</template>

<script>
import { ref, reactive, onMounted, computed } from 'vue'
import Chart from 'chart.js/auto'

export default {
  name: 'AdminReportes',
  setup() {
    // Estados reactivos
    const activeTab = ref('dashboard')
    const dateRange = ref('30')
    const barberFilter = ref('')
    const serviceCategory = ref('')
    const temporalView = ref('hours')
    const isRefreshing = ref(false)
    const isExporting = ref(false)

    // Datos principales
    const totalRevenue = ref(15420)
    const totalReservations = ref(342)
    const averageTicket = ref(45.12)
    const conversionRate = ref(78.5)

    // Configuración de pestañas
    const tabs = ref([
      { id: 'dashboard', name: 'Dashboard General' },
      { id: 'barberos', name: 'Performance Barberos' },
      { id: 'servicios', name: 'Análisis Servicios' },
      { id: 'temporal', name: 'Análisis Temporal' }
    ])

    // Datos de barberos
    const barbers = ref([
      { id: 1, name: 'Carlos Mendez', specialty: 'Cortes Clásicos', efficiency: 92, totalReservations: 85, revenue: 3400, rating: 4.8 },
      { id: 2, name: 'Ana García', specialty: 'Barbas y Bigotes', efficiency: 88, totalReservations: 72, revenue: 2890, rating: 4.6 },
      { id: 3, name: 'Luis Torres', specialty: 'Cortes Modernos', efficiency: 95, totalReservations: 98, revenue: 4100, rating: 4.9 },
      { id: 4, name: 'María López', specialty: 'Tratamientos', efficiency: 82, totalReservations: 65, revenue: 2750, rating: 4.7 }
    ])

    const barberUtilization = ref([
      { id: 1, name: 'Luis Torres', workedHours: 42, utilization: 95 },
      { id: 2, name: 'Carlos Mendez', workedHours: 40, utilization: 92 },
      { id: 3, name: 'Ana García', workedHours: 38, utilization: 88 },
      { id: 4, name: 'María López', workedHours: 35, utilization: 82 }
    ])

    // Datos de servicios
    const popularServices = ref([
      { id: 1, name: 'Corte + Barba', category: 'combo', bookings: 124, revenue: 6200, rating: 4.8 },
      { id: 2, name: 'Corte Clásico', category: 'corte', bookings: 98, revenue: 2940, rating: 4.7 },
      { id: 3, name: 'Arreglo de Barba', category: 'barba', bookings: 76, revenue: 1520, rating: 4.6 },
      { id: 4, name: 'Corte Fade', category: 'corte', bookings: 89, revenue: 3560, rating: 4.9 }
    ])

    // Datos temporales
    const weekDays = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    const workingHours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    // Datos de demanda por horas (simulados)
    const heatmapData = reactive({
      'Lun': { 9: 2, 10: 4, 11: 6, 12: 8, 13: 5, 14: 7, 15: 9, 16: 12, 17: 10, 18: 8, 19: 6, 20: 3 },
      'Mar': { 9: 3, 10: 5, 11: 7, 12: 9, 13: 6, 14: 8, 15: 10, 16: 13, 17: 11, 18: 9, 19: 7, 20: 4 },
      'Mié': { 9: 4, 10: 6, 11: 8, 12: 10, 13: 7, 14: 9, 15: 11, 16: 14, 17: 12, 18: 10, 19: 8, 20: 5 },
      'Jue': { 9: 5, 10: 7, 11: 9, 12: 11, 13: 8, 14: 10, 15: 12, 16: 15, 17: 13, 18: 11, 19: 9, 20: 6 },
      'Vie': { 9: 6, 10: 8, 11: 10, 12: 12, 13: 9, 14: 11, 15: 13, 16: 16, 17: 14, 18: 12, 19: 10, 20: 7 },
      'Sáb': { 9: 8, 10: 10, 11: 12, 12: 14, 13: 11, 14: 13, 15: 15, 16: 18, 17: 16, 18: 14, 19: 12, 20: 9 },
      'Dom': { 9: 3, 10: 5, 11: 7, 12: 9, 13: 6, 14: 8, 15: 10, 16: 13, 17: 11, 18: 9, 19: 7, 20: 4 }
    })

    // Computadas
    const filteredBarbers = computed(() => {
      if (!barberFilter.value) return barbers.value
      return barbers.value.filter(barber => barber.id === parseInt(barberFilter.value))
    })

    const hasDataToExport = computed(() => {
      return totalReservations.value > 0
    })

    // Métodos
    const refreshAllData = async () => {
      isRefreshing.value = true
      try {
        // Simular carga de datos
        await new Promise(resolve => setTimeout(resolve, 2000))
        // Aquí cargarías datos reales
      } finally {
        isRefreshing.value = false
      }
    }

    const exportCompleteReport = async () => {
      isExporting.value = true
      try {
        // Lógica de exportación completa
        await new Promise(resolve => setTimeout(resolve, 1500))
      } finally {
        isExporting.value = false
      }
    }

    const exportCurrentView = async () => {
      isExporting.value = true
      try {
        // Lógica de exportación de vista actual
        await new Promise(resolve => setTimeout(resolve, 1000))
      } finally {
        isExporting.value = false
      }
    }

    const getPerformanceBadgeClass = (efficiency) => {
      if (efficiency >= 90) return 'bg-emerald-100 text-emerald-700 border border-emerald-200'
      if (efficiency >= 80) return 'bg-blue-100 text-blue-700 border border-blue-200'
      if (efficiency >= 70) return 'bg-yellow-100 text-yellow-700 border border-yellow-200'
      return 'bg-red-100 text-red-700 border border-red-200'
    }

    const getPerformanceText = (efficiency) => {
      if (efficiency >= 90) return 'Excelente'
      if (efficiency >= 80) return 'Bueno'
      if (efficiency >= 70) return 'Regular'
      return 'Necesita mejora'
    }

    const getReservationCount = (hour, day) => {
      return heatmapData[day]?.[hour] || 0
    }

    const getHeatmapIntensity = (hour, day) => {
      const count = getReservationCount(hour, day)
      if (count === 0) return 0
      if (count <= 5) return 1
      if (count <= 10) return 2
      if (count <= 15) return 3
      return 4
    }

    const showHourDetails = (hour, day) => {
      const count = getReservationCount(hour, day)
      alert(`${day} ${hour}:00 - ${count} reservas`)
    }

    // Referencias para gráficos
    const revenueChart = ref(null)
    const servicesChart = ref(null)
    const temporalChart = ref(null)

    // Inicialización de gráficos
    const initCharts = () => {
      // Configuración básica de Chart.js aquí
      if (revenueChart.value) {
        new Chart(revenueChart.value, {
          type: 'line',
          data: {
            labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
            datasets: [{
              label: 'Ingresos',
              data: [12000, 13500, 11800, 15200, 14600, 16800],
              borderColor: '#8b5cf6',
              backgroundColor: 'rgba(139, 92, 246, 0.1)',
              tension: 0.4
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false
          }
        })
      }
    }

    onMounted(() => {
      initCharts()
    })

    return {
      // Estados
      activeTab,
      dateRange,
      barberFilter,
      serviceCategory,
      temporalView,
      isRefreshing,
      isExporting,
      
      // Datos
      totalRevenue,
      totalReservations,
      averageTicket,
      conversionRate,
      tabs,
      barbers,
      barberUtilization,
      popularServices,
      weekDays,
      workingHours,
      
      // Computadas
      filteredBarbers,
      hasDataToExport,
      
      // Métodos
      refreshAllData,
      exportCompleteReport,
      exportCurrentView,
      getPerformanceBadgeClass,
      getPerformanceText,
      getReservationCount,
      getHeatmapIntensity,
      showHourDetails,
      
      // Referencias
      revenueChart,
      servicesChart,
      temporalChart
    }
  }
}
</script>

<style scoped>
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>
