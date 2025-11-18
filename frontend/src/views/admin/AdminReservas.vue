<!--
  AdminReservas.vue - Gestión completa de reservas
  FASE 8.4: Integración con base de datos real
-->
<template>
  <div class="p-8 bg-gradient-to-br from-slate-50 to-slate-100 min-h-[calc(100vh-80px)]">
    <!-- Header del dashboard modernizado -->
    <div class="mb-6 bg-white rounded-2xl p-6 shadow-sm border border-gray-200">
      <div class="flex flex-col lg:flex-row lg:justify-between lg:items-start gap-6">
        <div class="flex-1">
          <h1 class="text-3xl font-extrabold bg-gradient-to-r from-black to-gray-500 bg-clip-text text-transparent mb-2">
            Gestión de Reservas
          </h1>
          <p class="text-lg text-gray-600 font-medium">
            Panel de administración y control de reservas de Low Barber Shop
          </p>
        </div>
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
          <button 
            @click="loadReservations" 
            :disabled="loadingReservations"
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-black to-gray-500 text-white border-0 rounded-xl font-semibold text-sm transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5 disabled:opacity-70 disabled:cursor-not-allowed"
          >
            <svg :class="{ 'animate-spin': loadingReservations }" class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            {{ loadingReservations ? 'Actualizando...' : 'Actualizar' }}
          </button>
          <button 
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white border-0 rounded-xl font-semibold text-sm transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5"
            @click="openCreateModal"
          >
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
            </svg>
            Nueva Reserva
          </button>
        </div>
      </div>
    </div> 

    <!-- Grid de estadísticas modernizado -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <!-- Total de reservas -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Total</h3>
            <p class="text-3xl font-black text-blue-600">{{ stats.total || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-blue-100 to-blue-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Reservas de hoy -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Hoy</h3>
            <p class="text-3xl font-black text-emerald-600">{{ stats.today || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-emerald-100 to-emerald-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Reservas pendientes -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Pendientes</h3>
            <p class="text-3xl font-black text-amber-600">{{ stats.pending || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-amber-100 to-amber-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Reservas completadas -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Completadas</h3>
            <p class="text-3xl font-black text-green-600">{{ stats.completed || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-green-100 to-green-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
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
              placeholder="Buscar por cliente, barbero, servicio o email..."
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
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <!-- Filtro por Estado -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Estado</label>
            <select 
              v-model="statusFilter" 
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
            >
              <option value="">Todos</option>
              <option value="pendiente">⏳ Pendientes</option>
              <option value="confirmada">✓ Confirmadas</option>
              <option value="completada">✓✓ Completadas</option>
              <option value="cancelada">✗ Canceladas</option>
            </select>
          </div>

          <!-- Filtro por Barbero -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Barbero</label>
            <select 
              v-model="barberFilter" 
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
            >
              <option value="">Todos los barberos</option>
              <option v-for="barber in availableBarbers" :key="barber.id" :value="barber.id">
                {{ barber.nombre }}
              </option>
            </select>
          </div>

          <!-- Ordenar por -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Ordenar por</label>
            <select 
              v-model="sortBy" 
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
            >
              <option value="fecha_desc">📅 Fecha: Más reciente</option>
              <option value="fecha_asc">📅 Fecha: Más antigua</option>
              <option value="cliente_asc">👤 Cliente: A-Z</option>
              <option value="cliente_desc">👤 Cliente: Z-A</option>
              <option value="estado">📊 Estado</option>
            </select>
          </div>

          <!-- Filtro por Rango de Fechas -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Periodo</label>
            <select 
              v-model="dateRangeFilter" 
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
            >
              <option value="">Todas las fechas</option>
              <option value="today">🔵 Hoy</option>
              <option value="tomorrow">🟢 Mañana</option>
              <option value="this_week">📆 Esta semana</option>
              <option value="next_week">📆 Próxima semana</option>
              <option value="this_month">📅 Este mes</option>
              <option value="past">⏮️ Pasadas</option>
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
          
          <span v-if="statusFilter" class="inline-flex items-center gap-1 px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-medium">
            Estado: {{ getStatusLabel(statusFilter) }}
            <button @click="statusFilter = ''" class="hover:text-blue-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>
          
          <span v-if="barberFilter" class="inline-flex items-center gap-1 px-3 py-1 bg-green-100 text-green-700 rounded-full text-xs font-medium">
            Barbero seleccionado
            <button @click="barberFilter = ''" class="hover:text-green-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>
          
          <span v-if="dateRangeFilter" class="inline-flex items-center gap-1 px-3 py-1 bg-orange-100 text-orange-700 rounded-full text-xs font-medium">
            Periodo: {{ getDateRangeLabel(dateRangeFilter) }}
            <button @click="dateRangeFilter = ''" class="hover:text-orange-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>

          <span class="text-xs text-gray-500 ml-auto">
            {{ filteredReservations.length }} resultado{{ filteredReservations.length !== 1 ? 's' : '' }}
          </span>
        </div>
      </div>
    </div>

    <!-- Lista de reservas modernizada -->
    <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-200">
      <div v-if="loadingReservations" class="flex flex-col items-center justify-center py-16 text-gray-500">
        <div class="w-12 h-12 border-[3px] border-gray-200 border-t-violet-500 rounded-full animate-spin mb-4"></div>
        <p class="text-lg font-medium">Cargando reservas...</p>
      </div>
      
      <div v-else-if="filteredReservations.length === 0" class="flex flex-col items-center justify-center py-16 text-gray-500 text-center">
        <svg class="w-16 h-16 text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
        </svg>
        <h3 class="text-xl font-semibold text-gray-700 mb-2">No se encontraron reservas</h3>
        <p class="text-gray-500 mb-6">No hay reservas que coincidan con los filtros aplicados.</p>
      </div>
      
      <div v-else class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
        <div
          v-for="reservation in filteredReservations"
          :key="reservation.id"
          class="bg-slate-50 border border-slate-200 rounded-2xl p-6 transition-all duration-200 hover:shadow-lg hover:-translate-y-0.5"
        >
          <!-- Header de la reserva con cliente -->
          <div class="flex items-start gap-4 mb-4">
            <div class="w-12 h-12 flex-shrink-0">
              <div class="w-full h-full rounded-xl bg-gradient-to-br from-blue-500 to-blue-600 text-white flex items-center justify-center font-semibold text-sm">
                {{ getInitials(reservation.cliente_nombre || 'Usuario') }}
              </div>
            </div>
            
            <div class="flex-1 min-w-0">
              <h3 class="font-semibold text-gray-900 text-base mb-1 truncate">{{ reservation.cliente_nombre || 'Sin nombre' }}</h3>
              <p class="text-gray-500 text-sm mb-2 truncate">{{ reservation.cliente_email || 'Sin email' }}</p>
              <span :class="getStatusBadgeClass(reservation.estado)" class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold">
                <div :class="getStatusDotClass(reservation.estado)" class="w-2 h-2 rounded-full"></div>
                {{ getStatusLabel(reservation.estado) }}
              </span>
            </div>
          </div>
          
          <!-- Información de la reserva -->
          <div class="space-y-3 mb-4">
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Barbero:</span>
              <span class="text-sm text-gray-900 font-medium">
                {{ reservation.barbero_nombre || 'Sin asignar' }}
              </span>
            </div>
            
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Fecha:</span>
              <span class="text-sm text-gray-900 font-medium">{{ formatDate(reservation.fecha_reserva) }}</span>
            </div>
            
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Hora:</span>
              <span class="text-sm text-gray-900 font-medium">{{ formatTime(reservation.hora_inicio) }}</span>
            </div>
            
            <div v-if="reservation.servicio_nombre" class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Servicio:</span>
              <span class="text-sm text-gray-900 font-medium">{{ reservation.servicio_nombre }}</span>
            </div>
          </div>
          
          <!-- Acciones -->
          <div class="flex gap-2 justify-end flex-wrap">
            <button @click="viewReservation(reservation)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200 bg-blue-50 text-blue-700 border-blue-200 hover:bg-blue-100 hover:border-blue-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
              </svg>
              Ver
            </button>
            
            <button v-if="reservation.estado === 'pendiente'" @click="confirmReservation(reservation)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200 bg-green-50 text-green-700 border-green-200 hover:bg-green-100 hover:border-green-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              Confirmar
            </button>
            
            <button v-if="reservation.estado === 'confirmada'" @click="completeReservation(reservation)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200 bg-emerald-50 text-emerald-700 border-emerald-200 hover:bg-emerald-100 hover:border-emerald-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Completar
            </button>
            
            <button v-if="reservation.estado !== 'completada' && reservation.estado !== 'cancelada'" @click="editReservation(reservation)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200 bg-amber-50 text-amber-700 border-amber-200 hover:bg-amber-100 hover:border-amber-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
              Editar
            </button>
            
            <button v-if="reservation.estado !== 'completada' && reservation.estado !== 'cancelada'" @click="cancelReservation(reservation)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200 bg-red-50 text-red-700 border-red-200 hover:bg-red-100 hover:border-red-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
              Cancelar
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal para Ver Reserva -->
    <div v-if="showViewModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">Detalles de la Reserva</h2>
          <button @click="closeViewModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="p-8" v-if="currentReservation">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Información del Cliente -->
            <div class="bg-slate-50 rounded-xl p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <svg class="w-5 h-5 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
                Cliente
              </h3>
              <div class="space-y-3">
                <div>
                  <span class="text-sm font-medium text-gray-600">Nombre:</span>
                  <p class="text-sm text-gray-900 font-medium">{{ currentReservation.cliente_nombre || 'Sin nombre' }}</p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Email:</span>
                  <p class="text-sm text-gray-900">{{ currentReservation.cliente_email || 'Sin email' }}</p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Teléfono:</span>
                  <p class="text-sm text-gray-900">{{ currentReservation.cliente_telefono || 'Sin teléfono' }}</p>
                </div>
              </div>
            </div>

            <!-- Información del Servicio -->
            <div class="bg-slate-50 rounded-xl p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <svg class="w-5 h-5 mr-2 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
                </svg>
                Servicio
              </h3>
              <div class="space-y-3">
                <div>
                  <span class="text-sm font-medium text-gray-600">Servicio:</span>
                  <p class="text-sm text-gray-900 font-medium">{{ currentReservation.servicio_nombre || 'Sin servicio' }}</p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Barbero:</span>
                  <p class="text-sm text-gray-900">{{ currentReservation.barbero_nombre || 'Sin asignar' }}</p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Precio:</span>
                  <p class="text-sm text-gray-900 font-medium">Bs {{ currentReservation.servicio_precio || 'No definido' }}</p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Duración:</span>
                  <p class="text-sm text-gray-900">{{ currentReservation.servicio_duracion || 'No definida' }} minutos</p>
                </div>
              </div>
            </div>

            <!-- Información de la Cita -->
            <div class="bg-slate-50 rounded-xl p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <svg class="w-5 h-5 mr-2 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                Fecha y Hora
              </h3>
              <div class="space-y-3">
                <div>
                  <span class="text-sm font-medium text-gray-600">Fecha:</span>
                  <p class="text-sm text-gray-900 font-medium">{{ formatDate(currentReservation.fecha_reserva) }}</p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Hora:</span>
                  <p class="text-sm text-gray-900 font-medium">{{ formatTime(currentReservation.hora_inicio) }}</p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Estado:</span>
                  <span :class="getStatusBadgeClass(currentReservation.estado)" class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold">
                    <div :class="getStatusDotClass(currentReservation.estado)" class="w-2 h-2 rounded-full"></div>
                    {{ getStatusLabel(currentReservation.estado) }}
                  </span>
                </div>
              </div>
            </div>

            <!-- Notas -->
            <div class="bg-slate-50 rounded-xl p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <svg class="w-5 h-5 mr-2 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
                Notas
              </h3>
              <div class="space-y-3">
                <div>
                  <span class="text-sm font-medium text-gray-600">Notas:</span>
                  <p class="text-sm text-gray-900">{{ currentReservation.notas || 'Sin notas adicionales' }}</p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">ID:</span>
                  <p class="text-xs text-gray-500 font-mono">{{ currentReservation.id }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeViewModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            Cerrar
          </button>
        </div>
      </div>
    </div>

    <!-- Modal para Editar Reserva -->
    <div v-if="showEditModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">Editar Reserva</h2>
          <button @click="closeEditModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="p-8" v-if="currentReservation">
          <div class="bg-amber-50 border border-amber-200 rounded-xl p-4 mb-6">
            <div class="flex items-center">
              <svg class="w-5 h-5 text-amber-600 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.864-.833-2.634 0L4.732 8.5C3.962 14.833 4.924 16.5 6.464 16.5z" />
              </svg>
              <span class="text-amber-800 font-medium">Función en desarrollo</span>
            </div>
            <p class="text-amber-700 text-sm mt-1">Esta funcionalidad permitirá modificar fecha, hora, barbero, servicio y notas de la reserva.</p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="space-y-4">
              <h3 class="text-lg font-semibold text-gray-900">Datos Actuales</h3>
              <div class="space-y-2">
                <p><span class="font-medium text-gray-600">Cliente:</span> {{ currentReservation.cliente_nombre }}</p>
                <p><span class="font-medium text-gray-600">Fecha:</span> {{ formatDate(currentReservation.fecha_reserva) }}</p>
                <p><span class="font-medium text-gray-600">Hora:</span> {{ formatTime(currentReservation.hora_inicio) }}</p>
                <p><span class="font-medium text-gray-600">Barbero:</span> {{ currentReservation.barbero_nombre }}</p>
                <p><span class="font-medium text-gray-600">Servicio:</span> {{ currentReservation.servicio_nombre }}</p>
                <p><span class="font-medium text-gray-600">Estado:</span> {{ getStatusLabel(currentReservation.estado) }}</p>
              </div>
            </div>
            
            <div class="space-y-4">
              <h3 class="text-lg font-semibold text-gray-900">Próximamente</h3>
              <div class="text-sm text-gray-600 space-y-2">
                <p>• Cambiar fecha y hora</p>
                <p>• Reasignar barbero</p>
                <p>• Modificar servicio</p>
                <p>• Actualizar notas</p>
                <p>• Cambiar información de contacto</p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeEditModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            Cerrar
          </button>
        </div>
      </div>
    </div>

    <!-- Modal para Confirmar Reserva -->
    <div v-if="showConfirmModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">Confirmar Reserva</h2>
          <button @click="closeConfirmModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="p-8" v-if="currentReservation">
          <div class="text-center mb-6">
            <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">¿Confirmar esta reserva?</h3>
            <p class="text-gray-600">La reserva pasará de pendiente a confirmada</p>
          </div>

          <div class="bg-slate-50 rounded-xl p-4 space-y-2">
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Cliente:</span>
              <span class="text-sm text-gray-900">{{ currentReservation.cliente_nombre }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Fecha:</span>
              <span class="text-sm text-gray-900">{{ formatDate(currentReservation.fecha_reserva) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Hora:</span>
              <span class="text-sm text-gray-900">{{ formatTime(currentReservation.hora_inicio) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Servicio:</span>
              <span class="text-sm text-gray-900">{{ currentReservation.servicio_nombre }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Barbero:</span>
              <span class="text-sm text-gray-900">{{ currentReservation.barbero_nombre }}</span>
            </div>
          </div>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeConfirmModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            Cancelar
          </button>
          <button @click="proceedConfirm" :disabled="confirmingReservation" class="px-6 py-3 bg-green-500 text-white border-0 rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-green-600">
            {{ confirmingReservation ? 'Confirmando...' : 'Confirmar' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Modal para Completar Reserva -->
    <div v-if="showCompleteModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">Completar Reserva</h2>
          <button @click="closeCompleteModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="p-8" v-if="currentReservation">
          <div class="text-center mb-6">
            <div class="w-16 h-16 bg-emerald-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">¿Marcar como completada?</h3>
            <p class="text-gray-600">El servicio ha sido realizado y el cliente está satisfecho</p>
          </div>

          <div class="bg-emerald-50 border border-emerald-200 rounded-xl p-4 mb-6">
            <div class="flex items-start">
              <svg class="w-5 h-5 text-emerald-600 mr-2 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <div>
                <span class="text-emerald-800 font-medium">Información</span>
                <p class="text-emerald-700 text-sm mt-1">Esta acción marcará el servicio como finalizado y permitirá registrar el pago si es necesario.</p>
              </div>
            </div>
          </div>

          <div class="bg-slate-50 rounded-xl p-4 space-y-2">
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Cliente:</span>
              <span class="text-sm text-gray-900">{{ currentReservation.cliente_nombre }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Fecha:</span>
              <span class="text-sm text-gray-900">{{ formatDate(currentReservation.fecha_reserva) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Hora:</span>
              <span class="text-sm text-gray-900">{{ formatTime(currentReservation.hora_inicio) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Servicio:</span>
              <span class="text-sm text-gray-900">{{ currentReservation.servicio_nombre }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Barbero:</span>
              <span class="text-sm text-gray-900">{{ currentReservation.barbero_nombre }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Precio:</span>
              <span class="text-sm text-gray-900 font-semibold">Bs {{ currentReservation.servicio_precio }}</span>
            </div>
          </div>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeCompleteModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            Cancelar
          </button>
          <button @click="proceedComplete" :disabled="completingReservation" class="px-6 py-3 bg-emerald-500 text-white border-0 rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-emerald-600">
            {{ completingReservation ? 'Completando...' : 'Completar' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Modal para Cancelar Reserva -->
    <div v-if="showCancelModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">Cancelar Reserva</h2>
          <button @click="closeCancelModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="p-8" v-if="currentReservation">
          <div class="text-center mb-6">
            <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">¿Cancelar esta reserva?</h3>
            <p class="text-gray-600">Esta acción no se puede deshacer</p>
          </div>

          <div class="bg-red-50 border border-red-200 rounded-xl p-4 mb-6">
            <div class="flex items-start">
              <svg class="w-5 h-5 text-red-600 mr-2 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.864-.833-2.634 0L4.732 8.5C3.962 14.833 4.924 16.5 6.464 16.5z" />
              </svg>
              <div>
                <span class="text-red-800 font-medium">Atención</span>
                <p class="text-red-700 text-sm mt-1">El cliente será notificado de la cancelación y el horario quedará disponible para nuevas reservas.</p>
              </div>
            </div>
          </div>

          <div class="bg-slate-50 rounded-xl p-4 space-y-2">
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Cliente:</span>
              <span class="text-sm text-gray-900">{{ currentReservation.cliente_nombre }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Fecha:</span>
              <span class="text-sm text-gray-900">{{ formatDate(currentReservation.fecha_reserva) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Hora:</span>
              <span class="text-sm text-gray-900">{{ formatTime(currentReservation.hora_inicio) }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm font-medium text-gray-600">Servicio:</span>
              <span class="text-sm text-gray-900">{{ currentReservation.servicio_nombre }}</span>
            </div>
          </div>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeCancelModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            No cancelar
          </button>
          <button @click="proceedCancel" :disabled="cancelingReservation" class="px-6 py-3 bg-red-500 text-white border-0 rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-red-600">
            {{ cancelingReservation ? 'Cancelando...' : 'Sí, cancelar' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import reservationService from '@/services/reservationService'
import { barberService } from '@/services/barberService'

export default {
  name: 'AdminReservas',
  setup() {
    // Estados reactivos
    const loadingReservations = ref(true)
    const reservations = ref([])
    const selectedReservations = ref([])
    const stats = ref({
      total: 0,
      today: 0,
      pending: 0,
      confirmed: 0,
      completed: 0
    })
    const modoDemo = ref(false)
    
    // Filtros
    const searchTerm = ref('')
    const statusFilter = ref('')
    const barberFilter = ref('')
    const dateRangeFilter = ref('')
    const sortBy = ref('fecha_desc')
    const availableBarbers = ref([])
    
    // Modales
    const showViewModal = ref(false)
    const showEditModal = ref(false)
    const showConfirmModal = ref(false)
    const showCompleteModal = ref(false)
    const showCancelModal = ref(false)
    const currentReservation = ref(null)
    const confirmingReservation = ref(false)
    const completingReservation = ref(false)
    const cancelingReservation = ref(false)
    
    // Configuración de tabla
    const tableColumns = [
      {
        key: 'cliente_nombre',
        label: 'Cliente',
        sortable: true
      },
      {
        key: 'barbero_nombre',
        label: 'Barbero',
        sortable: true
      },
      {
        key: 'estado',
        label: 'Estado',
        sortable: true
      },
      {
        key: 'fecha_reserva',
        label: 'Fecha y Hora',
        sortable: true
      }
    ]
    
    const filteredReservations = computed(() => {
      if (!Array.isArray(reservations.value)) {
        return []
      }

      let filtered = [...reservations.value]
      
      // Filtro por término de búsqueda
      if (searchTerm.value) {
        const term = searchTerm.value.toLowerCase()
        filtered = filtered.filter(reservation => 
          (reservation.cliente_nombre && reservation.cliente_nombre.toLowerCase().includes(term)) ||
          (reservation.cliente_email && reservation.cliente_email.toLowerCase().includes(term)) ||
          (reservation.barbero_nombre && reservation.barbero_nombre.toLowerCase().includes(term)) ||
          (reservation.servicio_nombre && reservation.servicio_nombre.toLowerCase().includes(term))
        )
      }
      
      // Filtro por estado
      if (statusFilter.value) {
        filtered = filtered.filter(reservation => reservation.estado === statusFilter.value)
      }
      
      // Filtro por barbero
      if (barberFilter.value) {
        filtered = filtered.filter(reservation => reservation.barber_id === parseInt(barberFilter.value))
      }
      
      // Filtro por rango de fecha
      if (dateRangeFilter.value) {
        const now = new Date()
        const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
        const tomorrow = new Date(today)
        tomorrow.setDate(tomorrow.getDate() + 1)
        
        filtered = filtered.filter(reservation => {
          // Usar fecha_reserva que viene en formato YYYY-MM-DD
          const fechaReserva = reservation.fecha_reserva
          if (!fechaReserva) return false
          
          const [year, month, day] = fechaReserva.split('-').map(Number)
          const reservationDay = new Date(year, month - 1, day)
          
          switch(dateRangeFilter.value) {
            case 'today':
              return reservationDay.getTime() === today.getTime()
            case 'tomorrow':
              return reservationDay.getTime() === tomorrow.getTime()
            case 'this_week': {
              const endOfWeek = new Date(today)
              endOfWeek.setDate(endOfWeek.getDate() + (7 - endOfWeek.getDay()))
              return reservationDay >= today && reservationDay <= endOfWeek
            }
            case 'next_week': {
              const startOfNextWeek = new Date(today)
              startOfNextWeek.setDate(startOfNextWeek.getDate() + (7 - startOfNextWeek.getDay()) + 1)
              const endOfNextWeek = new Date(startOfNextWeek)
              endOfNextWeek.setDate(endOfNextWeek.getDate() + 6)
              return reservationDay >= startOfNextWeek && reservationDay <= endOfNextWeek
            }
            case 'this_month': {
              return reservationDay.getMonth() === now.getMonth() && 
                     reservationDay.getFullYear() === now.getFullYear()
            }
            case 'past':
              return reservationDay < today
            default:
              return true
          }
        })
      }
      
      // Ordenamiento
      if (sortBy.value) {
        filtered.sort((a, b) => {
          switch(sortBy.value) {
            case 'fecha_desc':
              return new Date(b.fecha_hora) - new Date(a.fecha_hora)
            case 'fecha_asc':
              return new Date(a.fecha_hora) - new Date(b.fecha_hora)
            case 'cliente_asc':
              return (a.cliente_nombre || '').localeCompare(b.cliente_nombre || '')
            case 'cliente_desc':
              return (b.cliente_nombre || '').localeCompare(a.cliente_nombre || '')
            case 'estado':
              const estadoOrder = { 'pendiente': 1, 'confirmada': 2, 'completada': 3, 'cancelada': 4 }
              return (estadoOrder[a.estado] || 5) - (estadoOrder[b.estado] || 5)
            default:
              return 0
          }
        })
      }
      
      return filtered
    })

    const paginatedReservations = computed(() => {
      return filteredReservations.value
    })
    
    // Computed para filtros activos
    const hasActiveFilters = computed(() => {
      return !!(searchTerm.value || statusFilter.value || barberFilter.value || dateRangeFilter.value)
    })
    
    // Helper para etiquetas de rango de fecha
    const getDateRangeLabel = (rangeValue) => {
      const labels = {
        'today': 'Hoy',
        'tomorrow': 'Mañana',
        'this_week': 'Esta semana',
        'next_week': 'Próxima semana',
        'this_month': 'Este mes',
        'past': 'Pasadas'
      }
      return labels[rangeValue || dateRangeFilter.value] || ''
    }
    
    // Métodos
    const loadReservations = async () => {
      try {
        loadingReservations.value = true
        console.log('🔄 Cargando reservas desde el servicio...')
        
        const response = await reservationService.getAll()
        console.log('📡 Respuesta completa del servicio:', response)
        
        // El servicio devuelve { data: [...], total: number, isDemo: boolean }
        if (response) {
          const reservasData = response.data || response.reservations || response
          console.log('📋 Datos de reservas procesados:', reservasData)
          
          if (Array.isArray(reservasData)) {
            reservations.value = reservasData
            modoDemo.value = response.isDemo || false
            calculateStats()
            console.log('✅ Reservas cargadas exitosamente:', reservations.value.length)
          } else {
            console.log('⚠️ Los datos no son un array, cargando datos de fallback')
            loadFallbackData()
          }
        } else {
          console.log('⚠️ Respuesta vacía, cargando datos de fallback')
          loadFallbackData()
        }
      } catch (error) {
        console.error('❌ Error cargando reservas:', error)
        console.log('🔄 Cargando datos de fallback debido al error')
        loadFallbackData()
      } finally {
        loadingReservations.value = false
      }
    }

    const loadBarbers = async () => {
      try {
        console.log('🔄 Cargando barberos desde el servicio...')
        const barbers = await barberService.getAll()
        console.log('👨‍💼 Barberos cargados:', barbers)
        availableBarbers.value = barbers
      } catch (error) {
        console.error('❌ Error cargando barberos:', error)
        availableBarbers.value = []
      }
    }

    const calculateStats = () => {
      if (!Array.isArray(reservations.value)) {
        console.log('⚠️ Reservations no es un array, inicializando stats vacías')
        stats.value = { total: 0, today: 0, pending: 0, confirmed: 0, completed: 0 }
        return
      }
      
      const today = new Date()
      const todayStr = today.toISOString().split('T')[0]
      
      console.log('📊 Calculando estadísticas para', reservations.value.length, 'reservas')
      console.log('📅 Fecha de hoy:', todayStr)
      
      const total = reservations.value.length
      const today_count = reservations.value.filter(r => r.fecha_reserva === todayStr).length
      const pending = reservations.value.filter(r => r.estado === 'pendiente').length
      const confirmed = reservations.value.filter(r => r.estado === 'confirmada').length
      const completed = reservations.value.filter(r => r.estado === 'completada').length
      
      stats.value = {
        total,
        today: today_count,
        pending,
        confirmed,
        completed
      }
      
      console.log('📈 Estadísticas calculadas:', stats.value)
    }

    const loadFallbackData = () => {
      console.log('📊 Cargando datos de reservas de fallback...')
      
      const today = new Date()
      const tomorrow = new Date(today.getTime() + 24 * 60 * 60 * 1000)
      const yesterday = new Date(today.getTime() - 24 * 60 * 60 * 1000)
      
      reservations.value = [
        {
          id: '1',
          cliente_nombre: 'Juan Pérez González',
          cliente_email: 'juan.perez@email.com',
          cliente_telefono: '+57 300 123 4567',
          user_id: 'user-1',
          barber_id: 'barber-1',
          barbero_nombre: 'Carlos Martínez',
          barbero_especialidad: 'Cortes clásicos y modernos',
          service_id: 'service-1',
          servicio_nombre: 'Corte Clásico',
          servicio_precio: 25000,
          servicio_duracion: 30,
          fecha_reserva: today.toISOString().split('T')[0],
          hora_inicio: '10:00:00',
          hora_fin: '10:30:00',
          estado: 'confirmada',
          notas: 'Cliente regular, prefiere corte corto',
          precio_final: 25000,
          created_at: today.toISOString(),
          updated_at: today.toISOString()
        },
        {
          id: '2',
          cliente_nombre: 'María García Silva',
          cliente_email: 'maria.garcia@email.com',
          cliente_telefono: '+57 310 987 6543',
          user_id: 'user-2',
          barber_id: 'barber-2',
          barbero_nombre: 'Miguel Rodríguez',
          barbero_especialidad: 'Especialista en barba y bigote',
          service_id: 'service-2',
          servicio_nombre: 'Barba + Bigote Premium',
          servicio_precio: 20000,
          servicio_duracion: 45,
          fecha_reserva: tomorrow.toISOString().split('T')[0],
          hora_inicio: '14:30:00',
          hora_fin: '15:15:00',
          estado: 'pendiente',
          notas: 'Primera vez en el local',
          precio_final: null,
          created_at: tomorrow.toISOString(),
          updated_at: tomorrow.toISOString()
        },
        {
          id: '3',
          cliente_nombre: 'Pedro López Martín',
          cliente_email: 'pedro.lopez@email.com',
          cliente_telefono: '+57 320 555 7890',
          user_id: 'user-3',
          barber_id: 'barber-1',
          barbero_nombre: 'Carlos Martínez',
          barbero_especialidad: 'Cortes clásicos y modernos',
          service_id: 'service-3',
          servicio_nombre: 'Corte + Barba Premium',
          servicio_precio: 35000,
          servicio_duracion: 60,
          fecha_reserva: yesterday.toISOString().split('T')[0],
          hora_inicio: '16:00:00',
          hora_fin: '17:00:00',
          estado: 'completada',
          notas: 'Excelente servicio, muy satisfecho',
          precio_final: 35000,
          created_at: yesterday.toISOString(),
          updated_at: yesterday.toISOString()
        },
        {
          id: '4',
          cliente_nombre: 'Ana Morales Torres',
          cliente_email: 'ana.morales@email.com',
          cliente_telefono: '+57 315 444 3333',
          user_id: 'user-4',
          barber_id: 'barber-3',
          barbero_nombre: 'Roberto Jiménez',
          barbero_especialidad: 'Cortes modernos y tendencias',
          service_id: 'service-4',
          servicio_nombre: 'Corte Moderno + Styling',
          servicio_precio: 30000,
          servicio_duracion: 45,
          fecha_reserva: today.toISOString().split('T')[0],
          hora_inicio: '11:00:00',
          hora_fin: '11:45:00',
          estado: 'en_proceso',
          notas: 'Corte con degradado, estilo moderno',
          precio_final: 30000,
          created_at: today.toISOString(),
          updated_at: today.toISOString()
        },
        {
          id: '5',
          cliente_nombre: 'Roberto Silva Castro',
          cliente_email: 'roberto.silva@email.com',
          cliente_telefono: '+57 301 222 1111',
          user_id: 'user-5',
          barber_id: 'barber-2',
          barbero_nombre: 'Miguel Rodríguez',
          barbero_especialidad: 'Especialista en barba y bigote',
          service_id: 'service-1',
          servicio_nombre: 'Corte Clásico',
          servicio_precio: 25000,
          servicio_duracion: 30,
          fecha_reserva: tomorrow.toISOString().split('T')[0],
          hora_inicio: '09:30:00',
          hora_fin: '10:00:00',
          estado: 'cancelada',
          notas: 'Cliente canceló por motivos personales',
          precio_final: null,
          created_at: tomorrow.toISOString(),
          updated_at: tomorrow.toISOString()
        }
      ]
      
      modoDemo.value = true
      calculateStats()
      console.log('✅ Datos de fallback cargados:', reservations.value.length, 'reservas')
    }

    const clearFilters = () => {
      searchTerm.value = ''
      statusFilter.value = ''
      barberFilter.value = ''
      dateRangeFilter.value = ''
      sortBy.value = 'fecha_desc'
    }

    const openCreateModal = () => {
      console.log('� Función de crear reserva en desarrollo')
      // TODO: Implementar modal de creación de reservas
    }

    const viewReservation = (reservation) => {
      currentReservation.value = reservation
      showViewModal.value = true
    }

    const closeViewModal = () => {
      showViewModal.value = false
      currentReservation.value = null
    }

    const editReservation = (reservation) => {
      currentReservation.value = reservation
      showEditModal.value = true
    }

    const closeEditModal = () => {
      showEditModal.value = false
      currentReservation.value = null
    }

    const confirmReservation = async (reservation) => {
      if (reservation.estado !== 'pendiente') {
        console.warn('⚠️ Solo se pueden confirmar reservas pendientes')
        return
      }
      currentReservation.value = reservation
      showConfirmModal.value = true
    }

    const closeConfirmModal = () => {
      showConfirmModal.value = false
      confirmingReservation.value = false
      // Delay the reset to avoid race conditions
      setTimeout(() => {
        currentReservation.value = null
      }, 100)
    }

    const proceedConfirm = async () => {
      if (!currentReservation.value) {
        console.error('❌ No hay reserva seleccionada para confirmar')
        return
      }

      try {
        confirmingReservation.value = true
        
        // Guardar referencia a la reserva antes de que se pueda perder
        const reservationToConfirm = currentReservation.value
        console.log('🔄 Confirmando reserva:', reservationToConfirm.id)
        
        // Llamada al backend para confirmar la reserva
        try {
          await reservationService.confirm(reservationToConfirm.id)
          console.log('✅ Reserva confirmada exitosamente')
          
          // Recargar reservas desde el backend para obtener datos actualizados
          await loadReservations()
          
          closeConfirmModal()
          
        } catch (backendError) {
          console.error('❌ Error en el backend, aplicando cambio local:', backendError)
          
          // Fallback: Actualizar localmente si falla el backend
          const reservaIndex = reservations.value.findIndex(r => r.id === reservationToConfirm.id)
          if (reservaIndex !== -1) {
            reservations.value[reservaIndex].estado = 'confirmada'
            calculateStats()
          }
          
          closeConfirmModal()
          
          // Solo mostrar error si realmente falló
          console.warn('⚠️ La reserva se actualizó localmente pero hubo un error con el servidor')
        }
        
      } catch (error) {
        console.error('Error confirmando reserva:', error)
        closeConfirmModal()
      } finally {
        confirmingReservation.value = false
      }
    }

    const completeReservation = async (reservation) => {
      if (reservation.estado !== 'confirmada') {
        console.warn('⚠️ Solo se pueden completar reservas confirmadas')
        return
      }
      currentReservation.value = reservation
      showCompleteModal.value = true
    }

    const closeCompleteModal = () => {
      showCompleteModal.value = false
      completingReservation.value = false
      // Delay the reset to avoid race conditions
      setTimeout(() => {
        currentReservation.value = null
      }, 100)
    }

    const proceedComplete = async () => {
      if (!currentReservation.value) {
        console.error('❌ No hay reserva seleccionada para completar')
        return
      }

      try {
        completingReservation.value = true
        
        // Guardar referencia a la reserva antes de que se pueda perder
        const reservationToComplete = currentReservation.value
        console.log('🔄 Completando reserva:', reservationToComplete.id)
        
        // Llamada al backend para completar la reserva
        try {
          await reservationService.complete(reservationToComplete.id)
          console.log('✅ Reserva completada exitosamente')
          
          // Recargar reservas desde el backend para obtener datos actualizados
          await loadReservations()
          
          closeCompleteModal()
          
        } catch (backendError) {
          console.error('❌ Error en el backend, aplicando cambio local:', backendError)
          
          // Fallback: Actualizar localmente si falla el backend
          const reservaIndex = reservations.value.findIndex(r => r.id === reservationToComplete.id)
          if (reservaIndex !== -1) {
            reservations.value[reservaIndex].estado = 'completada'
            calculateStats()
          }
          
          closeCompleteModal()
          
          // Solo mostrar error si realmente falló
          console.warn('⚠️ La reserva se actualizó localmente pero hubo un error con el servidor')
        }
        
      } catch (error) {
        console.error('Error completando reserva:', error)
        closeCompleteModal()
      } finally {
        completingReservation.value = false
      }
    }

    const cancelReservation = async (reservation) => {
      if (reservation.estado === 'cancelada') {
        console.warn('⚠️ Esta reserva ya está cancelada')
        return
      }

      if (reservation.estado === 'completada') {
        console.warn('⚠️ No se puede cancelar una reserva completada')
        return
      }

      currentReservation.value = reservation
      showCancelModal.value = true
    }

    const closeCancelModal = () => {
      showCancelModal.value = false
      cancelingReservation.value = false
      // Delay the reset to avoid race conditions
      setTimeout(() => {
        currentReservation.value = null
      }, 100)
    }

    const proceedCancel = async () => {
      if (!currentReservation.value) {
        console.error('❌ No hay reserva seleccionada para cancelar')
        return
      }

      try {
        cancelingReservation.value = true
        
        // Guardar referencia a la reserva antes de que se pueda perder
        const reservationToCancel = currentReservation.value
        console.log('🔄 Cancelando reserva:', reservationToCancel.id)
        
        // Llamada al backend para cancelar la reserva
        try {
          await reservationService.cancel(reservationToCancel.id)
          console.log('✅ Reserva cancelada exitosamente')
          
          // Recargar reservas desde el backend para obtener datos actualizados
          await loadReservations()
          
          closeCancelModal()
          
        } catch (backendError) {
          console.error('❌ Error en el backend, aplicando cambio local:', backendError)
          
          // Fallback: Actualizar localmente si falla el backend
          const reservaIndex = reservations.value.findIndex(r => r.id === reservationToCancel.id)
          if (reservaIndex !== -1) {
            reservations.value[reservaIndex].estado = 'cancelada'
            calculateStats()
          }
          
          closeCancelModal()
          
          // Solo mostrar error si realmente falló
          console.warn('⚠️ La reserva se actualizó localmente pero hubo un error con el servidor')
        }
        
      } catch (error) {
        console.error('Error cancelando reserva:', error)
        closeCancelModal()
      } finally {
        cancelingReservation.value = false
      }
    }
    
    // Helpers
    const getInitials = (name) => {
      if (!name) return '??'
      return name.split(' ')
        .map(word => word.charAt(0))
        .join('')
        .toUpperCase()
        .slice(0, 2)
    }

    const getStatusBadgeClass = (status) => {
      switch (status) {
        case 'pendiente': return 'bg-amber-50 text-amber-700 border border-amber-200'
        case 'confirmada': return 'bg-blue-50 text-blue-700 border border-blue-200'
        case 'completada': return 'bg-green-50 text-green-700 border border-green-200'
        case 'cancelada': return 'bg-red-50 text-red-700 border border-red-200'
        default: return 'bg-gray-50 text-gray-700 border border-gray-200'
      }
    }

    const getStatusDotClass = (status) => {
      switch (status) {
        case 'pendiente': return 'bg-amber-400'
        case 'confirmada': return 'bg-blue-400'
        case 'completada': return 'bg-green-400'
        case 'cancelada': return 'bg-red-400'
        default: return 'bg-gray-400'
      }
    }

    const getStatusLabel = (status) => {
      switch (status) {
        case 'pendiente': return 'Pendiente'
        case 'confirmada': return 'Confirmada'
        case 'completada': return 'Completada'
        case 'cancelada': return 'Cancelada'
        default: return 'Pendiente'
      }
    }

    const formatDate = (date) => {
      if (!date) return 'Sin fecha'
      
      // Si la fecha viene como string YYYY-MM-DD, parsearla sin zona horaria
      if (typeof date === 'string' && date.match(/^\d{4}-\d{2}-\d{2}$/)) {
        const [year, month, day] = date.split('-')
        const localDate = new Date(parseInt(year), parseInt(month) - 1, parseInt(day))
        return localDate.toLocaleDateString('es-ES')
      }
      
      // Para otros formatos de fecha
      return new Date(date).toLocaleDateString('es-ES')
    }
    
    const formatTime = (time) => {
      if (!time) return 'Sin hora'
      // Si viene en formato HH:MM:SS, tomar solo HH:MM
      if (time.includes(':')) {
        const parts = time.split(':')
        return `${parts[0]}:${parts[1]}`
      }
      return time
    }
    
    // Lifecycle
    onMounted(() => {
      loadReservations()
      loadBarbers()
    })

    return {
      // Estados
      loadingReservations,
      reservations,
      selectedReservations,
      stats,
      modoDemo,
      searchTerm,
      statusFilter,
      barberFilter,
      dateRangeFilter,
      sortBy,
      availableBarbers,
      
      // Modales
      showViewModal,
      showEditModal,
      showConfirmModal,
      showCompleteModal,
      showCancelModal,
      currentReservation,
      confirmingReservation,
      completingReservation,
      cancelingReservation,
      
      // Computed
      filteredReservations,
      paginatedReservations,
      hasActiveFilters,
      
      // Métodos
      loadReservations,
      loadBarbers,
      clearFilters,
      openCreateModal,
      viewReservation,
      closeViewModal,
      editReservation,
      closeEditModal,
      confirmReservation,
      closeConfirmModal,
      proceedConfirm,
      completeReservation,
      closeCompleteModal,
      proceedComplete,
      cancelReservation,
      closeCancelModal,
      proceedCancel,
      
      // Helpers
      getInitials,
      getStatusBadgeClass,
      getDateRangeLabel,
      getStatusDotClass,
      getStatusLabel,
      formatDate,
      formatTime,
      loadFallbackData
    }
  }
}
</script>

<style scoped>
/* AdminReservas.vue - Tailwind CSS v4 */
/* Todas las utilidades son nativas de Tailwind v4 */
/* No se requiere CSS custom - 100% utility-first */
</style>
