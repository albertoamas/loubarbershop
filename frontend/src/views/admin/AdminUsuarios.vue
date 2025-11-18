<!--
  AdminUsuarios.vue - Gestión completa de usuarios y clientes
  MODERNIZADO: Tailwind CSS v4 - Sistema consistente
-->
<template>
  <div class="p-8 bg-gradient-to-br from-slate-50 to-slate-100 min-h-[calc(100vh-80px)]">
    <!-- Header del Dashboard -->
    <div class="mb-6 bg-white rounded-2xl p-6 shadow-sm border border-gray-200">
      <div class="flex flex-col lg:flex-row lg:justify-between lg:items-start gap-6">
        <div class="flex-1">
          <h1 class="text-3xl font-extrabold bg-gradient-to-r from-black to-gray-500 bg-clip-text text-transparent mb-2 flex items-center gap-4">
            Gestión de Usuarios
            <span v-if="modoDemo" class="inline-flex items-center px-2 py-1 bg-amber-50 text-amber-700 border border-amber-200 rounded text-xs font-semibold uppercase tracking-wide">MODO DEMO</span>
          </h1>
          <p class="text-lg text-gray-600 font-medium">
            Administra usuarios, roles y permisos del sistema de Low Barber Shop
            <span v-if="modoDemo" class="text-amber-600">• Usando datos de ejemplo - Backend no disponible</span>
          </p>
        </div>
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
          <button 
            @click="loadUsers" 
            :disabled="loadingUsers"
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-black to-gray-500 text-white border-0 rounded-xl font-semibold text-sm transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5 disabled:opacity-70 disabled:cursor-not-allowed"
          >
            <svg :class="{ 'animate-spin': loadingUsers }" class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            {{ loadingUsers ? 'Actualizando...' : 'Actualizar' }}
          </button>
          <button 
            class="flex items-center justify-center px-6 py-3 bg-gradient-to-r from-violet-500 to-purple-600 text-white border-0 rounded-xl font-semibold text-sm transition-all duration-200 shadow-lg hover:shadow-xl hover:-translate-y-0.5"
            @click="openCreateModal"
          >
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
            </svg>
            Nuevo Usuario
          </button>
        </div>
      </div>
    </div>

    <!-- Grid de estadísticas modernizado -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
      <!-- Total de usuarios -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Total</h3>
            <p class="text-3xl font-black text-blue-600">{{ stats.totalUsers || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-blue-100 to-blue-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Clientes -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Clientes</h3>
            <p class="text-3xl font-black text-green-600">{{ stats.totalClients || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-green-100 to-green-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Barberos -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Barberos</h3>
            <p class="text-3xl font-black text-purple-600">{{ stats.totalBarbers || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-purple-100 to-purple-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1.5a2.5 2.5 0 01.5.5V11M12 12.5v-.5m0 0a2.5 2.5 0 00-2.5-2.5M9.5 9h5.5" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Activos hoy -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 hover:shadow-md transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Activos</h3>
            <p class="text-3xl font-black text-orange-600">{{ stats.activeToday || 0 }}</p>
          </div>
          <div class="w-14 h-14 bg-gradient-to-br from-orange-100 to-orange-200 rounded-2xl flex items-center justify-center">
            <svg class="w-7 h-7 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
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
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <input
              v-model="searchTerm"
              type="text"
              placeholder="Buscar por nombre, email o teléfono..."
              class="w-full pl-12 pr-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
            />
            <button 
              v-if="searchTerm"
              @click="searchTerm = ''"
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
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
            Limpiar
          </button>
        </div>

        <!-- Fila 2: Filtros -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <!-- Filtro por Rol -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Rol</label>
            <select 
              v-model="filters.role"
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
              @change="applyFilters"
            >
              <option value="">Todos los roles</option>
              <option value="client">Clientes</option>
              <option value="barber">Barberos</option>
              <option value="admin">Administradores</option>
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

          <!-- Ordenar por -->
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wider">Ordenar por</label>
            <select 
              v-model="sortBy"
              class="w-full px-4 py-3.5 border border-gray-300 rounded-xl bg-white text-sm font-medium focus:outline-none focus:border-violet-500 transition-all duration-200"
            >
              <option value="nombre_asc">Nombre (A-Z)</option>
              <option value="nombre_desc">Nombre (Z-A)</option>
              <option value="email_asc">Email (A-Z)</option>
              <option value="email_desc">Email (Z-A)</option>
              <option value="fecha_desc">Más recientes</option>
              <option value="fecha_asc">Más antiguos</option>
            </select>
          </div>
        </div>

        <!-- Indicadores de filtros activos -->
        <div v-if="hasActiveFilters" class="flex flex-wrap gap-2 items-center pt-2 border-t border-gray-200">
          <span class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Filtros activos:</span>
          
          <span v-if="searchTerm" class="inline-flex items-center gap-1 px-3 py-1 bg-violet-100 text-violet-700 rounded-full text-xs font-medium">
            Búsqueda: {{ searchTerm }}
            <button @click="searchTerm = ''" class="ml-1 hover:text-violet-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>
          
          <span v-if="filters.role" class="inline-flex items-center gap-1 px-3 py-1 bg-violet-100 text-violet-700 rounded-full text-xs font-medium">
            Rol: {{ getRoleFilterLabel(filters.role) }}
            <button @click="filters.role = ''; applyFilters()" class="ml-1 hover:text-violet-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>
          
          <span v-if="filters.status" class="inline-flex items-center gap-1 px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-medium">
            Estado: {{ getStatusFilterLabel(filters.status) }}
            <button @click="filters.status = ''; applyFilters()" class="ml-1 hover:text-blue-900">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </span>
          
          <span class="text-xs text-gray-500 ml-auto">
            {{ filteredUsers.length }} resultado(s)
          </span>
        </div>
      </div>
    </div>

    <!-- Lista de Usuarios -->
    <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
      <div v-if="loadingUsers" class="flex flex-col items-center justify-center py-16 px-8 text-slate-500">
        <svg class="w-8 h-8 animate-spin mb-4" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
        <p class="text-base font-medium">Cargando usuarios...</p>
      </div>
      
      <div v-else-if="filteredUsers.length === 0" class="flex flex-col items-center justify-center py-16 px-8 text-center">
        <svg class="w-16 h-16 text-slate-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
        </svg>
        <h3 class="text-xl font-bold text-slate-900 mb-2">No se encontraron usuarios</h3>
        <p class="text-slate-600 mb-8 max-w-md">No hay usuarios que coincidan con los filtros aplicados.</p>
        <button @click="openCreateModal" class="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-violet-600 to-purple-600 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
          Crear primer usuario
        </button>
      </div>
      
      <div v-else class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6 p-6">
        <div
          v-for="user in paginatedUsers"
          :key="user.id"
          class="bg-slate-50 border border-slate-200 rounded-2xl p-6 transition-all duration-200 hover:shadow-lg hover:-translate-y-0.5"
        >
          <!-- Header del Usuario -->
          <div class="flex items-start gap-4 mb-4">
            <div class="w-12 h-12 flex-shrink-0">
              <img
                v-if="user.avatar"
                :src="user.avatar"
                :alt="user.name"
                class="w-full h-full rounded-xl object-cover"
              />
              <div v-else class="w-full h-full rounded-xl bg-gradient-to-br from-violet-500 to-violet-600 text-white flex items-center justify-center font-semibold text-sm">
                {{ getInitials(user.name) }}
              </div>
            </div>
            
            <div class="flex-1 min-w-0">
              <h3 class="font-semibold text-gray-900 text-base mb-1 truncate">{{ user.name }}</h3>
              <p class="text-gray-500 text-sm mb-2 truncate">{{ user.email }}</p>
              <span :class="getRoleBadgeClass(user.role)" class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold border">
                {{ getRoleLabel(user.role) }}
              </span>
            </div>
          </div>
          
          <!-- Detalles del Usuario -->
          <div class="space-y-3 mb-4">
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Estado:</span>
              <span :class="['inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold', getStatusClass(user.status)]">
                <div class="w-2 h-2 rounded-full" :class="user.status === 'active' ? 'bg-emerald-500' : 'bg-red-500'"></div>
                {{ getStatusLabel(user.status) }}
              </span>
            </div>
            
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Teléfono:</span>
              <span class="text-sm text-gray-900 font-medium">
                {{ user.phone || 'No registrado' }}
              </span>
            </div>
            
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Email verificado:</span>
              <div class="flex items-center gap-2">
                <svg v-if="user.emailVerified" class="w-4 h-4 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <svg v-else class="w-4 h-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span class="text-sm text-gray-900 font-medium">{{ user.emailVerified ? 'Sí' : 'No' }}</span>
              </div>
            </div>
            
            <div class="flex justify-between items-center">
              <span class="text-sm font-medium text-gray-600">Registrado:</span>
              <span class="text-sm text-gray-900 font-medium">{{ formatDate(user.createdAt) }}</span>
            </div>
          </div>
          
          <!-- Acciones del Usuario -->
          <div class="flex gap-2 justify-end flex-wrap">
            <button @click="viewUserDetails(user)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200 bg-blue-50 text-blue-700 border-blue-200 hover:bg-blue-100 hover:border-blue-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
              </svg>
              Ver
            </button>
            
            <button @click="editUser(user)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200 bg-amber-50 text-amber-700 border-amber-200 hover:bg-amber-100 hover:border-amber-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
              Editar
            </button>
            
            <button v-if="user.status === 'active'" @click="toggleUserStatus(user)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200 bg-red-50 text-red-700 border-red-200 hover:bg-red-100 hover:border-red-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
              </svg>
              Desactivar
            </button>
            
            <button v-if="user.status === 'inactive'" @click="toggleUserStatus(user)" class="flex items-center gap-1.5 px-3 py-2 text-xs font-medium border rounded-lg transition-all duration-200 bg-green-50 text-green-700 border-green-200 hover:bg-green-100 hover:border-green-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Activar
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Paginación -->
    <div class="bg-white rounded-xl p-6 mt-6 shadow-sm border border-slate-200 flex justify-between items-center max-lg:flex-col max-lg:gap-4">
      <div class="text-sm text-slate-600 font-medium">
        Mostrando {{ startItem }} a {{ endItem }} de {{ totalUsers }} usuarios
      </div>
      <div class="flex items-center gap-3">
        <button 
          @click="previousPage"
          :disabled="currentPage === 1"
          class="flex items-center justify-center w-10 h-10 rounded-lg border border-slate-300 bg-white text-slate-600 hover:bg-slate-50 hover:border-slate-400 hover:-translate-y-0.5 hover:shadow-md disabled:opacity-50 disabled:cursor-not-allowed transition-all"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
        </button>
        
        <span class="px-4 text-sm text-slate-900 font-semibold whitespace-nowrap">
          Página {{ currentPage }} de {{ totalPages }}
        </span>
        
        <button 
          @click="nextPage"
          :disabled="currentPage >= totalPages"
          class="flex items-center justify-center w-10 h-10 rounded-lg border border-slate-300 bg-white text-slate-600 hover:bg-slate-50 hover:border-slate-400 hover:-translate-y-0.5 hover:shadow-md disabled:opacity-50 disabled:cursor-not-allowed transition-all"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Acciones Masivas -->
    <div v-if="selectedUsers.length > 0" class="bg-white rounded-xl p-6 mt-6 shadow-sm border border-slate-200 flex justify-between items-center max-lg:flex-col max-lg:gap-4">
      <div class="text-sm text-slate-600 font-medium">
        {{ selectedUsers.length }} usuario(s) seleccionado(s)
      </div>
      <div class="flex gap-3 max-lg:w-full">
        <button @click="bulkActivate" class="flex items-center gap-2 px-4 py-2 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-lg text-sm font-medium hover:bg-emerald-100 hover:border-emerald-300 transition-all">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          Activar Seleccionados
        </button>
        <button @click="bulkDeactivate" class="flex items-center gap-2 px-4 py-2 bg-amber-50 text-amber-700 border border-amber-200 rounded-lg text-sm font-medium hover:bg-amber-100 hover:border-amber-300 transition-all">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728L5.636 5.636" />
          </svg>
          Desactivar Seleccionados
        </button>
        <button @click="bulkChangeRole" class="flex items-center gap-2 px-4 py-2 bg-violet-50 text-violet-700 border border-violet-200 rounded-lg text-sm font-medium hover:bg-violet-100 hover:border-violet-300 transition-all">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0z" />
          </svg>
          Cambiar Rol
        </button>
      </div>
    </div>

    <!-- Modal para Ver Usuario (Solo Lectura) -->
    <div v-if="showViewModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">Detalles del Usuario</h2>
          <button @click="closeViewModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="p-8" v-if="currentUser">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Información Personal -->
            <div class="bg-slate-50 rounded-xl p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <svg class="w-5 h-5 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
                Información Personal
              </h3>
              <div class="space-y-3">
                <div>
                  <span class="text-sm font-medium text-gray-600">Nombre:</span>
                  <p class="text-sm text-gray-900 font-medium">{{ currentUser.name }}</p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Email:</span>
                  <p class="text-sm text-gray-900">{{ currentUser.email }}</p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Teléfono:</span>
                  <p class="text-sm text-gray-900">{{ currentUser.phone || 'No registrado' }}</p>
                </div>
              </div>
            </div>

            <!-- Información de Cuenta -->
            <div class="bg-slate-50 rounded-xl p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <svg class="w-5 h-5 mr-2 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
                Información de Cuenta
              </h3>
              <div class="space-y-3">
                <div>
                  <span class="text-sm font-medium text-gray-600">Rol:</span>
                  <p class="mt-1">
                    <span :class="getRoleBadgeClass(currentUser.role)" class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold border">
                      {{ getRoleLabel(currentUser.role) }}
                    </span>
                  </p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Estado:</span>
                  <p class="mt-1">
                    <span :class="['inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold', getStatusClass(currentUser.status)]">
                      <div class="w-2 h-2 rounded-full" :class="currentUser.status === 'active' ? 'bg-emerald-500' : 'bg-red-500'"></div>
                      {{ getStatusLabel(currentUser.status) }}
                    </span>
                  </p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Email Verificado:</span>
                  <div class="flex items-center gap-2 mt-1">
                    <svg v-if="currentUser.emailVerified" class="w-5 h-5 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <svg v-else class="w-5 h-5 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <span class="text-sm text-gray-900 font-medium">{{ currentUser.emailVerified ? 'Verificado' : 'No verificado' }}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Fechas -->
            <div class="bg-slate-50 rounded-xl p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <svg class="w-5 h-5 mr-2 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                Registro
              </h3>
              <div class="space-y-3">
                <div>
                  <span class="text-sm font-medium text-gray-600">Fecha de Registro:</span>
                  <p class="text-sm text-gray-900 font-medium">{{ formatDate(currentUser.createdAt) }}</p>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-600">Última Actualización:</span>
                  <p class="text-sm text-gray-900 font-medium">{{ formatDate(currentUser.updatedAt) }}</p>
                </div>
              </div>
            </div>

            <!-- ID del Sistema -->
            <div class="bg-slate-50 rounded-xl p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <svg class="w-5 h-5 mr-2 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                </svg>
                Sistema
              </h3>
              <div class="space-y-3">
                <div>
                  <span class="text-sm font-medium text-gray-600">ID de Usuario:</span>
                  <p class="text-xs text-gray-500 font-mono break-all">{{ currentUser.id }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeViewModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            Cerrar
          </button>
          <button @click="editFromView" class="px-6 py-3 bg-violet-600 text-white border-0 rounded-xl font-medium transition-all duration-200 hover:bg-violet-700">
            Editar Usuario
          </button>
        </div>
      </div>
    </div>

    <!-- Modal de Creación/Edición de Usuario -->
    <div v-if="showUserModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">{{ editingUser ? 'Editar Usuario' : 'Crear Usuario' }}</h2>
          <button @click="closeUserModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="p-8">
          <form @submit.prevent="saveUser" class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <!-- Nombre (editable) -->
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">Nombre completo *</label>
                <input
                  v-model="userForm.name"
                  type="text"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:border-violet-500 transition-all"
                  placeholder="Nombre y apellido"
                />
              </div>

              <!-- Email (solo lectura si está editando) -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Email *</label>
                <input
                  v-model="userForm.email"
                  type="email"
                  required
                  :readonly="!!editingUser"
                  :class="[
                    'w-full px-4 py-3 border rounded-xl text-sm transition-all',
                    editingUser 
                      ? 'bg-gray-100 text-gray-600 border-gray-300 cursor-not-allowed' 
                      : 'bg-white text-gray-900 placeholder-gray-400 border-gray-300 focus:outline-none focus:border-violet-500'
                  ]"
                  placeholder="correo@ejemplo.com"
                />
                <p v-if="editingUser" class="mt-1 text-xs text-gray-500">El email no puede modificarse</p>
              </div>

              <!-- Teléfono (editable) -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Teléfono</label>
                <input
                  v-model="userForm.phone"
                  type="tel"
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:border-violet-500 transition-all"
                  placeholder="+591 765 43210"
                />
              </div>

              <!-- Rol (editable) -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Rol *</label>
                <select
                  v-model="userForm.role"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-900 focus:outline-none focus:border-violet-500 transition-all"
                >
                  <option value="cliente">Cliente</option>
                  <option value="barbero">Barbero</option>
                  <option value="admin">Administrador</option>
                </select>
              </div>

              <!-- Estado (editable solo en edición) -->
              <div v-if="editingUser">
                <label class="block text-sm font-medium text-gray-700 mb-2">Estado *</label>
                <select
                  v-model="userForm.status"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-900 focus:outline-none focus:border-violet-500 transition-all"
                >
                  <option value="active">Activo</option>
                  <option value="inactive">Inactivo</option>
                </select>
              </div>

              <!-- Contraseña (obligatoria en creación, opcional en edición) -->
              <div :class="editingUser ? 'md:col-span-2' : 'md:col-span-2'">
                <label class="block text-sm font-medium text-gray-700 mb-2">
                  Contraseña {{ editingUser ? '(opcional - dejar vacío para mantener)' : '*' }}
                </label>
                <input
                  v-model="userForm.password"
                  type="password"
                  :required="!editingUser"
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:border-violet-500 transition-all"
                  :placeholder="editingUser ? 'Dejar vacío para no cambiar' : 'Mínimo 8 caracteres'"
                />
                <p v-if="editingUser" class="mt-1 text-xs text-gray-500">Solo completa este campo si deseas cambiar la contraseña</p>
              </div>
            </div>
          </form>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeUserModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            Cancelar
          </button>
          <button @click="saveUser" :disabled="savingUser" class="px-6 py-3 bg-violet-600 text-white border-0 rounded-xl font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-violet-700">
            <span v-if="savingUser" class="flex items-center gap-2">
              <svg class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Guardando...
            </span>
            <span v-else>
              {{ editingUser ? 'Actualizar' : 'Crear' }} Usuario
            </span>
          </button>
        </div>
      </div>
    </div>

    <!-- Modal de Cambio de Rol Masivo -->
    <div v-if="showBulkRoleModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full">
        <div class="flex justify-between items-center px-8 py-6 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">Cambiar Rol Masivo</h2>
          <button @click="closeBulkRoleModal" class="p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 rounded-lg transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="p-8">
          <form @submit.prevent="confirmBulkRoleChange" class="space-y-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Nuevo Rol</label>
              <select
                v-model="bulkRoleForm.newRole"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white text-sm text-gray-900 focus:outline-none focus:border-violet-500 transition-all"
              >
                <option value="cliente">Cliente</option>
                <option value="barbero">Barbero</option>
                <option value="admin">Administrador</option>
              </select>
            </div>
            
            <div class="bg-amber-50 border border-amber-200 rounded-xl p-4">
              <div class="flex items-start gap-3">
                <svg class="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
                <div>
                  <h4 class="text-sm font-semibold text-amber-900 mb-1">Advertencia</h4>
                  <p class="text-sm text-amber-800">
                    Esta acción cambiará el rol de {{ selectedUsers.length }} usuario(s) seleccionado(s). Esta acción no se puede deshacer.
                  </p>
                </div>
              </div>
            </div>
          </form>
        </div>
        
        <div class="flex justify-end gap-3 px-8 py-6 border-t border-gray-200 bg-gray-50 rounded-b-2xl">
          <button @click="closeBulkRoleModal" class="px-6 py-3 bg-white text-gray-600 border border-gray-300 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-400 transition-all duration-200">
            Cancelar
          </button>
          <button @click="confirmBulkRoleChange" class="px-6 py-3 bg-violet-600 text-white border-0 rounded-xl font-medium transition-all duration-200 hover:bg-violet-700">
            Cambiar Rol
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { userService } from '@/services/userService'

export default {
  name: 'AdminUsuarios',
  setup() {
    // Estado reactivo
    const loadingStats = ref(true)
    const loadingUsers = ref(true)
    const savingUser = ref(false)
    const modoDemo = ref(false) // Indicador si estamos en modo demo
    
    const users = ref([])
    const selectedUsers = ref([])
    const stats = ref({
      totalUsers: 0,
      totalClients: 0,
      totalBarbers: 0,
      activeToday: 0
    })
    
    // Filtros
    const searchTerm = ref('')
    const sortBy = ref('nombre_asc')
    const filters = ref({
      role: '',
      status: ''
    })
    
    // Paginación
    const currentPage = ref(1)
    const itemsPerPage = 25
    
    // Modales
    const showUserModal = ref(false)
    const showViewModal = ref(false)
    const showBulkRoleModal = ref(false)
    const editingUser = ref(null)
    const currentUser = ref(null)
    
    // Formularios
    const userForm = ref({
      name: '',
      email: '',
      phone: '',
      role: 'cliente', // Valor por defecto según la BD
      status: 'active',
      password: ''
    })
    
    const bulkRoleForm = ref({
      newRole: 'cliente' // Valor por defecto según la BD
    })
    
    // Configuración de tabla actualizada según la estructura de la BD
    const tableColumns = [
      { key: 'usuario', label: 'Usuario', sortable: false },
      { key: 'rol', label: 'Rol', sortable: false },
      { key: 'estado', label: 'Estado', sortable: false },
      { key: 'contacto', label: 'Contacto', sortable: false },
      { key: 'fechas', label: 'Fechas', sortable: false },
      { key: 'actions', label: 'Acciones', sortable: false }
    ]
    
    const filteredUsers = computed(() => {
      let filtered = [...users.value]
      
      // Filtro por término de búsqueda
      if (searchTerm.value) {
        const term = searchTerm.value.toLowerCase()
        filtered = filtered.filter(user => 
          user.name?.toLowerCase().includes(term) ||
          user.email?.toLowerCase().includes(term) ||
          user.phone?.toLowerCase().includes(term)
        )
      }
      
      if (filters.value.role) {
        // Mapear filtros del frontend a los roles de la BD
        const roleMap = {
          'client': 'cliente',
          'barber': 'barbero',
          'admin': 'admin'
        }
        const backendRole = roleMap[filters.value.role] || filters.value.role
        filtered = filtered.filter(user => user.role === backendRole)
      }
      
      if (filters.value.status) {
        filtered = filtered.filter(user => user.status === filters.value.status)
      }
      
      // Ordenamiento
      if (sortBy.value) {
        filtered.sort((a, b) => {
          switch (sortBy.value) {
            case 'nombre_asc':
              return (a.name || '').localeCompare(b.name || '')
            case 'nombre_desc':
              return (b.name || '').localeCompare(a.name || '')
            case 'email_asc':
              return (a.email || '').localeCompare(b.email || '')
            case 'email_desc':
              return (b.email || '').localeCompare(a.email || '')
            case 'fecha_desc':
              return new Date(b.createdAt || 0) - new Date(a.createdAt || 0)
            case 'fecha_asc':
              return new Date(a.createdAt || 0) - new Date(b.createdAt || 0)
            default:
              return 0
          }
        })
      }
      
      return filtered
    })
    
    const paginatedUsers = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage
      const end = start + itemsPerPage
      const result = filteredUsers.value.slice(start, end)
      
      return result
    })
    
    const totalUsers = computed(() => filteredUsers.value.length)
    const totalPages = computed(() => Math.ceil(totalUsers.value / itemsPerPage))
    const startItem = computed(() => (currentPage.value - 1) * itemsPerPage + 1)
    const endItem = computed(() => Math.min(currentPage.value * itemsPerPage, totalUsers.value))
    
    // Computed para filtros activos
    const hasActiveFilters = computed(() => {
      return !!(searchTerm.value || filters.value.role || filters.value.status)
    })
    
    // Métodos
    const loadUsers = async () => {
      try {
        loadingUsers.value = true
        
        const response = await userService.getAll()
        
        // El servicio devuelve {data: [], total: number, isDemo: boolean}
        if (response && response.data && Array.isArray(response.data)) {
          users.value = response.data
          modoDemo.value = response.isDemo || false
        } else {
          users.value = []
          modoDemo.value = true
        }
      } catch (error) {
        console.error('❌ Error cargando usuarios:', error)
        // Usar datos de fallback que mapean a los campos reales
        const fallbackUsers = userService.getFallbackUsersRealFormat()
        users.value = fallbackUsers
        modoDemo.value = true
      } finally {
        loadingUsers.value = false
      }
    }
    
    const loadStats = async () => {
      try {
        loadingStats.value = true
        
        const response = await userService.getStats()
        
        // Mapear estadísticas al formato esperado por el frontend
        stats.value = {
          totalUsers: response.totalUsers || 0,
          totalClients: response.totalClients || 0,
          totalBarbers: response.totalBarbers || 0,
          activeToday: response.activeToday || 0
        }
        
      } catch (error) {
        console.error('❌ Error cargando estadísticas:', error)
        // Calcular estadísticas desde los usuarios cargados
        stats.value = {
          totalUsers: users.value.length,
          totalClients: users.value.filter(u => u.role === 'cliente').length,
          totalBarbers: users.value.filter(u => u.role === 'barbero').length,
          activeToday: users.value.filter(u => u.status === 'active').length
        }
      } finally {
        loadingStats.value = false
      }
    }
    
    const clearFilters = () => {
      searchTerm.value = ''
      sortBy.value = 'nombre_asc'
      filters.value = {
        role: '',
        status: ''
      }
      currentPage.value = 1
    }
    
    const applyFilters = () => {
      currentPage.value = 1
    }
    
    // Paginación
    const previousPage = () => {
      if (currentPage.value > 1) {
        currentPage.value--
      }
    }
    
    const nextPage = () => {
      if (currentPage.value < totalPages.value) {
        currentPage.value++
      }
    }
    
    // Gestión de usuarios
    const resetForm = () => {
      userForm.value = {
        name: '',
        email: '',
        phone: '',
        role: 'cliente', // Valor por defecto según la BD
        status: 'active',
        password: ''
      }
    }
    
    const openCreateModal = () => {
      editingUser.value = null
      resetForm()
      showUserModal.value = true
    }
    
    const closeUserModal = () => {
      showUserModal.value = false
      editingUser.value = null
    }
    
    const closeViewModal = () => {
      showViewModal.value = false
      currentUser.value = null
    }
    
    const viewUserDetails = (user) => {
      currentUser.value = user
      showViewModal.value = true
    }
    
    const editFromView = () => {
      if (currentUser.value) {
        editUser(currentUser.value)
        closeViewModal()
      }
    }
    
    const editUser = (user) => {
      editingUser.value = user
      userForm.value = {
        name: user.name,
        email: user.email,
        phone: user.phone || '',
        role: user.role,
        status: user.status || 'active',
        password: ''
      }
      showUserModal.value = true
    }
    
    const saveUser = async () => {
      try {
        savingUser.value = true
        
        if (editingUser.value) {
          await userService.update(editingUser.value.id, userForm.value)
        } else {
          await userService.create(userForm.value)
        }
        
        await loadUsers()
        await loadStats()
        closeUserModal()
      } catch (error) {
        console.error('Error saving user:', error)
      } finally {
        savingUser.value = false
      }
    }
    
    const toggleUserStatus = async (user) => {
      try {
        const newStatus = user.status === 'active' ? 'inactive' : 'active'
        await userService.updateStatus(user.id, newStatus)
        await loadUsers()
        await loadStats()
      } catch (error) {
        console.error('Error toggling user status:', error)
      }
    }
    
    // Acciones masivas
    const bulkActivate = async () => {
      try {
        await userService.bulkUpdateStatus(selectedUsers.value.map(u => u.id), 'active')
        await loadUsers()
        await loadStats()
        selectedUsers.value = []
      } catch (error) {
        console.error('Error bulk activating users:', error)
      }
    }
    
    const bulkDeactivate = async () => {
      try {
        await userService.bulkUpdateStatus(selectedUsers.value.map(u => u.id), 'inactive')
        await loadUsers()
        await loadStats()
        selectedUsers.value = []
      } catch (error) {
        console.error('Error bulk deactivating users:', error)
      }
    }
    
    const bulkChangeRole = () => {
      showBulkRoleModal.value = true
    }
    
    const closeBulkRoleModal = () => {
      showBulkRoleModal.value = false
      bulkRoleForm.value.newRole = 'cliente' // Valor por defecto según la BD
    }
    
    const confirmBulkRoleChange = async () => {
      try {
        savingUser.value = true
        await userService.bulkUpdateRole(selectedUsers.value.map(u => u.id), bulkRoleForm.value.newRole)
        await loadUsers()
        await loadStats()
        selectedUsers.value = []
        closeBulkRoleModal()
      } catch (error) {
        console.error('Error bulk changing roles:', error)
      } finally {
        savingUser.value = false
      }
    }
    
    // Helpers
    const getInitials = (name) => {
      return name?.split(' ').map(n => n[0]).join('').toUpperCase() || '?'
    }
    
    const getRoleBadgeClass = (role) => {
      const classes = {
        admin: 'bg-red-100 text-red-800 border-red-200',
        barbero: 'bg-purple-100 text-purple-800 border-purple-200',
        cliente: 'bg-blue-100 text-blue-800 border-blue-200'
      }
      return classes[role] || 'bg-gray-100 text-gray-800 border-gray-200'
    }
    
    const getRoleLabel = (role) => {
      const labels = {
        admin: 'Administrador',
        barbero: 'Barbero',
        cliente: 'Cliente'
      }
      return labels[role] || role
    }
    
    const getStatusClass = (status) => {
      const classes = {
        active: 'bg-emerald-50 text-emerald-700 border-emerald-200',
        inactive: 'bg-red-50 text-red-700 border-red-200'
      }
      return classes[status] || 'bg-gray-50 text-gray-700 border-gray-200'
    }
    
    const getStatusLabel = (status) => {
      const labels = {
        active: 'Activo',
        inactive: 'Inactivo'
      }
      return labels[status] || status
    }
    
    const formatDate = (date) => {
      if (!date) return 'N/A'
      return new Date(date).toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    }
    
    const getRoleFilterLabel = (role) => {
      const labels = {
        'client': 'Clientes',
        'barber': 'Barberos',
        'admin': 'Administradores'
      }
      return labels[role] || role
    }
    
    const getStatusFilterLabel = (status) => {
      const labels = {
        'active': 'Activos',
        'inactive': 'Inactivos'
      }
      return labels[status] || status
    }
    
    // Verificar autenticación antes de cargar datos
    const ensureAdminAuth = async () => {
      try {
        // Verificar si hay token válido
        const token = localStorage.getItem('authToken')
        const user = localStorage.getItem('user')
        
        if (!token || !user) {
          const { authService } = await import('@/services/authService.js')
          await authService.loginAsAdmin()
        } else {
          const userData = JSON.parse(user)
          if (userData.rol !== 'admin' && userData.role !== 'admin') {
            const { authService } = await import('@/services/authService.js')
            await authService.loginAsAdmin()
          }
        }
      } catch (error) {
        console.error('❌ Error en autenticación admin:', error)
      }
    }

    // Lifecycle
    onMounted(async () => {
      await ensureAdminAuth()
      await loadUsers()
      await loadStats()
    })
    
    return {
      // Estado
      loadingStats,
      loadingUsers,
      savingUser,
      modoDemo,
      users,
      selectedUsers,
      stats,
      searchTerm,
      sortBy,
      filters,
      currentPage,
      totalPages,
      startItem,
      endItem,
      totalUsers,
      
      // Modales
      showUserModal,
      showViewModal,
      showBulkRoleModal,
      editingUser,
      currentUser,
      
      // Formularios
      userForm,
      bulkRoleForm,
      
      // Configuración
      tableColumns,
      
      // Computed
      filteredUsers,
      paginatedUsers,
      hasActiveFilters,
      
      // Métodos
      clearFilters,
      applyFilters,
      previousPage,
      nextPage,
      openCreateModal,
      closeUserModal,
      closeViewModal,
      viewUserDetails,
      editFromView,
      editUser,
      saveUser,
      toggleUserStatus,
      bulkActivate,
      bulkDeactivate,
      bulkChangeRole,
      closeBulkRoleModal,
      confirmBulkRoleChange,
      
      // Helpers
      getInitials,
      getRoleBadgeClass,
      getRoleLabel,
      getStatusClass,
      getStatusLabel,
      formatDate,
      getRoleFilterLabel,
      getStatusFilterLabel
    }
  }
}
</script>

<style scoped>
/* AdminUsuarios.vue - Tailwind CSS v4 */
/* Todas las utilidades son nativas de Tailwind v4 */
/* No se requiere CSS custom - 100% utility-first */
</style>
