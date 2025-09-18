<!--
  ServiceCard - Tarjeta de servicio
  Actualizada para usar Tailwind CSS v4 con clases estándar
-->
<template>
  <div class="bg-white rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 relative overflow-hidden group cursor-pointer transform hover:-translate-y-2">
    <!-- Badge de estado -->
    <div v-if="service.popular" class="absolute top-6 right-6 bg-orange-500 text-white px-4 py-2 rounded-full text-xs font-bold tracking-wide z-10">
      POPULAR
    </div>
    <div v-else-if="service.recommended" class="absolute top-6 right-6 bg-green-500 text-white px-4 py-2 rounded-full text-xs font-bold tracking-wide z-10">
      RECOMENDADO
    </div>

    <!-- Contenido -->
    <div class="p-8 text-center">
      <!-- Icono del servicio -->
      <div class="w-20 h-20 bg-black rounded-full flex items-center justify-center mx-auto mb-6 transition-all duration-300 group-hover:scale-110">
        <svg v-if="service.icon === 'scissors'" class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        <svg v-else-if="service.icon === 'user'" class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
        </svg>
        <svg v-else-if="service.icon === 'sparkles'" class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/>
        </svg>
        <svg v-else class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
      </div>

      <!-- Título -->
      <h3 class="text-2xl font-bold text-gray-900 mb-4 group-hover:text-black transition-colors">
        {{ service.name }}
      </h3>

      <!-- Descripción -->
      <p class="text-gray-600 mb-6 leading-relaxed line-clamp-3">
        {{ service.description }}
      </p>

      <!-- Precio -->
      <div class="mb-6">
        <span class="text-2xl font-bold text-black">
          Bs {{ formatPrice(service.price) }}
        </span>
      </div>

      <!-- Características -->
      <div class="space-y-3 mb-8">
        <div v-if="service.features && service.features.length > 0">
          <div v-for="feature in service.features.slice(0, 2)" :key="feature" class="flex items-center justify-center text-gray-700">
            <svg class="w-4 h-4 text-green-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
            <span class="text-sm font-medium">{{ feature }}</span>
          </div>
        </div>
        
        <!-- Duración -->
        <div class="flex items-center justify-center mt-6">
          <div class="bg-gray-100 text-gray-800 px-4 py-2 rounded-full text-sm font-semibold border border-gray-200">
            <svg class="w-4 h-4 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            {{ service.duration }} minutos
          </div>
        </div>
      </div>

      <!-- Botón de acción -->
      <button 
        @click="selectService"
        class="w-full bg-gradient-to-r from-[var(--color-barber-primary)] to-[color-mix(in_srgb,var(--color-barber-primary),black_20%)] text-white px-8 py-4 rounded-xl font-bold text-sm tracking-wide hover:from-[var(--color-barber-gold)] hover:to-[color-mix(in_srgb,var(--color-barber-gold),black_20%)] transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl"
      >
        RESERVAR AHORA
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ServiceCard',
  props: {
    service: {
      type: Object,
      required: true,
      validator(value) {
        return (
          value &&
          typeof value.name === 'string' &&
          typeof value.price === 'number' &&
          typeof value.description === 'string' &&
          typeof value.duration === 'number'
        )
      }
    }
  },
  methods: {
    formatPrice(price) {
      return price.toFixed(2)
    },
    selectService() {
      // Emitir evento para que el padre maneje la selección
      this.$emit('select-service', this.service)
      
      // Redirigir a reservas con el servicio seleccionado
      this.$router.push({
        name: 'reservations',
        query: { service: this.service.id }
      }).then(() => {
        // Asegurar que el scroll esté en el top después de la navegación
        window.scrollTo(0, 0)
      })
    }
  }
}
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
