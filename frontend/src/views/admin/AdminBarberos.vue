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
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-black to-gray-500 text-white border-none rounded-xl font-semibold text-sm cursor-pointer transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5 disabled:opacity-70 disabled:cursor-not-allowed disabled:transform-none"
          >
            <svg :class="{ 'animate-spin': loadingBarbers }" class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            {{ loadingBarbers ? 'Actualizando...' : 'Actualizar' }}
          </button>
          <button 
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white border-none rounded-xl font-semibold text-sm cursor-pointer transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5"
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
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
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
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
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
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
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
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:transform hover:-translate-y-1">
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
      <div class="flex flex-col sm:flex-row gap-4 items-stretch sm:items-center">
        <input
          v-model="searchTerm"
          type="text"
          placeholder="Buscar barberos..."
          class="flex-1 min-w-0 px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:ring-2 focus:ring-violet-500 focus:border-transparent transition-all duration-200"
        />
        
        <select v-model="statusFilter" class="px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:ring-2 focus:ring-violet-500 focus:border-transparent transition-all duration-200 min-w-[180px]">
          <option value="">Todos los estados</option>
          <option value="true">Disponibles</option>
          <option value="false">No Disponibles</option>
        </select>
        
        <select v-model="especialidadFilter" class="px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:ring-2 focus:ring-violet-500 focus:border-transparent transition-all duration-200 min-w-[200px]">
          <option value="">Todas las especialidades</option>
          <option value="Especialista en cortes modernos">Cortes Modernos</option>
          <option value="Barba y Bigote">Barba y Bigote</option>
          <option value="Tratamientos">Tratamientos</option>
          <option value="Cortes Clásicos">Cortes Clásicos</option>
        </select>
      </div>
    </div>

    <!-- Lista de barberos modernizada -->
    <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200">
      <div v-if="loadingBarbers" class="flex flex-col items-center justify-center py-16 text-gray-500">
        <div class="w-12 h-12 border-3 border-gray-200 border-t-violet-500 rounded-full animate-spin mb-4"></div>
        <p class="text-lg font-medium">Cargando barberos...</p>
      </div>
      
      <div v-else-if="filteredBarbers.length === 0" class="flex flex-col items-center justify-center py-16 text-gray-500 text-center">
        <svg class="w-16 h-16 text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
        </svg>
        <h3 class="text-xl font-semibold text-gray-700 mb-2">No se encontraron barberos</h3>
        <p class="text-gray-500 mb-6">No hay barberos que coincidan con los filtros aplicados.</p>
        <button @click="openCreateModal" class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white border-none rounded-xl font-semibold text-sm cursor-pointer transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5">
          Crear primer barbero
        </button>
      </div>
      
      <div v-else class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
        <div
          v-for="barber in filteredBarbers"
          :key="barber.id"
          class="bg-slate-50 border border-slate-200 rounded-2xl p-6 transition-all duration-200 hover:border-violet-400 hover:shadow-lg hover:-translate-y-0.5"
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
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Horario:</span>
              <span class="text-sm text-gray-900 font-medium">
                {{ barber.horario_inicio || '09:00' }} - {{ barber.horario_fin || '18:00' }}
              </span>
            </div>
            
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Días:</span>
              <span class="text-sm text-gray-900 font-medium">{{ getWorkingDays(barber.dias_trabajo) }}</span>
            </div>
            
            <div v-if="barber.experiencia" class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Experiencia:</span>
              <span class="text-sm text-gray-900 font-medium">{{ barber.experiencia }}</span>
            </div>
          </div>
          
          <div class="flex gap-2 justify-end flex-wrap">
            <button @click="editBarber(barber)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg cursor-pointer transition-all duration-200 bg-amber-50 text-amber-700 border-amber-200 hover:bg-amber-100 hover:border-amber-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
              Editar
            </button>
            
            <button @click="manageSchedule(barber)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg cursor-pointer transition-all duration-200 bg-green-50 text-green-700 border-green-200 hover:bg-green-100 hover:border-green-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
              Horarios
            </button>
            
            <button @click="deleteBarber(barber)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg cursor-pointer transition-all duration-200 bg-red-50 text-red-700 border-red-200 hover:bg-red-100 hover:border-red-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
              Eliminar
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

            <div class="space-y-2">
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

            <div class="space-y-2">
              <label for="telefono" class="block text-sm font-medium text-gray-700">Teléfono</label>
              <input
                id="telefono"
                v-model="barberForm.telefono"
                type="tel"
                placeholder="+34 123 456 789"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
              />
            </div>

            <div class="space-y-2">
              <label for="especialidad" class="block text-sm font-medium text-gray-700">Especialidad *</label>
              <select id="especialidad" v-model="barberForm.especialidad" required class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent">
                <option value="">Selecciona una especialidad</option>
                <option value="Especialista en cortes modernos">Cortes Modernos</option>
                <option value="Barba y Bigote">Barba y Bigote</option>
                <option value="Tratamientos">Tratamientos</option>
                <option value="Cortes Clásicos">Cortes Clásicos</option>
              </select>
            </div>

            <div class="space-y-2">
              <label for="experiencia" class="block text-sm font-medium text-gray-700">Experiencia</label>
              <input
                id="experiencia"
                v-model="barberForm.experiencia"
                type="text"
                placeholder="Ej: 5 años"
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

            <div class="space-y-2">
              <label for="horario_inicio" class="block text-sm font-medium text-gray-700">Hora de inicio</label>
              <input
                id="horario_inicio"
                v-model="barberForm.horario_inicio"
                type="time"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
              />
            </div>

            <div class="space-y-2">
              <label for="horario_fin" class="block text-sm font-medium text-gray-700">Hora de fin</label>
              <input
                id="horario_fin"
                v-model="barberForm.horario_fin"
                type="time"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
              />
            </div>
          </div>

          <div class="space-y-2 mb-6">
            <label class="block text-sm font-medium text-gray-700">Días de trabajo</label>
            <div class="grid grid-cols-3 md:grid-cols-7 gap-2">
              <label
                v-for="day in weekDays"
                :key="day.value"
                :class="['flex items-center justify-center px-3 py-3 border rounded-xl cursor-pointer transition-all duration-200 text-sm font-medium',
                  barberForm.dias_trabajo.includes(day.value) 
                    ? 'bg-violet-100 border-violet-400 text-violet-700' 
                    : 'bg-white border-gray-300 text-gray-600 hover:bg-gray-50 hover:border-gray-400']"
              >
                <input
                  type="checkbox"
                  :value="day.value"
                  v-model="barberForm.dias_trabajo"
                  class="hidden"
                />
                <span>{{ day.label }}</span>
              </label>
            </div>
          </div>

          <div class="flex justify-end gap-3 pt-6 border-t border-gray-200 bg-gray-50 -mx-8 -mb-8 px-8 py-6 rounded-b-2xl">
            <button type="button" @click="closeBarberModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
              Cancelar
            </button>
            <button
              type="submit"
              :disabled="!isBarberFormValid || savingBarber"
              class="px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white border-none rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:shadow-lg hover:-translate-y-0.5"
            >
              {{ savingBarber ? 'Guardando...' : (isEditing ? 'Actualizar' : 'Crear') }}
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal de confirmación para eliminar modernizado -->
    <div v-if="showDeleteModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full">
        <div class="px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">Eliminar Barbero</h2>
        </div>
        
        <div class="p-8">
          <p class="text-gray-600 mb-2">¿Estás seguro de que quieres eliminar a <strong>{{ currentBarber?.nombre }}</strong>?</p>
          <p class="text-sm text-gray-500">Esta acción no se puede deshacer.</p>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeDeleteModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            Cancelar
          </button>
          <button
            @click="confirmDelete"
            :disabled="deletingBarber"
            class="px-6 py-3 bg-red-500 text-white border-none rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-red-600"
          >
            {{ deletingBarber ? 'Eliminando...' : 'Eliminar' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { barberService } from '@/services/barberService'

export default {
  name: 'AdminBarberos',
  setup() {
    // Estado reactivo
    const loadingStats = ref(true)
    const loadingBarbers = ref(true)
    const savingBarber = ref(false)
    const deletingBarber = ref(false)
    
    const barbers = ref([])
    const stats = ref({})
    const modoDemo = ref(false)
    
    // Filtros
    const searchTerm = ref('')
    const statusFilter = ref('')
    const especialidadFilter = ref('')
    
    // Modales
    const showBarberModal = ref(false)
    const showDeleteModal = ref(false)
    const isEditing = ref(false)
    const currentBarber = ref(null)
    
    // Formulario
    const barberForm = ref({
      nombre: '',
      email: '',
      telefono: '',
      especialidad: '',
      experiencia: '',
      disponible: true,
      horario_inicio: '09:00',
      horario_fin: '18:00',
      dias_trabajo: ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
    })
    
    // Días de la semana
    const weekDays = [
      { value: 'lunes', label: 'Lun' },
      { value: 'martes', label: 'Mar' },
      { value: 'miércoles', label: 'Mié' },
      { value: 'jueves', label: 'Jue' },
      { value: 'viernes', label: 'Vie' },
      { value: 'sábado', label: 'Sáb' },
      { value: 'domingo', label: 'Dom' }
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
        filtered = filtered.filter(barber => barber.disponible === isDisponible)
      }
      
      // Filtro por especialidad
      if (especialidadFilter.value) {
        filtered = filtered.filter(barber => 
          barber.especialidad && barber.especialidad.includes(especialidadFilter.value)
        )
      }
      
      return filtered
    })
    
    const isBarberFormValid = computed(() => {
      return barberForm.value.nombre &&
             barberForm.value.email &&
             barberForm.value.especialidad
    })
    
    // Métodos
    const loadBarbers = async () => {
      try {
        loadingBarbers.value = true
        const data = await barberService.getAll()
        barbers.value = data
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
        experiencia: '',
        disponible: true,
        horario_inicio: '09:00',
        horario_fin: '18:00',
        dias_trabajo: ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
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
        experiencia: barber.experiencia || '',
        disponible: barber.disponible !== false,
        horario_inicio: barber.horario_inicio || '09:00',
        horario_fin: barber.horario_fin || '18:00',
        dias_trabajo: barber.dias_trabajo || ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
      }
      
      showBarberModal.value = true
    }
    
    const saveBarber = async () => {
      try {
        savingBarber.value = true
        
        if (isEditing.value) {
          await barberService.update(currentBarber.value.id, barberForm.value)
        } else {
          await barberService.create(barberForm.value)
        }
        
        await loadBarbers()
        await loadStats()
        closeBarberModal()
        
      } catch (error) {
        console.error('Error guardando barbero:', error)
      } finally {
        savingBarber.value = false
      }
    }
    
    const deleteBarber = (barber) => {
      currentBarber.value = barber
      showDeleteModal.value = true
    }
    
    const closeDeleteModal = () => {
      showDeleteModal.value = false
      currentBarber.value = null
    }
    
    const confirmDelete = async () => {
      try {
        deletingBarber.value = true
        await barberService.delete(currentBarber.value.id)
        await loadBarbers()
        await loadStats()
        closeDeleteModal()
      } catch (error) {
        console.error('Error eliminando barbero:', error)
      } finally {
        deletingBarber.value = false
      }
    }
    
    const manageSchedule = (barber) => {
      console.log('Gestionar horarios:', barber)
    }
    
    // Helpers
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
      deletingBarber,
      barbers,
      stats,
      modoDemo,
      searchTerm,
      statusFilter,
      especialidadFilter,
      showBarberModal,
      showDeleteModal,
      isEditing,
      currentBarber,
      barberForm,
      
      // Configuración
      weekDays,
      
      // Computed
      filteredBarbers,
      isBarberFormValid,
      
      // Métodos
      loadBarbers,
      loadStats,
      openCreateModal,
      closeBarberModal,
      editBarber,
      saveBarber,
      deleteBarber,
      closeDeleteModal,
      confirmDelete,
      manageSchedule,
      
      // Helpers
      getInitials,
      getWorkingDays
    }
  }
}
</script>

<style scoped>
/* Estilos esenciales para AdminBarberos */

/* Animaciones necesarias */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

/* Utilidades para transiciones suaves */
.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

/* Estilos de enfoque personalizados si es necesario */
.focus-ring:focus {
  outline: 2px solid #8b5cf6;
  outline-offset: 2px;
}

/* Estilos para elementos interactivos */
.hover-lift:hover {
  transform: translateY(-2px);
}
</style>