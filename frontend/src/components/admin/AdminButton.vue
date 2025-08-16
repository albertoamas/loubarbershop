<!--
  AdminButton.vue - Componente de botón reutilizable con múltiples variantes
  Usado en toda la interfaz administrativa para mantener consistencia visual
-->
<template>
  <component
    :is="tag"
    :to="to"
    :href="href"
    :target="target"
    :disabled="disabled || loading"
    :class="buttonClasses"
    @click="handleClick"
  >
    <!-- Spinner de carga -->
    <svg
      v-if="loading"
      class="animate-spin -ml-1 mr-3 h-5 w-5"
      fill="none"
      viewBox="0 0 24 24"
    >
      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
    </svg>

    <!-- Icono izquierdo -->
    <i
      v-if="leftIcon && !loading && (leftIcon.startsWith('fas') || leftIcon.startsWith('far'))"
      :class="[leftIcon, iconSizeClasses[size]]"
      class="mr-2"
    ></i>
    <span
      v-else-if="leftIcon && !loading"
      :class="iconSizeClasses[size]"
      class="mr-2"
    >{{ leftIcon }}</span>

    <!-- Contenido del botón -->
    <span v-if="$slots.default || text">
      <slot>{{ text }}</slot>
    </span>

    <!-- Icono derecho -->
    <i
      v-if="rightIcon && (rightIcon.startsWith('fas') || rightIcon.startsWith('far'))"
      :class="[rightIcon, iconSizeClasses[size]]"
      class="ml-2"
    ></i>
    <span
      v-else-if="rightIcon"
      :class="iconSizeClasses[size]"
      class="ml-2"
    >{{ rightIcon }}</span>

    <!-- Badge/contador -->
    <span
      v-if="badge"
      class="ml-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-white/20 text-current"
    >
      {{ badge }}
    </span>
  </component>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'AdminButton',
  props: {
    // Contenido
    text: {
      type: String,
      default: ''
    },
    
    // Tipo de elemento
    tag: {
      type: String,
      default: 'button',
      validator: (value) => ['button', 'router-link', 'a'].includes(value)
    },
    
    // Props para enlaces
    to: {
      type: [String, Object],
      default: null
    },
    href: {
      type: String,
      default: null
    },
    target: {
      type: String,
      default: null
    },
    
    // Variantes de estilo
    variant: {
      type: String,
      default: 'primary',
      validator: (value) => [
        'primary', 'secondary', 'success', 'warning', 'danger', 'info',
        'outline-primary', 'outline-secondary', 'outline-success', 'outline-warning', 
        'outline-danger', 'outline-info', 'ghost', 'link'
      ].includes(value)
    },
    
    // Tamaños
    size: {
      type: String,
      default: 'md',
      validator: (value) => ['xs', 'sm', 'md', 'lg', 'xl'].includes(value)
    },
    
    // Estados
    disabled: {
      type: Boolean,
      default: false
    },
    loading: {
      type: Boolean,
      default: false
    },
    active: {
      type: Boolean,
      default: false
    },
    
    // Forma
    rounded: {
      type: String,
      default: 'md',
      validator: (value) => ['none', 'sm', 'md', 'lg', 'full'].includes(value)
    },
    
    // Iconos
    leftIcon: {
      type: [String, Object],
      default: null
    },
    rightIcon: {
      type: [String, Object],
      default: null
    },
    
    // Extras
    badge: {
      type: [String, Number],
      default: null
    },
    
    // Ancho completo
    fullWidth: {
      type: Boolean,
      default: false
    },
    
    // Sombra
    shadow: {
      type: String,
      default: 'sm',
      validator: (value) => ['none', 'sm', 'md', 'lg', 'xl'].includes(value)
    }
  },
  emits: ['click'],
  setup(props, { emit }) {
    // Clases base
    const baseClasses = 'inline-flex items-center justify-center font-medium transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2'
    
    // Clases de tamaño
    const sizeClasses = {
      xs: 'px-2.5 py-1.5 text-xs',
      sm: 'px-3 py-2 text-sm',
      md: 'px-4 py-2 text-sm',
      lg: 'px-4 py-2 text-base',
      xl: 'px-6 py-3 text-base'
    }
    
    // Clases de forma redondeada
    const roundedClasses = {
      none: 'rounded-none',
      sm: 'rounded-sm',
      md: 'rounded-md',
      lg: 'rounded-lg',
      full: 'rounded-full'
    }
    
    // Clases de sombra
    const shadowClasses = {
      none: '',
      sm: 'shadow-sm',
      md: 'shadow',
      lg: 'shadow-lg',
      xl: 'shadow-xl'
    }
    
    // Clases de tamaño de iconos
    const iconSizeClasses = {
      xs: 'h-3 w-3',
      sm: 'h-4 w-4',
      md: 'h-4 w-4',
      lg: 'h-5 w-5',
      xl: 'h-5 w-5'
    }
    
    // Clases de variantes
    const variantClasses = {
      // Variantes sólidas
      primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500 active:bg-blue-800',
      secondary: 'bg-gray-600 text-white hover:bg-gray-700 focus:ring-gray-500 active:bg-gray-800',
      success: 'bg-green-600 text-white hover:bg-green-700 focus:ring-green-500 active:bg-green-800',
      warning: 'bg-yellow-600 text-white hover:bg-yellow-700 focus:ring-yellow-500 active:bg-yellow-800',
      danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500 active:bg-red-800',
      info: 'bg-indigo-600 text-white hover:bg-indigo-700 focus:ring-indigo-500 active:bg-indigo-800',
      
      // Variantes outline
      'outline-primary': 'border border-blue-600 text-blue-600 hover:bg-blue-50 focus:ring-blue-500 active:bg-blue-100',
      'outline-secondary': 'border border-gray-600 text-gray-600 hover:bg-gray-50 focus:ring-gray-500 active:bg-gray-100',
      'outline-success': 'border border-green-600 text-green-600 hover:bg-green-50 focus:ring-green-500 active:bg-green-100',
      'outline-warning': 'border border-yellow-600 text-yellow-600 hover:bg-yellow-50 focus:ring-yellow-500 active:bg-yellow-100',
      'outline-danger': 'border border-red-600 text-red-600 hover:bg-red-50 focus:ring-red-500 active:bg-red-100',
      'outline-info': 'border border-indigo-600 text-indigo-600 hover:bg-indigo-50 focus:ring-indigo-500 active:bg-indigo-100',
      
      // Variantes especiales
      ghost: 'text-gray-700 hover:bg-gray-100 focus:ring-gray-500 active:bg-gray-200',
      link: 'text-blue-600 hover:text-blue-800 focus:ring-blue-500 underline-offset-4 hover:underline'
    }
    
    // Estado deshabilitado
    const disabledClasses = 'disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none'
    
    // Estado activo
    const activeClasses = computed(() => {
      if (!props.active) return ''
      
      const baseActive = 'ring-2 ring-offset-2'
      
      if (props.variant.startsWith('outline-') || props.variant === 'ghost') {
        return `${baseActive} ring-blue-500 bg-blue-50`
      }
      
      return `${baseActive} ring-blue-300`
    })
    
    // Clases finales del botón
    const buttonClasses = computed(() => {
      const classes = [
        baseClasses,
        sizeClasses[props.size],
        roundedClasses[props.rounded],
        shadowClasses[props.shadow],
        variantClasses[props.variant],
        disabledClasses
      ]
      
      if (props.fullWidth) {
        classes.push('w-full')
      }
      
      if (props.active) {
        classes.push(activeClasses.value)
      }
      
      if (props.loading) {
        classes.push('cursor-wait')
      }
      
      return classes.filter(Boolean).join(' ')
    })
    
    // Manejo de clicks
    const handleClick = (event) => {
      if (!props.disabled && !props.loading) {
        emit('click', event)
      }
    }
    
    return {
      buttonClasses,
      iconSizeClasses,
      handleClick
    }
  }
}
</script>

<style scoped>
/* Estilos adicionales si son necesarios */
.admin-button {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Animación suave para el estado hover */
.admin-button:hover {
  transform: translateY(-1px);
}

.admin-button:active {
  transform: translateY(0);
}

/* Estados especiales para variantes outline */
.admin-button.outline:hover {
  transform: none;
}
</style>
