<!--
  AdminBarberos.vue - Gestión completa de barberos
  FASE 8.3: Rediseño minimalista y moderno con el estilo premium aplicado
-->
<template>
  <div class="p-8 bg-gradient-to-br from-slate-50 to-slate-100 min-h-screen font-sans">
    <!-- Header del dashboard modernizado -->
    <div class="mb-6 bg-white rounded-2xl p-6 shadow-sm border border-slate-200">
      <div class="flex flex-col lg:flex-row lg:justify-between lg:items-start gap-6">
        <div class="flex-1">
          <h1 class="text-3xl font-extrabold bg-gradient-to-r from-black to-gray-500 bg-clip-text text-transparent mb-2">
            Gestión de Barberos
          </h1>
          <p class="text-lg text-slate-600 font-medium">
            Administra el equipo de barberos y sus horarios de Low Barber Shop
          </p>
        </div>
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
          <button 
            @click="loadBarbers" 
            :disabled="loadingBarbers"
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-black to-gray-500 text-white border-0 rounded-xl font-semibold text-sm transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5 disabled:opacity-70 disabled:cursor-not-allowed"
          >
            <svg :class="{ 'animate-spin': loadingBarbers }" class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            {{ loadingBarbers ? 'Actualizando...' : 'Actualizar' }}
          </button>
          <button 
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white border-0 rounded-xl font-semibold text-sm transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5"
            @click="openCreateModal"
          >
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
            </svg>
            Nuevo Barbero
          </button>
        </div>
      </div>
    </div>

    <!-- Grid de estadísticas modernizado -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
      <!-- Total de barberos -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Total</h3>
            <p class="text-3xl font-black text-blue-600">{{ stats.total || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-blue-100 to-blue-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Barberos activos -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Activos</h3>
            <p class="text-3xl font-black text-green-600">{{ stats.activos || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-green-100 to-green-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Disponibles hoy -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Disponibles</h3>
            <p class="text-3xl font-black text-purple-600">{{ stats.disponibles_hoy || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-purple-100 to-purple-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Promedio de reservas -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Promedio</h3>
            <p class="text-3xl font-black text-orange-600">{{ stats.promedio_reservas || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-orange-100 to-orange-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
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
              <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <input
              v-model="searchTerm"
              type="text"
              placeholder="Buscar por nombre, email, teléfono o especialidad..."
              class="w-full pl-12 pr-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
            />
            <button 
              v-if="searchTerm"
              @click="searchTerm = ''"
              class="absolute inset-y-0 right-0 pr-4 flex items-center text-gray-400 hover:text-gray-600"
            >
              <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
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
          <!-- Filtro por Estado -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Estado</label>
            <select 
              v-model="statusFilter" 
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
            >
              <option value="">Todos los estados</option>
              <option value="true">✓ Activos</option>
              <option value="false">⊗ Desactivados</option>
            </select>
          </div>

          <!-- Filtro por Especialidad -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Especialidad</label>
            <select 
              v-model="especialidadFilter" 
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
            >
              <option value="">Todas las especialidades</option>
              <option value="Especialista en cortes modernos">✂️ Cortes Modernos</option>
              <option value="Barba y Bigote">🧔 Barba y Bigote</option>
              <option value="Tratamientos">💆 Tratamientos</option>
              <option value="Cortes Clásicos">👔 Cortes Clásicos</option>
            </select>
          </div>

          <!-- Ordenar por -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Ordenar por</label>
            <select 
              v-model="sortBy" 
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
            >
              <option value="nombre_asc">👤 Nombre: A-Z</option>
              <option value="nombre_desc">👤 Nombre: Z-A</option>
              <option value="experiencia_desc">⭐ Experiencia: Mayor a menor</option>
            </select>
          </div>
        </div>

        <!-- Indicadores de filtros activos -->
        <div v-if="hasActiveFilters" class="flex flex-wrap gap-2 items-center pt-2 border-t border-gray-200">
          <span class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Filtros activos:</span>
          
          <span v-if="searchTerm" class="inline-flex items-center gap-1 px-3 py-1 bg-violet-100 text-violet-700 rounded-full text-xs font-medium">
            Búsqueda: "{{ searchTerm }}"
            <button @click="searchTerm = ''" class="hover:text-violet-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>
          
          <span v-if="statusFilter !== ''" class="inline-flex items-center gap-1 px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-medium">
            Estado: {{ statusFilter === 'true' ? 'Activos' : 'Desactivados' }}
            <button @click="statusFilter = ''" class="hover:text-blue-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>
          
          <span v-if="especialidadFilter" class="inline-flex items-center gap-1 px-3 py-1 bg-green-100 text-green-700 rounded-full text-xs font-medium">
            Especialidad: {{ getEspecialidadLabel(especialidadFilter) }}
            <button @click="especialidadFilter = ''" class="hover:text-green-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>

          <span class="text-xs text-gray-500 ml-auto">
            {{ filteredBarbers.length }} resultado{{ filteredBarbers.length !== 1 ? 's' : '' }}
          </span>
        </div>
      </div>
    </div>

    <!-- Lista de barberos modernizada -->
    <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200">
      <div v-if="loadingBarbers" class="flex flex-col items-center justify-center py-16 text-gray-500">
        <div class="w-12 h-12 border-[3px] border-gray-200 border-t-violet-500 rounded-full animate-spin mb-4"></div>
        <p class="text-lg font-medium">Cargando barberos...</p>
      </div>
      
      <div v-else-if="filteredBarbers.length === 0" class="flex flex-col items-center justify-center py-16 text-gray-500 text-center">
        <svg class="w-16 h-16 text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
        </svg>
        <h3 class="text-xl font-semibold text-gray-700 mb-2">No se encontraron barberos</h3>
        <p class="text-gray-500 mb-6">No hay barberos que coincidan con los filtros aplicados.</p>
        <button @click="openCreateModal" class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white border-0 rounded-xl font-semibold text-sm transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5">
          Crear primer barbero
        </button>
      </div>
      
      <div v-else class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
        <div
          v-for="barber in filteredBarbers"
          :key="barber.id"
          :class="[
            'bg-slate-50 border rounded-2xl p-6 transition-all duration-200 hover:shadow-lg hover:-translate-y-0.5',
            barber.disponible 
              ? 'border-slate-200' 
              : 'border-red-200 bg-red-50/30 opacity-75'
          ]"
        >
          <div class="flex items-start gap-4 mb-4">
            <div class="w-12 h-12 flex-shrink-0">
              <img
                v-if="barber.avatar"
                :src="barber.avatar"
                :alt="barber.nombre"
                class="w-full h-full rounded-xl object-cover border-2 border-slate-300"
              />
              <div v-else class="w-full h-full rounded-xl bg-gradient-to-br from-black to-gray-500 text-white flex items-center justify-center font-semibold text-sm">
                {{ getInitials(barber.nombre) }}
              </div>
            </div>
            
            <div class="flex-1 min-w-0">
              <h3 class="font-semibold text-gray-900 text-base mb-1 truncate">{{ barber.nombre }}</h3>
              <p class="text-gray-500 text-sm mb-2 truncate">{{ barber.email }}</p>
              <span class="inline-flex items-center px-3 py-1 bg-gray-200 text-gray-700 rounded-full text-xs font-medium border border-gray-300">
                {{ barber.especialidad }}
              </span>
            </div>
            
            <div class="flex-shrink-0">
              <span :class="['inline-flex items-center gap-2 px-3 py-1.5 rounded-full text-xs font-semibold', 
                barber.disponible 
                  ? 'bg-green-50 text-green-700 border border-green-200' 
                  : 'bg-red-50 text-red-700 border border-red-200']">
                <div :class="['w-2 h-2 rounded-full', 
                  barber.disponible ? 'bg-green-500' : 'bg-red-500']"></div>
                {{ barber.disponible ? 'Disponible' : 'No Disponible' }}
              </span>
            </div>
          </div>
          
          <div class="space-y-3 mb-4">
            <div v-if="barber.horario_trabajo" class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Horario:</span>
              <span class="text-sm text-gray-900 font-medium">
                {{ getWorkScheduleSummary(barber.horario_trabajo) }}
              </span>
            </div>
            
            <div v-if="barber.horario_trabajo" class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Días:</span>
              <span class="text-sm text-gray-900 font-medium">{{ getWorkingDaysFromSchedule(barber.horario_trabajo) }}</span>
            </div>
            
            <div v-if="barber.experiencia_anos" class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Experiencia:</span>
              <span class="text-sm text-gray-900 font-medium">{{ barber.experiencia_anos }} año{{ barber.experiencia_anos !== 1 ? 's' : '' }}</span>
            </div>
            
            <div v-if="barber.descripcion" class="pt-2 border-t border-gray-200">
              <p class="text-xs text-gray-500 line-clamp-2">{{ barber.descripcion }}</p>
            </div>
          </div>
          
          <div class="flex gap-2 justify-end flex-wrap">
            <button @click="editBarber(barber)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200 bg-amber-50 text-amber-700 border-amber-200 hover:bg-amber-100 hover:border-amber-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
              Editar
            </button>
            
            <button @click="manageSchedule(barber)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200 bg-blue-50 text-blue-700 border-blue-200 hover:bg-blue-100 hover:border-blue-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
              Horarios
            </button>
            
            <button 
              @click="toggleBarberStatus(barber)" 
              :class="[
                'flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200',
                barber.disponible 
                  ? 'bg-red-50 text-red-700 border-red-200 hover:bg-red-100 hover:border-red-300'
                  : 'bg-green-50 text-green-700 border-green-200 hover:bg-green-100 hover:border-green-300'
              ]"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path v-if="barber.disponible" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
                <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              {{ barber.disponible ? 'Desactivar' : 'Activar' }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal para crear/editar barbero modernizado -->
    <div v-if="showBarberModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">{{ isEditing ? 'Editar Barbero' : 'Nuevo Barbero' }}</h2>
          <button @click="closeBarberModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <form @submit.prevent="saveBarber" class="p-8">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            <div class="space-y-2">
              <label for="nombre" class="block text-sm font-medium text-gray-700">Nombre completo *</label>
              <input
                id="nombre"
                v-model="barberForm.nombre"
                type="text"
                required
                placeholder="Ej: Juan Pérez"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
              />
            </div>

            <div class="space-y-2" v-if="!isEditing">
              <label for="email" class="block text-sm font-medium text-gray-700">Email *</label>
              <input
                id="email"
                v-model="barberForm.email"
                type="email"
                required
                placeholder="juan@ejemplo.com"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
              />
            </div>

            <div class="space-y-2" v-if="isEditing">
              <label class="block text-sm font-medium text-gray-700">Email</label>
              <input
                type="email"
                :value="currentBarber?.email"
                disabled
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-gray-100 text-sm text-gray-500 cursor-not-allowed"
              />
              <p class="text-xs text-gray-500">El email no se puede modificar</p>
            </div>

            <div class="space-y-2">
              <label for="telefono" class="block text-sm font-medium text-gray-700">Teléfono</label>
              <input
                id="telefono"
                v-model="barberForm.telefono"
                type="tel"
                placeholder="+591 123 456 789"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
              />
            </div>

            <div class="space-y-2">
              <label for="especialidad" class="block text-sm font-medium text-gray-700">Especialidad *</label>
              <select id="especialidad" v-model="barberForm.especialidad" required class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent">
                <option value="">Selecciona una especialidad</option>
                <option value="Cortes modernos">Cortes Modernos</option>
                <option value="Barba y Bigote">Barba y Bigote</option>
                <option value="Tratamientos capilares">Tratamientos</option>
                <option value="Cortes Clásicos">Cortes Clásicos</option>
              </select>
            </div>

            <div class="space-y-2">
              <label for="descripcion" class="block text-sm font-medium text-gray-700">Descripción</label>
              <textarea
                id="descripcion"
                v-model="barberForm.descripcion"
                rows="3"
                placeholder="Breve descripción del barbero..."
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
              ></textarea>
            </div>

            <div class="space-y-2">
              <label for="experiencia_anos" class="block text-sm font-medium text-gray-700">Años de experiencia</label>
              <input
                id="experiencia_anos"
                v-model.number="barberForm.experiencia_anos"
                type="number"
                min="0"
                placeholder="Ej: 5"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
              />
            </div>

            <div class="space-y-2">
              <label for="disponible" class="block text-sm font-medium text-gray-700">Estado</label>
              <select id="disponible" v-model="barberForm.disponible" class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent">
                <option :value="true">Disponible</option>
                <option :value="false">No Disponible</option>
              </select>
            </div>

            <div class="space-y-2" v-if="!isEditing">
              <label for="password" class="block text-sm font-medium text-gray-700">Contraseña *</label>
              <input
                id="password"
                v-model="barberForm.password"
                type="password"
                required
                placeholder="Mínimo 6 caracteres"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
              />
            </div>

            <div class="space-y-2" v-if="!isEditing">
              <label for="password_confirmation" class="block text-sm font-medium text-gray-700">Confirmar contraseña *</label>
              <input
                id="password_confirmation"
                v-model="barberForm.password_confirmation"
                type="password"
                required
                placeholder="Repite la contraseña"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
              />
            </div>
          </div>

          <div class="flex justify-end gap-3 pt-6 border-t border-gray-200 bg-gray-50 -mx-8 -mb-8 px-8 py-6 rounded-b-2xl">
            <button type="button" @click="closeBarberModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
              Cancelar
            </button>
            <button
              type="submit"
              :disabled="!isBarberFormValid || savingBarber"
              class="px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white border-0 rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:shadow-lg hover:-translate-y-0.5"
            >
              {{ savingBarber ? 'Guardando...' : (isEditing ? 'Actualizar' : 'Crear') }}
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal para gestionar horarios -->
    <div v-if="showScheduleModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-3xl w-full max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <div>
            <h2 class="text-xl font-semibold text-gray-900">Horarios de {{ currentBarber?.nombre }}</h2>
            <p class="text-sm text-gray-500 mt-1">Configura los horarios de trabajo por día</p>
          </div>
          <button @click="closeScheduleModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="p-8">
          <div class="space-y-4">
            <div v-for="day in weekDaysFull" :key="day.value" class="border border-gray-200 rounded-xl p-4 hover:border-violet-300 transition-all duration-200">
              <div class="flex items-center justify-between gap-4">
                <div class="flex items-center gap-3 flex-1">
                  <label class="flex items-center gap-2">
                    <input
                      type="checkbox"
                      v-model="scheduleForm[day.value].activo"
                      class="w-5 h-5 text-violet-600 border-gray-300 rounded focus:ring-violet-500"
                    />
                    <span class="font-medium text-gray-900 min-w-[100px]">{{ day.label }}</span>
                  </label>
                </div>
                
                <div v-if="scheduleForm[day.value].activo" class="flex items-center gap-3">
                  <div class="flex items-center gap-2">
                    <label class="text-sm text-gray-600">Desde:</label>
                    <input
                      type="time"
                      v-model="scheduleForm[day.value].inicio"
                      class="px-3 py-2 border border-gray-300 rounded-lg bg-white text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
                    />
                  </div>
                  <span class="text-gray-400">-</span>
                  <div class="flex items-center gap-2">
                    <label class="text-sm text-gray-600">Hasta:</label>
                    <input
                      type="time"
                      v-model="scheduleForm[day.value].fin"
                      class="px-3 py-2 border border-gray-300 rounded-lg bg-white text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
                    />
                  </div>
                </div>
                <div v-else class="text-sm text-gray-400 italic">
                  No disponible
                </div>
              </div>
            </div>
          </div>

          <div class="mt-6 bg-blue-50 border border-blue-200 rounded-xl p-4">
            <div class="flex items-start gap-3">
              <svg class="w-5 h-5 text-blue-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <div class="text-sm text-blue-800">
                <p class="font-medium mb-1">Consejos para configurar horarios:</p>
                <ul class="list-disc list-inside space-y-1 text-blue-700">
                  <li>Marca los días en los que el barbero trabaja</li>
                  <li>Define el horario de inicio y fin para cada día</li>
                  <li>Los horarios deben tener al menos 30 minutos de duración</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeScheduleModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            Cancelar
          </button>
          <button
            @click="saveSchedule"
            :disabled="savingSchedule"
            class="px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white border-0 rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:shadow-lg hover:-translate-y-0.5"
          >
            {{ savingSchedule ? 'Guardando...' : 'Guardar Horarios' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Modal de confirmación para activar/desactivar -->
    <div v-if="showStatusModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full">
        <div class="px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">
            {{ currentBarber?.disponible ? 'Desactivar Barbero' : 'Activar Barbero' }}
          </h2>
        </div>
        
        <div class="p-8">
          <div class="flex items-start gap-4 mb-4">
            <div :class="[
              'w-12 h-12 rounded-full flex items-center justify-center flex-shrink-0',
              currentBarber?.disponible ? 'bg-red-100' : 'bg-green-100'
            ]">
              <svg 
                class="w-6 h-6" 
                :class="currentBarber?.disponible ? 'text-red-600' : 'text-green-600'"
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path v-if="currentBarber?.disponible" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
                <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            
            <div class="flex-1">
              <p class="text-gray-900 font-medium mb-2">
                <template v-if="currentBarber?.disponible">
                  ¿Desactivar a <strong>{{ currentBarber?.nombre }}</strong>?
                </template>
                <template v-else>
                  ¿Activar a <strong>{{ currentBarber?.nombre }}</strong>?
                </template>
              </p>
              
              <div :class="[
                'text-sm rounded-lg p-3 mt-3',
                currentBarber?.disponible ? 'bg-red-50 text-red-700' : 'bg-green-50 text-green-700'
              ]">
                <template v-if="currentBarber?.disponible">
                  <p class="font-medium mb-1">Al desactivar este barbero:</p>
                  <ul class="list-disc list-inside space-y-1 text-xs">
                    <li>No aparecerá disponible para nuevas reservas</li>
                    <li>Las reservas existentes se mantendrán</li>
                    <li>Podrás reactivarlo cuando quieras</li>
                    <li>Todo su historial se conservará</li>
                  </ul>
                </template>
                <template v-else>
                  <p class="font-medium mb-1">Al activar este barbero:</p>
                  <ul class="list-disc list-inside space-y-1 text-xs">
                    <li>Estará disponible para nuevas reservas</li>
                    <li>Aparecerá en el listado de barberos activos</li>
                    <li>Mantendrá todo su historial anterior</li>
                  </ul>
                </template>
              </div>
            </div>
          </div>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeStatusModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            Cancelar
          </button>
          <button
            @click="confirmToggleStatus"
            :disabled="togglingStatus"
            :class="[
              'px-6 py-3 text-white border-0 rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed',
              currentBarber?.disponible 
                ? 'bg-red-500 hover:bg-red-600' 
                : 'bg-green-500 hover:bg-green-600'
            ]"
          >
            {{ togglingStatus ? 'Procesando...' : (currentBarber?.disponible ? 'Sí, desactivar' : 'Sí, activar') }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue'
import { barberService } from '@/services/barberService'

export default {
  name: 'AdminBarberos',
  setup() {
    // Estado reactivo
    const loadingStats = ref(true)
    const loadingBarbers = ref(true)
    const savingBarber = ref(false)
    const togglingStatus = ref(false)
    const savingSchedule = ref(false)
    
    const barbers = ref([])
    const stats = ref({})
    const modoDemo = ref(false)
    
    // Filtros
    const searchTerm = ref('')
    const statusFilter = ref('')
    const especialidadFilter = ref('')
    const sortBy = ref('nombre_asc')
    
    // Modales
    const showBarberModal = ref(false)
    const showStatusModal = ref(false)
    const showScheduleModal = ref(false)
    const isEditing = ref(false)
    const currentBarber = ref(null)
    
    // Formulario de barbero
    const barberForm = ref({
      nombre: '',
      email: '',
      telefono: '',
      especialidad: '',
      descripcion: '',
      experiencia_anos: 0,
      disponible: true,
      password: '',
      password_confirmation: ''
    })
    
    // Formulario de horarios
    const scheduleForm = ref({
      lunes: { activo: true, inicio: '09:00', fin: '18:00' },
      martes: { activo: true, inicio: '09:00', fin: '18:00' },
      miércoles: { activo: true, inicio: '09:00', fin: '18:00' },
      jueves: { activo: true, inicio: '09:00', fin: '18:00' },
      viernes: { activo: true, inicio: '09:00', fin: '18:00' },
      sábado: { activo: false, inicio: '09:00', fin: '14:00' },
      domingo: { activo: false, inicio: '09:00', fin: '14:00' }
    })
    
    // Días de la semana (formato corto para el formulario de barbero)
    const weekDays = [
      { value: 'lunes', label: 'Lun' },
      { value: 'martes', label: 'Mar' },
      { value: 'miércoles', label: 'Mié' },
      { value: 'jueves', label: 'Jue' },
      { value: 'viernes', label: 'Vie' },
      { value: 'sábado', label: 'Sáb' },
      { value: 'domingo', label: 'Dom' }
    ]

    // Días de la semana (formato completo para el modal de horarios)
    const weekDaysFull = [
      { value: 'lunes', label: 'Lunes' },
      { value: 'martes', label: 'Martes' },
      { value: 'miércoles', label: 'Miércoles' },
      { value: 'jueves', label: 'Jueves' },
      { value: 'viernes', label: 'Viernes' },
      { value: 'sábado', label: 'Sábado' },
      { value: 'domingo', label: 'Domingo' }
    ]
    
    // Computed
    const filteredBarbers = computed(() => {
      let filtered = [...barbers.value]
      
      // Filtro por término de búsqueda
      if (searchTerm.value) {
        const term = searchTerm.value.toLowerCase()
        filtered = filtered.filter(barber => 
          barber.nombre.toLowerCase().includes(term) ||
          barber.email.toLowerCase().includes(term) ||
          (barber.especialidad && barber.especialidad.toLowerCase().includes(term))
        )
      }
      
      // Filtro por estado
      if (statusFilter.value !== '') {
        const isDisponible = statusFilter.value === 'true'
        filtered = filtered.filter(barber => {
          // Asegurar que disponible sea un booleano
          const barberDisponible = barber.disponible === true || barber.disponible === 'true'
          return barberDisponible === isDisponible
        })
      }
      
      // Filtro por especialidad
      if (especialidadFilter.value) {
        filtered = filtered.filter(barber => 
          barber.especialidad && barber.especialidad.includes(especialidadFilter.value)
        )
      }
      
      // Ordenamiento
      if (sortBy.value) {
        filtered.sort((a, b) => {
          switch (sortBy.value) {
            case 'nombre_asc':
              return a.nombre.localeCompare(b.nombre)
            case 'nombre_desc':
              return b.nombre.localeCompare(a.nombre)
            case 'experiencia_desc':
              return (b.experiencia_anos || 0) - (a.experiencia_anos || 0)
            default:
              return 0
          }
        })
      }
      
      return filtered
    })
    
    // Computed para filtros activos
    const hasActiveFilters = computed(() => {
      return !!(searchTerm.value || statusFilter.value !== '' || especialidadFilter.value)
    })
    
    const isBarberFormValid = computed(() => {
      if (isEditing.value) {
        // Al editar, no se requieren campos de password
        return barberForm.value.nombre &&
               barberForm.value.especialidad
      } else {
        // Al crear, se requieren todos los campos incluyendo password
        return barberForm.value.nombre &&
               barberForm.value.email &&
               barberForm.value.especialidad &&
               barberForm.value.password &&
               barberForm.value.password_confirmation &&
               barberForm.value.password === barberForm.value.password_confirmation
      }
    })
    
    // Watchers para debugging
    watch(statusFilter, (newValue) => {
      console.log('🔍 Filtro de estado cambiado a:', newValue)
      console.log('📊 Barberos filtrados:', filteredBarbers.value.length)
      console.log('👥 Barberos totales:', barbers.value.length)
    })
    
    watch(filteredBarbers, (newValue) => {
      console.log('📋 Lista filtrada actualizada:', newValue.map(b => ({ nombre: b.nombre, disponible: b.disponible })))
    })
    
    // Métodos
    const loadBarbers = async () => {
      try {
        loadingBarbers.value = true
        // Pasar true para obtener TODOS los barberos (incluso desactivados)
        const data = await barberService.getAll(true)
        barbers.value = data
        console.log('📋 Barberos cargados:', data)
        console.log('📊 Estados disponible:', data.map(b => ({ nombre: b.nombre, disponible: b.disponible, tipo: typeof b.disponible })))
        modoDemo.value = false
      } catch (error) {
        console.error('Error cargando barberos:', error)
        barbers.value = barberService.getFallbackBarbers()
        modoDemo.value = true
      } finally {
        loadingBarbers.value = false
      }
    }
    
    const loadStats = async () => {
      try {
        loadingStats.value = true
        const data = await barberService.getStats()
        
        stats.value = {
          total: data.total || 0,
          activos: data.activos || 0,
          disponibles_hoy: data.disponibles_hoy || data.activos || 0,
          promedio_reservas: data.promedio_reservas || 0
        }
      } catch (error) {
        console.error('Error cargando estadísticas:', error)
        
        const totalBarbers = barbers.value.length
        const activeBarberos = barbers.value.filter(b => b.disponible).length
        
        stats.value = {
          total: totalBarbers,
          activos: activeBarberos,
          disponibles_hoy: activeBarberos,
          promedio_reservas: 12
        }
      } finally {
        loadingStats.value = false
      }
    }
    
    const resetForm = () => {
      barberForm.value = {
        nombre: '',
        email: '',
        telefono: '',
        especialidad: '',
        descripcion: '',
        experiencia_anos: 0,
        disponible: true,
        password: '',
        password_confirmation: ''
      }
    }
    
    const openCreateModal = () => {
      resetForm()
      isEditing.value = false
      showBarberModal.value = true
    }
    
    const closeBarberModal = () => {
      showBarberModal.value = false
      currentBarber.value = null
      resetForm()
    }
    
    const editBarber = (barber) => {
      currentBarber.value = barber
      isEditing.value = true
      
      barberForm.value = {
        nombre: barber.nombre || '',
        email: barber.email || '',
        telefono: barber.telefono || '',
        especialidad: barber.especialidad || '',
        descripcion: barber.descripcion || '',
        experiencia_anos: barber.experiencia_anos || 0,
        disponible: barber.disponible !== false,
        password: '',
        password_confirmation: ''
      }
      
      showBarberModal.value = true
    }
    
    const saveBarber = async () => {
      try {
        savingBarber.value = true
        
        // Preparar datos según si es creación o edición
        const dataToSend = {
          nombre: barberForm.value.nombre,
          especialidad: barberForm.value.especialidad,
          telefono: barberForm.value.telefono,
          descripcion: barberForm.value.descripcion,
          experiencia_anos: barberForm.value.experiencia_anos,
          disponible: barberForm.value.disponible
        }

        if (isEditing.value) {
          // Actualizar barbero existente
          await barberService.update(currentBarber.value.id, dataToSend)
          console.log('✅ Barbero actualizado correctamente')
        } else {
          // Crear nuevo barbero (incluir email y password)
          dataToSend.email = barberForm.value.email
          dataToSend.password = barberForm.value.password
          dataToSend.password_confirmation = barberForm.value.password_confirmation
          
          await barberService.create(dataToSend)
          console.log('✅ Barbero creado correctamente')
        }
        
        await loadBarbers()
        await loadStats()
        closeBarberModal()
        
      } catch (error) {
        console.error('Error guardando barbero:', error)
        alert(error.message || 'Error al guardar el barbero')
      } finally {
        savingBarber.value = false
      }
    }
    
    const toggleBarberStatus = (barber) => {
      currentBarber.value = barber
      showStatusModal.value = true
    }
    
    const closeStatusModal = () => {
      showStatusModal.value = false
      currentBarber.value = null
    }
    
    const confirmToggleStatus = async () => {
      try {
        togglingStatus.value = true
        
        // Cambiar el estado de disponibilidad
        const newStatus = !currentBarber.value.disponible
        
        await barberService.update(currentBarber.value.id, {
          disponible: newStatus
        })
        
        console.log(`✅ Barbero ${newStatus ? 'activado' : 'desactivado'} correctamente`)
        
        await loadBarbers()
        await loadStats()
        closeStatusModal()
        
      } catch (error) {
        console.error('Error cambiando estado del barbero:', error)
        alert('Error al cambiar el estado del barbero')
      } finally {
        togglingStatus.value = false
      }
    }
    
    const manageSchedule = (barber) => {
      currentBarber.value = barber
      
      // Cargar horarios existentes o usar valores por defecto
      if (barber.horario_trabajo && typeof barber.horario_trabajo === 'object') {
        // Si el barbero tiene horarios guardados, cargarlos
        Object.keys(scheduleForm.value).forEach(day => {
          if (barber.horario_trabajo[day]) {
            scheduleForm.value[day] = {
              activo: barber.horario_trabajo[day].activo !== false,
              inicio: barber.horario_trabajo[day].inicio || '09:00',
              fin: barber.horario_trabajo[day].fin || '18:00'
            }
          }
        })
      } else {
        // Valores por defecto
        scheduleForm.value = {
          lunes: { activo: true, inicio: '09:00', fin: '18:00' },
          martes: { activo: true, inicio: '09:00', fin: '18:00' },
          miércoles: { activo: true, inicio: '09:00', fin: '18:00' },
          jueves: { activo: true, inicio: '09:00', fin: '18:00' },
          viernes: { activo: true, inicio: '09:00', fin: '18:00' },
          sábado: { activo: false, inicio: '09:00', fin: '14:00' },
          domingo: { activo: false, inicio: '09:00', fin: '14:00' }
        }
      }
      
      showScheduleModal.value = true
    }

    const closeScheduleModal = () => {
      showScheduleModal.value = false
      currentBarber.value = null
    }

    const saveSchedule = async () => {
      try {
        savingSchedule.value = true
        
        // Preparar datos de horarios para enviar al backend
        const horarioData = {
          horario_trabajo: scheduleForm.value
        }
        
        await barberService.update(currentBarber.value.id, horarioData)
        console.log('✅ Horarios guardados correctamente')
        
        await loadBarbers()
        closeScheduleModal()
        
      } catch (error) {
        console.error('Error guardando horarios:', error)
        alert('Error al guardar los horarios')
      } finally {
        savingSchedule.value = false
      }
    }
    
    // Helpers
    const clearFilters = () => {
      searchTerm.value = ''
      statusFilter.value = ''
      especialidadFilter.value = ''
      sortBy.value = 'nombre_asc'
    }

    const getEspecialidadLabel = (especialidad) => {
      const labels = {
        'Especialista en cortes modernos': 'Cortes Modernos',
        'Barba y Bigote': 'Barba y Bigote',
        'Tratamientos': 'Tratamientos',
        'Cortes Clásicos': 'Cortes Clásicos'
      }
      return labels[especialidad] || especialidad
    }
    
    const getInitials = (name) => {
      if (!name || typeof name !== 'string') {
        return '??'
      }
      return name.split(' ')
        .map(word => word.charAt(0))
        .join('')
        .toUpperCase()
        .slice(0, 2)
    }
    
    const getWorkingDays = (days) => {
      if (!days || !Array.isArray(days)) {
        return 'No definido'
      }
      
      const dayLabels = {
        lunes: 'L', martes: 'M', miércoles: 'X', jueves: 'J',
        viernes: 'V', sábado: 'S', domingo: 'D',
        monday: 'L', tuesday: 'M', wednesday: 'X', thursday: 'J',
        friday: 'V', saturday: 'S', sunday: 'D'
      }
      
      return days.map(day => dayLabels[day] || day.charAt(0).toUpperCase()).join(', ')
    }

    const getWorkingDaysFromSchedule = (horario_trabajo) => {
      if (!horario_trabajo || typeof horario_trabajo !== 'object') {
        return 'No definido'
      }

      const dayLabels = {
        lunes: 'L', martes: 'M', miércoles: 'X', jueves: 'J',
        viernes: 'V', sábado: 'S', domingo: 'D'
      }

      const activeDays = Object.keys(horario_trabajo)
        .filter(day => horario_trabajo[day]?.activo)
        .map(day => dayLabels[day] || day.charAt(0).toUpperCase())

      return activeDays.length > 0 ? activeDays.join(', ') : 'No definido'
    }

    const getWorkScheduleSummary = (horario_trabajo) => {
      if (!horario_trabajo || typeof horario_trabajo !== 'object') {
        return 'No definido'
      }

      // Obtener el primer día activo para mostrar su horario
      const activeDays = Object.keys(horario_trabajo).filter(day => horario_trabajo[day]?.activo)
      
      if (activeDays.length === 0) {
        return 'No definido'
      }

      const firstDay = horario_trabajo[activeDays[0]]
      return `${firstDay.inicio || '09:00'} - ${firstDay.fin || '18:00'}`
    }
    
    // Lifecycle
    onMounted(async () => {
      await loadBarbers()
      await loadStats()
    })
    
    return {
      // Estado
      loadingStats,
      loadingBarbers,
      savingBarber,
      togglingStatus,
      savingSchedule,
      barbers,
      stats,
      modoDemo,
      searchTerm,
      statusFilter,
      especialidadFilter,
      sortBy,
      showBarberModal,
      showStatusModal,
      showScheduleModal,
      isEditing,
      currentBarber,
      barberForm,
      scheduleForm,
      
      // Configuración
      weekDays,
      weekDaysFull,
      
      // Computed
      filteredBarbers,
      hasActiveFilters,
      isBarberFormValid,
      
      // Métodos
      loadBarbers,
      loadStats,
      clearFilters,
      openCreateModal,
      closeBarberModal,
      editBarber,
      saveBarber,
      toggleBarberStatus,
      closeStatusModal,
      confirmToggleStatus,
      manageSchedule,
      closeScheduleModal,
      saveSchedule,
      
      // Helpers
      getInitials,
      getEspecialidadLabel,
      getWorkingDays,
      getWorkingDaysFromSchedule,
      getWorkScheduleSummary
    }
  }
}
</script>

<style scoped>
/* AdminBarberos.vue - Tailwind CSS v4 */
/* Todas las utilidades son nativas de Tailwind v4 */
/* No se requiere CSS custom - 100% utility-first */
</style>