<!--
  RegisterView - Vista de registro
  Formulario de registro para nuevos usuarios
-->
<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center py-12">
    <div class="max-w-7xl mx-auto px-4">
      <div class="max-w-md mx-auto">
        <div class="bg-white rounded-2xl shadow-lg p-8">
          <!-- Logo y título -->
          <div class="text-center mb-8">
            <h1 class="text-3xl font-bold text-black mb-2">
              Crear Cuenta
            </h1>
            <p class="text-gray-600">
              Únete a la comunidad Low Barber
            </p>
          </div>

          <!-- Formulario de registro -->
          <form @submit.prevent="register" class="space-y-6">
            <!-- Nombre y Apellido -->
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-black mb-2">
                  Nombre
                </label>
                <input
                  v-model="form.firstName"
                  type="text"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-black focus:border-transparent"
                  placeholder="Tu nombre"
                  :class="{ 'border-red-500': errors.firstName }"
                />
                <p v-if="errors.firstName" class="text-red-500 text-sm mt-1">
                  {{ errors.firstName }}
                </p>
              </div>
              <div>
                <label class="block text-sm font-medium text-black mb-2">
                  Apellido
                </label>
                <input
                  v-model="form.lastName"
                  type="text"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-black focus:border-transparent"
                  placeholder="Tu apellido"
                  :class="{ 'border-red-500': errors.lastName }"
                />
                <p v-if="errors.lastName" class="text-red-500 text-sm mt-1">
                  {{ errors.lastName }}
                </p>
              </div>
            </div>

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

            <!-- Teléfono -->
            <div>
              <label class="block text-sm font-medium text-black mb-2">
                Teléfono
              </label>
              <input
                v-model="form.phone"
                type="tel"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-black focus:border-transparent"
                placeholder="Tu número de teléfono"
                :class="{ 'border-red-500': errors.phone }"
              />
              <p v-if="errors.phone" class="text-red-500 text-sm mt-1">
                {{ errors.phone }}
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

            <!-- Confirmar contraseña -->
            <div>
              <label class="block text-sm font-medium text-black mb-2">
                Confirmar Contraseña
              </label>
              <div class="relative">
                <input
                  v-model="form.confirmPassword"
                  :type="showConfirmPassword ? 'text' : 'password'"
                  required
                  class="w-full px-4 py-3 pr-10 border border-gray-300 rounded-xl focus:ring-2 focus:ring-black focus:border-transparent"
                  placeholder="Confirma tu contraseña"
                  :class="{ 'border-red-500': errors.confirmPassword }"
                />
                <button
                  type="button"
                  @click="showConfirmPassword = !showConfirmPassword"
                  class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-black"
                >
                  <svg v-if="showConfirmPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                  </svg>
                  <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.878 9.878L3 3m6.878 6.878L21 21"/>
                  </svg>
                </button>
              </div>
              <p v-if="errors.confirmPassword" class="text-red-500 text-sm mt-1">
                {{ errors.confirmPassword }}
              </p>
            </div>

            <!-- Términos y condiciones -->
            <div class="flex items-start">
              <input
                v-model="form.acceptTerms"
                type="checkbox"
                id="accept-terms"
                required
                class="w-4 h-4 text-black border-gray-300 rounded focus:ring-black mt-1"
                :class="{ 'border-red-500': errors.acceptTerms }"
              />
              <label for="accept-terms" class="ml-3 text-sm text-gray-600">
                Acepto los 
                <a href="#" class="text-black hover:text-gray-700 font-medium">
                  Términos de Servicio
                </a>
                y la 
                <a href="#" class="text-black hover:text-gray-700 font-medium">
                  Política de Privacidad
                </a>
                de Low Barber
              </label>
            </div>
            <p v-if="errors.acceptTerms" class="text-red-500 text-sm">
              {{ errors.acceptTerms }}
            </p>

            <!-- Newsletter -->
            <div class="flex items-start">
              <input
                v-model="form.newsletter"
                type="checkbox"
                id="newsletter"
                class="w-4 h-4 text-black border-gray-300 rounded focus:ring-black mt-1"
              />
              <label for="newsletter" class="ml-3 text-sm text-gray-600">
                Quiero recibir ofertas especiales y noticias por email
              </label>
            </div>

            <!-- Botón de registro -->
            <button
              type="submit"
              :disabled="isLoading"
              class="w-full bg-black text-white px-6 py-3 rounded-xl font-medium hover:bg-gray-800 transition-all duration-200 disabled:opacity-50"
            >
              {{ isLoading ? 'Creando cuenta...' : 'Crear Cuenta' }}
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
                  ¿Ya tienes cuenta?
                </span>
              </div>
            </div>
          </div>

          <!-- Enlace a login -->
          <div class="text-center">
            <RouterLink
              to="/login"
              class="text-black hover:text-gray-700 font-medium"
            >
              Iniciar sesión
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { authService } from '@/services'

export default {
  name: 'RegisterView',
  data() {
    return {
      showPassword: false,
      showConfirmPassword: false,
      isLoading: false,
      form: {
        firstName: '',
        lastName: '',
        email: '',
        phone: '',
        password: '',
        confirmPassword: '',
        acceptTerms: false,
        newsletter: false
      },
      errors: {}
    }
  },
  methods: {
    async register() {
      // Limpiar errores previos
      this.errors = {}

      // Validar formulario
      if (!this.validateForm()) {
        return
      }

      this.isLoading = true

      try {
        // Crear datos de usuario para el backend
        const userData = {
          nombre: this.form.firstName,
          email: this.form.email,
          telefono: this.form.phone,
          password: this.form.password,
          password_confirmation: this.form.confirmPassword
        }

        console.log('Registrando usuario:', userData)
        
        // Llamar al servicio de registro
        const response = await authService.register(userData)
        
        console.log('Registro exitoso:', response)
        
        // Mostrar mensaje de éxito
        alert('¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.')
        
        // Redirigir al login después del registro exitoso
        this.$router.push('/login')
        
      } catch (error) {
        console.error('Error en registro:', error)
        
        // Manejar errores específicos
        if (error.message.includes('ya existe')) {
          this.errors.email = 'Este email ya está registrado'
        } else if (error.message.includes('validación')) {
          this.errors.general = 'Por favor, verifica que todos los campos sean correctos'
        } else {
          this.errors.general = error.message || 'Error al crear la cuenta. Por favor, inténtalo de nuevo.'
        }
      } finally {
        this.isLoading = false
      }
    },

    validateForm() {
      let isValid = true

      // Validar nombre
      if (!this.form.firstName.trim()) {
        this.errors.firstName = 'El nombre es requerido'
        isValid = false
      }

      // Validar apellido
      if (!this.form.lastName.trim()) {
        this.errors.lastName = 'El apellido es requerido'
        isValid = false
      }

      // Validar email
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if (!emailRegex.test(this.form.email)) {
        this.errors.email = 'Email no válido'
        isValid = false
      }

      // Validar teléfono
      if (!this.form.phone.trim()) {
        this.errors.phone = 'El teléfono es requerido'
        isValid = false
      }

      // Validar contraseña
      if (this.form.password.length < 6) {
        this.errors.password = 'La contraseña debe tener al menos 6 caracteres'
        isValid = false
      }

      // Validar confirmación de contraseña
      if (this.form.password !== this.form.confirmPassword) {
        this.errors.confirmPassword = 'Las contraseñas no coinciden'
        isValid = false
      }

      // Validar términos y condiciones
      if (!this.form.acceptTerms) {
        this.errors.acceptTerms = 'Debes aceptar los términos y condiciones'
        isValid = false
      }

      return isValid
    },

    isValidEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      return emailRegex.test(email)
    }
  },
  mounted() {
    // Cambiar el título de la página
    document.title = 'Registrarse - Low Barber'
  }
}
</script>
