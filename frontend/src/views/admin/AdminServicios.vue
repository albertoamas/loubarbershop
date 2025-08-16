<!--
  AdminServicios.vue - Gestión completa de servicios
  FASE 8.7: Rediseño minimalista y moderno
-->
<template>
  <div class="admin-servicios">
    <!-- Header con acciones -->
    <div class="admin-header">
      <div>
        <h1 class="admin-title">Gestión de Servicios</h1>
        <p class="admin-subtitle">Administra el catálogo de servicios de la barbería</p>
      </div>
      <div class="header-actions">
        <button 
          @click="openCreateModal"
          class="btn-primary"
          :disabled="loading"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
          Nuevo Servicio
        </button>
      </div>
    </div>

    <!-- Estadísticas rápidas -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-content">
          <div class="stat-number">{{ stats.totalServices || 0 }}</div>
          <div class="stat-label">Total Servicios</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-success">
        <div class="stat-content">
          <div class="stat-number">{{ stats.activeServices || 0 }}</div>
          <div class="stat-label">Servicios Activos</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-info">
        <div class="stat-content">
          <div class="stat-number">{{ stats.totalServices - stats.activeServices || 0 }}</div>
          <div class="stat-label">Servicios Inactivos</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-purple">
        <div class="stat-content">
          <div class="stat-number">Bs {{ formatPrice(stats.avgRevenue || 0) }}</div>
          <div class="stat-label">Precio Promedio</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z"/>
          </svg>
        </div>
      </div>
    </div>

    <!-- Filtros compactos -->
    <div class="filters-container-compact">
      <div class="filters-row">
        <select 
          v-model="filters.category"
          class="filter-select-compact"
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
          class="filter-select-compact"
          @change="applyFilters"
        >
          <option value="">Todos los estados</option>
          <option value="active">Activos</option>
          <option value="inactive">Inactivos</option>
        </select>

        <select 
          v-model="filters.priceRange"
          class="filter-select-compact"
          @change="applyFilters"
        >
          <option value="">Todos los precios</option>
          <option value="0-30000">Bs 0 - Bs 30,000</option>
          <option value="30000-50000">Bs 30,000 - Bs 50,000</option>
          <option value="50000-100000">Bs 50,000+</option>
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

    <!-- Tabla de servicios -->
    <AdminTable
      title="Lista de Servicios"
      description="Gestiona todos los servicios del catálogo"
      :columns="tableColumns"
      :data="paginatedServices"
      :loading="loading"
      :selected="selectedServices"
      @update:selected="selectedServices = $event"
      :selectable="true"
    >
      <!-- Servicio -->
      <template #cell-servicio="{ item }">
        <div class="servicio-info">
          <div class="servicio-image">
            <img 
              :src="item.image || getDefaultServiceImage(item.category)" 
              :alt="item.name"
              class="service-img"
            />
          </div>
          <div class="servicio-details">
            <div class="servicio-nombre">{{ item.name }}</div>
            <div class="servicio-descripcion">{{ item.description || 'Sin descripción' }}</div>
          </div>
        </div>
      </template>

      <!-- Categoría -->
      <template #cell-categoria="{ item }">
        <span :class="getCategoryBadgeClass(item.category || 'default')" class="categoria-badge">
          {{ getCategoryLabel(item.category) }}
        </span>
      </template>

      <!-- Precio -->
      <template #cell-precio="{ item }">
        <div class="precio-info">
          <div class="precio-value">Bs {{ formatPrice(item.price || 0) }}</div>
        </div>
      </template>

      <!-- Duración -->
      <template #cell-duracion="{ item }">
        <div class="duracion-info">
          <div class="duracion-value">{{ item.duration || 0 }} min</div>
        </div>
      </template>

      <!-- Estado -->
      <template #cell-estado="{ item }">
        <div class="status-badge" :class="getStatusClass(item.status)">
          <div class="status-dot"></div>
          <span>{{ getStatusLabel(item.status) }}</span>
        </div>
      </template>

      <!-- Acciones -->
      <template #actions="{ item }">
        <div class="action-buttons">
          <button @click="editService(item)" class="action-btn action-edit">
            Editar
          </button>
          <button 
            @click="toggleServiceStatus(item)" 
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
        Mostrando {{ startItem }} a {{ endItem }} de {{ totalServices }} servicios
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
    <div v-if="selectedServices.length > 0" class="bulk-actions-container">
      <div class="bulk-actions-info">
        {{ selectedServices.length }} servicio(s) seleccionado(s)
      </div>
      <div class="bulk-actions">
        <button @click="bulkActivate" class="bulk-btn bulk-activate">
          Activar Seleccionados
        </button>
        <button @click="bulkDeactivate" class="bulk-btn bulk-deactivate">
          Desactivar Seleccionados
        </button>
        <button @click="bulkUpdateCategory" class="bulk-btn bulk-role">
          Cambiar Categoría
        </button>
      </div>
    </div>

    <!-- Modal de creación/edición simple -->
    <AdminModal
      :show="showServiceModal"
      :title="editingService ? 'Editar Servicio' : 'Crear Servicio'"
      @close="closeServiceModal"
      showActions
    >
      <form @submit.prevent="saveService" class="space-y-4">
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Nombre del servicio *</label>
            <input
              v-model="serviceForm.name"
              type="text"
              required
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
              placeholder="Ej: Corte Clásico"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Descripción</label>
            <textarea
              v-model="serviceForm.description"
              rows="3"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
              placeholder="Descripción del servicio..."
            ></textarea>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Categoría *</label>
            <select
              v-model="serviceForm.category"
              required
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
            >
              <option value="">Seleccionar categoría</option>
              <option value="cortes">Cortes</option>
              <option value="barbas">Barbas</option>
              <option value="tratamientos">Tratamientos</option>
              <option value="combos">Combos</option>
            </select>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Precio *</label>
              <div class="relative">
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <span class="text-gray-500 text-sm">Bs</span>
                </div>
                <input
                  v-model="serviceForm.price"
                  type="number"
                  required
                  min="0"
                  step="1000"
                  class="w-full pl-8 pr-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
                  placeholder="30000"
                />
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Duración (min) *</label>
              <input
                v-model="serviceForm.duration"
                type="number"
                required
                min="15"
                max="240"
                step="15"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
                placeholder="45"
              />
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Estado</label>
            <select
              v-model="serviceForm.status"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
            >
              <option value="active">Activo</option>
              <option value="inactive">Inactivo</option>
            </select>
          </div>
        </div>

        <div class="flex justify-end gap-3 pt-4 border-t">
          <button type="button" @click="closeServiceModal" class="btn-secondary">
            Cancelar
          </button>
          <button type="submit" class="btn-primary" :disabled="saving">
            {{ editingService ? 'Actualizar' : 'Crear' }} Servicio
          </button>
        </div>
      </form>
    </AdminModal>

    <!-- Modal simple para cambio de categoría masivo -->
    <AdminModal
      :show="showBulkCategoryModal"
      title="Cambiar Categoría Masiva"
      @close="closeBulkCategoryModal"
      showActions
    >
      <form @submit.prevent="confirmBulkCategoryChange" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Nueva categoría</label>
          <select
            v-model="bulkCategoryForm.newCategory"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
          >
            <option value="cortes">Cortes</option>
            <option value="barbas">Barbas</option>
            <option value="tratamientos">Tratamientos</option>
            <option value="combos">Combos</option>
          </select>
        </div>
        <div class="bg-yellow-50 p-3 rounded text-sm text-yellow-800">
          Se cambiará la categoría de {{ selectedServices.length }} servicio(s) seleccionado(s).
        </div>
        <div class="flex justify-end gap-3">
          <button type="button" @click="closeBulkCategoryModal" class="btn-secondary">
            Cancelar
          </button>
          <button type="submit" class="btn-primary" :disabled="saving">
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
    cortes: 'categoria-cortes',
    barbas: 'categoria-barbas',
    tratamientos: 'categoria-tratamientos',
    combos: 'categoria-combos',
    default: 'categoria-default'
  }
  return `categoria-badge ${classes[category] || classes.default}`
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
/* Contenedor principal */
.admin-servicios {
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

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
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
  display: flex;
  align-items: center;
  gap: 0.5rem;
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
  width: 3rem;
  height: 3rem;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f3f4f6;
  color: #6b7280;
}

.stat-success .stat-number { color: #059669; }
.stat-success .stat-icon { background: #d1fae5; color: #059669; }

.stat-info .stat-number { color: #0284c7; }
.stat-info .stat-icon { background: #dbeafe; color: #0284c7; }

.stat-purple .stat-number { color: #7c3aed; }
.stat-purple .stat-icon { background: #ede9fe; color: #7c3aed; }

/* Filtros compactos */
.filters-container-compact {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 0.75rem;
  padding: 1rem;
  margin-bottom: 1.5rem;
}

.filters-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.filter-select-compact {
  padding: 0.5rem 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  background: white;
  color: #374151;
  min-width: 150px;
  flex: 1;
}

.filter-select-compact:focus {
  outline: none;
  border-color: #000000;
  box-shadow: 0 0 0 1px #000000;
}

.filter-clear-btn-compact {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  padding: 0.5rem 0.75rem;
  background: #f8fafc;
  color: #64748b;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  font-size: 0.75rem;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-clear-btn-compact:hover {
  background: #f1f5f9;
  color: #475569;
}

/* Contenido específico de servicios */
.servicio-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.servicio-image {
  flex-shrink: 0;
}

.service-img {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 0.5rem;
  object-fit: cover;
  border: 1px solid #e5e7eb;
}

.servicio-details {
  flex: 1;
  min-width: 0;
}

.servicio-nombre {
  font-weight: 600;
  color: #111827;
  font-size: 0.875rem;
  line-height: 1.2;
}

.servicio-descripcion {
  color: #6B7280;
  font-size: 0.75rem;
  margin-top: 0.125rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.categoria-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.5rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.025em;
}

.categoria-cortes {
  background: #dbeafe;
  color: #1e40af;
}

.categoria-barbas {
  background: #dcfce7;
  color: #15803d;
}

.categoria-tratamientos {
  background: #fef3c7;
  color: #d97706;
}

.categoria-combos {
  background: #f3e8ff;
  color: #7c3aed;
}

.categoria-default {
  background: #f3f4f6;
  color: #6b7280;
}

.precio-info {
  text-align: left;
}

.precio-value {
  font-weight: 600;
  color: #111827;
  font-size: 0.875rem;
}

.duracion-info {
  text-align: left;
}

.duracion-value {
  color: #111827;
  font-weight: 500;
  font-size: 0.875rem;
}

/* Status badges */
.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.25rem 0.75rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 500;
}

.status-badge.status-active {
  background: #dcfce7;
  color: #15803d;
}

.status-badge.status-inactive {
  background: #fee2e2;
  color: #dc2626;
}

.status-dot {
  width: 0.375rem;
  height: 0.375rem;
  border-radius: 50%;
}

.status-active .status-dot {
  background: #15803d;
}

.status-inactive .status-dot {
  background: #dc2626;
}

/* Botones de acción */
.action-buttons {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  justify-content: flex-start;
  max-width: 200px;
}

.action-btn {
  padding: 0.375rem 0.75rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  border: 1px solid;
  white-space: nowrap;
  flex-shrink: 0;
}

.action-edit {
  background: #f8fafc;
  color: #475569;
  border-color: #e2e8f0;
}

.action-edit:hover {
  background: #f1f5f9;
  border-color: #cbd5e1;
}

.action-activate {
  background: #ecfdf5;
  color: #059669;
  border-color: #a7f3d0;
}

.action-activate:hover {
  background: #d1fae5;
  border-color: #6ee7b7;
}

.action-deactivate {
  background: #fef2f2;
  color: #dc2626;
  border-color: #fecaca;
}

.action-deactivate:hover {
  background: #fee2e2;
  border-color: #fca5a5;
}

/* Paginación */
.pagination-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 1.5rem;
  padding: 1rem;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 0.75rem;
}

.pagination-info {
  font-size: 0.875rem;
  color: #6B7280;
  flex: 1;
}

.pagination-buttons {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.pagination-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2rem;
  height: 2rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  background: white;
  color: #374151;
  cursor: pointer;
  transition: all 0.2s;
}

.pagination-btn:hover:not(.pagination-btn-disabled) {
  background: #f9fafb;
  border-color: #9ca3af;
}

.pagination-btn-disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-current {
  font-size: 0.875rem;
  color: #374151;
  font-weight: 500;
}

/* Acciones masivas */
.bulk-actions-container {
  position: fixed;
  bottom: 1.5rem;
  left: 50%;
  transform: translateX(-50%);
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 0.75rem;
  padding: 1rem 1.5rem;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 1rem;
  z-index: 50;
}

.bulk-actions-info {
  font-size: 0.875rem;
  color: #374151;
  font-weight: 500;
}

.bulk-actions {
  display: flex;
  gap: 0.5rem;
}

.bulk-btn {
  padding: 0.5rem 0.75rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  border: 1px solid;
}

.bulk-activate {
  background: #ecfdf5;
  color: #059669;
  border-color: #a7f3d0;
}

.bulk-activate:hover {
  background: #d1fae5;
  border-color: #6ee7b7;
}

.bulk-deactivate {
  background: #fef2f2;
  color: #dc2626;
  border-color: #fecaca;
}

.bulk-deactivate:hover {
  background: #fee2e2;
  border-color: #fca5a5;
}

.bulk-role {
  background: #f8fafc;
  color: #475569;
  border-color: #e2e8f0;
}

.bulk-role:hover {
  background: #f1f5f9;
  border-color: #cbd5e1;
}

/* Utilidades adicionales */
.w-4 { width: 1rem; }
.h-4 { height: 1rem; }
.w-3 { width: 0.75rem; }
.h-3 { height: 0.75rem; }
.w-6 { width: 1.5rem; }
.h-6 { height: 1.5rem; }

.fill-current { fill: currentColor; }

.space-y-4 > * + * {
  margin-top: 1rem;
}

.grid-cols-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}

.gap-4 {
  gap: 1rem;
}

.text-sm {
  font-size: 0.875rem;
}

.font-medium {
  font-weight: 500;
}

.text-gray-700 {
  color: #374151;
}

.mb-1 {
  margin-bottom: 0.25rem;
}

.block {
  display: block;
}

.w-full {
  width: 100%;
}

.px-3 {
  padding-left: 0.75rem;
  padding-right: 0.75rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.border {
  border-width: 1px;
}

.border-gray-300 {
  border-color: #d1d5db;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.focus\:ring-1:focus {
  box-shadow: 0 0 0 1px;
}

.focus\:ring-black:focus {
  box-shadow: 0 0 0 1px #000000;
}

.focus\:border-black:focus {
  border-color: #000000;
}

.relative {
  position: relative;
}

.absolute {
  position: absolute;
}

.inset-y-0 {
  top: 0;
  bottom: 0;
}

.left-0 {
  left: 0;
}

.pl-3 {
  padding-left: 0.75rem;
}

.flex {
  display: flex;
}

.items-center {
  align-items: center;
}

.pointer-events-none {
  pointer-events: none;
}

.text-gray-500 {
  color: #6b7280;
}

.pl-8 {
  padding-left: 2rem;
}

.pr-3 {
  padding-right: 0.75rem;
}

.justify-end {
  justify-content: flex-end;
}

.pt-4 {
  padding-top: 1rem;
}

.border-t {
  border-top-width: 1px;
}

.bg-yellow-50 {
  background-color: #fffbeb;
}

.p-3 {
  padding: 0.75rem;
}

.rounded {
  border-radius: 0.25rem;
}

.text-yellow-800 {
  color: #92400e;
}
</style>
