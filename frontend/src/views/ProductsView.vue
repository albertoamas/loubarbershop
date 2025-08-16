<!--
  ProductsView - Vista de productos
  Página que muestra todos los productos disponibles
-->
<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Hero Section -->
    <section class="py-24 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-4">
          <h1 class="text-4xl lg:text-5xl font-bold text-black mb-4">
            Nuestros Productos
          </h1>
          <p class="text-lg text-gray-600 max-w-3xl mx-auto">
            Descubre nuestra selección de productos premium para el cuidado personal masculino, 
            cuidadosamente elegidos para complementar nuestros servicios profesionales.
          </p>
        </div>
      </div>
    </section>

    <!-- Loading State -->
    <div v-if="loading" class="flex justify-center items-center py-16">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900"></div>
    </div>

    <!-- Error State -->
    <div v-if="error" class="text-center py-16">
      <div class="text-red-600 text-lg mb-4">{{ error }}</div>
      <button @click="loadProducts" class="bg-gray-900 text-white px-6 py-2 rounded-lg hover:bg-gray-800">
        Reintentar
      </button>
    </div>

    <!-- Sección de búsqueda y filtros -->
    <section v-if="!loading && !error" class="py-4 bg-gray-100 border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Buscador -->
        <div class="mb-6">
          <div class="max-w-2xl mx-auto">
            <div class="relative">
              <input
                type="text"
                v-model="searchQuery"
                @keyup.enter="searchProducts"
                placeholder="Buscar productos..."
                class="w-full pl-12 pr-4 py-4 bg-gray-50 border border-gray-200 rounded-xl text-gray-900 placeholder-gray-500 focus:ring-2 focus:ring-gray-900 focus:border-transparent focus:outline-none transition-all duration-200"
              >
              <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                </svg>
              </div>
            </div>
          </div>
        </div>

        <!-- Filtros -->
        <div class="flex flex-wrap gap-3 justify-center">
          <button 
            :class="activeFilter === 'all' ? 'bg-gray-900 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'"
            @click="filterByCategory('all')"
            class="px-6 py-3 rounded-xl font-medium transition-all duration-200"
          >
            Todos
          </button>
          <button 
            v-for="category in categories.filter(cat => cat !== 'all')"
            :key="category"
            :class="activeFilter === category ? 'bg-gray-900 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'"
            @click="filterByCategory(category)"
            class="px-6 py-3 rounded-xl font-medium transition-all duration-200"
          >
            {{ category }}
          </button>
        </div>

        <!-- Resultados encontrados -->
        <div class="mt-6 text-center">
          <p class="text-gray-600">
            {{ filteredProducts.length }} {{ filteredProducts.length === 1 ? 'producto encontrado' : 'productos encontrados' }}
          </p>
        </div>
      </div>
    </section>

    <!-- Grid de productos -->
    <section v-if="!loading && !error" class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div v-if="filteredProducts.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <ProductCard 
            v-for="product in filteredProducts"
            :key="product.id"
            :product="product"
            @view-product="handleProductView"
          />
        </div>
        
        <!-- Mensaje cuando no hay productos -->
        <div v-else class="text-center py-12">
          <svg class="w-16 h-16 text-gray-300 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M9 21V9l-5-3m5 3l8-4"/>
          </svg>
          <h3 class="text-xl font-semibold text-gray-900 mb-2">No se encontraron productos</h3>
          <p class="text-gray-500 mb-6">Intenta con otros términos de búsqueda o filtros</p>
          <button 
            @click="clearFilters"
            class="bg-gray-200 text-gray-800 px-6 py-3 rounded-xl font-medium hover:bg-gray-300 transition-all duration-200"
          >
            Limpiar filtros
          </button>
        </div>
      </div>
    </section>

    <!-- Sección de información adicional -->
    <section class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 class="text-3xl lg:text-4xl font-bold text-gray-900 mb-6">
              ¿Por qué elegir nuestros productos?
            </h2>
            <div class="space-y-6">
              <div class="flex items-start space-x-4">
                <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="text-xl font-semibold text-gray-900 mb-2">
                    Calidad Premium
                  </h3>
                  <p class="text-gray-600">
                    Todos nuestros productos son de marcas reconocidas y alta calidad.
                  </p>
                </div>
              </div>
              
              <div class="flex items-start space-x-4">
                <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="text-xl font-semibold text-gray-900 mb-2">
                    Ingredientes Naturales
                  </h3>
                  <p class="text-gray-600">
                    Priorizamos productos con ingredientes naturales que cuiden tu piel y cabello.
                  </p>
                </div>
              </div>
              
              <div class="flex items-start space-x-4">
                <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="text-xl font-semibold text-gray-900 mb-2">
                    Resultados Garantizados
                  </h3>
                  <p class="text-gray-600">
                    Productos probados y recomendados por nuestros barberos profesionales.
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Imagen placeholder -->
          <div class="aspect-video lg:aspect-square bg-gray-200 rounded-lg overflow-hidden">
            <div class="w-full h-full bg-gradient-to-br from-gray-100 to-gray-300 flex items-center justify-center">
              <div class="text-center text-gray-500">
                <svg class="w-16 h-16 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M9 21V9l-5-3m5 3l8-4"/>
                </svg>
                <p class="text-sm">Productos de calidad</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import ProductCard from '@/components/ProductCard.vue'
import { productService } from '../services/index.js'

export default {
  name: 'ProductsView',
  components: {
    ProductCard
  },
  data() {
    return {
      searchQuery: '',
      activeFilter: 'all',
      allProducts: [],
      loading: true,
      error: null
    }
  },
  
  computed: {
    categories() {
      if (!this.allProducts.length) return ['all']
      
      const categories = ['all']
      const uniqueCategories = [...new Set(this.allProducts.map(product => product.categoria || product.category))]
      return categories.concat(uniqueCategories)
    },
    
    filteredProducts() {
      let filtered = this.allProducts
      
      // Filtrar por categoría
      if (this.activeFilter !== 'all') {
        filtered = filtered.filter(product => 
          (product.categoria || product.category) === this.activeFilter
        )
      }
      
      // Filtrar por búsqueda
      if (this.searchQuery.trim()) {
        const query = this.searchQuery.toLowerCase()
        filtered = filtered.filter(product =>
          product.name.toLowerCase().includes(query) ||
          product.description.toLowerCase().includes(query) ||
          (product.marca && product.marca.toLowerCase().includes(query))
        )
      }
      
      return filtered
    }
  },
  
  async mounted() {
    await this.loadProducts()
  },
  
  methods: {
    async loadProducts() {
      this.loading = true
      this.error = null
      
      console.log('🔄 Iniciando carga de productos...')
      
      try {
        const response = await productService.getProducts()
        
        console.log('📦 Respuesta del productService:', response)
        
        if (response.success) {
          console.log('✅ Productos del backend:', response.data)
          console.log('📄 Respuesta completa:', JSON.stringify(response, null, 2))
          this.allProducts = response.data.map(product => ({
            id: product.id,
            name: product.nombre,
            description: product.descripcion || 'Sin descripción disponible',
            price: parseFloat(product.precio) || 0,
            brand: product.marca || 'Sin marca',
            category: product.categoria || 'General',
            stock: product.stock || 0,
            rating: product.rating || 4.0,
            featured: product.destacado || false,
            isNew: product.nuevo || false,
            active: product.activo,
            image: product.imagen_url || product.imagen,
            tags: product.tags ? product.tags.split(',') : [(product.categoria || 'General')]
          }))
          console.log('🎯 Productos mapeados:', this.allProducts)
        } else {
          console.log('❌ Error en respuesta del backend:', response.message)
          this.error = response.message
          this.loadFallbackProducts()
        }
      } catch (error) {
        console.error('💥 Error al cargar productos:', error)
        this.error = 'Error al conectar con el servidor'
        this.loadFallbackProducts()
      } finally {
        this.loading = false
      }
    },
    
    loadFallbackProducts() {
      console.log('🚨 Cargando productos de fallback...')
      // Productos de ejemplo como fallback
      this.allProducts = [
        {
          id: 1,
          name: 'Pomada Fijadora',
          description: 'Pomada de alta calidad para un peinado duradero y con brillo natural.',
          price: 35.00,
          brand: 'Premium Hair',
          category: 'Styling',
          stock: 15,
          rating: 4.5,
          featured: true,
          tags: ['Fijación', 'Brillo']
        },
        {
          id: 2,
          name: 'Shampoo Anticaspa',
          description: 'Shampoo especializado para combatir la caspa con ingredientes naturales.',
          price: 28.00,
          brand: 'Natural Care',
          category: 'Cuidado',
          stock: 8,
          rating: 4.2,
          isNew: true,
          tags: ['Anticaspa', 'Natural']
        },
        {
          id: 3,
          name: 'Aceite para Barba',
          description: 'Aceite nutritivo para barba que suaviza y da brillo natural.',
          price: 45.00,
          brand: 'Beard Master',
          category: 'Barba',
          stock: 12,
          rating: 4.8,
          featured: true,
          tags: ['Barba', 'Nutritivo']
        },
        {
          id: 4,
          name: 'Crema de Afeitar',
          description: 'Crema hidratante para un afeitado suave y sin irritaciones.',
          price: 22.00,
          brand: 'Smooth Shave',
          category: 'Afeitado',
          stock: 20,
          rating: 4.3,
          tags: ['Afeitado', 'Hidratante']
        }
      ]
      console.log('📦 Productos fallback cargados:', this.allProducts)
    },
    
    async searchProducts() {
      if (this.searchQuery.trim()) {
        try {
          const response = await productService.searchProducts(this.searchQuery)
          if (response.success) {
            this.allProducts = response.data
          }
        } catch (error) {
          console.error('Error en búsqueda:', error)
        }
      } else {
        await this.loadProducts()
      }
    },
    
    async filterByCategory(category) {
      this.activeFilter = category
      
      if (category === 'all') {
        await this.loadProducts()
      } else {
        try {
          const response = await productService.getProductsByCategory(category)
          if (response.success) {
            this.allProducts = response.data
          }
        } catch (error) {
          console.error('Error al filtrar:', error)
        }
      }
    },
    
    handleProductView(product) {
      console.log('🛍️ Producto seleccionado:', product)
      // Aquí podrías manejar la lógica adicional para la vista del producto
    },
    
    clearFilters() {
      this.searchQuery = ''
      this.activeFilter = 'all'
      this.loadProducts()
    }
  }
}
</script>
