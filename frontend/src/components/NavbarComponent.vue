<!--
  Navbar - Navegación principal
  Diseño idéntico al de la imagen de referencia
-->
<template>
  <nav class="bg-black shadow-lg sticky top-0 z-50">
    <div class="container mx-auto px-6">
      <div class="flex justify-between items-center py-4">
        <!-- Logo -->
        <RouterLink to="/" class="flex items-center space-x-2">
          <div class="text-center leading-none">
            <div class="text-4xl text-white" style="font-family: 'Dancing Script', cursive; font-weight: 700; line-height: 0.8; letter-spacing: 2px; margin-bottom: 2px;">
              Lou
            </div>
            <div class="text-xs text-white" style="font-family: 'Oswald', sans-serif; font-weight: 600; letter-spacing: 0.35em; line-height: 1;">
              BARBERSHOP
            </div>
          </div>
        </RouterLink>

        <!-- Navegación Desktop -->
        <div class="hidden md:flex items-center space-x-12 ml-auto mr-8">
          <RouterLink 
            to="/"
            class="text-white hover:text-gray-300 transition-colors font-medium text-sm tracking-wide"
            :class="{ 'text-gray-300 font-semibold': $route.path === '/' }"
          >
            Inicio
          </RouterLink>
          <RouterLink 
            to="/servicios"
            class="text-white hover:text-gray-300 transition-colors font-medium text-sm tracking-wide"
            :class="{ 'text-gray-300 font-semibold': $route.path === '/servicios' }"
          >
            Servicios
          </RouterLink>
          <RouterLink 
            to="/productos"
            class="text-white hover:text-gray-300 transition-colors font-medium text-sm tracking-wide"
            :class="{ 'text-gray-300 font-semibold': $route.path === '/productos' }"
          >
            Productos
          </RouterLink>
          <RouterLink 
            to="/reservas"
            class="text-white hover:text-gray-300 transition-colors font-medium text-sm tracking-wide"
            :class="{ 'text-gray-300 font-semibold': $route.path === '/reservas' }"
          >
            Reservar
          </RouterLink>
        </div>

        <!-- Botones de acción -->
        <div class="hidden md:flex items-center space-x-6">
          <!-- Si el usuario está autenticado -->
          <template v-if="isAuthenticated">
            <!-- Menú desplegable del usuario -->
            <div class="relative" ref="userMenu">
              <button
                @click="toggleUserMenu"
                class="text-white hover:text-gray-300 transition-colors font-medium text-sm tracking-wide flex items-center space-x-2 focus:outline-none"
              >
                <span>{{ currentUser?.nombre || 'Usuario' }}</span>
                <svg 
                  class="w-4 h-4 transition-transform duration-200"
                  :class="{ 'rotate-180': userMenuOpen }"
                  fill="none" 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </button>

              <!-- Menú desplegable -->
              <div 
                v-if="userMenuOpen"
                class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border border-gray-200 py-2 z-50"
              >
                <!-- Mi perfil -->
                <RouterLink
                  to="/perfil"
                  @click="closeUserMenu"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 transition-colors flex items-center space-x-2"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                  <span>Mi perfil</span>
                </RouterLink>

                <!-- Panel Admin (solo si es admin) -->
                <RouterLink
                  v-if="isAdmin"
                  to="/admin"
                  @click="closeUserMenu"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 transition-colors flex items-center space-x-2"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                  </svg>
                  <span>Panel Admin</span>
                </RouterLink>

                <!-- Separador -->
                <hr class="my-1 border-gray-200">

                <!-- Cerrar sesión -->
                <button
                  @click="logout"
                  class="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50 transition-colors flex items-center space-x-2"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                  </svg>
                  <span>Cerrar sesión</span>
                </button>
              </div>
            </div>
          </template>
          
          <!-- Si el usuario NO está autenticado -->
          <template v-else>
            <RouterLink
              to="/login"
              class="text-white hover:text-gray-300 transition-colors font-medium text-sm tracking-wide"
            >
              Iniciar Sesión
            </RouterLink>
            <RouterLink
              to="/register"
              class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-colors font-medium text-sm tracking-wide"
            >
              Registrarse
            </RouterLink>
          </template>
        </div>

        <!-- Botón móvil -->
        <button
          @click="toggleMobileMenu"
          class="md:hidden p-2 rounded-md hover:bg-gray-800 transition-colors"
          aria-label="Menú"
        >
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Menú móvil -->
      <div 
        v-if="mobileMenuOpen"
        class="md:hidden py-4 border-t border-gray-700"
      >
        <div class="flex flex-col space-y-4">
          <RouterLink 
            to="/"
            @click="closeMobileMenu"
            class="text-white hover:text-gray-300 transition-colors font-medium py-2 text-sm tracking-wide"
            :class="{ 'text-gray-300 font-semibold': $route.path === '/' }"
          >
            Inicio
          </RouterLink>
          <RouterLink 
            to="/servicios"
            @click="closeMobileMenu"
            class="text-white hover:text-gray-300 transition-colors font-medium py-2 text-sm tracking-wide"
            :class="{ 'text-gray-300 font-semibold': $route.path === '/servicios' }"
          >
            Servicios
          </RouterLink>
          <RouterLink 
            to="/productos"
            @click="closeMobileMenu"
            class="text-white hover:text-gray-300 transition-colors font-medium py-2 text-sm tracking-wide"
            :class="{ 'text-gray-300 font-semibold': $route.path === '/productos' }"
          >
            Productos
          </RouterLink>
          <RouterLink 
            to="/reservas"
            @click="closeMobileMenu"
            class="text-white hover:text-gray-300 transition-colors font-medium py-2 text-sm tracking-wide"
            :class="{ 'text-gray-300 font-semibold': $route.path === '/reservas' }"
          >
            Reservar
          </RouterLink>
          
          <div class="flex flex-col space-y-2 pt-4 border-t border-gray-700">
            <!-- Si el usuario está autenticado -->
            <template v-if="isAuthenticated">
              <!-- Nombre del usuario (móvil) -->
              <div class="text-white text-sm py-2 font-medium">
                {{ currentUser?.nombre || 'Usuario' }}
              </div>
              
              <!-- Mi perfil móvil -->
              <RouterLink
                to="/perfil"
                @click="closeMobileMenu"
                class="text-white hover:text-gray-300 transition-colors font-medium py-2 text-sm tracking-wide flex items-center space-x-2"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
                <span>Mi perfil</span>
              </RouterLink>

              <!-- Panel Admin móvil (solo si es admin) -->
              <RouterLink
                v-if="isAdmin"
                to="/admin"
                @click="closeMobileMenu"
                class="text-white hover:text-gray-300 transition-colors font-medium py-2 text-sm tracking-wide flex items-center space-x-2"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                <span>Panel Admin</span>
              </RouterLink>
              
              <!-- Botón cerrar sesión móvil -->
              <button
                @click="logout"
                class="text-red-400 hover:text-red-300 transition-colors font-medium py-2 text-sm tracking-wide text-left flex items-center space-x-2"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                </svg>
                <span>Cerrar sesión</span>
              </button>
            </template>
            
            <!-- Si el usuario NO está autenticado -->
            <template v-else>
              <RouterLink
                to="/login"
                @click="closeMobileMenu"
                class="text-white hover:text-gray-300 transition-colors font-medium py-2 text-sm tracking-wide text-left"
              >
                Iniciar Sesión
              </RouterLink>
              <RouterLink
                to="/register"
                @click="closeMobileMenu"
                class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-colors font-medium text-sm tracking-wide"
              >
                Registrarse
              </RouterLink>
            </template>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { authService } from '@/services'

export default {
  name: 'NavbarComponent',
  components: {
  },
  data() {
    return {
      mobileMenuOpen: false,
      userMenuOpen: false,
      currentUser: null,
      isAuthenticated: false
    }
  },
  computed: {
    isAdmin() {
      // Verificar tanto 'rol' (backend) como 'role' (legacy)
      const userRole = this.currentUser?.rol || this.currentUser?.role
      return userRole === 'admin' || userRole === 'ADMIN'
    }
  },
  methods: {
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen
      // Cerrar menú de usuario al abrir menú móvil
      this.userMenuOpen = false
    },
    closeMobileMenu() {
      this.mobileMenuOpen = false
    },
    toggleUserMenu() {
      this.userMenuOpen = !this.userMenuOpen
      // Cerrar menú móvil al abrir menú de usuario
      this.mobileMenuOpen = false
    },
    closeUserMenu() {
      this.userMenuOpen = false
    },
    updateAuthState() {
      this.isAuthenticated = authService.isAuthenticated()
      this.currentUser = authService.getCurrentUser()
    },
    async logout() {
      try {
        authService.logout()
        this.updateAuthState()
        
        // Cerrar menús
        this.userMenuOpen = false
        this.mobileMenuOpen = false
        
        // Redirigir a home después del logout
        this.$router.push('/')
        
        alert('¡Hasta luego!')
      } catch (error) {
        console.error('Error al cerrar sesión:', error)
      }
    }
  },
  mounted() {
    // Cerrar menús al hacer clic fuera
    document.addEventListener('click', (event) => {
      if (!this.$el.contains(event.target)) {
        this.mobileMenuOpen = false
        this.userMenuOpen = false
      }
    })
    
    // Inicializar estado de autenticación
    this.updateAuthState()
    
    // Escuchar evento personalizado de cambio de autenticación
    window.addEventListener('authStateChanged', this.updateAuthState)
    
    // Escuchar cambios de storage para actualizaciones en tiempo real
    window.addEventListener('storage', this.updateAuthState)
    
    // Escuchar cambios de ruta para actualizar estado y cerrar menús
    this.$watch('$route', () => {
      this.updateAuthState()
      this.userMenuOpen = false
      this.mobileMenuOpen = false
    })
  },
  beforeUnmount() {
    // Limpiar event listeners
    window.removeEventListener('authStateChanged', this.updateAuthState)
    window.removeEventListener('storage', this.updateAuthState)
  }
}
</script>
