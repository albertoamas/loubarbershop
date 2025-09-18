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

    <!-- Filtros modernos con Tailwind v4 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-6 mb-8">
      <div class="flex flex-wrap items-center gap-4">
        <select 
          v-model="filters.category"
          class="px-4 py-2.5 border border-slate-200 rounded-xl text-sm bg-white text-slate-700 min-w-40 focus:ring-2 focus:ring-black focus:border-black transition-all duration-200"
          @change="applyFilters"
        >
          <option value="">Todas las categorías</option>
          <option value="cortes">Cortes</option>
          <option value="barbas">Barbas</option>
          <option value="tratamientos">Tratamientos</option>
          <option value="combos">Combos</option>
        </select>

        <select 
          v-model="filters.status"
          class="px-4 py-2.5 border border-slate-200 rounded-xl text-sm bg-white text-slate-700 min-w-40 focus:ring-2 focus:ring-black focus:border-black transition-all duration-200"
          @change="applyFilters"
        >
          <option value="">Todos los estados</option>
          <option value="active">Activos</option>
          <option value="inactive">Inactivos</option>
        </select>

        <select 
          v-model="filters.priceRange"
          class="px-4 py-2.5 border border-slate-200 rounded-xl text-sm bg-white text-slate-700 min-w-40 focus:ring-2 focus:ring-black focus:border-black transition-all duration-200"
          @change="applyFilters"
        >
          <option value="">Todos los precios</option>
          <option value="0-30000">Bs 0 - Bs 30,000</option>
          <option value="30000-50000">Bs 30,000 - Bs 50,000</option>
          <option value="50000-100000">Bs 50,000+</option>
        </select>

        <button 
          @click="clearFilters"
          class="flex items-center gap-2 px-4 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-600 border border-slate-200 rounded-xl text-sm transition-all duration-200"
        >
          <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
          Limpiar
        </button>
      </div>
    </div>

    <!-- Grid de servicios modernizado con Tailwind v4 -->
    <div class="bg-white rounded-2xl p-8 shadow-sm border border-slate-200">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        <div
          v-for="service in paginatedServices"
          :key="service.id"
          class="bg-gradient-to-br from-white to-slate-50 border border-slate-200 rounded-2xl p-6 hover:shadow-lg hover:-translate-y-1 transition-all duration-300 cursor-pointer group"
          @click="selectService(service)"
        >
          <!-- Imagen del servicio -->
          <div class="relative mb-4">
            <img 
              :src="service.image || getDefaultServiceImage(service.category)" 
              :alt="service.name"
              class="w-full h-32 object-cover rounded-xl border border-slate-200"
            />
            <div class="absolute top-3 right-3">
              <div :class="[
                'inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold',
                service.status === 'active' 
                  ? 'bg-emerald-100 text-emerald-700' 
                  : 'bg-red-100 text-red-700'
              ]">
                <div :class="[
                  'w-2 h-2 rounded-full',
                  service.status === 'active' ? 'bg-emerald-500' : 'bg-red-500'
                ]"></div>
                <span>{{ service.status === 'active' ? 'Activo' : 'Inactivo' }}</span>
              </div>
            </div>
          </div>

          <!-- Información del servicio -->
          <div class="space-y-4">
            <!-- Header con nombre y categoría -->
            <div class="flex items-start justify-between gap-3">
              <h3 class="text-lg font-bold text-slate-800 leading-tight group-hover:text-black transition-colors duration-200">
                {{ service.name }}
              </h3>
              <span :class="[
                'inline-flex px-2.5 py-1 rounded-lg text-xs font-semibold uppercase tracking-wide',
                getCategoryBadgeClass(service.category || 'default')
              ]">
                {{ getCategoryLabel(service.category) }}
              </span>
            </div>

            <!-- Descripción -->
            <p class="text-sm text-slate-600 line-clamp-2">
              {{ service.description || 'Sin descripción' }}
            </p>

            <!-- Detalles en grid -->
            <div class="grid grid-cols-2 gap-4">
              <div>
                <span class="block text-xs font-medium text-slate-500 mb-1">Precio</span>
                <span class="text-lg font-bold text-violet-600">Bs {{ formatPrice(service.price || 0) }}</span>
              </div>
              <div>
                <span class="block text-xs font-medium text-slate-500 mb-1">Duración</span>
                <span class="text-base font-semibold text-slate-800">{{ service.duration || 0 }} min</span>
              </div>
            </div>

            <!-- Acciones -->
            <div class="flex gap-2 pt-4 border-t border-slate-100">
              <button 
                @click.stop="editService(service)" 
                class="flex-1 flex items-center justify-center gap-2 px-3 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 rounded-lg text-sm font-medium transition-all duration-200"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
                Editar
              </button>
              <button 
                @click.stop="toggleServiceStatus(service)" 
                :class="[
                  'flex-1 flex items-center justify-center gap-2 px-3 py-2 border rounded-lg text-sm font-medium transition-all duration-200',
                  service.status === 'active' 
                    ? 'bg-red-50 hover:bg-red-100 text-red-600 border-red-200' 
                    : 'bg-emerald-50 hover:bg-emerald-100 text-emerald-600 border-emerald-200'
                ]"
              >
                <svg v-if="service.status === 'active'" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 9v6m4-6v6m7-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                {{ service.status === 'active' ? 'Desactivar' : 'Activar' }}
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
        <div class="w-12 h-12 border-3 border-slate-300 border-t-violet-500 rounded-full animate-spin mb-6"></div>
        <p class="text-slate-600 font-medium">Cargando servicios...</p>
      </div>
    </div>

    <!-- Paginación modernizada -->
    <div class="flex items-center justify-between bg-white rounded-2xl p-6 mt-8 shadow-sm border border-slate-200">
      <div class="text-sm text-slate-600 font-medium">
        Mostrando {{ startItem }} a {{ endItem }} de {{ totalServices }} servicios
      </div>
      <div class="flex items-center gap-4">
        <button 
          @click="previousPage"
          :class="[
            'flex items-center justify-center w-10 h-10 border rounded-xl transition-all duration-200',
            currentPage === 1 
              ? 'border-slate-200 text-slate-400 cursor-not-allowed' 
              : 'border-slate-300 text-slate-600 hover:bg-slate-50 hover:border-slate-400'
          ]"
          :disabled="currentPage === 1"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
        </button>
        
        <span class="text-sm font-semibold text-slate-700 px-4">
          Página {{ currentPage }} de {{ totalPages }}
        </span>
        
        <button 
          @click="nextPage"
          :class="[
            'flex items-center justify-center w-10 h-10 border rounded-xl transition-all duration-200',
            currentPage >= totalPages 
              ? 'border-slate-200 text-slate-400 cursor-not-allowed' 
              : 'border-slate-300 text-slate-600 hover:bg-slate-50 hover:border-slate-400'
          ]"
          :disabled="currentPage >= totalPages"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Acciones masivas modernizadas -->
    <div v-if="selectedServices.length > 0" class="fixed bottom-8 left-1/2 transform -translate-x-1/2 bg-white rounded-2xl p-6 shadow-2xl border border-slate-200 z-50 backdrop-blur-sm bg-white/95">
      <div class="flex items-center gap-6">
        <div class="text-sm text-slate-600 font-medium">
          {{ selectedServices.length }} servicio(s) seleccionado(s)
        </div>
        <div class="flex gap-3">
          <button 
            @click="bulkActivate" 
            class="px-4 py-2 bg-emerald-50 hover:bg-emerald-100 text-emerald-600 border border-emerald-200 rounded-xl text-sm font-semibold transition-all duration-200"
          >
            Activar Seleccionados
          </button>
          <button 
            @click="bulkDeactivate" 
            class="px-4 py-2 bg-red-50 hover:bg-red-100 text-red-600 border border-red-200 rounded-xl text-sm font-semibold transition-all duration-200"
          >
            Desactivar Seleccionados
          </button>
          <button 
            @click="bulkUpdateCategory" 
            class="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-600 border border-slate-200 rounded-xl text-sm font-semibold transition-all duration-200"
          >
            Cambiar Categoría
          </button>
        </div>
      </div>
    </div>

    <!-- Modal de creación/edición modernizado -->
    <AdminModal
      :show="showServiceModal"
      :title="editingService ? 'Editar Servicio' : 'Crear Servicio'"
      @close="closeServiceModal"
      showActions
    >
      <form @submit.prevent="saveService" class="space-y-6">
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
                  step="1000"
                  class="w-full pl-12 pr-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-black focus:border-black text-sm transition-all duration-200"
                  placeholder="30000"
                />
              </div>
            </div>

            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">Duración (min) *</label>
              <input
                v-model="serviceForm.duration"
                type="number"
                required
                min="15"
                max="240"
                step="15"
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

        <div class="flex justify-end gap-4 pt-6 border-t border-slate-200">
          <button 
            type="button" 
            @click="closeServiceModal" 
            class="px-6 py-3 bg-white hover:bg-slate-50 text-slate-700 border border-slate-200 rounded-xl font-semibold text-sm transition-all duration-200"
          >
            Cancelar
          </button>
          <button 
            type="submit" 
            class="px-6 py-3 bg-black hover:bg-slate-800 text-white rounded-xl font-semibold text-sm transition-all duration-200 disabled:opacity-50" 
            :disabled="saving"
          >
            {{ editingService ? 'Actualizar' : 'Crear' }} Servicio
          </button>
        </div>
      </form>
    </AdminModal>

    <!-- Modal de cambio de categoría masivo modernizado -->
    <AdminModal
      :show="showBulkCategoryModal"
      title="Cambiar Categoría Masiva"
      @close="closeBulkCategoryModal"
      showActions
    >
      <form @submit.prevent="confirmBulkCategoryChange" class="space-y-6">
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Nueva categoría</label>
          <select
            v-model="bulkCategoryForm.newCategory"
            required
            class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-black focus:border-black text-sm transition-all duration-200"
          >
            <option value="cortes">Cortes</option>
            <option value="barbas">Barbas</option>
            <option value="tratamientos">Tratamientos</option>
            <option value="combos">Combos</option>
          </select>
        </div>
        <div class="bg-amber-50 border border-amber-200 text-amber-800 p-4 rounded-xl text-sm font-medium">
          Se cambiará la categoría de {{ selectedServices.length }} servicio(s) seleccionado(s).
        </div>
        <div class="flex justify-end gap-4">
          <button 
            type="button" 
            @click="closeBulkCategoryModal" 
            class="px-6 py-3 bg-white hover:bg-slate-50 text-slate-700 border border-slate-200 rounded-xl font-semibold text-sm transition-all duration-200"
          >
            Cancelar
          </button>
          <button 
            type="submit" 
            class="px-6 py-3 bg-black hover:bg-slate-800 text-white rounded-xl font-semibold text-sm transition-all duration-200 disabled:opacity-50" 
            :disabled="saving"
          >
            Cambiar Categoría
          </button>
        </div>
      </form>
    </AdminModal>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import AdminTable from '@/components/admin/AdminTable.vue'
import AdminModal from '@/components/admin/AdminModal.vue'
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
const showBulkCategoryModal = ref(false)

// Selección múltiple
const selectedServices = ref([])

// Formularios
const editingService = ref(null)
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

// Computadas para estadísticas
const stats = computed(() => ({
  totalServices: filteredServices.value.length,
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

// Métodos
const loadServices = async () => {
  loading.value = true
  try {
    const servicesData = await serviceService.getAll()
    services.value = servicesData || []
    console.log('Servicios cargados:', services.value.length)
    console.log('Primer servicio para debug:', services.value[0])
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

const editService = (service) => {
  editingService.value = service
  serviceForm.value = { ...service }
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
      const updatedService = await serviceService.update(editingService.value.id, serviceForm.value)
      const index = services.value.findIndex(s => s.id === editingService.value.id)
      if (index !== -1) {
        services.value[index] = updatedService
      }
      console.log('Servicio actualizado correctamente')
    } else {
      // Crear nuevo servicio
      const newService = await serviceService.create(serviceForm.value)
      services.value.unshift(newService)
      console.log('Servicio creado correctamente')
    }
    
    closeServiceModal()
  } catch (error) {
    console.error('Error al guardar servicio:', error)
  } finally {
    saving.value = false
  }
}

const toggleServiceStatus = async (service) => {
  try {
    const newStatus = service.status === 'active' ? 'inactive' : 'active'
    await serviceService.update(service.id, { status: newStatus })
    
    const index = services.value.findIndex(s => s.id === service.id)
    if (index !== -1) {
      services.value[index].status = newStatus
    }
    
    const statusText = newStatus === 'active' ? 'activado' : 'desactivado'
    console.log(`Servicio ${statusText} correctamente`)
  } catch (error) {
    console.error('Error al cambiar estado del servicio:', error)
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
    
    console.log(`${selectedServices.value.length} servicios activados`)
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
    
    console.log(`${selectedServices.value.length} servicios desactivados`)
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
    
    console.log(`Categoría actualizada para ${selectedServices.value.length} servicios`)
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
  console.log('Servicio seleccionado:', service.name)
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
/* Utilidades adicionales para Tailwind v4 */
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Animación de spin personalizada */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

/* Border width 3 para loading spinner */
.border-3 {
  border-width: 3px;
}
</style>
