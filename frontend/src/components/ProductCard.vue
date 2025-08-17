<!--
  ProductCard - Tarjeta de producto
  Actualizada con estilo elegante similar a ServiceCard
-->
<template>
  <div class="bg-white rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 relative overflow-hidden group cursor-pointer transform hover:-translate-y-2">
    <!-- Badges de estado -->
    <div class="absolute top-6 right-6 z-10 flex flex-col gap-2">
      <div v-if="product.isNew" class="bg-green-500 text-white px-4 py-2 rounded-full text-xs font-bold tracking-wide">
        NUEVO
      </div>
      <div v-if="product.discount" class="bg-red-500 text-white px-4 py-2 rounded-full text-xs font-bold tracking-wide">
        -{{ product.discount }}%
      </div>
      <div v-if="product.featured" class="bg-purple-500 text-white px-4 py-2 rounded-full text-xs font-bold tracking-wide">
        DESTACADO
      </div>
    </div>

    <!-- Imagen del producto -->
    <div class="aspect-square bg-gray-100 rounded-t-2xl overflow-hidden relative">
      <div v-if="product.image" class="w-full h-full">
        <img 
          :src="product.image" 
          :alt="product.name"
          class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
        />
      </div>
      <div v-else class="w-full h-full flex items-center justify-center">
        <div class="text-center text-gray-400">
          <div class="w-20 h-20 bg-gradient-to-br from-gray-200 to-gray-300 rounded-full flex items-center justify-center mx-auto mb-4 shadow-md">
            <svg class="w-10 h-10 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M9 21V9l-5-3m5 3l8-4"/>
            </svg>
          </div>
          <p class="text-sm font-medium">{{ product.name }}</p>
        </div>
      </div>
      
      <!-- Overlay gradient -->
      <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
    </div>

    <!-- Contenido -->
    <div class="p-6 text-center">
      <!-- Título y marca -->
      <div class="mb-4">
        <h3 class="text-xl font-bold text-gray-900 mb-2 group-hover:text-black transition-colors">
          {{ product.name }}
        </h3>
        <p v-if="product.brand" class="text-gray-500 text-sm font-semibold tracking-wide">
          {{ product.brand }}
        </p>
      </div>

      <!-- Precio destacado -->
      <div class="mb-4">
        <span class="text-3xl font-bold text-black">
          Bs {{ formatPrice(product.price) }}
        </span>
      </div>

      <!-- Descripción -->
      <p class="text-gray-600 mb-6 leading-relaxed line-clamp-2">
        {{ product.description }}
      </p>

      <!-- Información y características -->
      <div class="space-y-4 mb-6">
        <!-- Rating -->
        <div v-if="product.rating" class="flex items-center justify-center">
          <div class="flex items-center">
            <svg 
              v-for="star in 5" 
              :key="star"
              class="w-5 h-5"
              :class="star <= product.rating ? 'text-yellow-400' : 'text-gray-300'"
              fill="currentColor" 
              viewBox="0 0 20 20"
            >
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
            </svg>
            <span class="text-sm text-gray-600 ml-2 font-medium">
              {{ product.rating.toFixed(1) }}
            </span>
          </div>
        </div>

        <!-- Categoría y Stock -->
        <div class="flex items-center justify-center gap-4 text-sm">
          <div v-if="product.category" class="flex items-center text-gray-600">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"/>
            </svg>
            <span class="font-medium">{{ product.category }}</span>
          </div>
          
          <div class="flex items-center">
            <div class="w-2 h-2 rounded-full mr-2"
                 :class="product.stock > 0 ? 'bg-green-500' : 'bg-red-500'">
            </div>
            <span class="text-sm font-medium"
                  :class="product.stock > 0 ? 'text-green-600' : 'text-red-600'">
              {{ product.stock > 0 ? `${product.stock} disponibles` : 'Agotado' }}
            </span>
          </div>
        </div>

        <!-- Etiquetas -->
        <div v-if="product.tags && product.tags.length > 0" class="flex flex-wrap gap-2 justify-center">
          <span 
            v-for="tag in product.tags" 
            :key="tag"
            class="px-3 py-1 bg-gray-100 text-gray-700 text-xs rounded-full font-medium"
          >
            {{ tag }}
          </span>
        </div>
      </div>

      <!-- Botón de acción -->
      <div class="flex justify-center">
        <button 
          @click="viewProduct"
          class="w-full bg-gray-200 text-gray-800 px-6 py-3 rounded-xl font-semibold text-sm hover:bg-gray-300 transition-all duration-300 transform hover:scale-105"
        >
          Ver Detalles
        </button>
      </div>
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
      return price.toFixed(2)
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
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
