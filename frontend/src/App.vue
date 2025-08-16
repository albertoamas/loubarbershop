<!--
  App.vue - Componente principal
  Layout estándar para toda la aplicación
-->
<template>
  <div id="app">
    <!-- Navegación (solo para rutas no administrativas) -->
    <NavbarComponent v-if="!isAdminRoute" />
    
    <!-- Contenido principal -->
    <main>
      <RouterView />
    </main>
    
    <!-- Footer (solo para rutas no administrativas) -->
    <FooterComponent v-if="!isAdminRoute" />
  </div>
</template>

<script>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import NavbarComponent from '@/components/NavbarComponent.vue'
import FooterComponent from '@/components/FooterComponent.vue'

export default {
  name: 'App',
  components: {
    NavbarComponent,
    FooterComponent
  },
  setup() {
    const route = useRoute()
    
    // Verificar si estamos en una ruta administrativa
    const isAdminRoute = computed(() => {
      return route.path.startsWith('/admin')
    })
    
    return {
      isAdminRoute
    }
  }
}
</script>

<style>
/* Estilos globales ya definidos en app.css */
</style>
