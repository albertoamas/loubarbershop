<!--
  LoginForm.vue - Formulario de login real
  Componente simple para autenticación
-->
<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50" v-if="isOpen">
    <div class="bg-white rounded-lg p-8 max-w-md w-full mx-4">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-gray-900">Iniciar Sesión</h2>
        <button @click="close" class="text-gray-400 hover:text-gray-600">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-4">
        <!-- Email -->
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700 mb-1">
            Email
          </label>
          <input
            type="email"
            id="email"
            v-model="form.email"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="tu@email.com"
          />
        </div>

        <!-- Password -->
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700 mb-1">
            Contraseña
          </label>
          <input
            type="password"
            id="password"
            v-model="form.password"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="••••••••"
          />
        </div>

        <!-- Error message -->
        <div v-if="error" class="text-red-600 text-sm bg-red-50 p-3 rounded-md">
          {{ error }}
        </div>

        <!-- Success message -->
        <div v-if="success" class="text-green-600 text-sm bg-green-50 p-3 rounded-md">
          {{ success }}
        </div>

        <!-- Buttons -->
        <div class="flex space-x-3 pt-4">
          <button
            type="submit"
            :disabled="loading"
            class="flex-1 bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="loading">Iniciando...</span>
            <span v-else>Iniciar Sesión</span>
          </button>
          <button
            type="button"
            @click="close"
            class="flex-1 bg-gray-200 text-gray-800 py-2 px-4 rounded-md hover:bg-gray-300"
          >
            Cancelar
          </button>
        </div>
      </form>

      <!-- Quick admin login -->
      <div class="mt-6 pt-6 border-t border-gray-200">
        <p class="text-sm text-gray-600 mb-3">Acceso rápido para desarrollo:</p>
        <button
          @click="quickAdminLogin"
          type="button"
          class="w-full bg-green-600 text-white py-2 px-4 rounded-md hover:bg-green-700 text-sm"
        >
          🔧 Login como Admin (Desarrollo)
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { authService } from '@/services/authService.js'

export default {
  name: 'LoginForm',
  props: {
    isOpen: {
      type: Boolean,
      default: false
    }
  },
  emits: ['close', 'login-success'],
  data() {
    return {
      form: {
        email: '',
        password: ''
      },
      loading: false,
      error: '',
      success: ''
    }
  },
  methods: {
    close() {
      this.form = { email: '', password: '' }
      this.error = ''
      this.success = ''
      this.$emit('close')
    },
    
    async handleLogin() {
      this.loading = true
      this.error = ''
      this.success = ''
      
      try {
        const response = await authService.login(this.form)
        this.success = '¡Login exitoso!'
        
        // Emitir evento de success
        this.$emit('login-success', response)
        
        // Emitir evento global para actualizar navbar
        window.dispatchEvent(new Event('authStateChanged'))
        
        // Cerrar modal después de 1 segundo
        setTimeout(() => {
          this.close()
        }, 1000)
        
      } catch (error) {
        this.error = error.message || 'Error al iniciar sesión'
      } finally {
        this.loading = false
      }
    },
    
    async quickAdminLogin() {
      this.loading = true
      this.error = ''
      this.success = ''
      
      try {
        await authService.loginAsAdmin()
        this.success = '¡Admin login exitoso!'
        
        // Emitir evento global para actualizar navbar
        window.dispatchEvent(new Event('authStateChanged'))
        
        // Cerrar modal después de 1 segundo
        setTimeout(() => {
          this.close()
        }, 1000)
        
      } catch (error) {
        this.error = 'Error en admin login: ' + error.message
      } finally {
        this.loading = false
      }
    }
  }
}
</script>
