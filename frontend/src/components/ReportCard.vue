<!--
  ReportCard.vue - Componente para mostrar tarjetas de reportes
-->
<template>
  <div class="bg-white rounded-lg shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-200">
    <!-- Header del reporte -->
    <div class="px-6 py-4 border-b border-gray-200">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div :class="iconClass">
            <component :is="iconComponent" class="h-6 w-6" />
          </div>
          <div>
            <h3 class="text-lg font-semibold text-gray-900">{{ title }}</h3>
            <p class="text-sm text-gray-500">{{ description }}</p>
          </div>
        </div>
        
        <!-- Botones de acción -->
        <div class="flex items-center space-x-2">
          <select 
            v-if="showPeriodSelector"
            v-model="selectedPeriod"
            @change="$emit('period-change', selectedPeriod)"
            class="text-sm border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring-blue-500"
          >
            <option value="week">Última semana</option>
            <option value="month">Último mes</option>
            <option value="quarter">Último trimestre</option>
            <option value="year">Último año</option>
          </select>
          
          <div class="relative" v-if="showExportMenu">
            <button
              @click="showDropdown = !showDropdown"
              class="flex items-center px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              Exportar
              <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            
            <!-- Dropdown de exportación -->
            <div v-if="showDropdown" class="absolute right-0 z-10 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5">
              <div class="py-1">
                <button
                  @click="exportReport('pdf')"
                  class="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                >
                  <svg class="w-4 h-4 mr-3 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
                  </svg>
                  Exportar como PDF
                </button>
                <button
                  @click="exportReport('excel')"
                  class="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                >
                  <svg class="w-4 h-4 mr-3 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
                  </svg>
                  Exportar como Excel
                </button>
                <button
                  @click="exportReport('csv')"
                  class="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                >
                  <svg class="w-4 h-4 mr-3 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
                  </svg>
                  Exportar como CSV
                </button>
              </div>
            </div>
          </div>
          
          <button
            @click="$emit('refresh')"
            class="flex items-center px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
          </button>
        </div>
      </div>
    </div>
    
    <!-- Loading state -->
    <div v-if="loading" class="px-6 py-8">
      <div class="flex items-center justify-center">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
        <span class="ml-3 text-gray-600">Cargando reporte...</span>
      </div>
    </div>
    
    <!-- Error state -->
    <div v-else-if="error" class="px-6 py-8">
      <div class="text-center">
        <svg class="mx-auto h-12 w-12 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h3 class="mt-2 text-sm font-medium text-gray-900">Error al cargar el reporte</h3>
        <p class="mt-1 text-sm text-gray-500">{{ error }}</p>
        <button
          @click="$emit('retry')"
          class="mt-3 px-4 py-2 text-sm font-medium text-blue-600 hover:text-blue-500"
        >
          Reintentar
        </button>
      </div>
    </div>
    
    <!-- Contenido del reporte -->
    <div v-else class="px-6 py-6">
      <slot :data="data"></slot>
    </div>
    
    <!-- Footer opcional -->
    <div v-if="$slots.footer" class="px-6 py-4 bg-gray-50 rounded-b-lg">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  name: 'ReportCard',
  props: {
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      default: ''
    },
    icon: {
      type: String,
      default: 'chart-bar'
    },
    iconColor: {
      type: String,
      default: 'blue',
      validator: (value) => ['blue', 'green', 'red', 'yellow', 'purple', 'indigo'].includes(value)
    },
    data: {
      type: [Object, Array],
      default: () => ({})
    },
    loading: {
      type: Boolean,
      default: false
    },
    error: {
      type: String,
      default: null
    },
    showPeriodSelector: {
      type: Boolean,
      default: false
    },
    showExportMenu: {
      type: Boolean,
      default: false
    },
    exportType: {
      type: String,
      default: ''
    }
  },
  emits: ['refresh', 'retry', 'period-change', 'export'],
  setup(props, { emit }) {
    const selectedPeriod = ref('month')
    const showDropdown = ref(false)
    
    // Mapeo de iconos
    const iconComponents = {
      'chart-bar': 'svg',
      'currency-dollar': 'svg',
      'users': 'svg',
      'clock': 'svg',
      'trending-up': 'svg',
      'calendar': 'svg'
    }
    
    const iconComponent = computed(() => {
      return iconComponents[props.icon] || 'svg'
    })
    
    const iconClass = computed(() => {
      const baseClass = 'flex items-center justify-center w-10 h-10 rounded-lg'
      const colorClasses = {
        blue: 'bg-blue-100 text-blue-600',
        green: 'bg-green-100 text-green-600',
        red: 'bg-red-100 text-red-600',
        yellow: 'bg-yellow-100 text-yellow-600',
        purple: 'bg-purple-100 text-purple-600',
        indigo: 'bg-indigo-100 text-indigo-600'
      }
      return `${baseClass} ${colorClasses[props.iconColor]}`
    })
    
    const exportReport = (format) => {
      showDropdown.value = false
      emit('export', {
        type: props.exportType,
        format,
        period: selectedPeriod.value
      })
    }
    
    // Cerrar dropdown cuando se hace click fuera
    const closeDropdown = (event) => {
      if (!event.target.closest('.relative')) {
        showDropdown.value = false
      }
    }
    
    return {
      selectedPeriod,
      showDropdown,
      iconComponent,
      iconClass,
      exportReport,
      closeDropdown
    }
  },
  mounted() {
    document.addEventListener('click', this.closeDropdown)
  },
  beforeUnmount() {
    document.removeEventListener('click', this.closeDropdown)
  }
}
</script>

<style scoped>
/* Estilos para los iconos SVG */
svg {
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}
</style>
