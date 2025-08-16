<!--
  AdminModal.vue - Modal reutilizable para formularios y confirmaciones
  Usado en todas las secciones administrativas para crear, editar y eliminar elementos
-->
<template>
  <Teleport to="body">
    <!-- Overlay del modal -->
    <Transition
      enter-active-class="transition-opacity duration-300"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-opacity duration-300"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="show"
        class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity z-40"
        @click="closeOnOverlay && close()"
      ></div>
    </Transition>

    <!-- Modal -->
    <Transition
      enter-active-class="transition-all duration-300"
      enter-from-class="opacity-0 scale-95 translate-y-4"
      enter-to-class="opacity-100 scale-100 translate-y-0"
      leave-active-class="transition-all duration-300"
      leave-from-class="opacity-100 scale-100 translate-y-0"
      leave-to-class="opacity-0 scale-95 translate-y-4"
    >
      <div
        v-if="show"
        class="fixed inset-0 z-50 overflow-y-auto"
        aria-labelledby="modal-title"
        role="dialog"
        aria-modal="true"
      >
        <div class="flex items-center justify-center min-h-full p-4 text-center sm:p-0">
          <div
            :class="[
              'relative bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all w-full',
              sizeClasses[size]
            ]"
          >
            <!-- Header del modal -->
            <div v-if="showHeader" class="bg-white px-6 py-4 border-b border-gray-200">
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <!-- Icono opcional -->
                  <div v-if="icon" :class="[
                    'flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-full mr-4',
                    iconColorClasses[iconColor]
                  ]">
                    <component :is="icon" class="h-6 w-6" />
                  </div>
                  
                  <!-- Título y descripción -->
                  <div>
                    <h3 id="modal-title" class="text-lg font-medium text-gray-900">
                      {{ title }}
                    </h3>
                    <p v-if="description" class="mt-1 text-sm text-gray-600">
                      {{ description }}
                    </p>
                  </div>
                </div>

                <!-- Botón de cerrar -->
                <button
                  v-if="closable"
                  @click="close()"
                  type="button"
                  class="bg-white rounded-md text-gray-400 hover:text-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                >
                  <span class="sr-only">Cerrar</span>
                  <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>
            </div>

            <!-- Contenido del modal -->
            <div class="bg-white">
              <!-- Contenido por slots -->
              <div v-if="$slots.default" :class="contentPadding">
                <slot></slot>
              </div>

              <!-- Contenido de confirmación -->
              <div v-else-if="type === 'confirm'" class="px-6 py-4">
                <div class="sm:flex sm:items-start">
                  <div v-if="confirmIcon" :class="[
                    'mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full sm:mx-0 sm:h-10 sm:w-10',
                    confirmIconClasses[confirmType]
                  ]">
                    <component :is="confirmIcon" class="h-6 w-6" />
                  </div>
                  <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                    <h3 class="text-lg font-medium text-gray-900">
                      {{ confirmTitle || title }}
                    </h3>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">
                        {{ confirmMessage }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Contenido de alerta -->
              <div v-else-if="type === 'alert'" class="px-6 py-4">
                <div class="flex">
                  <div v-if="alertIcon" :class="[
                    'flex-shrink-0',
                    alertIconClasses[alertType]
                  ]">
                    <component :is="alertIcon" class="h-5 w-5" />
                  </div>
                  <div class="ml-3">
                    <h3 class="text-sm font-medium" :class="alertTitleClasses[alertType]">
                      {{ alertTitle || title }}
                    </h3>
                    <div class="mt-2 text-sm" :class="alertMessageClasses[alertType]">
                      <p>{{ alertMessage }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Footer del modal -->
            <div v-if="showFooter" :class="[
              'bg-gray-50 px-6 py-3 flex',
              footerAlignment[footerAlign]
            ]">
              <!-- Botones personalizados por slot -->
              <slot name="footer">
                <!-- Botones por defecto según el tipo -->
                <template v-if="type === 'confirm'">
                  <button
                    @click="cancel()"
                    type="button"
                    class="w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
                  >
                    {{ cancelText }}
                  </button>
                  <button
                    @click="confirm()"
                    type="button"
                    :disabled="loading"
                    :class="[
                      'w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 text-base font-medium text-white focus:outline-none focus:ring-2 focus:ring-offset-2 sm:ml-3 sm:w-auto sm:text-sm',
                      confirmButtonClasses[confirmType],
                      loading ? 'opacity-75 cursor-not-allowed' : ''
                    ]"
                  >
                    <svg v-if="loading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    {{ confirmText }}
                  </button>
                </template>

                <template v-else-if="type === 'alert'">
                  <button
                    @click="close()"
                    type="button"
                    class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:w-auto sm:text-sm"
                  >
                    {{ okText }}
                  </button>
                </template>

                <template v-else>
                  <!-- Botones por defecto para formularios -->
                  <button
                    v-if="showCancel"
                    @click="cancel()"
                    type="button"
                    class="w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:mt-0 sm:w-auto sm:text-sm"
                  >
                    {{ cancelText }}
                  </button>
                  <button
                    @click="save()"
                    type="button"
                    :disabled="loading || saveDisabled"
                    class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    <svg v-if="loading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    {{ saveText }}
                  </button>
                </template>
              </slot>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script>
import { computed, watch, nextTick } from 'vue'

export default {
  name: 'AdminModal',
  props: {
    // Control del modal
    show: {
      type: Boolean,
      default: false
    },
    closable: {
      type: Boolean,
      default: true
    },
    closeOnOverlay: {
      type: Boolean,
      default: true
    },
    
    // Apariencia
    size: {
      type: String,
      default: 'md',
      validator: (value) => ['xs', 'sm', 'md', 'lg', 'xl', '2xl', 'full'].includes(value)
    },
    
    // Header
    showHeader: {
      type: Boolean,
      default: true
    },
    title: {
      type: String,
      default: ''
    },
    description: {
      type: String,
      default: ''
    },
    icon: {
      type: [String, Object],
      default: null
    },
    iconColor: {
      type: String,
      default: 'blue',
      validator: (value) => ['blue', 'green', 'yellow', 'red', 'gray'].includes(value)
    },
    
    // Contenido
    type: {
      type: String,
      default: 'default',
      validator: (value) => ['default', 'confirm', 'alert'].includes(value)
    },
    contentPadding: {
      type: String,
      default: 'px-6 py-4'
    },
    
    // Footer
    showFooter: {
      type: Boolean,
      default: true
    },
    showActions: {
      type: Boolean,
      default: true
    },
    footerAlign: {
      type: String,
      default: 'right',
      validator: (value) => ['left', 'center', 'right', 'between'].includes(value)
    },
    showCancel: {
      type: Boolean,
      default: true
    },
    
    // Estados
    loading: {
      type: Boolean,
      default: false
    },
    saveDisabled: {
      type: Boolean,
      default: false
    },
    
    // Textos de botones
    saveText: {
      type: String,
      default: 'Guardar'
    },
    cancelText: {
      type: String,
      default: 'Cancelar'
    },
    confirmText: {
      type: String,
      default: 'Confirmar'
    },
    okText: {
      type: String,
      default: 'Entendido'
    },
    
    // Props para tipo 'confirm'
    confirmType: {
      type: String,
      default: 'warning',
      validator: (value) => ['warning', 'danger', 'info'].includes(value)
    },
    confirmTitle: {
      type: String,
      default: ''
    },
    confirmMessage: {
      type: String,
      default: ''
    },
    confirmIcon: {
      type: [String, Object],
      default: null
    },
    
    // Props para tipo 'alert'
    alertType: {
      type: String,
      default: 'info',
      validator: (value) => ['success', 'warning', 'error', 'info'].includes(value)
    },
    alertTitle: {
      type: String,
      default: ''
    },
    alertMessage: {
      type: String,
      default: ''
    },
    alertIcon: {
      type: [String, Object],
      default: null
    }
  },
  emits: ['close', 'save', 'confirm', 'cancel'],
  setup(props, { emit }) {
    // Clases reactivas
    const sizeClasses = {
      xs: 'sm:max-w-xs',
      sm: 'sm:max-w-sm',
      md: 'sm:max-w-md',
      lg: 'sm:max-w-lg',
      xl: 'sm:max-w-xl',
      '2xl': 'sm:max-w-2xl',
      full: 'sm:max-w-full sm:m-4'
    }

    const iconColorClasses = {
      blue: 'bg-blue-100 text-blue-600',
      green: 'bg-green-100 text-green-600',
      yellow: 'bg-yellow-100 text-yellow-600',
      red: 'bg-red-100 text-red-600',
      gray: 'bg-gray-100 text-gray-600'
    }

    const footerAlignment = {
      left: 'justify-start',
      center: 'justify-center',
      right: 'justify-end',
      between: 'justify-between'
    }

    const confirmIconClasses = {
      warning: 'bg-yellow-100 text-yellow-600',
      danger: 'bg-red-100 text-red-600',
      info: 'bg-blue-100 text-blue-600'
    }

    const confirmButtonClasses = {
      warning: 'bg-yellow-600 hover:bg-yellow-700 focus:ring-yellow-500',
      danger: 'bg-red-600 hover:bg-red-700 focus:ring-red-500',
      info: 'bg-blue-600 hover:bg-blue-700 focus:ring-blue-500'
    }

    const alertIconClasses = {
      success: 'text-green-400',
      warning: 'text-yellow-400',
      error: 'text-red-400',
      info: 'text-blue-400'
    }

    const alertTitleClasses = {
      success: 'text-green-800',
      warning: 'text-yellow-800',
      error: 'text-red-800',
      info: 'text-blue-800'
    }

    const alertMessageClasses = {
      success: 'text-green-700',
      warning: 'text-yellow-700',
      error: 'text-red-700',
      info: 'text-blue-700'
    }

    // Métodos
    const close = () => {
      emit('close')
    }

    const save = () => {
      emit('save')
    }

    const confirm = () => {
      emit('confirm')
    }

    const cancel = () => {
      emit('cancel')
    }

    // Manejo de teclas
    const handleKeydown = (event) => {
      if (event.key === 'Escape' && props.closable) {
        close()
      }
    }

    // Watchers
    watch(() => props.show, (newValue) => {
      if (newValue) {
        nextTick(() => {
          document.addEventListener('keydown', handleKeydown)
          document.body.style.overflow = 'hidden'
        })
      } else {
        document.removeEventListener('keydown', handleKeydown)
        document.body.style.overflow = ''
      }
    })

    return {
      sizeClasses,
      iconColorClasses,
      footerAlignment,
      confirmIconClasses,
      confirmButtonClasses,
      alertIconClasses,
      alertTitleClasses,
      alertMessageClasses,
      close,
      save,
      confirm,
      cancel
    }
  }
}
</script>

<style scoped>
/* Asegurar que el modal esté por encima de todo */
.modal-overlay {
  z-index: 9998;
}

.modal-container {
  z-index: 9999;
}
</style>
