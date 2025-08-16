<!--
  AdminCard.vue - Componente reutilizable para tarjetas de estadísticas
  Usado en dashboards y paneles de información
-->
<template>
  <div class="admin-card bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow duration-200">
    <!-- Header opcional -->
    <div v-if="title || $slots.header" class="px-6 py-4 border-b border-gray-200 bg-gray-50">
      <slot name="header">
        <div class="flex items-center justify-between">
          <h3 class="text-lg font-medium text-gray-900">{{ title }}</h3>
          <slot name="actions"></slot>
        </div>
      </slot>
    </div>

    <!-- Contenido principal -->
    <div class="px-6 py-4">
      <!-- Slot para ícono y valor principal -->
      <div class="flex items-center">
        <div v-if="icon" class="flex-shrink-0 mr-4">
          <div :class="iconBgClass" class="w-12 h-12 rounded-lg flex items-center justify-center">
            <i v-if="icon.startsWith('fas') || icon.startsWith('far')" :class="[icon, iconColorClass]" class="w-6 h-6"></i>
            <span v-else class="text-2xl">{{ icon }}</span>
          </div>
        </div>
        
        <div class="flex-1">
          <!-- Valor principal -->
          <div v-if="value !== undefined" class="text-2xl font-bold text-gray-900">
            {{ formattedValue }}
          </div>
          
          <!-- Título si no hay header -->
          <div v-if="!title && label" class="text-sm font-medium text-gray-600 mt-1">
            {{ label }}
          </div>
          
          <!-- Contenido personalizado -->
          <slot></slot>
        </div>
      </div>

      <!-- Cambio/tendencia -->
      <div v-if="change !== undefined" class="mt-4 flex items-center">
        <div :class="changeColorClass" class="flex items-center text-sm font-medium">
          <svg v-if="change > 0" class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M5.293 9.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L10 6.414 6.707 9.707a1 1 0 01-1.414 0z" clip-rule="evenodd" />
          </svg>
          <svg v-else-if="change < 0" class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M14.707 10.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L10 13.586l3.293-3.293a1 1 0 011.414 0z" clip-rule="evenodd" />
          </svg>
          <span>{{ Math.abs(change) }}%</span>
        </div>
        <span class="text-sm text-gray-600 ml-2">{{ changeLabel }}</span>
      </div>

      <!-- Footer opcional -->
      <div v-if="$slots.footer" class="mt-4 pt-4 border-t border-gray-200">
        <slot name="footer"></slot>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'AdminCard',
  props: {
    title: {
      type: String,
      default: ''
    },
    label: {
      type: String,
      default: ''
    },
    value: {
      type: [String, Number],
      default: undefined
    },
    change: {
      type: Number,
      default: undefined
    },
    changeLabel: {
      type: String,
      default: 'vs mes anterior'
    },
    icon: {
      type: [String, Object],
      default: null
    },
    iconColor: {
      type: String,
      default: 'blue',
      validator: (value) => ['blue', 'green', 'red', 'yellow', 'orange', 'purple', 'indigo'].includes(value)
    },
    color: {
      type: String,
      default: null,
      validator: (value) => !value || ['blue', 'green', 'red', 'yellow', 'orange', 'purple', 'indigo'].includes(value)
    },
    format: {
      type: String,
      default: 'number',
      validator: (value) => ['number', 'currency', 'percentage'].includes(value)
    },
    loading: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    // Formatear el valor según el tipo
    const formattedValue = computed(() => {
      if (props.loading) return '...'
      if (props.value === undefined || props.value === null) return '--'
      
      switch (props.format) {
        case 'currency':
          return new Intl.NumberFormat('es-ES', {
            style: 'currency',
            currency: 'EUR'
          }).format(props.value)
        case 'percentage':
          return `${props.value}%`
        case 'number':
        default:
          return new Intl.NumberFormat('es-ES').format(props.value)
      }
    })

    // Clases para el color del ícono
    const iconColorClass = computed(() => {
      const colorToUse = props.color || props.iconColor
      const colors = {
        blue: 'text-blue-600',
        green: 'text-green-600',
        red: 'text-red-600',
        yellow: 'text-yellow-600',
        orange: 'text-orange-600',
        purple: 'text-purple-600',
        indigo: 'text-indigo-600'
      }
      return colors[colorToUse] || colors.blue
    })

    const iconBgClass = computed(() => {
      const colorToUse = props.color || props.iconColor
      const colors = {
        blue: 'bg-blue-100',
        green: 'bg-green-100',
        red: 'bg-red-100',
        yellow: 'bg-yellow-100',
        orange: 'bg-orange-100',
        purple: 'bg-purple-100',
        indigo: 'bg-indigo-100'
      }
      return colors[colorToUse] || colors.blue
    })

    // Clases para el color del cambio
    const changeColorClass = computed(() => {
      if (props.change === undefined) return ''
      if (props.change > 0) return 'text-green-600'
      if (props.change < 0) return 'text-red-600'
      return 'text-gray-600'
    })

    return {
      formattedValue,
      iconColorClass,
      iconBgClass,
      changeColorClass
    }
  }
}
</script>

<style scoped>
.admin-card {
  transition: all 0.2s ease-in-out;
}

.admin-card:hover {
  transform: translateY(-1px);
}
</style>
