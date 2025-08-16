<!--
  AdminLayout.vue - Layout principal para el panel administrativo
  Actualizado con el tema de la aplicación: negro, blanco y gris
-->
<template>
  <div class="admin-layout h-screen bg-gray-100 flex">
    <!-- Sidebar -->
    <div class="admin-sidebar fixed inset-y-0 left-0 z-50 w-64 bg-black transform transition-transform duration-200 ease-in-out lg:translate-x-0 lg:static lg:inset-0 lg:flex lg:flex-col"
         :class="{ '-translate-x-full': !sidebarOpen, 'translate-x-0': sidebarOpen }">
      
      <!-- Logo y título -->
      <div class="sidebar-header bg-black border-b border-gray-800 p-6">
        <div class="text-center mb-6">
          <!-- Logo idéntico al navbar -->
          <div class="text-center leading-none mb-4">
            <div class="text-3xl text-white" style="font-family: 'Dancing Script', cursive; font-weight: 700; line-height: 0.8; letter-spacing: 2px; margin-bottom: 2px;">
              Lou
            </div>
            <div class="text-xs text-white" style="font-family: 'Oswald', sans-serif; font-weight: 600; letter-spacing: 0.35em; line-height: 1;">
              BARBERSHOP
            </div>
          </div>
          <div class="w-12 h-0.5 bg-white mx-auto mb-3"></div>
        </div>
        
        <!-- Info del usuario actual -->
        <div class="bg-gray-800 rounded-lg p-4 text-center border border-gray-700">
          <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center mx-auto mb-3">
            <span class="text-black font-bold text-lg">
              {{ currentUser?.nombre?.charAt(0)?.toUpperCase() || 'A' }}
            </span>
          </div>
          <p class="text-white font-medium text-sm tracking-wide">
            {{ currentUser?.nombre || 'Administrador' }}
          </p>
          <p class="text-gray-400 text-xs uppercase tracking-wider">
            {{ currentUser?.rol || 'admin' }}
          </p>
        </div>
      </div>

      <!-- Navegación -->
      <nav class="flex-1 px-4 py-6 overflow-y-auto">
        <div class="space-y-1">
          <!-- Dashboard -->
          <RouterLink
            to="/admin"
            class="admin-nav-link flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-all duration-200 group"
            :class="$route.path === '/admin' ? 'bg-white text-black shadow-lg' : 'text-gray-300 hover:bg-gray-900 hover:text-white'"
          >
            <svg class="w-5 h-5 mr-3 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 20 20">
              <path d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zM3 10a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1v-6zM14 9a1 1 0 00-1 1v6a1 1 0 001 1h2a1 1 0 001-1v-6a1 1 0 00-1-1h-2z" />
            </svg>
            <span class="tracking-wide">Inicio</span>
          </RouterLink>

          <!-- Reservas -->
          <RouterLink
            to="/admin/reservas"
            class="admin-nav-link flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-all duration-200 group"
            :class="$route.path.startsWith('/admin/reservas') ? 'bg-white text-black shadow-lg' : 'text-gray-300 hover:bg-gray-900 hover:text-white'"
          >
            <svg class="w-5 h-5 mr-3 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd" />
            </svg>
            <span class="tracking-wide">Reservas</span>
          </RouterLink>

          <!-- Barberos -->
          <RouterLink
            to="/admin/barberos"
            class="admin-nav-link flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-all duration-200 group"
            :class="$route.path.startsWith('/admin/barberos') ? 'bg-white text-black shadow-lg' : 'text-gray-300 hover:bg-gray-900 hover:text-white'"
          >
            <svg class="w-5 h-5 mr-3 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
            </svg>
            <span class="tracking-wide">Barberos</span>
          </RouterLink>

          <!-- Usuarios -->
          <RouterLink
            to="/admin/usuarios"
            class="admin-nav-link flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-all duration-200 group"
            :class="$route.path.startsWith('/admin/usuarios') ? 'bg-white text-black shadow-lg' : 'text-gray-300 hover:bg-gray-900 hover:text-white'"
          >
            <svg class="w-5 h-5 mr-3 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 20 20">
              <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
            </svg>
            <span class="tracking-wide">Usuarios</span>
          </RouterLink>

          <!-- Servicios -->
          <RouterLink
            to="/admin/servicios"
            class="admin-nav-link flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-all duration-200 group"
            :class="$route.path.startsWith('/admin/servicios') ? 'bg-white text-black shadow-lg' : 'text-gray-300 hover:bg-gray-900 hover:text-white'"
          >
            <svg class="w-5 h-5 mr-3 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd" />
            </svg>
            <span class="tracking-wide">Servicios</span>
          </RouterLink>

          <!-- Productos -->
          <RouterLink
            to="/admin/productos"
            class="admin-nav-link flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-all duration-200 group"
            :class="$route.path.startsWith('/admin/productos') ? 'bg-white text-black shadow-lg' : 'text-gray-300 hover:bg-gray-900 hover:text-white'"
          >
            <svg class="w-5 h-5 mr-3 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 2L3 7v11a1 1 0 001 1h12a1 1 0 001-1V7l-7-5zM8.5 13a1.5 1.5 0 103 0 1.5 1.5 0 00-3 0z" clip-rule="evenodd" />
            </svg>
            <span class="tracking-wide">Productos</span>
          </RouterLink>

          <!-- Calendario -->
          <RouterLink
            to="/admin/calendario"
            class="admin-nav-link flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-all duration-200 group"
            :class="$route.path.startsWith('/admin/calendario') ? 'bg-white text-black shadow-lg' : 'text-gray-300 hover:bg-gray-900 hover:text-white'"
          >
            <svg class="w-5 h-5 mr-3 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd" />
            </svg>
            <span class="tracking-wide">Calendario</span>
          </RouterLink>

          <!-- Reportes -->
          <RouterLink
            to="/admin/reportes"
            class="admin-nav-link flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-all duration-200 group"
            :class="$route.path.startsWith('/admin/reportes') ? 'bg-white text-black shadow-lg' : 'text-gray-300 hover:bg-gray-900 hover:text-white'"
          >
            <svg class="w-5 h-5 mr-3 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 20 20">
              <path d="M2 11a1 1 0 011-1h2a1 1 0 011 1v5a1 1 0 01-1 1H3a1 1 0 01-1-1v-5zM8 7a1 1 0 011-1h2a1 1 0 011 1v9a1 1 0 01-1 1H9a1 1 0 01-1-1V7zM14 4a1 1 0 011-1h2a1 1 0 011 1v12a1 1 0 01-1 1h-2a1 1 0 01-1-1V4z" />
            </svg>
            <span class="tracking-wide">Reportes</span>
          </RouterLink>
        </div>
        
        <!-- Botón volver al inicio (movido al final) -->
        <div class="pt-4 border-t border-gray-800">
          <RouterLink
            to="/"
            class="admin-nav-link flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-all duration-200 bg-gray-800 text-white hover:bg-gray-700 border border-gray-700 group"
          >
            <svg class="w-5 h-5 mr-3 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 20 20">
              <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L8 6.414V17a1 1 0 102 0V6.414l4.293 4.293a1 1 0 001.414-1.414l-7-7z"/>
            </svg>
            <span class="tracking-wide">Volver al Inicio</span>
          </RouterLink>
        </div>
      </nav>
    </div>

    <!-- Overlay para móvil -->
    <div v-if="sidebarOpen" 
         @click="sidebarOpen = false"
         class="fixed inset-0 z-40 bg-black bg-opacity-50 lg:hidden"></div>

    <!-- Contenido principal -->
    <div class="flex-1 flex flex-col min-w-0 lg:ml-0">
      <!-- Header simplificado -->
      <header class="admin-header bg-white shadow-lg border-b border-gray-200 flex-shrink-0">
        <div class="px-4 sm:px-6 lg:px-8">
          <div class="flex justify-between items-center h-16">
            <!-- Botón menú móvil -->
            <button
              @click="sidebarOpen = !sidebarOpen"
              class="lg:hidden p-2 rounded-md text-gray-700 hover:text-black hover:bg-gray-100 transition-colors"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>

            <!-- Título de la página -->
            <div class="flex-1 lg:flex-none">
              <h2 class="text-xl font-semibold text-black tracking-wide">
                {{ pageTitle }}
              </h2>
            </div>

            <!-- Acciones rápidas -->
            <div class="flex items-center space-x-3">
              <!-- Botón volver al home (visible en desktop) -->
              <RouterLink
                to="/"
                class="hidden lg:flex items-center justify-center w-9 h-9 bg-gray-50 hover:bg-black rounded-lg text-gray-600 hover:text-white transition-all duration-200 transform hover:scale-105"
                title="Ir al sitio web"
              >
                <svg class="w-4 h-4 transition-transform duration-200" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L8 6.414V17a1 1 0 102 0V6.414l4.293 4.293a1 1 0 001.414-1.414l-7-7z"/>
                </svg>
              </RouterLink>

              <!-- Botón cerrar sesión -->
              <button
                @click="logout"
                class="w-9 h-9 flex items-center justify-center text-gray-600 hover:text-white hover:bg-red-500 bg-gray-50 rounded-lg transition-all duration-200 transform hover:scale-105"
                title="Cerrar sesión"
              >
                <svg class="w-4 h-4 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </header>

      <!-- Área de contenido -->
      <main class="admin-content flex-1 p-4 sm:p-6 lg:p-8 overflow-y-auto bg-gray-100 min-h-screen">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { authService } from '@/services/authService.js'

export default {
  name: 'AdminLayout',
  setup() {
    const route = useRoute()
    const router = useRouter()
    
    const sidebarOpen = ref(false)
    const currentUser = ref(null)

    // Título de la página basado en la ruta
    const pageTitle = computed(() => {
      const path = route.path
      if (path === '/admin') return 'Inicio'
      if (path.startsWith('/admin/reservas')) return 'Reservas'
      if (path.startsWith('/admin/barberos')) return 'Barberos'
      if (path.startsWith('/admin/usuarios')) return 'Usuarios'
      if (path.startsWith('/admin/servicios')) return 'Servicios'
      if (path.startsWith('/admin/productos')) return 'Productos'
      if (path.startsWith('/admin/calendario')) return 'Calendario'
      if (path.startsWith('/admin/reportes')) return 'Reportes'
      return 'Admin'
    })

    // Cargar datos del usuario actual
    const loadUserData = () => {
      currentUser.value = authService.getCurrentUser()
    }

    // Cerrar sesión
    const logout = async () => {
      try {
        authService.logout()
        router.push('/')
      } catch (error) {
        console.error('Error al cerrar sesión:', error)
      }
    }

    onMounted(() => {
      loadUserData()
    })

    return {
      sidebarOpen,
      currentUser,
      pageTitle,
      logout
    }
  }
}
</script>

<style scoped>
/* Estilos específicos para el panel admin */
.admin-layout {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  min-height: 100vh;
  background-color: #f3f4f6; /* gray-100 */
}

.sidebar-header {
  flex-shrink: 0;
}

.admin-nav-link {
  transition: all 0.3s ease-in-out;
  position: relative;
  overflow: hidden;
}

.admin-nav-link:hover {
  transform: translateX(3px);
}

.admin-nav-link::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transition: left 0.6s ease;
}

.admin-nav-link:hover::before {
  left: 100%;
}

.admin-sidebar {
  background: #000000;
  box-shadow: 4px 0 20px rgba(0, 0, 0, 0.3);
}

.admin-header {
  background: #ffffff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.admin-content {
  background-color: #f3f4f6; /* gray-100 */
}

/* Asegurar que el sidebar ocupe toda la altura en desktop */
@media (min-width: 1024px) {
  .admin-sidebar {
    height: 100vh;
    position: fixed;
    left: 0;
    top: 0;
  }
  
  .admin-layout {
    padding-left: 16rem; /* 256px = w-64 */
  }
}

/* Animaciones para el sidebar en móvil */
@media (max-width: 1023px) {
  .admin-sidebar {
    transition: transform 0.3s ease-in-out;
  }
  
  .admin-layout {
    padding-left: 0;
  }
}

/* Scroll personalizado para la navegación */
.admin-sidebar nav::-webkit-scrollbar {
  width: 4px;
}

.admin-sidebar nav::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
}

.admin-sidebar nav::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 2px;
}

.admin-sidebar nav::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.3);
}

/* Animaciones adicionales */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.admin-content {
  animation: fadeIn 0.4s ease-in-out;
}
</style>
