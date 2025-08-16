<!--
  AdvancedChart.vue - Componente para gráficos avanzados en reportes
-->
<template>
  <div class="advanced-chart">
    <!-- Controles del gráfico -->
    <div v-if="showControls" class="flex items-center justify-between mb-4">
      <div class="flex items-center space-x-4">
        <select
          v-if="chartTypes.length > 1"
          v-model="selectedChartType"
          @change="updateChartType"
          class="text-sm border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring-blue-500"
        >
          <option v-for="type in chartTypes" :key="type.value" :value="type.value">
            {{ type.label }}
          </option>
        </select>
        
        <div v-if="showLegendToggle" class="flex items-center">
          <input
            id="legend-toggle"
            v-model="showLegend"
            @change="updateLegend"
            type="checkbox"
            class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
          >
          <label for="legend-toggle" class="ml-2 text-sm text-gray-700">
            Mostrar leyenda
          </label>
        </div>
      </div>
      
      <div class="flex items-center space-x-2">
        <button
          @click="downloadChart"
          class="flex items-center px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
        >
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          Descargar
        </button>
        
        <button
          @click="toggleFullscreen"
          class="flex items-center px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" />
          </svg>
        </button>
      </div>
    </div>
    
    <!-- Container del gráfico -->
    <div :class="chartContainerClass">
      <canvas :ref="canvasRef" :width="width" :height="height"></canvas>
    </div>
    
    <!-- Loading overlay -->
    <div v-if="loading" class="absolute inset-0 bg-white bg-opacity-75 flex items-center justify-center">
      <div class="text-center">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto mb-2"></div>
        <span class="text-sm text-gray-600">Cargando gráfico...</span>
      </div>
    </div>
    
    <!-- Error state -->
    <div v-if="error" class="absolute inset-0 bg-white flex items-center justify-center">
      <div class="text-center">
        <svg class="mx-auto h-12 w-12 text-red-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h3 class="text-sm font-medium text-gray-900 mb-2">Error al cargar el gráfico</h3>
        <p class="text-sm text-gray-500 mb-4">{{ error }}</p>
        <button
          @click="$emit('retry')"
          class="px-4 py-2 text-sm font-medium text-blue-600 hover:text-blue-500"
        >
          Reintentar
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  RadialLinearScale,
  Filler
} from 'chart.js'

// Registrar componentes de Chart.js
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  RadialLinearScale,
  Filler
)

export default {
  name: 'AdvancedChart',
  props: {
    type: {
      type: String,
      default: 'bar',
      validator: (value) => ['bar', 'line', 'pie', 'doughnut', 'radar', 'polarArea'].includes(value)
    },
    data: {
      type: Object,
      required: true
    },
    options: {
      type: Object,
      default: () => ({})
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 200
    },
    chartTypes: {
      type: Array,
      default: () => []
    },
    showControls: {
      type: Boolean,
      default: true
    },
    showLegendToggle: {
      type: Boolean,
      default: true
    },
    loading: {
      type: Boolean,
      default: false
    },
    error: {
      type: String,
      default: null
    },
    responsive: {
      type: Boolean,
      default: true
    },
    maintainAspectRatio: {
      type: Boolean,
      default: false
    }
  },
  emits: ['chart-ready', 'retry'],
  setup(props, { emit }) {
    const canvasRef = ref('chartCanvas')
    const chart = ref(null)
    const selectedChartType = ref(props.type)
    const showLegend = ref(true)
    const isFullscreen = ref(false)
    
    const chartContainerClass = computed(() => ({
      'relative': true,
      'w-full': true,
      'h-full': true,
      'fixed inset-0 z-50 bg-white p-8': isFullscreen.value
    }))
    
    // Configuración por defecto para diferentes tipos de gráficos
    const getDefaultOptions = (chartType) => {
      const baseOptions = {
        responsive: props.responsive,
        maintainAspectRatio: props.maintainAspectRatio,
        plugins: {
          legend: {
            display: showLegend.value,
            position: 'top'
          },
          tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: 'rgba(0, 0, 0, 0.8)',
            titleColor: '#fff',
            bodyColor: '#fff',
            cornerRadius: 8,
            displayColors: true
          }
        },
        scales: {},
        animation: {
          duration: 1000,
          easing: 'easeInOutQuart'
        }
      }
      
      // Configuraciones específicas por tipo
      switch (chartType) {
        case 'bar':
          baseOptions.scales = {
            y: {
              beginAtZero: true,
              grid: {
                color: 'rgba(0, 0, 0, 0.1)'
              }
            },
            x: {
              grid: {
                display: false
              }
            }
          }
          break
          
        case 'line':
          baseOptions.elements = {
            line: {
              tension: 0.4
            },
            point: {
              radius: 4,
              hoverRadius: 8
            }
          }
          baseOptions.scales = {
            y: {
              beginAtZero: true,
              grid: {
                color: 'rgba(0, 0, 0, 0.1)'
              }
            },
            x: {
              grid: {
                color: 'rgba(0, 0, 0, 0.05)'
              }
            }
          }
          break
          
        case 'pie':
        case 'doughnut':
          baseOptions.plugins.tooltip = {
            callbacks: {
              label: function(context) {
                const label = context.label || ''
                const value = context.parsed
                const total = context.dataset.data.reduce((sum, val) => sum + val, 0)
                const percentage = ((value / total) * 100).toFixed(1)
                return `${label}: ${value} (${percentage}%)`
              }
            }
          }
          break
      }
      
      return baseOptions
    }
    
    const createChart = async () => {
      if (!canvasRef.value) return
      
      await nextTick()
      
      const canvas = document.querySelector(`[ref="${canvasRef.value}"]`)
      if (!canvas) return
      
      const ctx = canvas.getContext('2d')
      
      // Destruir gráfico existente
      if (chart.value) {
        chart.value.destroy()
      }
      
      // Combinar opciones
      const defaultOptions = getDefaultOptions(selectedChartType.value)
      const mergedOptions = {
        ...defaultOptions,
        ...props.options,
        plugins: {
          ...defaultOptions.plugins,
          ...props.options.plugins
        }
      }
      
      // Crear nuevo gráfico
      chart.value = new ChartJS(ctx, {
        type: selectedChartType.value,
        data: props.data,
        options: mergedOptions
      })
      
      emit('chart-ready', chart.value)
    }
    
    const updateChartType = () => {
      createChart()
    }
    
    const updateLegend = () => {
      if (chart.value) {
        chart.value.options.plugins.legend.display = showLegend.value
        chart.value.update()
      }
    }
    
    const downloadChart = () => {
      if (chart.value) {
        const url = chart.value.toBase64Image('image/png', 1)
        const link = document.createElement('a')
        link.download = `grafico-${Date.now()}.png`
        link.href = url
        link.click()
      }
    }
    
    const toggleFullscreen = () => {
      isFullscreen.value = !isFullscreen.value
      // Redimensionar el gráfico después del cambio
      setTimeout(() => {
        if (chart.value) {
          chart.value.resize()
        }
      }, 100)
    }
    
    // Watchers
    watch(() => props.data, () => {
      if (chart.value) {
        chart.value.data = props.data
        chart.value.update()
      }
    }, { deep: true })
    
    watch(() => props.type, (newType) => {
      selectedChartType.value = newType
      createChart()
    })
    
    // Lifecycle
    onMounted(() => {
      if (!props.loading && !props.error) {
        createChart()
      }
    })
    
    onBeforeUnmount(() => {
      if (chart.value) {
        chart.value.destroy()
      }
    })
    
    // Manejar tecla ESC para salir de pantalla completa
    const handleKeydown = (event) => {
      if (event.key === 'Escape' && isFullscreen.value) {
        toggleFullscreen()
      }
    }
    
    onMounted(() => {
      document.addEventListener('keydown', handleKeydown)
    })
    
    onBeforeUnmount(() => {
      document.removeEventListener('keydown', handleKeydown)
    })
    
    return {
      canvasRef,
      chart,
      selectedChartType,
      showLegend,
      isFullscreen,
      chartContainerClass,
      updateChartType,
      updateLegend,
      downloadChart,
      toggleFullscreen,
      createChart
    }
  }
}
</script>

<style scoped>
.advanced-chart {
  position: relative;
}

/* Animaciones para pantalla completa */
.fixed {
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
</style>
