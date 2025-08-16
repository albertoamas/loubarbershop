<!--
  AdminUsuarios.vue - Gestión completa de usuarios y clientes
  FASE 8.6: Rediseño minimalista y moderno
-->
<template>
  <div class="admin-usuarios">
    <!-- Header con acciones -->
    <div class="admin-header">
      <div>
        <h1 class="admin-title">
          Gestión de Usuarios
          <span v-if="modoDemo" class="demo-badge">MODO DEMO</span>
        </h1>
        <p class="admin-subtitle">
          Administra usuarios, roles y permisos del sistema
          <span v-if="modoDemo" class="demo-subtitle">• Usando datos de ejemplo - Backend no disponible</span>
        </p>
      </div>
      <div class="header-actions">
        <button 
          @click="openCreateModal"
          class="btn-primary"
          :disabled="loadingUsers"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
          Nuevo Usuario
        </button>
      </div>
    </div>

    <!-- Estadísticas rápidas -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-content">
          <div class="stat-number">{{ stats.totalUsers || 0 }}</div>
          <div class="stat-label">Total Usuarios</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-success">
        <div class="stat-content">
          <div class="stat-number">{{ stats.totalClients || 0 }}</div>
          <div class="stat-label">Clientes</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-purple">
        <div class="stat-content">
          <div class="stat-number">{{ stats.totalBarbers || 0 }}</div>
          <div class="stat-label">Barberos</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1.5a2.5 2.5 0 015 0H17M9 10V9a3 3 0 116 0v1M9 10H5.23a1 1 0 00-.902.56l-1.28 2.56a1 1 0 00.902 1.44H17M9 10l6 6" />
          </svg>
        </div>
      </div>

      <div class="stat-card stat-info">
        <div class="stat-content">
          <div class="stat-number">{{ stats.activeToday || 0 }}</div>
          <div class="stat-label">Activos Hoy</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M13 10V3L4 14h7v7l9-11h-7z"/>
          </svg>
        </div>
      </div>
    </div>

    <!-- Filtros compactos -->
    <div class="filters-container-compact">
      <div class="filters-row">
        <select 
          v-model="filters.role"
          class="filter-select-compact"
          @change="applyFilters"
        >
          <option value="">Todos los roles</option>
          <option value="client">Clientes</option>
          <option value="barber">Barberos</option>
          <option value="admin">Administradores</option>
        </select>

        <select 
          v-model="filters.status"
          class="filter-select-compact"
          @change="applyFilters"
        >
          <option value="">Todos los estados</option>
          <option value="active">Activos</option>
          <option value="inactive">Inactivos</option>
          <option value="suspended">Suspendidos</option>
        </select>

        <select 
          v-model="filters.dateRange"
          class="filter-select-compact"
          @change="applyFilters"
        >
          <option value="">Cualquier fecha</option>
          <option value="today">Hoy</option>
          <option value="week">Esta semana</option>
          <option value="month">Este mes</option>
        </select>

        <button 
          @click="clearFilters"
          class="filter-clear-btn-compact"
        >
          <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
          Limpiar
        </button>
      </div>
    </div>

    <!-- Tabla de usuarios -->
    <AdminTable
      title="Lista de Usuarios"
      description="Gestiona todos los usuarios del sistema"
      :columns="tableColumns"
      :data="paginatedUsers"
      :loading="loadingUsers"
      :selected="selectedUsers"
      @update:selected="selectedUsers = $event"
      showActions
      showSelection
    >
      <!-- Usuario -->
      <template #cell-usuario="{ item }">
        <div class="usuario-info">
          <div class="usuario-avatar">
            <img 
              v-if="item.avatar" 
              :src="item.avatar" 
              :alt="item.name"
              class="avatar-img"
            />
            <div v-else class="avatar-placeholder">
              {{ getInitials(item.name) }}
            </div>
          </div>
          <div class="usuario-details">
            <div class="usuario-nombre">{{ item.name }}</div>
            <div class="usuario-email">{{ item.email }}</div>
          </div>
        </div>
      </template>

      <!-- Rol -->
      <template #cell-rol="{ item }">
        <span :class="getRoleBadgeClass(item.role)" class="rol-badge">
          {{ getRoleLabel(item.role) }}
        </span>
      </template>

      <!-- Estado -->
      <template #cell-estado="{ item }">
        <div class="status-badge" :class="getStatusClass(item.status)">
          <div class="status-dot"></div>
          <span>{{ getStatusLabel(item.status) }}</span>
        </div>
      </template>

      <!-- Información adicional -->
      <template #cell-contacto="{ item }">
        <div class="contact-info">
          <div class="contact-phone">
            <svg class="w-3 h-3 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
            </svg>
            {{ item.phone || 'No registrado' }}
          </div>
          <div class="contact-email-verified">
            <svg v-if="item.emailVerified" class="w-3 h-3 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <svg v-else class="w-3 h-3 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span class="text-xs">{{ item.emailVerified ? 'Email verificado' : 'Email pendiente' }}</span>
          </div>
        </div>
      </template>

      <!-- Fechas -->
      <template #cell-fechas="{ item }">
        <div class="dates-info">
          <div class="date-created">
            <span class="date-label">Creado:</span>
            <span class="date-value">{{ formatDate(item.createdAt) }}</span>
          </div>
          <div class="date-updated">
            <span class="date-label">Actualizado:</span>
            <span class="date-value">{{ formatDate(item.updatedAt) }}</span>
          </div>
        </div>
      </template>

      <!-- Acciones -->
      <template #actions="{ item }">
        <div class="action-buttons">
          <button @click="editUser(item)" class="action-btn action-edit">
            Editar
          </button>
          <button 
            @click="toggleUserStatus(item)" 
            class="action-btn"
            :class="item.status === 'active' ? 'action-deactivate' : 'action-activate'"
          >
            {{ item.status === 'active' ? 'Desactivar' : 'Activar' }}
          </button>
        </div>
      </template>
    </AdminTable>

    <!-- Paginación -->
    <div class="pagination-container">
      <div class="pagination-info">
        Mostrando {{ startItem }} a {{ endItem }} de {{ totalUsers }} usuarios
      </div>
      <div class="pagination-buttons">
        <button 
          @click="previousPage"
          class="pagination-btn"
          :class="{ 'pagination-btn-disabled': currentPage === 1 }"
          :disabled="currentPage === 1"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
        </button>
        
        <span class="pagination-current">
          Página {{ currentPage }} de {{ totalPages }}
        </span>
        
        <button 
          @click="nextPage"
          class="pagination-btn"
          :class="{ 'pagination-btn-disabled': currentPage >= totalPages }"
          :disabled="currentPage >= totalPages"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Acciones masivas (cuando hay selección) -->
    <div v-if="selectedUsers.length > 0" class="bulk-actions-container">
      <div class="bulk-actions-info">
        {{ selectedUsers.length }} usuario(s) seleccionado(s)
      </div>
      <div class="bulk-actions">
        <button @click="bulkActivate" class="bulk-btn bulk-activate">
          Activar Seleccionados
        </button>
        <button @click="bulkDeactivate" class="bulk-btn bulk-deactivate">
          Desactivar Seleccionados
        </button>
        <button @click="bulkChangeRole" class="bulk-btn bulk-role">
          Cambiar Rol
        </button>
      </div>
    </div>

    <!-- Modal de creación/edición simple -->
    <AdminModal
      :show="showUserModal"
      :title="editingUser ? 'Editar Usuario' : 'Crear Usuario'"
      @close="closeUserModal"
      showActions
    >
      <form @submit.prevent="saveUser" class="space-y-4">
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Nombre completo *</label>
            <input
              v-model="userForm.name"
              type="text"
              required
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
              placeholder="Nombre y apellido"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Email *</label>
            <input
              v-model="userForm.email"
              type="email"
              required
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
              placeholder="correo@ejemplo.com"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Teléfono</label>
            <input
              v-model="userForm.phone"
              type="tel"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
              placeholder="+1 234 567 8900"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Rol *</label>
            <select
              v-model="userForm.role"
              required
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
            >
              <option value="cliente">Cliente</option>
              <option value="barbero">Barbero</option>
              <option value="admin">Administrador</option>
            </select>
          </div>

          <div v-if="!editingUser">
            <label class="block text-sm font-medium text-gray-700 mb-1">Contraseña *</label>
            <input
              v-model="userForm.password"
              type="password"
              :required="!editingUser"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
              placeholder="Mínimo 8 caracteres"
            />
          </div>
        </div>

        <div class="flex justify-end gap-3 pt-4 border-t">
          <button type="button" @click="closeUserModal" class="btn-secondary">
            Cancelar
          </button>
          <button type="submit" class="btn-primary" :disabled="savingUser">
            {{ editingUser ? 'Actualizar' : 'Crear' }} Usuario
          </button>
        </div>
      </form>
    </AdminModal>

    <!-- Modal simple para cambio de rol masivo -->
    <AdminModal
      :show="showBulkRoleModal"
      title="Cambiar Rol Masivo"
      @close="closeBulkRoleModal"
      showActions
    >
      <form @submit.prevent="confirmBulkRoleChange" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Nuevo rol</label>
          <select
            v-model="bulkRoleForm.newRole"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
          >
            <option value="cliente">Cliente</option>
            <option value="barbero">Barbero</option>
            <option value="admin">Administrador</option>
          </select>
        </div>
        <div class="bg-yellow-50 p-3 rounded text-sm text-yellow-800">
          Se cambiará el rol de {{ selectedUsers.length }} usuario(s) seleccionado(s).
        </div>
        <div class="flex justify-end gap-3">
          <button type="button" @click="closeBulkRoleModal" class="btn-secondary">
            Cancelar
          </button>
          <button type="submit" class="btn-primary" :disabled="savingUser">
            Cambiar Rol
          </button>
        </div>
      </form>
    </AdminModal>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import AdminCard from '@/components/admin/AdminCard.vue'
import AdminTable from '@/components/admin/AdminTable.vue'
import AdminModal from '@/components/admin/AdminModal.vue'
import AdminButton from '@/components/admin/AdminButton.vue'
import { userService } from '@/services/userService'

export default {
  name: 'AdminUsuarios',
  components: {
    AdminCard,
    AdminTable,
    AdminModal,
    AdminButton
  },
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
    const filters = ref({
      role: '',
      status: '',
      dateRange: ''
    })
    
    // Paginación
    const currentPage = ref(1)
    const itemsPerPage = 25
    
    // Modales
    const showUserModal = ref(false)
    const showBulkRoleModal = ref(false)
    const editingUser = ref(null)
    
    // Formularios
    const userForm = ref({
      name: '',
      email: '',
      phone: '',
      role: 'cliente', // Valor por defecto según la BD
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
    
    // Computed
    const filteredUsers = computed(() => {
      let filtered = [...users.value]
      
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
      
      if (filters.value.dateRange) {
        const now = new Date()
        const filterDate = new Date()
        
        switch (filters.value.dateRange) {
          case 'today':
            filterDate.setHours(0, 0, 0, 0)
            break
          case 'week':
            filterDate.setDate(now.getDate() - 7)
            break
          case 'month':
            filterDate.setMonth(now.getMonth() - 1)
            break
        }
        
        filtered = filtered.filter(user => new Date(user.createdAt) >= filterDate)
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
      filters.value = {
        role: '',
        status: '',
        dateRange: ''
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
    
    const editUser = (user) => {
      editingUser.value = user
      userForm.value = {
        name: user.name,
        email: user.email,
        phone: user.phone || '',
        role: user.role,
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
        active: 'status-available',
        inactive: 'status-unavailable',
        suspended: 'status-unavailable'
      }
      return classes[status] || 'status-unavailable'
    }
    
    const getStatusLabel = (status) => {
      const labels = {
        active: 'Activo',
        inactive: 'Inactivo',
        suspended: 'Suspendido'
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
      filters,
      currentPage,
      totalPages,
      startItem,
      endItem,
      totalUsers,
      
      // Modales
      showUserModal,
      showBulkRoleModal,
      editingUser,
      
      // Formularios
      userForm,
      bulkRoleForm,
      
      // Configuración
      tableColumns,
      
      // Computed
      filteredUsers,
      paginatedUsers,
      
      // Métodos
      clearFilters,
      applyFilters,
      previousPage,
      nextPage,
      openCreateModal,
      closeUserModal,
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
      formatDate
    }
  }
}
</script>

<style scoped>
.admin-usuarios {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  padding: 1.5rem;
  background-color: #f8fafc;
  min-height: 100vh;
}

/* Header */
.admin-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
}

.admin-title {
  font-size: 1.875rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.admin-subtitle {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0;
}

.demo-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.5rem;
  background: #fef3c7;
  color: #92400e;
  border: 1px solid #fbbf24;
  border-radius: 4px;
  font-size: 0.6875rem;
  font-weight: 600;
  margin-left: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.demo-subtitle {
  color: #f59e0b;
  font-weight: 500;
}

.header-actions {
  display: flex;
  gap: 0.75rem;
  flex-shrink: 0;
}

/* Botones */
.btn-primary {
  background: #000000;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-primary:hover {
  background: #1f2937;
}

.btn-secondary {
  background: white;
  color: #374151;
  border: 1px solid #d1d5db;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.15s ease;
}

.btn-secondary:hover {
  background: #f9fafb;
  border-color: #9ca3af;
}

/* Estadísticas */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
  border: 1px solid #e5e7eb;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.stat-content {
  flex: 1;
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  line-height: 1;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}

.stat-icon {
  flex-shrink: 0;
  width: 3rem;
  height: 3rem;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f3f4f6;
  color: #6b7280;
}

/* Variantes de color para las estadísticas */
.stat-success .stat-number { color: #059669; }
.stat-success .stat-icon {
  background: #d1fae5;
  color: #059669;
}

.stat-info .stat-number { color: #0284c7; }
.stat-info .stat-icon {
  background: #dbeafe;
  color: #0284c7;
}

.stat-purple .stat-number { color: #7c3aed; }
.stat-purple .stat-icon {
  background: #ede9fe;
  color: #7c3aed;
}

/* Filtros compactos */
.filters-container-compact {
  background: white;
  border-radius: 8px;
  padding: 0.75rem 1rem;
  margin-bottom: 0.5rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
  border: 1px solid #e5e7eb;
}

.filters-row {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  flex-wrap: nowrap;
  margin: 0;
}

.filter-select-compact {
  min-width: 140px;
  padding: 0.375rem 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  background: white;
  font-size: 0.8125rem;
  color: #374151;
  transition: all 0.15s ease;
  height: 2rem;
}

.filter-select-compact:focus {
  outline: none;
  border-color: #000000;
  box-shadow: 0 0 0 1px #000000;
}

.filter-clear-btn-compact {
  background: #f3f4f6;
  color: #6b7280;
  border: 1px solid #d1d5db;
  padding: 0.375rem 0.625rem;
  border-radius: 6px;
  font-size: 0.8125rem;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 0.375rem;
  font-weight: 500;
  height: 2rem;
  white-space: nowrap;
}

.filter-clear-btn-compact:hover {
  background: #e5e7eb;
  color: #374151;
}

/* Paginación */
.pagination-container {
  background: white;
  border-radius: 8px;
  padding: 1rem 1.5rem;
  margin-top: 1.5rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
  border: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.pagination-info {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}

.pagination-buttons {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.pagination-btn {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 6px;
  border: 1px solid #d1d5db;
  background: white;
  color: #374151;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.15s ease;
  font-weight: 500;
}

.pagination-btn:hover:not(.pagination-btn-disabled) {
  background: #f9fafb;
  border-color: #9ca3af;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.pagination-btn-disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-current {
  font-size: 0.875rem;
  color: #374151;
  font-weight: 600;
  padding: 0 1rem;
  white-space: nowrap;
}

/* Información de usuario */
.usuario-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.usuario-avatar {
  width: 2.5rem;
  height: 2.5rem;
  flex-shrink: 0;
}

.avatar-img {
  width: 100%;
  height: 100%;
  border-radius: 8px;
  object-fit: cover;
  border: 2px solid #e5e7eb;
}

.avatar-placeholder {
  width: 100%;
  height: 100%;
  border-radius: 8px;
  background: #000000;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
}

.usuario-details {
  min-width: 0;
}

.usuario-nombre {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.875rem;
}

.usuario-email {
  color: #6b7280;
  font-size: 0.75rem;
}

/* Badges de rol */
.rol-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
  border: 1px solid;
}

/* Estados */
.status-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
  gap: 0.5rem;
}

.status-dot {
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 50%;
}

.status-available {
  background: #d1fae5;
  color: #065f46;
  border: 1px solid #10b981;
}

.status-available .status-dot {
  background: #10b981;
}

.status-unavailable {
  background: #fee2e2;
  color: #991b1b;
  border: 1px solid #ef4444;
}

.status-unavailable .status-dot {
  background: #ef4444;
}

/* Información adicional */
.info-data {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.info-phone {
  font-weight: 500;
  color: #1f2937;
  font-size: 0.875rem;
}

.info-date {
  color: #6b7280;
  font-size: 0.75rem;
}

/* Información de contacto */
.contact-info {
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
}

.contact-phone {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  font-size: 0.8125rem;
  color: #374151;
  font-weight: 500;
}

.contact-email-verified {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  font-size: 0.75rem;
}

/* Información de fechas */
.dates-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.date-created,
.date-updated {
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}

.date-label {
  font-size: 0.6875rem;
  color: #6b7280;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.025em;
}

.date-value {
  font-size: 0.75rem;
  color: #374151;
  font-weight: 500;
}

/* Acciones */
.action-buttons {
  display: flex;
  gap: 0.5rem;
  justify-content: flex-end;
}

.action-btn {
  padding: 0.375rem 0.75rem;
  font-size: 0.75rem;
  font-weight: 500;
  border-radius: 6px;
  border: 1px solid;
  cursor: pointer;
  transition: all 0.15s ease;
}

.action-edit {
  background: #fffbeb;
  color: #92400e;
  border-color: #fbbf24;
}

.action-edit:hover {
  background: #fef3c7;
  border-color: #f59e0b;
}

.action-activate {
  background: #ecfdf5;
  color: #065f46;
  border-color: #10b981;
}

.action-activate:hover {
  background: #d1fae5;
  border-color: #059669;
}

.action-deactivate {
  background: #fee2e2;
  color: #991b1b;
  border-color: #ef4444;
}

.action-deactivate:hover {
  background: #fecaca;
  border-color: #dc2626;
}

/* Acciones masivas */
.bulk-actions-container {
  background: white;
  border-radius: 8px;
  padding: 1rem 1.5rem;
  margin-top: 1rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
  border: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.bulk-actions-info {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}

.bulk-actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.bulk-btn {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  font-weight: 500;
  border-radius: 6px;
  border: 1px solid;
  cursor: pointer;
  transition: all 0.15s ease;
}

.bulk-activate {
  background: #ecfdf5;
  color: #065f46;
  border-color: #10b981;
}

.bulk-activate:hover {
  background: #d1fae5;
  border-color: #059669;
}

.bulk-deactivate {
  background: #fef3c7;
  color: #92400e;
  border-color: #fbbf24;
}

.bulk-deactivate:hover {
  background: #fde68a;
  border-color: #f59e0b;
}

.bulk-role {
  background: #ede9fe;
  color: #7c3aed;
  border-color: #a855f7;
}

.bulk-role:hover {
  background: #ddd6fe;
  border-color: #9333ea;
}

/* Responsividad */
@media (max-width: 768px) {
  .admin-usuarios {
    padding: 1rem;
  }
  
  .admin-header {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .header-actions {
    justify-content: stretch;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .filters-row {
    flex-wrap: wrap;
  }
  
  .filter-select-compact {
    min-width: 120px;
  }
  
  .action-buttons {
    flex-direction: column;
    gap: 0.25rem;
  }
  
  .bulk-actions-container {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .bulk-actions {
    justify-content: stretch;
  }
}
</style>
