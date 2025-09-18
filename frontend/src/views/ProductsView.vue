<!--
  ProductsView - Vista de productos rediseñada
  Página que muestra todos los productos disponibles con diseño moderno
-->
<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Hero Section Mejorado con variables CSS v4 -->
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
              🛍️ Low BarberShop
            </div>
            <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold text-white mb-4 leading-tight">
              Nuestros 
              <span class="bg-gradient-to-r from-[var(--color-barber-gold)] to-yellow-300 bg-clip-text text-transparent">
                Productos
              </span>
            </h1>
          </div>
          
          <!-- Descripción mejorada -->
          <p class="text-gray-300 max-w-3xl mx-auto text-lg md:text-xl leading-relaxed">
            Productos profesionales de las mejores marcas para el cuidado masculino premium
          </p>
          
          <!-- Estadísticas rápidas -->
          <div class="grid grid-cols-3 gap-4 md:gap-8 max-w-2xl mx-auto mt-12">
            <div class="text-center">
              <div class="text-2xl md:text-3xl font-bold text-[var(--color-barber-gold)] mb-1">100%</div>
              <div class="text-gray-300 text-sm md:text-base">Originales</div>
            </div>
            <div class="text-center">
              <div class="text-2xl md:text-3xl font-bold text-[var(--color-barber-gold)] mb-1">Premium</div>
              <div class="text-gray-300 text-sm md:text-base">Calidad</div>
            </div>
            <div class="text-center">
              <div class="text-2xl md:text-3xl font-bold text-[var(--color-barber-gold)] mb-1">24h</div>
              <div class="text-gray-300 text-sm md:text-base">Entrega</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Loading State Mejorado -->
    <div v-if="loading" class="flex flex-col justify-center items-center py-24">
      <div class="relative">
        <div class="animate-spin rounded-full h-16 w-16 border-4 border-gray-200"></div>
        <div class="animate-spin rounded-full h-16 w-16 border-4 border-[var(--color-barber-primary)] border-t-transparent absolute inset-0"></div>
      </div>
      <p class="text-gray-600 text-lg font-medium mt-6">Cargando productos premium...</p>
    </div>

    <!-- Error State Mejorado -->
    <div v-if="error" class="text-center py-24">
      <div class="max-w-md mx-auto">
        <div class="w-16 h-16 bg-yellow-100 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-3">Error al cargar productos</h3>
        <p class="text-gray-600 mb-6">{{ error }}</p>
        <button 
          @click="loadProducts" 
          class="bg-[var(--color-barber-primary)] text-white px-8 py-3 rounded-lg hover:bg-[var(--color-barber-gold)] transition-all duration-200 transform hover:scale-105 shadow-lg"
        >
          Reintentar
        </button>
      </div>
    </div>

    <!-- Sección de estadísticas modernizada -->
    <section v-if="!loading && !error" class="py-12 bg-gradient-to-br from-white to-gray-50 border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Título de la sección -->
        <div class="text-center mb-10">
          <div class="inline-flex items-center justify-center px-4 py-2 bg-[var(--color-barber-primary)] text-white rounded-full text-sm font-medium mb-4">
            📈 Nuestros Números
          </div>
          <h2 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">
            Productos de Confianza
          </h2>
          <div class="w-16 h-1 bg-gradient-to-r from-[var(--color-barber-gold)] to-yellow-300 mx-auto rounded-full"></div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Productos Disponibles -->
          <div class="group text-center bg-white rounded-3xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 border border-gray-100">
            <div class="w-16 h-16 bg-gradient-to-br from-[var(--color-barber-primary)] to-gray-700 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M9 9h6m-6 4h6"/>
              </svg>
            </div>
            <div class="text-4xl lg:text-5xl font-bold text-[var(--color-barber-primary)] mb-2 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
              {{ allProducts.length }}
            </div>
            <div class="text-sm lg:text-base text-gray-600 font-medium tracking-wide uppercase">
              Productos Premium
            </div>
            <p class="text-gray-500 text-sm mt-2">
              Marcas reconocidas internacionalmente
            </p>
          </div>
          
          <!-- Marcas Originales -->
          <div class="group text-center bg-white rounded-3xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 border border-gray-100">
            <div class="w-16 h-16 bg-gradient-to-br from-[var(--color-barber-gold)] to-yellow-400 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <div class="text-4xl lg:text-5xl font-bold text-[var(--color-barber-primary)] mb-2 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
              100%
            </div>
            <div class="text-sm lg:text-base text-gray-600 font-medium tracking-wide uppercase">
              Productos Originales
            </div>
            <p class="text-gray-500 text-sm mt-2">
              Garantizamos su autenticidad
            </p>
          </div>
          
          <!-- Envío Rápido -->
          <div class="group text-center bg-white rounded-3xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 border border-gray-100">
            <div class="w-16 h-16 bg-gradient-to-br from-green-500 to-emerald-600 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <div class="text-4xl lg:text-5xl font-bold text-[var(--color-barber-primary)] mb-2 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
              24h
            </div>
            <div class="text-sm lg:text-base text-gray-600 font-medium tracking-wide uppercase">
              Envío Express
            </div>
            <p class="text-gray-500 text-sm mt-2">
              Recíbelo al día siguiente
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Sección de búsqueda y filtros mejorada -->
    <section v-if="!loading && !error" class="py-8 bg-gradient-to-br from-gray-50 to-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Barra de búsqueda mejorada con variables CSS v4 -->
        <div class="mb-8">
          <div class="max-w-3xl mx-auto">
            <div class="relative group">

              <!-- Input principal -->
              <div class="relative bg-white rounded-2xl shadow-lg border border-gray-200 overflow-hidden">
                <input
                  type="text"
                  v-model="searchQuery"
                  @keyup.enter="searchProducts"
                  placeholder="¿Qué producto estás buscando hoy?"
                  class="w-full pl-14 pr-16 py-5 bg-transparent text-gray-900 placeholder-gray-500 focus:outline-none text-lg"
                >
                
                <!-- Icono de búsqueda -->
                <div class="absolute inset-y-0 left-0 pl-5 flex items-center pointer-events-none">
                  <svg class="h-6 w-6 text-gray-400 group-hover:text-[var(--color-barber-gold)] transition-colors duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                  </svg>
                </div>
                
                <!-- Botón de búsqueda -->
                <div class="absolute inset-y-0 right-0 pr-2 flex items-center">
                  <button 
                    @click="searchProducts"
                    class="bg-[var(--color-barber-primary)] hover:bg-[var(--color-barber-gold)] text-white px-6 py-2 rounded-xl font-medium transition-all duration-200 transform hover:scale-105 shadow-md"
                  >
                    Buscar
                  </button>
                </div>
              </div>
              
              <!-- Texto de ayuda -->
              <div class="mt-2 text-center">
                <p class="text-sm text-gray-500">
                  Busca por nombre, marca o categoría de producto
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Filtros modernizados -->
        <div class="max-w-5xl mx-auto">
          <!-- Título de filtros -->
          <div class="text-center mb-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Filtrar por categoría</h3>
            <div class="w-16 h-1 bg-gradient-to-r from-[var(--color-barber-gold)] to-[var(--color-barber-primary)] mx-auto rounded-full"></div>
          </div>
          
          <!-- Contenedor de filtros con diseño de tarjetas -->
          <div class="bg-white rounded-3xl shadow-lg border border-gray-100 p-6 md:p-8">
            <div class="flex flex-wrap gap-3 justify-center">
              <!-- Botón "Todos" con variables CSS -->
              <button 
                :class="activeFilter === 'all' ? 'bg-[var(--color-barber-primary)] text-white shadow-xl scale-105' : 'bg-gray-50 text-gray-700 hover:bg-gray-100 hover:shadow-md'"
                @click="filterByCategory('all')"
                class="group px-8 py-4 rounded-2xl font-medium transition-all duration-300 transform hover:scale-105 border border-gray-200"
              >
                <span class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded-full flex items-center justify-center"
                       :class="activeFilter === 'all' ? 'bg-white/20' : 'bg-[var(--color-barber-gold)]'">
                    <svg class="w-4 h-4" :class="activeFilter === 'all' ? 'text-white' : 'text-white'" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M3 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"/>
                    </svg>
                  </div>
                  <span class="text-base">Todos los productos</span>
                  <div v-if="activeFilter === 'all'" class="w-2 h-2 bg-[var(--color-barber-gold)] rounded-full animate-pulse"></div>
                </span>
              </button>

              <!-- Botones de categorías con variables CSS -->
              <button 
                v-for="category in categories.filter(cat => cat !== 'all')"
                :key="category"
                :class="activeFilter === category ? 'bg-[var(--color-barber-primary)] text-white shadow-xl scale-105' : 'bg-gray-50 text-gray-700 hover:bg-gray-100 hover:shadow-md'"
                @click="filterByCategory(category)"
                class="group px-8 py-4 rounded-2xl font-medium transition-all duration-300 transform hover:scale-105 border border-gray-200 capitalize"
              >
                <span class="flex items-center gap-3">
                  <!-- Icono dinámico por categoría -->
                  <div class="w-8 h-8 rounded-full flex items-center justify-center"
                       :class="activeFilter === category ? 'bg-white/20' : 'bg-[var(--color-barber-gold)]'">
                    <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path v-if="category === 'styling'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zM7 3H6a1 1 0 00-1 1v13a2 2 0 104 0V4a1 1 0 00-1-1zM21 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4z"/>
                      <path v-else-if="category === 'barba'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                      <path v-else-if="category === 'cuidado'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                      <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"/>
                    </svg>
                  </div>
                  <span class="text-base">{{ category }}</span>
                  <div v-if="activeFilter === category" class="w-2 h-2 bg-[var(--color-barber-gold)] rounded-full animate-pulse"></div>
                </span>
              </button>
            </div>
            
            <!-- Información de resultados -->
            <div class="mt-6 text-center">
              <div class="inline-flex items-center gap-2 bg-gray-50 px-4 py-2 rounded-full">
                <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <span class="text-sm text-gray-600 font-medium">
                  {{ filteredProducts.length }} {{ filteredProducts.length === 1 ? 'producto encontrado' : 'productos encontrados' }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Grid de productos modernizado -->
    <section v-if="!loading && !error" class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Título de la sección -->
        <div class="text-center mb-16">
          <div class="inline-flex items-center justify-center px-4 py-2 bg-[var(--color-barber-gold)] text-[var(--color-barber-primary)] rounded-full text-sm font-bold mb-4 shadow-lg">
            🛍️ Productos Premium
          </div>
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Tu Estilo, Nuestra Pasión
          </h2>
          <div class="w-20 h-1 bg-gradient-to-r from-[var(--color-barber-gold)] to-yellow-300 mx-auto rounded-full mb-6"></div>
          <p class="text-gray-600 max-w-2xl mx-auto text-lg">
            Descubre nuestra selección de productos premium seleccionados especialmente para el cuidado masculino
          </p>
        </div>

        <!-- Mensaje cuando no hay productos -->
        <div v-if="filteredProducts.length === 0" class="text-center py-20">
          <div class="max-w-md mx-auto">
            <div class="w-24 h-24 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-8">
              <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M9 9h6m-6 4h6"/>
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-gray-900 mb-4">No encontramos productos</h3>
            <p class="text-gray-600 mb-8 leading-relaxed">
              No hay productos que coincidan con tu búsqueda actual.<br>
              Intenta con otros términos o explora nuestras categorías.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
              <button 
                @click="clearFilters"
                class="bg-[var(--color-barber-primary)] text-white px-8 py-3 rounded-lg font-medium hover:bg-[var(--color-barber-gold)] transition-all duration-200 shadow-lg"
              >
                Ver todos los productos
              </button>
              <button 
                @click="searchQuery = ''"
                class="bg-gray-100 text-gray-700 px-8 py-3 rounded-lg font-medium hover:bg-gray-200 transition-all duration-200"
              >
                Limpiar búsqueda
              </button>
            </div>
          </div>
        </div>

        <!-- Grid de productos -->
        <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-10">
          <div 
            v-for="product in filteredProducts"
            :key="product.id"
            class="group transform transition-all duration-300 hover:-translate-y-2"
          >
            <ProductCard 
              :product="product"
              @view-product="handleProductView"
              class="h-full shadow-lg hover:shadow-2xl transition-shadow duration-300"
            />
          </div>
        </div>
      </div>
    </section>

    <!-- Sección de información adicional modernizada -->
    <section class="py-20 bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 relative overflow-hidden">
      <!-- Elementos decorativos de fondo -->
      <div class="absolute inset-0">
        <div class="absolute top-10 left-10 w-32 h-32 bg-white/5 rounded-full blur-xl"></div>
        <div class="absolute bottom-10 right-10 w-48 h-48 bg-[var(--color-barber-gold)]/10 rounded-full blur-2xl"></div>
        <div class="absolute top-1/2 left-1/4 w-16 h-16 bg-white/10 rounded-full blur-lg"></div>
      </div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <!-- Contenido principal -->
          <div>
            <div class="mb-8">
              <div class="inline-flex items-center justify-center px-4 py-2 bg-[var(--color-barber-gold)] text-[var(--color-barber-primary)] rounded-full text-sm font-bold mb-6 shadow-lg">
                🏆 Calidad Premium
              </div>
              <h2 class="text-4xl lg:text-5xl font-bold text-white mb-6 leading-tight">
                ¿Por qué elegir nuestros 
                <span class="bg-gradient-to-r from-[var(--color-barber-gold)] to-yellow-300 bg-clip-text text-transparent">
                  productos?
                </span>
              </h2>
              <p class="text-gray-300 text-lg leading-relaxed">
                Cada producto en nuestra selección ha sido cuidadosamente elegido por su calidad excepcional y resultados comprobados.
              </p>
            </div>

            <div class="space-y-8">
              <!-- Productos Originales -->
              <div class="flex items-start space-x-6 group">
                <div class="flex-shrink-0">
                  <div class="w-16 h-16 bg-gradient-to-br from-[var(--color-barber-primary)] to-gray-700 rounded-2xl flex items-center justify-center backdrop-blur-sm border border-white/10 group-hover:scale-110 transition-transform duration-300">
                    <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                  </div>
                </div>
                <div>
                  <h3 class="text-xl font-bold text-white mb-3 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
                    100% Originales
                  </h3>
                  <p class="text-gray-300 leading-relaxed">
                    Garantizamos la autenticidad de todos nuestros productos. Trabajamos directamente con distribuidores autorizados de las mejores marcas.
                  </p>
                </div>
              </div>
              
              <!-- Marcas Premium -->
              <div class="flex items-start space-x-6 group">
                <div class="flex-shrink-0">
                  <div class="w-16 h-16 bg-gradient-to-br from-[var(--color-barber-gold)] to-yellow-500 rounded-2xl flex items-center justify-center backdrop-blur-sm border border-white/10 group-hover:scale-110 transition-transform duration-300">
                    <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/>
                    </svg>
                  </div>
                </div>
                <div>
                  <h3 class="text-xl font-bold text-white mb-3 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
                    Marcas Reconocidas
                  </h3>
                  <p class="text-gray-300 leading-relaxed">
                    Seleccionamos cuidadosamente productos de marcas líderes en el mercado internacional del cuidado masculino y barbería profesional.
                  </p>
                </div>
              </div>
              
              <!-- Envío Rápido -->
              <div class="flex items-start space-x-6 group">
                <div class="flex-shrink-0">
                  <div class="w-16 h-16 bg-gradient-to-br from-blue-600 to-indigo-700 rounded-2xl flex items-center justify-center backdrop-blur-sm border border-white/10 group-hover:scale-110 transition-transform duration-300">
                    <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                    </svg>
                  </div>
                </div>
                <div>
                  <h3 class="text-xl font-bold text-white mb-3 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
                    Entrega Express
                  </h3>
                  <p class="text-gray-300 leading-relaxed">
                    Envío en 24-48 horas a todo el país. Empaquetado seguro y discreto para proteger tus productos hasta tu puerta.
                  </p>
                </div>
              </div>

              <!-- Asesoría Personalizada -->
              <div class="flex items-start space-x-6 group">
                <div class="flex-shrink-0">
                  <div class="w-16 h-16 bg-gradient-to-br from-purple-600 to-pink-600 rounded-2xl flex items-center justify-center backdrop-blur-sm border border-white/10 group-hover:scale-110 transition-transform duration-300">
                    <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
                    </svg>
                  </div>
                </div>
                <div>
                  <h3 class="text-xl font-bold text-white mb-3 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
                    Asesoría Experta
                  </h3>
                  <p class="text-gray-300 leading-relaxed">
                    Nuestros barberos profesionales te ayudan a elegir los productos perfectos para tu tipo de cabello y estilo personal.
                  </p>
                </div>
              </div>
            </div>

            <!-- Call to Action -->
            <div class="mt-12 pt-8 border-t border-white/20">
              <div class="flex flex-col sm:flex-row gap-4">
                <button class="flex-1 bg-[var(--color-barber-gold)] text-[var(--color-barber-primary)] px-8 py-4 rounded-2xl font-bold hover:bg-yellow-300 transition-all duration-200 transform hover:scale-105 shadow-lg">
                  Ver Catálogo
                </button>
                <button class="flex-1 bg-transparent border-2 border-white/30 text-white px-8 py-4 rounded-2xl font-bold hover:bg-white/10 transition-all duration-200">
                  Contactar
                </button>
              </div>
            </div>
          </div>

          <!-- Imagen/Estadísticas -->
          <div class="relative">
            <div class="bg-gradient-to-br from-white/10 to-white/5 backdrop-blur-sm border border-white/20 rounded-3xl p-8 shadow-2xl">
              <!-- Estadísticas Grid -->
              <div class="grid grid-cols-2 gap-8 mb-8">
                <div class="text-center">
                  <div class="text-4xl font-bold text-white mb-2">50+</div>
                  <div class="text-gray-300 text-sm">Marcas premium</div>
                </div>
                <div class="text-center">
                  <div class="text-4xl font-bold text-white mb-2">1K+</div>
                  <div class="text-gray-300 text-sm">Productos vendidos</div>
                </div>
                <div class="text-center">
                  <div class="text-4xl font-bold text-white mb-2">98%</div>
                  <div class="text-gray-300 text-sm">Satisfacción</div>
                </div>
                <div class="text-center">
                  <div class="text-4xl font-bold text-white mb-2">24h</div>
                  <div class="text-gray-300 text-sm">Envío express</div>
                </div>
              </div>
              
              <!-- Separador -->
              <div class="border-t border-white/20 mb-8"></div>
              
              <!-- Contacto rápido -->
              <div class="text-center">
                <h4 class="text-lg font-bold text-white mb-6">¿Necesitas recomendaciones?</h4>
                <div class="space-y-4">
                  <div class="flex items-center justify-center space-x-3">
                    <div class="w-10 h-10 bg-[var(--color-barber-gold)] rounded-full flex items-center justify-center">
                      <svg class="w-5 h-5 text-[var(--color-barber-primary)]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                      </svg>
                    </div>
                    <span class="text-white font-medium">+591 77872911</span>
                  </div>
                  <div class="flex items-center justify-center space-x-3">
                    <div class="w-10 h-10 bg-green-500 rounded-full flex items-center justify-center">
                      <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/>
                        <path d="M11.893 0C5.333 0 0 5.333 0 11.893c0 2.096.547 4.142 1.588 5.946L.057 24l6.305-1.654C8.098 23.5 10.059 24 12.05 24c6.557 0 11.890-5.335 11.893-11.892C23.946 5.651 18.61.344 12.05.343 11.997.343 11.945.343 11.893 0z"/>
                      </svg>
                    </div>
                    <span class="text-white font-medium">WhatsApp</span>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Elemento decorativo -->
            <div class="absolute -bottom-6 -right-6 w-24 h-24 bg-[var(--color-barber-gold)]/20 rounded-full blur-2xl"></div>
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
