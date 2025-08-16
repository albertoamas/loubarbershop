<!--
  AdminProductos.vue - Gestión completa de productos
  FASE 8.7: Rediseño minimalista y moderno
-->
<template>
  <div class="admin-productos">
    <!-- Header con acciones -->
    <div class="admin-header">
      <div>
        <h1 class="admin-title">Gestión de Productos</h1>
        <p class="admin-subtitle">Administra el inventario de productos de la barbería</p>
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
          Nuevo Producto
        </button>
      </div>
    </div>

    <!-- Estadísticas rápidas -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-content">
          <div class="stat-number">{{ stats.totalProducts || 0 }}</div>
          <div class="stat-label">Total Productos</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-success">
        <div class="stat-content">
          <div class="stat-number">{{ stats.inStock || 0 }}</div>
          <div class="stat-label">En Stock</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-warning">
        <div class="stat-content">
          <div class="stat-number">{{ stats.lowStock || 0 }}</div>
          <div class="stat-label">Stock Bajo</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-purple">
        <div class="stat-content">
          <div class="stat-number">Bs {{ formatPrice(stats.totalValue || 0) }}</div>
          <div class="stat-label">Valor Inventario</div>
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
          <option value="Cuidado Capilar">Cuidado Capilar</option>
          <option value="Styling">Styling</option>
          <option value="Cuidado Facial">Cuidado Facial</option>
          <option value="Herramientas">Herramientas</option>
          <option value="Accesorios">Accesorios</option>
          <option value="General">General</option>
        </select>

        <select 
          v-model="filters.stock"
          class="filter-select-compact"
          @change="applyFilters"
        >
          <option value="">Todos los stock</option>
          <option value="in-stock">En Stock</option>
          <option value="low-stock">Stock Bajo</option>
          <option value="out-stock">Sin Stock</option>
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

    <!-- Tabla de productos -->
    <AdminTable
      title="Lista de Productos"
      description="Gestiona todos los productos del inventario"
      :columns="tableColumns"
      :data="paginatedProducts"
      :loading="loading"
      :selected="selectedProducts"
      @update:selected="selectedProducts = $event"
      :selectable="true"
    >
      <!-- Producto -->
      <template #cell-producto="{ item }">
        <div class="servicio-info">
          <div class="servicio-image">
            <img 
              :src="item.imagen || item.image || getDefaultProductImage(item.categoria || item.category)" 
              :alt="item.nombre || item.name"
              class="service-img"
            />
          </div>
          <div class="servicio-details">
            <div class="servicio-nombre">{{ item.nombre || item.name }}</div>
            <div class="servicio-descripcion">{{ item.codigo || item.code || 'Sin código' }}</div>
          </div>
        </div>
      </template>

      <!-- Categoría -->
      <template #cell-categoria="{ item }">
        <span :class="getCategoryBadgeClass((item.categoria || item.category) || 'default')" class="categoria-badge">
          {{ getCategoryLabel(item.categoria || item.category) }}
        </span>
      </template>

      <!-- Stock -->
      <template #cell-stock="{ item }">
        <div class="stock-info">
          <div class="stock-value" :class="getStockClass(item.stockActual || item.stock, item.stockMinimo || item.minStock)">
            {{ item.stockActual || item.stock || 0 }}
          </div>
          <div class="stock-min">Min: {{ item.stockMinimo || item.minStock || 0 }}</div>
        </div>
      </template>

      <!-- Precio -->
      <template #cell-precio="{ item }">
        <div class="precio-info">
          <div class="precio-value">Bs {{ formatPrice(item.precioVenta || item.price || 0) }}</div>
        </div>
      </template>

      <!-- Estado -->
      <template #cell-estado="{ item }">
        <div class="status-badge" :class="getStatusClass(item.estado || item.status)">
          <div class="status-dot"></div>
          <span>{{ getStatusLabel(item.estado || item.status) }}</span>
        </div>
      </template>

      <!-- Acciones -->
      <template #actions="{ item }">
        <div class="action-buttons">
          <button @click="editProduct(item)" class="action-btn action-edit">
            Editar
          </button>
          <button 
            @click="toggleProductStatus(item)" 
            class="action-btn"
            :class="getStatusClass(item.estado || item.status) === 'status-active' ? 'action-deactivate' : 'action-activate'"
          >
            {{ getStatusLabel(item.estado || item.status) === 'Activo' ? 'Desactivar' : 'Activar' }}
          </button>
        </div>
      </template>
    </AdminTable>

    <!-- Paginación -->
    <div class="pagination-container">
      <div class="pagination-info">
        Mostrando {{ startItem }} a {{ endItem }} de {{ totalProducts }} productos
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
    <div v-if="selectedProducts.length > 0" class="bulk-actions-container">
      <div class="bulk-actions-info">
        {{ selectedProducts.length }} producto(s) seleccionado(s)
      </div>
      <div class="bulk-actions">
        <button @click="bulkActivate" class="bulk-btn bulk-activate">
          Activar Seleccionados
        </button>
        <button @click="bulkDeactivate" class="bulk-btn bulk-deactivate">
          Desactivar Seleccionados
        </button>
        <button @click="bulkUpdateStock" class="bulk-btn bulk-role">
          Actualizar Stock
        </button>
      </div>
    </div>

    <!-- Modal de producto -->
    <AdminModal
      :show="showProductModal"
      @close="closeProductModal"
      :title="editingProduct ? 'Editar Producto' : 'Nuevo Producto'"
      size="md"
    >
      <form @submit.prevent="saveProduct" class="space-y-4">
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Nombre *</label>
            <input
              v-model="productForm.name"
              type="text"
              required
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
              placeholder="Shampoo Premium"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Código</label>
            <input
              v-model="productForm.code"
              type="text"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
              placeholder="SH001"
            />
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Categoría *</label>
          <select
            v-model="productForm.category"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
          >
            <option value="">Seleccionar categoría</option>
            <option value="cuidado-capilar">Cuidado Capilar</option>
            <option value="styling">Styling</option>
            <option value="cuidado-facial">Cuidado Facial</option>
            <option value="herramientas">Herramientas</option>
            <option value="accesorios">Accesorios</option>
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
                v-model="productForm.price"
                type="number"
                required
                min="0"
                step="0.01"
                class="w-full pl-8 pr-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
                placeholder="120.00"
              />
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Stock Actual *</label>
            <input
              v-model="productForm.stock"
              type="number"
              required
              min="0"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
              placeholder="50"
            />
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Stock Mínimo</label>
          <input
            v-model="productForm.minStock"
            type="number"
            min="0"
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
            placeholder="5"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Estado</label>
          <select
            v-model="productForm.status"
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-1 focus:ring-black focus:border-black text-sm"
          >
            <option value="active">Activo</option>
            <option value="inactive">Inactivo</option>
          </select>
        </div>

        <div class="flex justify-end gap-3 pt-4 border-t">
          <button
            type="button"
            @click="closeProductModal"
            class="btn-secondary"
          >
            Cancelar
          </button>
          <button
            type="submit"
            :disabled="saving"
            class="btn-primary"
          >
            {{ saving ? 'Guardando...' : (editingProduct ? 'Actualizar' : 'Crear') }}
          </button>
        </div>
      </form>
    </AdminModal>
  </div>
</template>

<script>
import { ref, reactive, computed, onMounted } from 'vue'
import AdminTable from '@/components/admin/AdminTable.vue'
import AdminModal from '@/components/admin/AdminModal.vue'
import { productService } from '@/services/productService.js'

export default {
  name: 'AdminProductos',
  components: {
    AdminTable,
    AdminModal
  },
  setup() {
    // Estado principal
    const loading = ref(false)
    const saving = ref(false)
    const products = ref([])
    const stats = ref({
      totalProducts: 0,
      inStock: 0,
      lowStock: 0,
      totalValue: 0
    })

    // Filtros y paginación
    const filters = reactive({
      category: '',
      stock: '',
      status: ''
    })

    const currentPage = ref(1)
    const pageSize = ref(10)

    // Modal y formulario
    const showProductModal = ref(false)
    const editingProduct = ref(null)
    const selectedProducts = ref([])

    const productForm = reactive({
      name: '',
      code: '',
      category: '',
      price: '',
      stock: '',
      minStock: '',
      status: 'active'
    })

    // Configuración de tabla
    const tableColumns = [
      { key: 'producto', label: 'Producto', sortable: true },
      { key: 'categoria', label: 'Categoría', sortable: true },
      { key: 'stock', label: 'Stock', sortable: true },
      { key: 'precio', label: 'Precio', sortable: true },
      { key: 'estado', label: 'Estado', sortable: true }
    ]

    // Computed
    const filteredProducts = computed(() => {
      let filtered = products.value

      if (filters.category) {
        filtered = filtered.filter(p => (p.categoria || p.category) === filters.category)
      }

      if (filters.stock) {
        if (filters.stock === 'in-stock') {
          filtered = filtered.filter(p => {
            const stock = p.stockActual || p.stock || 0
            const minStock = p.stockMinimo || p.minStock || 0
            return stock > minStock
          })
        } else if (filters.stock === 'low-stock') {
          filtered = filtered.filter(p => {
            const stock = p.stockActual || p.stock || 0
            const minStock = p.stockMinimo || p.minStock || 0
            return stock <= minStock && stock > 0
          })
        } else if (filters.stock === 'out-stock') {
          filtered = filtered.filter(p => (p.stockActual || p.stock || 0) === 0)
        }
      }

      if (filters.status) {
        const statusFilter = filters.status === 'active' ? 'activo' : 'inactivo'
        filtered = filtered.filter(p => {
          const status = p.estado || p.status
          return status === statusFilter || status === filters.status
        })
      }

      return filtered
    })

    const paginatedProducts = computed(() => {
      const start = (currentPage.value - 1) * pageSize.value
      const end = start + pageSize.value
      return filteredProducts.value.slice(start, end)
    })

    const totalProducts = computed(() => filteredProducts.value.length)
    const totalPages = computed(() => Math.ceil(totalProducts.value / pageSize.value))
    const startItem = computed(() => (currentPage.value - 1) * pageSize.value + 1)
    const endItem = computed(() => Math.min(currentPage.value * pageSize.value, totalProducts.value))

    // Métodos de utilidad
    const formatPrice = (price) => {
      return new Intl.NumberFormat('es-BO', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      }).format(price || 0)
    }

    const getCategoryLabel = (category) => {
      const labels = {
        'cuidado-capilar': 'Cuidado Capilar',
        'Cuidado Capilar': 'Cuidado Capilar',
        'styling': 'Styling',
        'Styling': 'Styling',
        'cuidado-facial': 'Cuidado Facial',
        'Cuidado Facial': 'Cuidado Facial',
        'herramientas': 'Herramientas',
        'Herramientas': 'Herramientas',
        'accesorios': 'Accesorios',
        'Accesorios': 'Accesorios',
        'General': 'General'
      }
      return labels[category] || category || 'Sin categoría'
    }

    const getCategoryBadgeClass = (category) => {
      const classes = {
        'cuidado-capilar': 'badge-blue',
        'Cuidado Capilar': 'badge-blue',
        'styling': 'badge-purple',
        'Styling': 'badge-purple',
        'cuidado-facial': 'badge-green',
        'Cuidado Facial': 'badge-green',
        'herramientas': 'badge-orange',
        'Herramientas': 'badge-orange',
        'accesorios': 'badge-indigo',
        'Accesorios': 'badge-indigo',
        'General': 'badge-gray',
        'default': 'badge-gray'
      }
      return classes[category] || classes.default
    }

    const getStockClass = (stock, minStock) => {
      const currentStock = stock || 0
      const minimumStock = minStock || 5
      if (currentStock <= 0) return 'stock-out'
      if (currentStock <= minimumStock) return 'stock-low'
      return 'stock-good'
    }

    const getStatusClass = (status) => {
      const normalizedStatus = status === 'activo' || status === 'active' ? 'active' : 'inactive'
      return normalizedStatus === 'active' ? 'status-active' : 'status-inactive'
    }

    const getStatusLabel = (status) => {
      const normalizedStatus = status === 'activo' || status === 'active' ? 'active' : 'inactive'
      return normalizedStatus === 'active' ? 'Activo' : 'Inactivo'
    }

    const getDefaultProductImage = (category) => {
      const images = {
        'cuidado-capilar': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=60&h=60&fit=crop',
        'styling': 'https://images.unsplash.com/photo-1522673607200-164d1b6ce486?w=60&h=60&fit=crop',
        'cuidado-facial': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=60&h=60&fit=crop',
        'herramientas': 'https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=60&h=60&fit=crop',
        'accesorios': 'https://images.unsplash.com/photo-1621605815971-fbc98d665033?w=60&h=60&fit=crop'
      }
      return images[category] || images['cuidado-capilar']
    }

    // Cargar datos
    const loadProducts = async () => {
      loading.value = true
      try {
        const result = await productService.getProductsAdmin()
        products.value = result.data || []
        calculateStats()
        console.log('Productos cargados:', products.value.length)
      } catch (error) {
        console.error('Error al cargar productos:', error)
        products.value = []
        // En caso de error, usar datos de fallback para mostrar al menos algo
        try {
          const fallbackData = productService.getFallbackProducts()
          products.value = fallbackData.data || []
          calculateStats()
          console.log('Usando datos de fallback:', products.value.length)
        } catch (fallbackError) {
          console.error('Error incluso con datos de fallback:', fallbackError)
        }
      } finally {
        loading.value = false
      }
    }

    const calculateStats = () => {
      const total = products.value.length
      const inStock = products.value.filter(p => (p.stockActual || p.stock || 0) > (p.stockMinimo || p.minStock || 0)).length
      const lowStock = products.value.filter(p => {
        const stock = p.stockActual || p.stock || 0
        const minStock = p.stockMinimo || p.minStock || 0
        return stock <= minStock && stock > 0
      }).length
      const totalValue = products.value.reduce((sum, p) => {
        const price = p.precioVenta || p.price || 0
        const stock = p.stockActual || p.stock || 0
        return sum + (price * stock)
      }, 0)

      stats.value = {
        totalProducts: total,
        inStock,
        lowStock,
        totalValue
      }
    }

    // Modal y formulario
    const openCreateModal = () => {
      editingProduct.value = null
      productForm.name = ''
      productForm.code = ''
      productForm.category = ''
      productForm.price = ''
      productForm.stock = ''
      productForm.minStock = ''
      productForm.status = 'active'
      showProductModal.value = true
    }

    const editProduct = (product) => {
      editingProduct.value = product
      Object.assign(productForm, product)
      showProductModal.value = true
    }

    const closeProductModal = () => {
      showProductModal.value = false
      editingProduct.value = null
    }

    const saveProduct = async () => {
      saving.value = true
      try {
        if (editingProduct.value) {
          const updatedProduct = await productService.update(editingProduct.value.id, productForm)
          const index = products.value.findIndex(p => p.id === editingProduct.value.id)
          if (index !== -1) {
            products.value[index] = updatedProduct
          }
        } else {
          const newProduct = await productService.create(productForm)
          products.value.unshift(newProduct)
        }
        
        calculateStats()
        closeProductModal()
      } catch (error) {
        console.error('Error al guardar producto:', error)
      } finally {
        saving.value = false
      }
    }

    const toggleProductStatus = async (product) => {
      const currentStatus = product.estado || product.status
      const newStatus = (currentStatus === 'activo' || currentStatus === 'active') ? 'inactivo' : 'activo'
      const index = products.value.findIndex(p => p.id === product.id)
      if (index !== -1) {
        if (products.value[index].estado !== undefined) {
          products.value[index].estado = newStatus
        } else {
          products.value[index].status = newStatus === 'activo' ? 'active' : 'inactive'
        }
        calculateStats()
      }
    }

    // Filtros
    const applyFilters = () => {
      currentPage.value = 1
    }

    const clearFilters = () => {
      Object.assign(filters, {
        category: '',
        stock: '',
        status: ''
      })
      currentPage.value = 1
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

    // Acciones masivas
    const bulkActivate = () => {
      selectedProducts.value.forEach(productId => {
        const index = products.value.findIndex(p => p.id === productId)
        if (index !== -1) {
          products.value[index].status = 'active'
        }
      })
      selectedProducts.value = []
      calculateStats()
    }

    const bulkDeactivate = () => {
      selectedProducts.value.forEach(productId => {
        const index = products.value.findIndex(p => p.id === productId)
        if (index !== -1) {
          products.value[index].status = 'inactive'
        }
      })
      selectedProducts.value = []
      calculateStats()
    }

    const bulkUpdateStock = () => {
      const newStock = prompt('Ingrese el nuevo stock:')
      if (newStock !== null && !isNaN(newStock)) {
        selectedProducts.value.forEach(productId => {
          const index = products.value.findIndex(p => p.id === productId)
          if (index !== -1) {
            products.value[index].stock = parseInt(newStock)
          }
        })
        selectedProducts.value = []
        calculateStats()
      }
    }

    // Inicialización
    onMounted(() => {
      loadProducts()
    })

    return {
      // Estado
      loading,
      saving,
      products,
      stats,
      
      // Filtros y paginación
      filters,
      currentPage,
      pageSize,
      
      // Modal y formulario
      showProductModal,
      editingProduct,
      selectedProducts,
      productForm,
      
      // Configuración
      tableColumns,
      
      // Computed
      filteredProducts,
      paginatedProducts,
      totalProducts,
      totalPages,
      startItem,
      endItem,
      
      // Métodos
      formatPrice,
      getCategoryLabel,
      getCategoryBadgeClass,
      getStockClass,
      getStatusClass,
      getStatusLabel,
      getDefaultProductImage,
      openCreateModal,
      editProduct,
      closeProductModal,
      saveProduct,
      toggleProductStatus,
      applyFilters,
      clearFilters,
      nextPage,
      previousPage,
      bulkActivate,
      bulkDeactivate,
      bulkUpdateStock
    }
  }
}
</script>

<style scoped>
/* Contenedor principal */
.admin-productos {
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
  opacity: 0.6;
}

.stat-success .stat-number { color: #10b981; }
.stat-success .stat-icon { color: #10b981; }

.stat-warning .stat-number { color: #f59e0b; }
.stat-warning .stat-icon { color: #f59e0b; }

.stat-purple .stat-number { color: #8b5cf6; }
.stat-purple .stat-icon { color: #8b5cf6; }

/* Filtros compactos */
.filters-container-compact {
  background: white;
  border-radius: 0.75rem;
  padding: 1rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
  border: 1px solid #e5e7eb;
}

.filters-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.filter-select-compact {
  padding: 0.5rem 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 0.875rem;
  background: white;
  color: #374151;
  min-width: 150px;
  transition: all 0.2s ease;
}

.filter-select-compact:focus {
  outline: none;
  border-color: #000;
  box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.1);
}

.filter-clear-btn-compact {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  background: #f3f4f6;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 0.875rem;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-clear-btn-compact:hover {
  background: #e5e7eb;
  color: #374151;
}

/* Tabla - Productos */
.servicio-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  min-width: 200px;
}

.servicio-image {
  width: 48px;
  height: 48px;
  border-radius: 8px;
  overflow: hidden;
  flex-shrink: 0;
}

.service-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.servicio-details {
  flex: 1;
}

.servicio-nombre {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.875rem;
  line-height: 1.2;
}

.servicio-descripcion {
  color: #6b7280;
  font-size: 0.75rem;
  font-family: monospace;
  margin-top: 0.25rem;
}

/* Categorías */
.categoria-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.badge-blue { background: #dbeafe; color: #1d4ed8; }
.badge-purple { background: #ede9fe; color: #7c3aed; }
.badge-green { background: #dcfce7; color: #16a34a; }
.badge-orange { background: #fed7aa; color: #ea580c; }
.badge-indigo { background: #e0e7ff; color: #4338ca; }
.badge-gray { background: #f3f4f6; color: #6b7280; }

/* Stock */
.stock-info {
  text-align: center;
  min-width: 80px;
}

.stock-value {
  font-weight: 700;
  font-size: 1rem;
  line-height: 1;
}

.stock-good { color: #10b981; }
.stock-low { color: #f59e0b; }
.stock-out { color: #dc2626; }

.stock-min {
  color: #6b7280;
  font-size: 0.75rem;
  margin-top: 0.25rem;
}

/* Precio */
.precio-info {
  text-align: right;
  min-width: 100px;
}

.precio-value {
  font-weight: 700;
  color: #1f2937;
  font-size: 0.875rem;
}

/* Estado */
.status-badge {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.375rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  min-width: 80px;
  justify-content: center;
}

.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
}

.status-active {
  background: #dcfce7;
  color: #16a34a;
}

.status-active .status-dot {
  background: #16a34a;
}

.status-inactive {
  background: #fef2f2;
  color: #dc2626;
}

.status-inactive .status-dot {
  background: #dc2626;
}

/* Acciones */
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

/* Botones principales */
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

.btn-primary:hover:not(:disabled) {
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

/* Utilidades de Tailwind */
.w-4 { width: 1rem; }
.h-4 { height: 1rem; }
.w-3 { width: 0.75rem; }
.h-3 { height: 0.75rem; }
.w-6 { width: 1.5rem; }
.h-6 { height: 1.5rem; }

.space-y-4 > * + * { margin-top: 1rem; }
.grid { display: grid; }
.grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
.gap-4 { gap: 1rem; }
.gap-3 { gap: 0.75rem; }

.text-sm { font-size: 0.875rem; }
.font-medium { font-weight: 500; }
.text-gray-700 { color: #374151; }
.text-gray-500 { color: #6b7280; }
.mb-1 { margin-bottom: 0.25rem; }
.pt-4 { padding-top: 1rem; }

.block { display: block; }
.flex { display: flex; }
.items-center { align-items: center; }
.justify-end { justify-content: flex-end; }
.relative { position: relative; }
.absolute { position: absolute; }
.inset-y-0 { top: 0; bottom: 0; }
.left-0 { left: 0; }
.pl-3 { padding-left: 0.75rem; }
.pl-8 { padding-left: 2rem; }
.pr-3 { padding-right: 0.75rem; }
.pointer-events-none { pointer-events: none; }

.w-full { width: 100%; }
.px-3 { padding-left: 0.75rem; padding-right: 0.75rem; }
.py-2 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
.border { border-width: 1px; }
.border-t { border-top-width: 1px; }
.border-gray-300 { border-color: #d1d5db; }
.rounded-lg { border-radius: 0.5rem; }

.focus\:ring-1:focus { box-shadow: 0 0 0 1px; }
.focus\:ring-black:focus { box-shadow: 0 0 0 1px #000000; }
.focus\:border-black:focus { border-color: #000000; }

/* Responsive */
@media (max-width: 768px) {
  .admin-productos {
    padding: 1rem;
  }

  .admin-header {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .filters-row {
    flex-direction: column;
    align-items: stretch;
  }

  .filter-select-compact {
    min-width: 100%;
  }

  .bulk-actions-container {
    left: 1rem;
    right: 1rem;
    transform: none;
    padding: 1rem;
  }

  .bulk-actions {
    flex-direction: column;
    gap: 0.5rem;
  }

  .bulk-btn {
    width: 100%;
    text-align: center;
  }
}
</style>
