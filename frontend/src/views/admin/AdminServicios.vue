<!--
  AdminServicios.vue - Gestión completa de servicios
  FASE 8.7: Rediseño minimalista y moderno
-->
<template>
  <div class="p-8 bg-gradient-to-br from-slate-50 to-slate-100 min-h-[calc(100vh-5rem)]">
    <!-- Header del dashboard modernizado -->
    <div class="mb-6 bg-white rounded-2xl p-6 shadow-sm border border-gray-200">
      <div class="flex flex-col lg:flex-row lg:justify-between lg:items-start gap-6">
        <div class="flex-1">
          <h1 class="text-3xl font-extrabold bg-gradient-to-r from-black to-gray-500 bg-clip-text text-transparent mb-2">
            Gestión de Servicios
          </h1>
          <p class="text-lg text-gray-600 font-medium">
            Administra el catálogo de servicios de Low Barber Shop
          </p>
        </div>
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
          <button 
            @click="loadServices" 
            :disabled="loading"
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-black to-gray-500 text-white border-none rounded-xl font-semibold text-sm cursor-pointer transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5 disabled:opacity-70 disabled:cursor-not-allowed disabled:transform-none"
          >
            <svg :class="{ 'animate-spin': loading }" class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            {{ loading ? 'Actualizando...' : 'Actualizar' }}
          </button>
          <button 
            class="flex items-center px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white rounded-xl font-semibold text-sm transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5 hover:from-purple-600 hover:to-violet-700"
            @click="openCreateModal"
          >
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
            </svg>
            Nuevo Servicio
          </button>
        </div>
      </div>
    </div>

    <!-- Grid de estadísticas modernizado -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
      <!-- Total servicios -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Total</h3>
            <p class="text-3xl font-black text-blue-600">{{ stats.totalServices || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-blue-100 to-blue-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Servicios activos -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Activos</h3>
            <p class="text-3xl font-black text-green-600">{{ stats.activeServices || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-green-100 to-green-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Servicios inactivos -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Inactivos</h3>
            <p class="text-3xl font-black text-orange-600">{{ stats.totalServices - stats.activeServices || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-orange-100 to-orange-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Precio promedio -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Promedio</h3>
            <p class="text-3xl font-black text-purple-600">Bs {{ formatPrice(stats.avgRevenue || 0) }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-purple-100 to-purple-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Filtros modernizados -->
    <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200 mb-6">
      <div class="flex flex-col gap-4">
        <!-- Fila 1: Búsqueda -->
        <div class="flex flex-col sm:flex-row gap-4 items-stretch">
          <div class="flex-1 relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <input
              v-model="filters.search"
              type="text"
              placeholder="Buscar por nombre o descripción del servicio..."
              class="w-full pl-12 pr-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
            />
            <button 
              v-if="filters.search"
              @click="filters.search = ''"
              class="absolute inset-y-0 right-0 pr-4 flex items-center text-gray-400 hover:text-gray-600"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <button 
            @click="clearFilters"
            class="px-6 py-3.5 bg-gray-100 text-gray-700 border border-gray-300 rounded-xl font-medium text-sm hover:bg-gray-200 transition-all duration-200 whitespace-nowrap"
          >
            <svg class="w-4 h-4 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            Limpiar
          </button>
        </div>

        <!-- Fila 2: Filtros -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <!-- Filtro por Categoría -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Categoría</label>
            <select 
              v-model="filters.category"
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
              @change="applyFilters"
            >
              <option value="">Todas las categorías</option>
              <option value="cortes">Cortes</option>
              <option value="barbas">Barbas</option>
              <option value="tratamientos">Tratamientos</option>
              <option value="combos">Combos</option>
            </select>
          </div>

          <!-- Filtro por Estado -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Estado</label>
            <select 
              v-model="filters.status"
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
              @change="applyFilters"
            >
              <option value="">Todos los estados</option>
              <option value="active">Activos</option>
              <option value="inactive">Inactivos</option>
            </select>
          </div>

          <!-- Filtro por Rango de Precio -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Rango de Precio</label>
            <select 
              v-model="filters.priceRange"
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
              @change="applyFilters"
            >
              <option value="">Todos los precios</option>
              <option value="0-30000">Bs 0 - Bs 30,000</option>
              <option value="30000-50000">Bs 30,000 - Bs 50,000</option>
              <option value="50000-100000">Bs 50,000+</option>
            </select>
          </div>
        </div>

        <!-- Indicadores de filtros activos -->
        <div v-if="hasActiveFilters" class="flex flex-wrap gap-2 items-center pt-2 border-t border-gray-200">
          <span class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Filtros activos:</span>
          
          <span v-if="filters.search" class="inline-flex items-center gap-1 px-3 py-1 bg-violet-100 text-violet-700 rounded-full text-xs font-medium">
            Búsqueda: "{{ filters.search }}"
            <button @click="filters.search = ''" class="hover:text-violet-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>
          
          <span v-if="filters.category" class="inline-flex items-center gap-1 px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-medium">
            Categoría: {{ getCategoryLabel(filters.category) }}
            <button @click="filters.category = ''; applyFilters()" class="hover:text-blue-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>
          
          <span v-if="filters.status" class="inline-flex items-center gap-1 px-3 py-1 bg-green-100 text-green-700 rounded-full text-xs font-medium">
            Estado: {{ getStatusLabel(filters.status) }}
            <button @click="filters.status = ''; applyFilters()" class="hover:text-green-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>
          
          <span v-if="filters.priceRange" class="inline-flex items-center gap-1 px-3 py-1 bg-orange-100 text-orange-700 rounded-full text-xs font-medium">
            Precio: {{ getPriceRangeLabel(filters.priceRange) }}
            <button @click="filters.priceRange = ''; applyFilters()" class="hover:text-orange-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>

          <span class="text-xs text-gray-500 ml-auto">
            {{ filteredServices.length }} resultado{{ filteredServices.length !== 1 ? 's' : '' }}
          </span>
        </div>
      </div>
    </div>

    <!-- Grid de servicios modernizado con Tailwind v4 -->
    <div class="bg-white rounded-2xl p-4 sm:p-6 lg:p-8 shadow-sm border border-slate-200">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 sm:gap-6">
        <div
          v-for="service in paginatedServices"
          :key="service.id"
          class="bg-gradient-to-br from-white to-slate-50 border border-slate-200 rounded-2xl p-4 sm:p-5 hover:shadow-lg hover:-translate-y-1 transition-all duration-300 cursor-pointer group flex flex-col"
          @click="selectService(service)"
        >
          <!-- Imagen del servicio -->
          <div class="relative mb-3 sm:mb-4">
            <img 
              :src="service.image || getDefaultServiceImage(service.category)" 
              :alt="service.name"
              class="w-full h-28 sm:h-32 object-cover rounded-xl border border-slate-200"
            />
            <div class="absolute top-2 sm:top-3 right-2 sm:right-3">
              <div :class="[
                'inline-flex items-center gap-1 sm:gap-1.5 px-2 sm:px-3 py-1 sm:py-1.5 rounded-lg text-[10px] sm:text-xs font-semibold',
                service.status === 'active' 
                  ? 'bg-emerald-100 text-emerald-700' 
                  : 'bg-red-100 text-red-700'
              ]">
                <div :class="[
                  'w-1.5 sm:w-2 h-1.5 sm:h-2 rounded-full',
                  service.status === 'active' ? 'bg-emerald-500' : 'bg-red-500'
                ]"></div>
                <span class="hidden sm:inline">{{ service.status === 'active' ? 'Activo' : 'Inactivo' }}</span>
              </div>
            </div>
          </div>

          <!-- Información del servicio - Flex grow para empujar los botones abajo -->
          <div class="flex flex-col flex-grow space-y-2.5 sm:space-y-3">
            <!-- Header con nombre y categoría -->
            <div class="flex flex-col gap-2">
              <div class="flex items-start justify-between gap-2">
                <h3 class="text-sm sm:text-base font-bold text-slate-800 leading-tight group-hover:text-black transition-colors duration-200 line-clamp-2 flex-1">
                  {{ service.name }}
                </h3>
                <span :class="[
                  'inline-flex shrink-0 px-2 py-0.5 rounded-lg text-[9px] sm:text-[10px] font-semibold uppercase tracking-wide whitespace-nowrap',
                  getCategoryBadgeClass(service.category || 'default')
                ]">
                  {{ getCategoryLabel(service.category) }}
                </span>
              </div>
            </div>

            <!-- Descripción -->
            <p class="text-xs sm:text-sm text-slate-600 line-clamp-2 min-h-[2.5rem]">
              {{ service.description || 'Sin descripción' }}
            </p>

            <!-- Detalles en grid -->
            <div class="grid grid-cols-2 gap-2 sm:gap-3 py-2">
              <div>
                <span class="block text-[10px] sm:text-xs font-medium text-slate-500 mb-0.5">Precio</span>
                <span class="text-sm sm:text-base font-bold text-violet-600">Bs {{ formatPrice(service.price || 0) }}</span>
              </div>
              <div>
                <span class="block text-[10px] sm:text-xs font-medium text-slate-500 mb-0.5">Duración</span>
                <span class="text-sm sm:text-base font-semibold text-slate-800">{{ service.duration || 0 }} min</span>
              </div>
            </div>

            <!-- Acciones - Siempre al final con mt-auto -->
            <div class="flex flex-col gap-1.5 pt-2 mt-auto border-t border-slate-100">
              <div class="flex gap-1.5">
                <button 
                  @click.stop="viewService(service)" 
                  class="flex items-center justify-center gap-1 px-2 py-1.5 text-[10px] sm:text-xs font-medium border rounded-lg transition-all duration-200 bg-blue-50 text-blue-700 border-blue-200 hover:bg-blue-100 hover:border-blue-300 flex-1"
                  title="Ver detalles"
                >
                  <svg class="w-3 h-3 sm:w-3.5 sm:h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                  </svg>
                  <span class="hidden sm:inline">Ver</span>
                </button>
                
                <button 
                  @click.stop="editService(service)" 
                  class="flex items-center justify-center gap-1 px-2 py-1.5 text-[10px] sm:text-xs font-medium border rounded-lg transition-all duration-200 bg-amber-50 text-amber-700 border-amber-200 hover:bg-amber-100 hover:border-amber-300 flex-1"
                  title="Editar servicio"
                >
                  <svg class="w-3 h-3 sm:w-3.5 sm:h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                  </svg>
                  <span class="hidden sm:inline">Editar</span>
                </button>
              </div>
              
              <button 
                @click.stop="toggleServiceStatus(service)" 
                :class="[
                  'flex items-center justify-center gap-1 px-2 py-1.5 text-[10px] sm:text-xs font-medium border rounded-lg transition-all duration-200 w-full',
                  service.status === 'active' 
                    ? 'bg-red-50 text-red-700 border-red-200 hover:bg-red-100 hover:border-red-300' 
                    : 'bg-green-50 text-green-700 border-green-200 hover:bg-green-100 hover:border-green-300'
                ]"
                :title="service.status === 'active' ? 'Desactivar servicio' : 'Activar servicio'"
              >
                <svg class="w-3 h-3 sm:w-3.5 sm:h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path v-if="service.status === 'active'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
                  <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span class="hidden sm:inline">{{ service.status === 'active' ? 'Desactivar' : 'Activar' }}</span>
                <span class="sm:hidden">{{ service.status === 'active' ? 'Off' : 'On' }}</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Estados de no resultados y carga modernizados -->
      <div v-if="paginatedServices.length === 0 && !loading" class="flex justify-center items-center min-h-96 border-2 border-dashed border-slate-300 rounded-2xl">
        <div class="text-center max-w-sm">
          <svg class="w-16 h-16 text-slate-400 mx-auto mb-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
          </svg>
          <h3 class="text-xl font-bold text-slate-700 mb-3">No se encontraron servicios</h3>
          <p class="text-slate-500">
            {{ filteredServices.length === 0 ? 'No hay servicios registrados' : 'Prueba con otros filtros' }}
          </p>
        </div>
      </div>

      <div v-if="loading" class="flex flex-col justify-center items-center min-h-96 bg-slate-50 border border-slate-200 rounded-2xl">
        <div class="w-12 h-12 border-[3px] border-slate-300 border-t-violet-500 rounded-full animate-spin mb-6"></div>
        <p class="text-slate-600 font-medium">Cargando servicios...</p>
      </div>
    </div>

    <!-- Paginación modernizada -->
    <div class="flex flex-col sm:flex-row items-center justify-between bg-white rounded-2xl p-4 sm:p-6 mt-6 sm:mt-8 shadow-sm border border-slate-200 gap-4">
      <div class="text-xs sm:text-sm text-slate-600 font-medium order-2 sm:order-1">
        Mostrando {{ startItem }} a {{ endItem }} de {{ totalServices }} servicios
      </div>
      <div class="flex items-center gap-2 sm:gap-4 order-1 sm:order-2">
        <button 
          @click="previousPage"
          :class="[
            'flex items-center justify-center w-9 h-9 sm:w-10 sm:h-10 border rounded-xl transition-all duration-200',
            currentPage === 1 
              ? 'border-slate-200 text-slate-400 cursor-not-allowed' 
              : 'border-slate-300 text-slate-600 hover:bg-slate-50 hover:border-slate-400'
          ]"
          :disabled="currentPage === 1"
        >
          <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
        </button>
        
        <span class="text-xs sm:text-sm font-semibold text-slate-700 px-2 sm:px-4 whitespace-nowrap">
          Página {{ currentPage }} de {{ totalPages }}
        </span>
        
        <button 
          @click="nextPage"
          :class="[
            'flex items-center justify-center w-9 h-9 sm:w-10 sm:h-10 border rounded-xl transition-all duration-200',
            currentPage >= totalPages 
              ? 'border-slate-200 text-slate-400 cursor-not-allowed' 
              : 'border-slate-300 text-slate-600 hover:bg-slate-50 hover:border-slate-400'
          ]"
          :disabled="currentPage >= totalPages"
        >
          <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Acciones masivas modernizadas -->
    <div v-if="selectedServices.length > 0" class="fixed bottom-4 sm:bottom-8 left-4 right-4 sm:left-1/2 sm:right-auto sm:transform sm:-translate-x-1/2 bg-white rounded-2xl p-4 sm:p-6 shadow-2xl border border-slate-200 z-50 backdrop-blur-sm bg-white/95 max-w-full sm:max-w-fit">
      <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 sm:gap-6">
        <div class="text-sm text-slate-600 font-medium text-center sm:text-left">
          {{ selectedServices.length }} servicio(s) seleccionado(s)
        </div>
        <div class="flex flex-col sm:flex-row gap-2 sm:gap-3">
          <button 
            @click="bulkActivate" 
            class="px-4 py-2 bg-emerald-50 hover:bg-emerald-100 text-emerald-600 border border-emerald-200 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-200 whitespace-nowrap"
          >
            <svg class="w-4 h-4 inline mr-1 sm:mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            Activar Seleccionados
          </button>
          <button 
            @click="bulkDeactivate" 
            class="px-4 py-2 bg-red-50 hover:bg-red-100 text-red-600 border border-red-200 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-200 whitespace-nowrap"
          >
            <svg class="w-4 h-4 inline mr-1 sm:mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
            Desactivar Seleccionados
          </button>
          <button 
            @click="bulkUpdateCategory" 
            class="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-600 border border-slate-200 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-200 whitespace-nowrap"
          >
            <svg class="w-4 h-4 inline mr-1 sm:mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
            </svg>
            Cambiar Categoría
          </button>
        </div>
      </div>
    </div>

    <!-- Modal para Ver Servicio -->
    <div v-if="showViewModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">Detalles del Servicio</h2>
          <button @click="closeViewModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="p-8" v-if="currentService">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Imagen del servicio -->
            <div class="space-y-4">
              <img 
                :src="currentService.image || getDefaultServiceImage(currentService.category)"
                :alt="currentService.name"
                class="w-full h-48 object-cover rounded-xl border border-slate-200"
              />
              <div class="flex items-center gap-2">
                <span 
                  :class="[
                    'px-3 py-1 rounded-full text-xs font-semibold',
                    getCategoryBadgeClass(currentService.category)
                  ]"
                >
                  {{ getCategoryLabel(currentService.category) }}
                </span>
                <span 
                  :class="[
                    'px-3 py-1 rounded-full text-xs font-semibold border',
                    currentService.status === 'active' 
                      ? 'bg-green-50 text-green-700 border-green-200' 
                      : 'bg-red-50 text-red-700 border-red-200'
                  ]"
                >
                  {{ getStatusLabel(currentService.status) }}
                </span>
              </div>
            </div>
            
            <!-- Detalles del servicio -->
            <div class="space-y-4">
              <div>
                <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Nombre</label>
                <p class="text-base font-semibold text-gray-900">{{ currentService.name }}</p>
              </div>
              
              <div>
                <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Descripción</label>
                <p class="text-sm text-gray-700">{{ currentService.description || 'Sin descripción' }}</p>
              </div>
              
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Precio</label>
                  <p class="text-lg font-bold text-purple-600">Bs {{ formatPrice(currentService.price) }}</p>
                </div>
                
                <div>
                  <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Duración</label>
                  <p class="text-lg font-bold text-blue-600">{{ currentService.duration }} min</p>
                </div>
              </div>
              
              <div v-if="currentService.created_at">
                <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Fecha de creación</label>
                <p class="text-sm text-gray-700">{{ new Date(currentService.created_at).toLocaleDateString('es-ES') }}</p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeViewModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            Cerrar
          </button>
          <button @click="editServiceFromView" class="px-6 py-3 bg-amber-50 text-amber-700 border border-amber-200 rounded-xl font-medium hover:bg-amber-100 hover:border-amber-300 transition-all duration-200">
            Editar Servicio
          </button>
        </div>
      </div>
    </div>

    <!-- Modal de creación/edición modernizado -->
    <div v-if="showServiceModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">{{ editingService ? 'Editar Servicio' : 'Crear Servicio' }}</h2>
          <button @click="closeServiceModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <form @submit.prevent="saveService" class="p-8">
          <div class="space-y-6">
            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">Nombre del servicio *</label>
              <input
                v-model="serviceForm.name"
                type="text"
                required
                class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-black focus:border-black text-sm transition-all duration-200"
                placeholder="Ej: Corte Clásico"
              />
            </div>

            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">Descripción</label>
              <textarea
                v-model="serviceForm.description"
                rows="3"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-black focus:border-black text-sm resize-none transition-all duration-200"
                placeholder="Descripción del servicio..."
              ></textarea>
            </div>

            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">Categoría *</label>
              <select
                v-model="serviceForm.category"
                required
                class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-black focus:border-black text-sm transition-all duration-200"
              >
                <option value="">Seleccionar categoría</option>
                <option value="cortes">Cortes</option>
                <option value="barbas">Barbas</option>
                <option value="tratamientos">Tratamientos</option>
                <option value="combos">Combos</option>
              </select>
            </div>

            <div class="grid grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-semibold text-slate-700 mb-2">Precio *</label>
                <div class="relative">
                  <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                    <span class="text-slate-500 text-sm font-medium">Bs</span>
                  </div>
                  <input
                    v-model="serviceForm.price"
                    type="number"
                    required
                    min="0"
                    step="1"
                    class="w-full pl-12 pr-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-black focus:border-black text-sm transition-all duration-200"
                    placeholder="40"
                  />
                </div>
              </div>

              <div>
                <label class="block text-sm font-semibold text-slate-700 mb-2">Duración (min) *</label>
                <input
                  v-model="serviceForm.duration"
                  type="number"
                  required
                  min="5"
                  max="240"
                  step="5"
                  class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-black focus:border-black text-sm transition-all duration-200"
                  placeholder="45"
                />
              </div>
            </div>

            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">Estado</label>
              <select
                v-model="serviceForm.status"
                class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-black focus:border-black text-sm transition-all duration-200"
              >
                <option value="active">Activo</option>
                <option value="inactive">Inactivo</option>
              </select>
            </div>
          </div>

          <div class="flex justify-end gap-3 pt-6 border-t border-gray-200 bg-gray-50 -mx-8 -mb-8 px-8 py-6 rounded-b-2xl mt-8">
            <button 
              type="button" 
              @click="closeServiceModal" 
              class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200"
            >
              Cancelar
            </button>
            <button 
              type="submit" 
              class="px-6 py-3 bg-black text-white border-0 rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-slate-800" 
              :disabled="saving"
            >
              {{ editingService ? 'Actualizar' : 'Crear' }} Servicio
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal de cambio de categoría masivo modernizado -->
    <div v-if="showBulkCategoryModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">Cambiar Categoría Masiva</h2>
          <button @click="closeBulkCategoryModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <form @submit.prevent="confirmBulkCategoryChange" class="p-8">
          <div class="space-y-6">
            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">Nueva categoría</label>
              <select
                v-model="bulkCategoryForm.newCategory"
                required
                class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-black focus:border-black text-sm transition-all duration-200"
              >
                <option value="">Seleccionar categoría</option>
                <option value="cortes">Cortes</option>
                <option value="barbas">Barbas</option>
                <option value="tratamientos">Tratamientos</option>
                <option value="combos">Combos</option>
              </select>
            </div>
            
            <div class="bg-amber-50 border border-amber-200 text-amber-800 p-4 rounded-xl text-sm font-medium">
              Se cambiará la categoría de {{ selectedServices.length }} servicio(s) seleccionado(s).
            </div>
          </div>
          
          <div class="flex justify-end gap-3 pt-6 border-t border-gray-200 bg-gray-50 -mx-8 -mb-8 px-8 py-6 rounded-b-2xl mt-8">
            <button 
              type="button" 
              @click="closeBulkCategoryModal" 
              class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200"
            >
              Cancelar
            </button>
            <button 
              type="submit" 
              class="px-6 py-3 bg-black text-white border-0 rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-slate-800" 
              :disabled="saving"
            >
              Cambiar Categoría
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import serviceService from '@/services/serviceService'

// Estados reactivos
const services = ref([])
const loading = ref(false)
const saving = ref(false)

// Filtros
const filters = ref({
  search: '',
  category: '',
  status: '',
  priceRange: ''
})

// Paginación
const currentPage = ref(1)
const itemsPerPage = ref(10)

// Modales
const showServiceModal = ref(false)
const showViewModal = ref(false)
const showBulkCategoryModal = ref(false)

// Selección múltiple
const selectedServices = ref([])

// Formularios
const editingService = ref(null)
const currentService = ref(null)
const serviceForm = ref({
  name: '',
  description: '',
  category: '',
  price: '',
  duration: '',
  status: 'active'
})

const bulkCategoryForm = ref({
  newCategory: ''
})

// Computadas para estadísticas (siempre usa todos los servicios, no filtrados)
const stats = computed(() => ({
  totalServices: services.value.length,
  activeServices: services.value.filter(s => s.status === 'active').length,
  mostPopular: services.value.length > 0 
    ? services.value.reduce((prev, current) => 
        (current.bookingsCount || 0) > (prev.bookingsCount || 0) ? current : prev
      ).name
    : 'N/A',
  avgRevenue: (() => {
    const active = services.value.filter(s => s.status === 'active')
    if (active.length === 0) return 0
    const sum = active.reduce((acc, service) => acc + service.price, 0)
    return Math.round(sum / active.length)
  })()
}))

const totalServices = computed(() => filteredServices.value.length)
const activeServices = computed(() => services.value.filter(s => s.status === 'active').length)
const inactiveServices = computed(() => services.value.filter(s => s.status === 'inactive').length)
const avgPrice = computed(() => {
  const active = services.value.filter(s => s.status === 'active')
  if (active.length === 0) return 0
  const sum = active.reduce((acc, service) => acc + service.price, 0)
  return Math.round(sum / active.length)
})

// Servicios filtrados
const filteredServices = computed(() => {
  let filtered = services.value

  if (filters.value.search) {
    const search = filters.value.search.toLowerCase()
    filtered = filtered.filter(service =>
      service.name.toLowerCase().includes(search) ||
      service.description.toLowerCase().includes(search)
    )
  }

  if (filters.value.category) {
    filtered = filtered.filter(service => service.category === filters.value.category)
  }

  if (filters.value.status) {
    filtered = filtered.filter(service => service.status === filters.value.status)
  }

  if (filters.value.priceRange) {
    const [min, max] = filters.value.priceRange.split('-').map(Number)
    filtered = filtered.filter(service => {
      if (max) {
        return service.price >= min && service.price <= max
      } else {
        return service.price >= min
      }
    })
  }

  return filtered
})

// Servicios paginados
const paginatedServices = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  return filteredServices.value.slice(start, end)
})

// Paginación
const totalPages = computed(() => Math.ceil(totalServices.value / itemsPerPage.value))
const startItem = computed(() => {
  if (totalServices.value === 0) return 0
  return (currentPage.value - 1) * itemsPerPage.value + 1
})
const endItem = computed(() => {
  const end = currentPage.value * itemsPerPage.value
  return Math.min(end, totalServices.value)
})

// Configuración de tabla
const tableColumns = [
  { key: 'servicio', label: 'Servicio', sortable: true },
  { key: 'categoria', label: 'Categoría', sortable: true },
  { key: 'precio', label: 'Precio', sortable: true },
  { key: 'duracion', label: 'Duración', sortable: true },
  { key: 'estado', label: 'Estado', sortable: true }
]

const tableConfig = computed(() => ({
  columns: tableColumns,
  data: paginatedServices.value,
  loading: loading.value,
  emptyMessage: 'No se encontraron servicios',
  selectable: true,
  selected: selectedServices.value
}))

// Computed para filtros activos
const hasActiveFilters = computed(() => {
  return !!(filters.value.search || filters.value.category || filters.value.status || filters.value.priceRange)
})

// Métodos
const loadServices = async () => {
  loading.value = true
  try {
    const servicesData = await serviceService.getAll()
    services.value = servicesData || []
  } catch (error) {
    console.error('Error al cargar servicios:', error)
    services.value = []
  } finally {
    loading.value = false
  }
}

const openCreateModal = () => {
  editingService.value = null
  serviceForm.value = {
    name: '',
    description: '',
    category: '',
    price: '',
    duration: '',
    status: 'active'
  }
  showServiceModal.value = true
}

const viewService = (service) => {
  currentService.value = service
  showViewModal.value = true
}

const closeViewModal = () => {
  showViewModal.value = false
  currentService.value = null
}

const editServiceFromView = () => {
  if (currentService.value) {
    editingService.value = currentService.value
    // Copiar datos asegurando que los tipos sean correctos
    serviceForm.value = {
      name: currentService.value.name || '',
      description: currentService.value.description || '',
      category: currentService.value.category || '',
      price: currentService.value.price || '',
      duration: currentService.value.duration || '',
      status: currentService.value.status || 'active',
      popular: currentService.value.popular || false,
      image: currentService.value.image || ''
    }
    showViewModal.value = false
    showServiceModal.value = true
  }
}

const editService = (service) => {
  editingService.value = service
  // Copiar datos asegurando que los tipos sean correctos
  serviceForm.value = {
    name: service.name || '',
    description: service.description || '',
    category: service.category || '',
    price: service.price || '',
    duration: service.duration || '',
    status: service.status || 'active',
    popular: service.popular || false,
    image: service.image || ''
  }
  showServiceModal.value = true
}

const closeServiceModal = () => {
  showServiceModal.value = false
  editingService.value = null
}

const saveService = async () => {
  saving.value = true
  try {
    if (editingService.value) {
      // Actualizar servicio existente
      await serviceService.update(editingService.value.id, serviceForm.value)
      // Recargar servicios después de actualizar para obtener datos frescos del backend
      await loadServices()
    } else {
      // Crear nuevo servicio
      await serviceService.create(serviceForm.value)
      // Recargar servicios después de crear
      await loadServices()
    }
    
    closeServiceModal()
  } catch (error) {
    console.error('Error al guardar servicio:', error)
    alert('Error al guardar el servicio. Verifica los datos e intenta nuevamente.')
  } finally {
    saving.value = false
  }
}

const toggleServiceStatus = async (service) => {
  try {
    const newStatus = service.status === 'active' ? 'inactive' : 'active'
    await serviceService.update(service.id, { status: newStatus })
    
    // Actualizar el servicio en la lista local
    const index = services.value.findIndex(s => s.id === service.id)
    if (index !== -1) {
      services.value[index].status = newStatus
      // Forzar actualización de la vista
      services.value = [...services.value]
    }
  } catch (error) {
    console.error('Error al cambiar estado del servicio:', error)
    alert('Error al cambiar el estado del servicio. Por favor intenta nuevamente.')
  }
}

// Acciones masivas
const bulkActivate = async () => {
  if (selectedServices.value.length === 0) return
  
  try {
    for (const serviceId of selectedServices.value) {
      await serviceService.update(serviceId, { status: 'active' })
      const index = services.value.findIndex(s => s.id === serviceId)
      if (index !== -1) {
        services.value[index].status = 'active'
      }
    }
    
    selectedServices.value = []
  } catch (error) {
    console.error('Error al activar servicios:', error)
  }
}

const bulkDeactivate = async () => {
  if (selectedServices.value.length === 0) return
  
  try {
    for (const serviceId of selectedServices.value) {
      await serviceService.update(serviceId, { status: 'inactive' })
      const index = services.value.findIndex(s => s.id === serviceId)
      if (index !== -1) {
        services.value[index].status = 'inactive'
      }
    }
    
    selectedServices.value = []
  } catch (error) {
    console.error('Error al desactivar servicios:', error)
  }
}

const bulkUpdateCategory = () => {
  if (selectedServices.value.length === 0) return
  bulkCategoryForm.value.newCategory = ''
  showBulkCategoryModal.value = true
}

const closeBulkCategoryModal = () => {
  showBulkCategoryModal.value = false
  bulkCategoryForm.value.newCategory = ''
}

const confirmBulkCategoryChange = async () => {
  if (!bulkCategoryForm.value.newCategory) return
  
  saving.value = true
  try {
    for (const serviceId of selectedServices.value) {
      await serviceService.update(serviceId, { category: bulkCategoryForm.value.newCategory })
      const index = services.value.findIndex(s => s.id === serviceId)
      if (index !== -1) {
        services.value[index].category = bulkCategoryForm.value.newCategory
      }
    }
    
    selectedServices.value = []
    closeBulkCategoryModal()
  } catch (error) {
    console.error('Error al actualizar categorías:', error)
  } finally {
    saving.value = false
  }
}

// Paginación
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

const previousPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

// Utilidades de formato
const formatPrice = (price) => {
  return new Intl.NumberFormat('es-CO').format(price)
}

const getCategoryLabel = (category) => {
  const labels = {
    cortes: 'Cortes',
    barbas: 'Barbas',
    tratamientos: 'Tratamientos',
    combos: 'Combos'
  }
  return labels[category] || category || 'Sin categoría'
}

const getCategoryBadgeClass = (category) => {
  const classes = {
    cortes: 'bg-blue-100 text-blue-700',
    barbas: 'bg-emerald-100 text-emerald-700',
    tratamientos: 'bg-amber-100 text-amber-700',
    combos: 'bg-violet-100 text-violet-700',
    default: 'bg-slate-100 text-slate-600'
  }
  return classes[category] || classes.default
}

const getStatusClass = (status) => {
  return status === 'active' 
    ? 'status-active' 
    : 'status-inactive'
}

const getStatusLabel = (status) => {
  return status === 'active' ? 'Activo' : 'Inactivo'
}

const getPriceRangeLabel = (range) => {
  const labels = {
    '0-30000': 'Bs 0 - Bs 30,000',
    '30000-50000': 'Bs 30,000 - Bs 50,000',
    '50000-100000': 'Bs 50,000+'
  }
  return labels[range] || range
}

const getDefaultServiceImage = (category) => {
  const images = {
    cortes: 'https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=60&h=60&fit=crop',
    barbas: 'https://images.unsplash.com/photo-1621605815971-fbc98d665033?w=60&h=60&fit=crop',
    tratamientos: 'https://images.unsplash.com/photo-1562004760-aceed7bb0fe3?w=60&h=60&fit=crop',
    combos: 'https://images.unsplash.com/photo-1599351431613-4b9e2c6ef504?w=60&h=60&fit=crop'
  }
  return images[category] || images.cortes
}

const clearFilters = () => {
  filters.value = {
    search: '',
    category: '',
    status: '',
    priceRange: ''
  }
}

const applyFilters = () => {
  currentPage.value = 1
}

const selectService = (service) => {
  // Función para seleccionar servicios (puede expandirse para funcionalidad adicional)
}

// Observadores
watch(filters, () => {
  currentPage.value = 1
}, { deep: true })

// Lifecycle
onMounted(() => {
  loadServices()
})
</script>

<style scoped>
/* AdminServicios.vue - Tailwind CSS v4 */
/* Todas las utilidades son nativas de Tailwind v4 */
/* No se requiere CSS custom - 100% utility-first */
</style>
