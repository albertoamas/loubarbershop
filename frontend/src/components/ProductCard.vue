<!--
  ProductCard - Tarjeta de producto premium
  Diseño horizontal moderno y elegante para la barbería
-->
<template>
  <div class="bg-white rounded-3xl shadow-xl hover:shadow-2xl transition-all duration-500 relative overflow-hidden group cursor-pointer transform hover:-translate-y-2 border border-gray-100/50">
    <!-- Badges de estado mejorados y responsive -->
    <div class="absolute top-4 right-4 z-20 flex flex-col sm:flex-row gap-2">
      <div v-if="product.isNew" class="bg-[linear-gradient(to_right,#10b981,#059669)] text-white px-2 sm:px-3 py-1 rounded-full text-xs font-bold tracking-wide shadow-lg backdrop-blur-sm">
        <span class="hidden sm:inline">✨ NUEVO</span>
        <span class="sm:hidden">✨</span>
      </div>
      <div v-if="product.discount" class="bg-[linear-gradient(to_right,#eab308,#ca8a04)] text-white px-2 sm:px-3 py-1 rounded-full text-xs font-bold tracking-wide shadow-lg backdrop-blur-sm">
        <span class="hidden sm:inline">🔥 -{{ product.discount }}%</span>
        <span class="sm:hidden">🔥</span>
      </div>
      <div v-if="product.featured" class="bg-[linear-gradient(to_right,#eab308,#ca8a04)] text-white px-2 sm:px-3 py-1 rounded-full text-xs font-bold tracking-wide shadow-lg backdrop-blur-sm">
        <span class="hidden sm:inline">⭐ DESTACADO</span>
        <span class="sm:hidden">⭐</span>
      </div>
    </div>

    <!-- Layout responsive: vertical en móvil, horizontal en desktop -->
    <div class="flex flex-col sm:flex-row sm:items-center">
      <!-- Imagen del producto responsive -->
      <div class="w-full sm:w-48 h-48 sm:h-36 bg-[linear-gradient(135deg,var(--color-gray-100),var(--color-gray-200))] rounded-t-3xl sm:rounded-l-3xl sm:rounded-tr-none overflow-hidden relative flex-shrink-0">
        <div v-if="product.image" class="w-full h-full relative">
          <img 
            :src="product.image" 
            :alt="product.name"
            class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
          />
          <!-- Overlay con gradiente usando color-mix -->
          <div class="absolute inset-0 bg-[linear-gradient(to_top,color-mix(in_srgb,black_30%,transparent),transparent)] opacity-0 group-hover:opacity-100 transition-all duration-500"></div>
          <!-- Brillo en hover con modern CSS -->
          <div class="absolute inset-0 bg-[linear-gradient(90deg,transparent,color-mix(in_srgb,white_10%,transparent),transparent)] -translate-x-full group-hover:translate-x-full transition-transform duration-1000"></div>
        </div>
        <div v-else class="w-full h-full flex items-center justify-center relative">
          <div class="text-center text-gray-500">
            <div class="w-16 h-16 sm:w-12 sm:h-12 bg-gradient-to-br from-gray-200 via-gray-300 to-gray-400 rounded-full flex items-center justify-center mx-auto mb-2 shadow-lg">
              <svg class="w-8 h-8 sm:w-6 sm:h-6 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M9 21V9l-5-3m5 3l8-4"/>
              </svg>
            </div>
            <p class="text-sm font-semibold text-gray-700">{{ product.name }}</p>
          </div>
        </div>
      </div>

      <!-- Contenido principal responsive -->
      <div class="flex-1 p-4 sm:p-6">
        <div class="flex flex-col sm:flex-row sm:justify-between sm:items-start">
          <!-- Información del producto -->
          <div class="flex-1 mb-4 sm:mb-0">
            <!-- Título y marca -->
            <div class="mb-3">
              <h3 class="text-lg sm:text-xl font-bold text-gray-900 mb-1 group-hover:text-black transition-colors leading-tight text-center sm:text-left">
                {{ product.name }}
              </h3>
              <p v-if="product.brand" class="text-gray-500 text-sm font-semibold tracking-wider uppercase text-center sm:text-left">
                {{ product.brand }}
              </p>
            </div>

            <!-- Descripción -->
            <p class="text-gray-600 mb-4 leading-relaxed line-clamp-2 text-center sm:text-left text-sm">
              {{ product.description }}
            </p>

            <!-- Información compacta -->
            <div class="flex items-center justify-center sm:justify-start gap-4 mb-3 flex-wrap">
              <!-- Rating compacto -->
              <div v-if="product.rating" class="flex items-center">
                <div class="flex items-center">
                  <svg 
                    v-for="star in 5" 
                    :key="star"
                    class="w-4 h-4 transition-colors duration-200"
                    :class="star <= product.rating ? 'text-[var(--color-barber-gold)]' : 'text-gray-300'"
                    fill="currentColor" 
                    viewBox="0 0 20 20"
                  >
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                  </svg>
                </div>
                <span class="text-xs text-gray-600 ml-2 font-medium">
                  {{ product.rating.toFixed(1) }}
                </span>
              </div>

              <!-- Stock compacto -->
              <div class="flex items-center text-xs" :class="product.stock > 0 ? 'text-green-600' : 'text-yellow-600'">
                <div class="w-2 h-2 rounded-full mr-1"
                     :class="product.stock > 0 ? 'bg-green-500' : 'bg-yellow-500'">
                </div>
                <span class="font-medium">
                  {{ product.stock > 0 ? `${product.stock} disponibles` : 'Agotado' }}
                </span>
              </div>
            </div>

            <!-- Categoría y etiquetas -->
            <div class="flex items-center justify-center sm:justify-start gap-2 mb-3 flex-wrap">
              <span v-if="product.category" class="px-2 py-1 bg-gray-100 text-gray-600 text-xs rounded-lg font-medium capitalize">
                {{ product.category }}
              </span>
              <span 
                v-for="(tag, index) in product.tags.slice(0, 2)" 
                :key="tag"
                class="px-2 py-1 text-xs rounded-lg font-medium"
                :class="{
                  'bg-blue-100 text-blue-700': index === 0,
                  'bg-purple-100 text-purple-700': index === 1
                }"
              >
                {{ tag }}
              </span>
            </div>
          </div>

          <!-- Sección de precio y botón -->
          <div class="flex flex-col items-center sm:items-end justify-between">
            <!-- Precio destacado con variables CSS nativas -->
            <div class="text-center sm:text-right mb-4">
              <div class="text-xl sm:text-2xl font-bold text-black">
                Bs {{ formatPrice(product.price) }}
              </div>
              <div v-if="product.originalPrice && product.originalPrice > product.price" class="mt-1">
                <span class="text-sm text-gray-400 line-through">
                  Bs {{ formatPrice(product.originalPrice) }}
                </span>
              </div>
            </div>

            <!-- Botón de acción con variables CSS -->
            <button 
              @click="viewProduct"
              class="w-full sm:w-auto bg-[var(--color-barber-primary)] text-white px-6 py-2 rounded-lg font-medium text-sm hover:bg-[var(--color-barber-gold)] transition-all duration-300 whitespace-nowrap shadow-lg hover:shadow-xl transform hover:scale-105"
            >
              <span class="flex items-center justify-center gap-2">
                Ver Detalles
                <svg class="w-4 h-4 transform transition-transform group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                </svg>
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Efecto de brillo en hover -->
    <div class="absolute inset-0 rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none">
      <div class="absolute inset-0 rounded-3xl bg-gradient-to-r from-transparent via-white/5 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductCard',
  props: {
    product: {
      type: Object,
      required: true,
      validator(value) {
        return (
          value &&
          typeof value.name === 'string' &&
          typeof value.price === 'number' &&
          typeof value.description === 'string' &&
          typeof value.stock === 'number'
        )
      }
    }
  },
  methods: {
    formatPrice(price) {
      if (!price && price !== 0) return '0.00'
      return parseFloat(price).toFixed(2)
    },
    viewProduct() {
      // Emitir evento para que el padre maneje la vista del producto
      this.$emit('view-product', this.product)
      
      // Aquí podrías redirigir a una página de detalles del producto
      // this.$router.push({ name: 'ProductDetail', params: { id: this.product.id } })
    }
  }
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
