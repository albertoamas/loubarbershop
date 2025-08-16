<!--
  NotFoundView - Vista de página no encontrada (404)
  Página que se muestra cuando la ruta no existe
-->
<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
    <div class="max-w-7xl mx-auto px-4">
      <div class="text-center">
        <!-- Número 404 grande -->
        <div class="mb-8">
          <h1 class="text-8xl lg:text-9xl font-bold text-black opacity-20 select-none animate-pulse">
            404
          </h1>
        </div>

        <!-- Contenido principal -->
        <div class="max-w-md mx-auto">
          <!-- Icono -->
          <div class="mb-6">
            <svg class="w-24 h-24 text-gray-400 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9.172 16.172a4 4 0 015.656 0M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
            </svg>
          </div>

          <!-- Título -->
          <h2 class="text-3xl lg:text-4xl font-bold text-black mb-4">
            Página no encontrada
          </h2>

          <!-- Descripción -->
          <p class="text-lg text-gray-600 mb-8">
            Lo sentimos, la página que buscas no existe o ha sido movida.
          </p>

          <!-- Botones de acción -->
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <button
              @click="goBack"
              class="bg-gray-200 text-black px-6 py-3 rounded-xl font-medium hover:bg-gray-300 transition-all duration-200"
            >
              Volver Atrás
            </button>
            <RouterLink
              to="/"
              class="bg-black text-white px-6 py-3 rounded-xl font-medium hover:bg-gray-800 transition-all duration-200 inline-block text-center"
            >
              Ir al Inicio
            </RouterLink>
          </div>
        </div>

        <!-- Enlaces útiles -->
        <div class="mt-12 pt-8 border-t border-gray-200">
          <h3 class="text-lg font-semibold text-black mb-4">
            Enlaces útiles
          </h3>
          <div class="flex flex-wrap gap-6 justify-center text-gray-600">
            <RouterLink
              to="/servicios"
              class="hover:text-black transition-colors"
            >
              Servicios
            </RouterLink>
            <RouterLink
              to="/productos"
              class="hover:text-black transition-colors"
            >
              Productos
            </RouterLink>
            <RouterLink
              to="/reservas"
              class="hover:text-black transition-colors"
            >
              Reservar Cita
            </RouterLink>
            <RouterLink
              to="/contacto"
              class="hover:text-black transition-colors"
            >
              Contacto
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFoundView',
  methods: {
    goBack() {
      // Verificar si hay historial
      if (window.history.length > 1) {
        this.$router.go(-1)
      } else {
        // Si no hay historial, ir al inicio
        this.$router.push('/')
      }
    }
  },
  mounted() {
    // Cambiar el título de la página
    document.title = 'Página no encontrada - Low Barber'
  }
}
</script>
