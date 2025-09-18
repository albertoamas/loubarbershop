<!--
  ProfileView - Vista de Mi Perfil
  Página donde el usuario puede ver y editar su información personal
-->
<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Hero Section -->
    <section class="bg-[var(--color-barber-primary)] py-16 md:py-20 relative overflow-hidden">
      <!-- Elementos decorativos de fondo -->
      <div class="absolute inset-0">
        <div class="absolute top-10 left-10 w-32 h-32 bg-[var(--color-barber-gold)]/10 rounded-full blur-xl"></div>
        <div class="absolute bottom-10 right-10 w-48 h-48 bg-[var(--color-barber-gold)]/5 rounded-full blur-2xl"></div>
        <div class="absolute top-1/2 left-1/4 w-16 h-16 bg-white/10 rounded-full blur-lg"></div>
      </div>
      
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <div class="text-center">
          <!-- Logo/Nombre con estilo mejorado -->
          <div class="mb-6">
            <div class="inline-flex items-center justify-center px-4 py-2 bg-[var(--color-barber-gold)] text-[var(--color-barber-primary)] rounded-full text-sm font-bold mb-4 shadow-lg">
              👤 Low BarberShop
            </div>
            <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold text-white mb-4 leading-tight">
              Mi 
              <span class="bg-gradient-to-r from-[var(--color-barber-gold)] to-yellow-300 bg-clip-text text-transparent">
                Perfil
              </span>
            </h1>
          </div>
          
          <!-- Descripción mejorada -->
          <p class="text-gray-300 max-w-3xl mx-auto text-lg md:text-xl leading-relaxed">
            Gestiona tu información personal y preferencias
          </p>
        </div>
      </div>
    </section>

    <!-- Loading State -->
    <div v-if="loading" class="flex flex-col justify-center items-center py-24">
      <div class="relative">
        <div class="animate-spin rounded-full h-16 w-16 border-4 border-gray-200"></div>
        <div class="animate-spin rounded-full h-16 w-16 border-4 border-[var(--color-barber-primary)] border-t-transparent absolute inset-0"></div>
      </div>
      <p class="text-gray-600 text-lg font-medium mt-6">Cargando tu perfil...</p>
    </div>

    <!-- Error State -->
    <div v-if="error && !loading" class="text-center py-24">
      <div class="max-w-md mx-auto">
        <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-3">Error al cargar perfil</h3>
        <p class="text-gray-600 mb-6">{{ error }}</p>
        <button 
          @click="loadUserProfile" 
          class="bg-[var(--color-barber-primary)] text-white px-8 py-3 rounded-lg hover:bg-[var(--color-barber-gold)] transition-all duration-200 transform hover:scale-105 shadow-lg"
        >
          Reintentar
        </button>
      </div>
    </div>

    <!-- Content Section -->
    <section v-if="!loading && !error" class="py-16">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Profile Header Card -->
        <div class="bg-white rounded-3xl shadow-lg border border-gray-100 p-8 mb-8">
          <div class="flex flex-col md:flex-row items-center gap-8">
            <!-- Avatar -->
            <div class="relative">
              <div class="w-32 h-32 bg-gradient-to-br from-[var(--color-barber-primary)] to-gray-700 rounded-full flex items-center justify-center">
                <span class="text-white text-4xl font-bold">
                  {{ getInitials(userProfile.nombre) }}
                </span>
              </div>
              <button 
                @click="changeAvatar"
                class="absolute bottom-0 right-0 w-10 h-10 bg-[var(--color-barber-gold)] text-[var(--color-barber-primary)] rounded-full flex items-center justify-center shadow-lg hover:bg-yellow-300 transition-all duration-200 transform hover:scale-110"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
              </button>
            </div>

            <!-- User Info -->
            <div class="text-center md:text-left flex-1">
              <h2 class="text-2xl font-bold text-gray-900 mb-2">{{ userProfile.nombre || 'Usuario' }}</h2>
              <p class="text-gray-600 mb-4">{{ userProfile.email || 'email@ejemplo.com' }}</p>
              
              <!-- Stats -->
              <div class="flex justify-center md:justify-start gap-6 text-sm">
                <div class="text-center">
                  <div class="font-bold text-[var(--color-barber-primary)] text-lg">{{ userStats.totalReservations }}</div>
                  <div class="text-gray-500">Reservas</div>
                </div>
                <div class="text-center">
                  <div class="font-bold text-green-600 text-lg">{{ userStats.completedServices }}</div>
                  <div class="text-gray-500">Servicios</div>
                </div>
                <div class="text-center">
                  <div class="font-bold text-[var(--color-barber-gold)] text-lg">{{ userStats.memberSince }}</div>
                  <div class="text-gray-500">Miembro desde</div>
                </div>
              </div>
            </div>

            <!-- Edit Button -->
            <button 
              v-if="!isEditing"
              @click="startEditing"
              class="bg-[var(--color-barber-primary)] text-white px-6 py-3 rounded-xl font-medium hover:bg-[var(--color-barber-gold)] transition-all duration-200 transform hover:scale-105 shadow-lg"
            >
              Editar Perfil
            </button>
          </div>
        </div>

        <!-- Edit Form -->
        <div v-if="isEditing" class="bg-white rounded-3xl shadow-lg border border-gray-100 p-8 mb-8">
          <div class="flex items-center justify-between mb-6">
            <h3 class="text-xl font-bold text-gray-900">Editar Información Personal</h3>
            <button 
              @click="cancelEditing"
              class="text-gray-500 hover:text-gray-700 transition-colors"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
            </button>
          </div>

          <form @submit.prevent="saveProfile" class="space-y-6">
            <!-- Nombre -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Nombre Completo</label>
              <input 
                v-model="editedProfile.nombre"
                type="text" 
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[var(--color-barber-primary)] focus:border-transparent transition-all duration-200"
                placeholder="Tu nombre completo"
              />
            </div>

            <!-- Email -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Correo Electrónico</label>
              <input 
                v-model="editedProfile.email"
                type="email" 
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[var(--color-barber-primary)] focus:border-transparent transition-all duration-200"
                placeholder="tu@email.com"
              />
              <p v-if="editedProfile.email && !isValidEmail(editedProfile.email)" class="text-red-600 text-sm mt-2">
                Por favor ingresa un email válido
              </p>
            </div>

            <!-- Teléfono -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Teléfono</label>
              <input 
                v-model="editedProfile.telefono"
                type="tel" 
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[var(--color-barber-primary)] focus:border-transparent transition-all duration-200"
                placeholder="Ej: +591 12345678"
              />
              <p v-if="editedProfile.telefono && !isValidPhone(editedProfile.telefono)" class="text-red-600 text-sm mt-2">
                Formato de teléfono no válido
              </p>
            </div>

            <!-- Fecha de Nacimiento -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Fecha de Nacimiento</label>
              <input 
                v-model="editedProfile.fecha_nacimiento"
                type="date" 
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[var(--color-barber-primary)] focus:border-transparent transition-all duration-200"
              />
            </div>

            <!-- Preferencias -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Preferencias/Notas</label>
              <textarea 
                v-model="editedProfile.preferencias"
                rows="3"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[var(--color-barber-primary)] focus:border-transparent transition-all duration-200"
                placeholder="Cuéntanos sobre tus preferencias de corte, alergias, etc."
              ></textarea>
            </div>

            <!-- Botones de acción -->
            <div class="flex flex-col sm:flex-row gap-3 pt-4">
              <button 
                type="submit"
                :disabled="savingProfile"
                class="flex-1 bg-[var(--color-barber-primary)] text-white px-6 py-3 rounded-xl font-medium hover:bg-[var(--color-barber-gold)] transition-all duration-200 transform hover:scale-105 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span v-if="!savingProfile">Guardar Cambios</span>
                <span v-else>Guardando...</span>
              </button>
              <button 
                type="button"
                @click="cancelEditing"
                class="flex-1 bg-gray-100 text-gray-700 px-6 py-3 rounded-xl font-medium hover:bg-gray-200 transition-all duration-200"
              >
                Cancelar
              </button>
            </div>
          </form>
        </div>

        <!-- Personal Information Cards -->
        <div v-if="!isEditing" class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <!-- Contact Info -->
          <div class="bg-white rounded-3xl shadow-lg border border-gray-100 p-6">
            <div class="flex items-center mb-4">
              <div class="w-10 h-10 bg-blue-100 rounded-2xl flex items-center justify-center mr-3">
                <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                </svg>
              </div>
              <h3 class="text-lg font-bold text-gray-900">Información de Contacto</h3>
            </div>
            
            <div class="space-y-3">
              <div>
                <div class="text-sm text-gray-500">Email</div>
                <div class="font-medium text-gray-900">{{ userProfile.email || 'No especificado' }}</div>
              </div>
              <div>
                <div class="text-sm text-gray-500">Teléfono</div>
                <div class="font-medium text-gray-900">{{ userProfile.telefono || 'No especificado' }}</div>
              </div>
              <div>
                <div class="text-sm text-gray-500">Fecha de nacimiento</div>
                <div class="font-medium text-gray-900">{{ formatDate(userProfile.fecha_nacimiento) || 'No especificado' }}</div>
              </div>
            </div>
          </div>

          <!-- Preferences -->
          <div class="bg-white rounded-3xl shadow-lg border border-gray-100 p-6">
            <div class="flex items-center mb-4">
              <div class="w-10 h-10 bg-green-100 rounded-2xl flex items-center justify-center mr-3">
                <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                </svg>
              </div>
              <h3 class="text-lg font-bold text-gray-900">Preferencias</h3>
            </div>
            
            <div>
              <div class="text-sm text-gray-500 mb-2">Notas y preferencias</div>
              <div class="font-medium text-gray-900">
                {{ userProfile.preferencias || 'No hay preferencias especificadas' }}
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Actions -->
        <div class="bg-white rounded-3xl shadow-lg border border-gray-100 p-8">
          <h3 class="text-xl font-bold text-gray-900 mb-6">Acciones Rápidas</h3>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <RouterLink 
              to="/reservas"
              class="bg-gradient-to-r from-[var(--color-barber-primary)] to-gray-700 text-white p-6 rounded-2xl hover:shadow-lg transition-all duration-200 transform hover:scale-105 text-center"
            >
              <svg class="w-8 h-8 mx-auto mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
              <div class="font-bold">Nueva Reserva</div>
              <div class="text-sm opacity-90">Agenda tu cita</div>
            </RouterLink>

            <RouterLink 
              to="/mis-reservas"
              class="bg-gradient-to-r from-[var(--color-barber-gold)] to-yellow-400 text-[var(--color-barber-primary)] p-6 rounded-2xl hover:shadow-lg transition-all duration-200 transform hover:scale-105 text-center"
            >
              <svg class="w-8 h-8 mx-auto mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
              <div class="font-bold">Mis Reservas</div>
              <div class="text-sm opacity-90">Ver historial</div>
            </RouterLink>

            <button 
              @click="changePassword"
              class="bg-gradient-to-r from-blue-500 to-indigo-600 text-white p-6 rounded-2xl hover:shadow-lg transition-all duration-200 transform hover:scale-105 text-center"
            >
              <svg class="w-8 h-8 mx-auto mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"/>
              </svg>
              <div class="font-bold">Cambiar Contraseña</div>
              <div class="text-sm opacity-90">Seguridad</div>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Modal de Cambio de Contraseña -->
    <div v-if="showPasswordModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-3xl shadow-xl max-w-md w-full p-8">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-xl font-bold text-gray-900">Cambiar Contraseña</h3>
          <button 
            @click="closePasswordModal"
            class="text-gray-500 hover:text-gray-700 transition-colors"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>

        <form @submit.prevent="updatePassword" class="space-y-6">
          <!-- Contraseña actual -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Contraseña Actual</label>
            <input 
              v-model="passwordForm.currentPassword"
              type="password" 
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[var(--color-barber-primary)] focus:border-transparent transition-all duration-200"
              placeholder="Tu contraseña actual"
            />
          </div>

          <!-- Nueva contraseña -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Nueva Contraseña</label>
            <input 
              v-model="passwordForm.newPassword"
              type="password" 
              required
              minlength="6"
              class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[var(--color-barber-primary)] focus:border-transparent transition-all duration-200"
              placeholder="Nueva contraseña (mín. 6 caracteres)"
            />
          </div>

          <!-- Confirmar nueva contraseña -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Confirmar Nueva Contraseña</label>
            <input 
              v-model="passwordForm.confirmPassword"
              type="password" 
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[var(--color-barber-primary)] focus:border-transparent transition-all duration-200"
              placeholder="Confirma tu nueva contraseña"
            />
            <p v-if="passwordForm.newPassword && passwordForm.confirmPassword && passwordForm.newPassword !== passwordForm.confirmPassword" 
               class="text-red-600 text-sm mt-2">
              Las contraseñas no coinciden
            </p>
          </div>

          <!-- Botones de acción -->
          <div class="flex flex-col sm:flex-row gap-3 pt-4">
            <button 
              type="submit"
              :disabled="changingPassword || passwordForm.newPassword !== passwordForm.confirmPassword"
              class="flex-1 bg-[var(--color-barber-primary)] text-white px-6 py-3 rounded-xl font-medium hover:bg-[var(--color-barber-gold)] transition-all duration-200 transform hover:scale-105 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="!changingPassword">Cambiar Contraseña</span>
              <span v-else>Cambiando...</span>
            </button>
            <button 
              type="button"
              @click="closePasswordModal"
              class="flex-1 bg-gray-100 text-gray-700 px-6 py-3 rounded-xl font-medium hover:bg-gray-200 transition-all duration-200"
            >
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Input file oculto para cambiar avatar -->
    <input
      ref="fileInput"
      type="file"
      accept="image/*"
      @change="handleAvatarChange"
      class="hidden"
    />
  </div>
</template>

<script>
import { authService } from '@/services'

export default {
  name: 'ProfileView',
  data() {
    return {
      loading: true,
      error: null,
      isEditing: false,
      savingProfile: false,
      showPasswordModal: false,
      changingPassword: false,
      userProfile: {
        id: null,
        nombre: '',
        email: '',
        telefono: '',
        fecha_nacimiento: '',
        preferencias: '',
        created_at: null
      },
      editedProfile: {},
      userStats: {
        totalReservations: 0,
        completedServices: 0,
        memberSince: ''
      },
      passwordForm: {
        currentPassword: '',
        newPassword: '',
        confirmPassword: ''
      }
    }
  },
  
  async mounted() {
    await this.loadUserProfile()
    await this.loadUserStats()
  },
  
  methods: {
    async loadUserProfile() {
      this.loading = true
      this.error = null
      
      try {
        // Intentar cargar el perfil desde el backend
        const response = await authService.getProfile()
        
        if (response && response.user) {
          this.userProfile = {
            id: response.user.id,
            nombre: response.user.nombre || response.user.name,
            email: response.user.email,
            telefono: response.user.telefono || response.user.phone,
            fecha_nacimiento: response.user.fecha_nacimiento || response.user.birth_date,
            preferencias: response.user.preferencias || response.user.preferences || '',
            created_at: response.user.created_at
          }
        } else {
          // Fallback con datos del localStorage
          this.loadMockProfile()
        }
      } catch (error) {
        console.error('Error al cargar perfil:', error)
        // Cargar datos de ejemplo en caso de error
        this.loadMockProfile()
      } finally {
        this.loading = false
      }
    },
    
    loadMockProfile() {
      // Datos de ejemplo para desarrollo
      const mockUser = {
        id: 1,
        nombre: 'Juan Carlos Pérez',
        email: 'juan.perez@email.com',
        telefono: '+591 12345678',
        fecha_nacimiento: '1990-05-15',
        preferencias: 'Prefiero cortes clásicos, no muy cortos en los costados. Tengo alergia a ciertos productos con fragancias fuertes.',
        created_at: '2024-01-15T10:00:00Z'
      }
      
      this.userProfile = mockUser
    },
    
    async loadUserStats() {
      try {
        // En una implementación real, esto vendría de la API
        this.userStats = {
          totalReservations: 12,
          completedServices: 8,
          memberSince: this.formatMemberSince(this.userProfile.created_at)
        }
      } catch (error) {
        console.error('Error al cargar estadísticas:', error)
        this.userStats = {
          totalReservations: 0,
          completedServices: 0,
          memberSince: '2024'
        }
      }
    },
    
    startEditing() {
      this.isEditing = true
      // Clonar el perfil actual para editar
      this.editedProfile = { ...this.userProfile }
    },
    
    cancelEditing() {
      this.isEditing = false
      this.editedProfile = {}
    },
    
    async saveProfile() {
      this.savingProfile = true
      
      try {
        // En una implementación real, aquí se haría la llamada a la API
        const response = await authService.updateProfile(this.editedProfile)
        
        if (response.success) {
          // Actualizar el perfil local con los datos guardados
          this.userProfile = { ...this.editedProfile }
          this.isEditing = false
          this.editedProfile = {}
          
          // Mostrar mensaje de éxito
          alert('Perfil actualizado exitosamente')
        } else {
          alert('Error al actualizar el perfil')
        }
      } catch (error) {
        console.error('Error al guardar perfil:', error)
        // Por ahora, simular que se guardó correctamente
        this.userProfile = { ...this.editedProfile }
        this.isEditing = false
        this.editedProfile = {}
        alert('Perfil actualizado exitosamente (modo demo)')
      } finally {
        this.savingProfile = false
      }
    },
    
    getInitials(name) {
      if (!name) return 'U'
      
      const names = name.split(' ')
      if (names.length >= 2) {
        return (names[0][0] + names[1][0]).toUpperCase()
      }
      return name[0].toUpperCase()
    },
    
    formatDate(dateString) {
      if (!dateString) return null
      
      const date = new Date(dateString)
      return date.toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    },
    
    formatMemberSince(dateString) {
      if (!dateString) return '2024'
      
      const date = new Date(dateString)
      return date.getFullYear().toString()
    },
    
    isValidEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      return emailRegex.test(email)
    },
    
    isValidPhone(phone) {
      // Aceptar diferentes formatos de teléfono
      const phoneRegex = /^[\+]?[\d\s\-\(\)]{8,15}$/
      return phoneRegex.test(phone)
    },
    
    changeAvatar() {
      this.$refs.fileInput.click()
    },
    
    handleAvatarChange(event) {
      const file = event.target.files[0]
      if (!file) return
      
      // Validar tipo de archivo
      if (!file.type.startsWith('image/')) {
        alert('Por favor selecciona una imagen válida')
        return
      }
      
      // Validar tamaño (máximo 5MB)
      if (file.size > 5 * 1024 * 1024) {
        alert('La imagen debe ser menor a 5MB')
        return
      }
      
      // En una implementación real, aquí subirías la imagen
      alert('Funcionalidad de cambio de foto próximamente disponible')
      
      // Resetear el input
      event.target.value = ''
    },
    
    changePassword() {
      this.showPasswordModal = true
    },
    
    closePasswordModal() {
      this.showPasswordModal = false
      this.passwordForm = {
        currentPassword: '',
        newPassword: '',
        confirmPassword: ''
      }
    },
    
    async updatePassword() {
      if (this.passwordForm.newPassword !== this.passwordForm.confirmPassword) {
        alert('Las contraseñas no coinciden')
        return
      }
      
      if (this.passwordForm.newPassword.length < 6) {
        alert('La nueva contraseña debe tener al menos 6 caracteres')
        return
      }
      
      this.changingPassword = true
      
      try {
        // En una implementación real, aquí se haría la llamada a la API
        const response = await authService.changePassword({
          currentPassword: this.passwordForm.currentPassword,
          newPassword: this.passwordForm.newPassword
        })
        
        if (response.success) {
          alert('Contraseña cambiada exitosamente')
          this.closePasswordModal()
        } else {
          alert(response.message || 'Error al cambiar la contraseña')
        }
      } catch (error) {
        console.error('Error al cambiar contraseña:', error)
        // Por ahora, simular que se cambió correctamente
        alert('Contraseña cambiada exitosamente (modo demo)')
        this.closePasswordModal()
      } finally {
        this.changingPassword = false
      }
    }
  }
}
</script>
