<!--
  LoginView - Vista de inicio de sesión
  Formulario de login para usuarios
-->
<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center py-12">
    <div class="max-w-7xl mx-auto px-4">
      <div class="max-w-md mx-auto">
        <div class="bg-white rounded-2xl shadow-lg p-8">
          <!-- Logo y título -->
          <div class="text-center mb-8">
            <h1 class="text-3xl font-bold text-black mb-2">
              Iniciar Sesión
            </h1>
            <p class="text-gray-600">
              Accede a tu cuenta de Low Barber
            </p>
          </div>

          <!-- Formulario de login -->
          <form @submit.prevent="login" class="space-y-6">
            <!-- Email -->
            <div>
              <label class="block text-sm font-medium text-black mb-2">
                Email
              </label>
              <input
                v-model="form.email"
                type="email"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-black focus:border-transparent"
                placeholder="tu@email.com"
                :class="{ 'border-red-500': errors.email }"
              />
              <p v-if="errors.email" class="text-red-500 text-sm mt-1">
                {{ errors.email }}
              </p>
            </div>

            <!-- Contraseña -->
            <div>
              <label class="block text-sm font-medium text-black mb-2">
                Contraseña
              </label>
              <div class="relative">
                <input
                  v-model="form.password"
                  :type="showPassword ? 'text' : 'password'"
                  required
                  class="w-full px-4 py-3 pr-10 border border-gray-300 rounded-xl focus:ring-2 focus:ring-black focus:border-transparent"
                  placeholder="Tu contraseña"
                  :class="{ 'border-red-500': errors.password }"
                />
                <button
                  type="button"
                  @click="showPassword = !showPassword"
                  class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-black"
                >
                  <svg v-if="showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                  </svg>
                  <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.878 9.878L3 3m6.878 6.878L21 21"/>
                  </svg>
                </button>
              </div>
              <p v-if="errors.password" class="text-red-500 text-sm mt-1">
                {{ errors.password }}
              </p>
            </div>

            <!-- Recordarme -->
            <div class="flex items-center justify-between">
              <div class="flex items-center">
                <input
                  v-model="form.remember"
                  type="checkbox"
                  id="remember"
                  class="w-4 h-4 text-black border-gray-300 rounded focus:ring-black"
                />
                <label for="remember" class="ml-2 text-sm text-gray-600">
                  Recordarme
                </label>
              </div>
              <a href="#" class="text-sm text-black hover:text-gray-700">
                ¿Olvidaste tu contraseña?
              </a>
            </div>

            <!-- Botón de login -->
            <button
              type="submit"
              :disabled="isLoading"
              class="w-full bg-black text-white px-6 py-3 rounded-xl font-medium hover:bg-gray-800 transition-all duration-200 disabled:opacity-50"
            >
              {{ isLoading ? 'Iniciando sesión...' : 'Iniciar Sesión' }}
            </button>

            <!-- Mensaje de error general -->
            <div v-if="errors.general" class="bg-red-50 border border-red-200 rounded-xl p-4">
              <p class="text-red-700 text-sm">
                {{ errors.general }}
              </p>
            </div>
          </form>

          <!-- Separador -->
          <div class="my-6">
            <div class="relative">
              <div class="absolute inset-0 flex items-center">
                <div class="w-full border-t border-gray-300"></div>
              </div>
              <div class="relative flex justify-center text-sm">
                <span class="bg-white px-2 text-gray-500">
                  ¿No tienes cuenta?
                </span>
              </div>
            </div>
          </div>

          <!-- Enlace a registro -->
          <div class="text-center">
            <RouterLink
              to="/register"
              class="text-black hover:text-gray-700 font-medium"
            >
              Crear una cuenta nueva
            </RouterLink>
          </div>
        </div>

        <!-- Información adicional -->
        <div class="mt-8 text-center text-sm text-gray-600">
          <p>
            Al iniciar sesión, aceptas nuestros 
            <a href="#" class="text-black hover:text-gray-700">
              Términos de Servicio
            </a>
            y 
            <a href="#" class="text-black hover:text-gray-700">
              Política de Privacidad
            </a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { authService } from '@/services'

export default {
  name: 'LoginView',
  data() {
    return {
      isLoading: false,
      showPassword: false,
      form: {
        email: '',
        password: '',
        remember: false
      },
      errors: {}
    }
  },
  methods: {
    async login() {
      this.isLoading = true
      this.errors = {}

      try {
        // Validación básica
        if (!this.form.email) {
          this.errors.email = 'El email es requerido'
        } else if (!this.isValidEmail(this.form.email)) {
          this.errors.email = 'El email no es válido'
        }

        if (!this.form.password) {
          this.errors.password = 'La contraseña es requerida'
        } else if (this.form.password.length < 6) {
          this.errors.password = 'La contraseña debe tener al menos 6 caracteres'
        }

        if (Object.keys(this.errors).length > 0) {
          this.isLoading = false
          return
        }

        // Autenticación con el backend
        const response = await authService.login({
          email: this.form.email,
          password: this.form.password
        })
        
        console.log('Login exitoso:', response)
        
        // Mostrar mensaje de éxito
        alert('¡Bienvenido de vuelta!')
        
        // Emitir evento personalizado para notificar el login
        window.dispatchEvent(new Event('authStateChanged'))
        
        // Redirigir a la página principal
        this.$router.push('/')

      } catch (error) {
        console.error('Error en login:', error)
        
        // Manejar diferentes tipos de errores
        if (error.message.includes('credenciales')) {
          this.errors.general = 'Email o contraseña incorrectos'
        } else if (error.message.includes('servidor')) {
          this.errors.general = 'Error del servidor. Por favor, intenta más tarde.'
        } else {
          this.errors.general = error.message || 'Hubo un error al iniciar sesión. Por favor, intenta nuevamente.'
        }
      } finally {
        this.isLoading = false
      }
    },
    isValidEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      return emailRegex.test(email)
    }
  }
}
</script>
