<!--
  AdminTable.vue - Componente de tabla reutilizable con filtros, búsqueda y paginación
  Usado en todas las secciones administrativas para mostrar datos
-->
<template>
  <div class="admin-table bg-white rounded-lg shadow-sm border border-gray-200">
    <!-- Header de la tabla -->
    <div class="px-6 py-3 border-b border-gray-200">
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
        <!-- Título y descripción -->
        <div>
          <h3 class="text-lg font-medium text-gray-900">{{ title }}</h3>
          <p v-if="description" class="mt-1 text-sm text-gray-600">{{ description }}</p>
        </div>

        <!-- Acciones principales -->
        <div class="flex items-center space-x-3">
          <slot name="header-actions"></slot>
        </div>
      </div>

      <!-- Filtros y búsqueda -->
      <div class="mt-3 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
        <!-- Búsqueda -->
        <div class="relative max-w-sm">
          <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <svg class="h-4 w-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </div>
          <input
            v-model="searchQuery"
            type="text"
            :placeholder="searchPlaceholder"
            class="block w-full pl-9 pr-3 py-1.5 border border-gray-300 rounded-md leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-1 focus:ring-blue-500 focus:border-blue-500 text-sm"
          />
        </div>

        <!-- Filtros -->
        <div class="flex items-center space-x-3">
          <slot name="filters"></slot>
          
          <!-- Filtro rápido de estado si está disponible -->
          <select
            v-if="statusFilter"
            v-model="selectedStatus"
            class="block px-3 py-1.5 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500"
          >
            <option value="">Todos los estados</option>
            <option v-for="status in statusOptions" :key="status.value" :value="status.value">
              {{ status.label }}
            </option>
          </select>

          <!-- Selector de elementos por página -->
          <select
            v-if="!hidePageSize"
            v-model="itemsPerPage"
            class="block px-3 py-1.5 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500"
          >
            <option :value="10">10</option>
            <option :value="25">25</option>
            <option :value="50">50</option>
            <option :value="100">100</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Contenido de la tabla -->
    <div class="overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-200">
        <!-- Header de columnas -->
        <thead class="bg-gray-50">
          <tr>
            <!-- Checkbox para seleccionar todos -->
            <th v-if="selectable" scope="col" class="relative px-6 py-3 text-left">
              <input
                type="checkbox"
                :checked="allSelected"
                @change="toggleSelectAll"
                class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
              />
            </th>
            
            <!-- Columnas dinámicas -->
            <th
              v-for="column in columns"
              :key="column.key"
              scope="col"
              :class="[
                'px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider',
                column.sortable ? 'cursor-pointer hover:bg-gray-100' : ''
              ]"
              @click="column.sortable ? toggleSort(column.key) : null"
            >
              <div class="flex items-center space-x-1">
                <span>{{ column.label }}</span>
                <svg
                  v-if="column.sortable && sortKey === column.key"
                  :class="sortOrder === 'asc' ? 'transform rotate-180' : ''"
                  class="w-4 h-4 text-gray-400"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
              </div>
            </th>
            
            <!-- Columna de acciones -->
            <th v-if="$slots.actions || actionsColumn" scope="col" class="relative px-6 py-3">
              <span class="sr-only">Acciones</span>
            </th>
          </tr>
        </thead>

        <!-- Cuerpo de la tabla -->
        <tbody class="bg-white divide-y divide-gray-200">
          <!-- Estado de carga -->
          <tr v-if="loading">
            <td :colspan="totalColumns" class="px-6 py-12 text-center">
              <div class="flex justify-center items-center">
                <svg class="animate-spin h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span class="ml-2 text-gray-600">Cargando...</span>
              </div>
            </td>
          </tr>

          <!-- Sin datos -->
          <tr v-else-if="!paginatedData.length">
            <td :colspan="totalColumns" class="px-6 py-12 text-center">
              <div class="text-gray-500">
                <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                <h3 class="mt-2 text-sm font-medium text-gray-900">No hay datos</h3>
                <p class="mt-1 text-sm text-gray-500">{{ emptyMessage }}</p>
              </div>
            </td>
          </tr>

          <!-- Filas de datos -->
          <tr v-else v-for="(item, index) in paginatedData" :key="getRowKey(item, index)" class="hover:bg-gray-50">
            <!-- Checkbox de selección -->
            <td v-if="selectable" class="px-6 py-4 whitespace-nowrap">
              <input
                type="checkbox"
                :checked="isSelected(item)"
                @change="toggleSelect(item)"
                class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
              />
            </td>

            <!-- Celdas de datos -->
            <td
              v-for="column in columns"
              :key="column.key"
              class="px-6 py-4 whitespace-nowrap text-sm"
              :class="column.class || 'text-gray-900'"
            >
              <slot
                :name="`cell-${column.key}`"
                :item="item"
                :value="getNestedValue(item, column.key)"
                :column="column"
              >
                {{ formatCellValue(item, column) }}
              </slot>
            </td>

            <!-- Celda de acciones -->
            <td v-if="$slots.actions || actionsColumn" class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <slot name="actions" :item="item" :index="index"></slot>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Paginación -->
    <div v-if="!loading && totalPages > 1" class="bg-white px-6 py-3 border-t border-gray-200 flex items-center justify-between">
      <div class="flex-1 flex justify-between items-center">
        <p class="text-sm text-gray-700">
          Mostrando
          <span class="font-medium">{{ startItem }}</span>
          a
          <span class="font-medium">{{ endItem }}</span>
          de
          <span class="font-medium">{{ totalItems }}</span>
          resultados
        </p>

        <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
          <!-- Botón anterior -->
          <button
            @click="goToPage(currentPage - 1)"
            :disabled="currentPage === 1"
            class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
          </button>

          <!-- Números de página -->
          <button
            v-for="page in visiblePages"
            :key="page"
            @click="goToPage(page)"
            :class="[
              page === currentPage
                ? 'z-10 bg-blue-50 border-blue-500 text-blue-600'
                : 'bg-white border-gray-300 text-gray-500 hover:bg-gray-50',
              'relative inline-flex items-center px-4 py-2 border text-sm font-medium'
            ]"
          >
            {{ page }}
          </button>

          <!-- Botón siguiente -->
          <button
            @click="goToPage(currentPage + 1)"
            :disabled="currentPage === totalPages"
            class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
            </svg>
          </button>
        </nav>
      </div>
    </div>

    <!-- Acciones masivas -->
    <div v-if="selectedItems.length > 0" class="bg-blue-50 px-6 py-3 border-t border-blue-200">
      <div class="flex items-center justify-between">
        <span class="text-sm font-medium text-blue-900">
          {{ selectedItems.length }} elemento{{ selectedItems.length !== 1 ? 's' : '' }} seleccionado{{ selectedItems.length !== 1 ? 's' : '' }}
        </span>
        <div class="flex items-center space-x-2">
          <slot name="bulk-actions" :selectedItems="selectedItems"></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue'

export default {
  name: 'AdminTable',
  props: {
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      default: ''
    },
    data: {
      type: Array,
      default: () => []
    },
    columns: {
      type: Array,
      required: true
    },
    loading: {
      type: Boolean,
      default: false
    },
    searchPlaceholder: {
      type: String,
      default: 'Buscar...'
    },
    emptyMessage: {
      type: String,
      default: 'No se encontraron registros'
    },
    selectable: {
      type: Boolean,
      default: false
    },
    actionsColumn: {
      type: Boolean,
      default: true
    },
    statusFilter: {
      type: Boolean,
      default: false
    },
    statusOptions: {
      type: Array,
      default: () => []
    },
    hidePageSize: {
      type: Boolean,
      default: false
    },
    rowKey: {
      type: String,
      default: 'id'
    }
  },
  emits: ['update:selected', 'sort-change'],
  setup(props, { emit }) {
    // Estado reactivo
    const searchQuery = ref('')
    const selectedStatus = ref('')
    const sortKey = ref('')
    const sortOrder = ref('asc')
    const currentPage = ref(1)
    const itemsPerPage = ref(25)
    const selectedItems = ref([])

    // Datos filtrados
    const filteredData = computed(() => {
      let filtered = [...props.data]

      // Filtro de búsqueda
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(item => {
          return props.columns.some(column => {
            const value = getNestedValue(item, column.key)
            return value && value.toString().toLowerCase().includes(query)
          })
        })
      }

      // Filtro de estado
      if (selectedStatus.value && props.statusFilter) {
        filtered = filtered.filter(item => item.estado === selectedStatus.value)
      }

      return filtered
    })

    // Datos ordenados
    const sortedData = computed(() => {
      if (!sortKey.value) return filteredData.value

      return [...filteredData.value].sort((a, b) => {
        const aVal = getNestedValue(a, sortKey.value)
        const bVal = getNestedValue(b, sortKey.value)

        let result = 0
        if (aVal < bVal) result = -1
        else if (aVal > bVal) result = 1

        return sortOrder.value === 'desc' ? -result : result
      })
    })

    // Paginación
    const totalItems = computed(() => sortedData.value.length)
    const totalPages = computed(() => Math.ceil(totalItems.value / itemsPerPage.value))
    const totalColumns = computed(() => {
      let count = props.columns.length
      if (props.selectable) count++
      if (props.actionsColumn) count++
      return count
    })

    const startItem = computed(() => {
      return Math.min((currentPage.value - 1) * itemsPerPage.value + 1, totalItems.value)
    })

    const endItem = computed(() => {
      return Math.min(currentPage.value * itemsPerPage.value, totalItems.value)
    })

    const paginatedData = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage.value
      const end = start + itemsPerPage.value
      return sortedData.value.slice(start, end)
    })

    const visiblePages = computed(() => {
      const delta = 2
      const range = []
      const rangeWithDots = []

      for (let i = Math.max(2, currentPage.value - delta); 
           i <= Math.min(totalPages.value - 1, currentPage.value + delta); 
           i++) {
        range.push(i)
      }

      if (currentPage.value - delta > 2) {
        rangeWithDots.push(1, '...')
      } else {
        rangeWithDots.push(1)
      }

      rangeWithDots.push(...range)

      if (currentPage.value + delta < totalPages.value - 1) {
        rangeWithDots.push('...', totalPages.value)
      } else {
        rangeWithDots.push(totalPages.value)
      }

      return rangeWithDots.filter((item, index, array) => array.indexOf(item) === index)
    })

    // Selección
    const allSelected = computed(() => {
      return paginatedData.value.length > 0 && 
             paginatedData.value.every(item => isSelected(item))
    })

    // Métodos
    const getNestedValue = (obj, path) => {
      return path.split('.').reduce((current, key) => current?.[key], obj)
    }

    const getRowKey = (item, index) => {
      return getNestedValue(item, props.rowKey) || index
    }

    const formatCellValue = (item, column) => {
      const value = getNestedValue(item, column.key)
      
      if (value === null || value === undefined) return '--'
      
      if (column.format === 'currency') {
        return new Intl.NumberFormat('es-ES', {
          style: 'currency',
          currency: 'EUR'
        }).format(value)
      }
      
      if (column.format === 'date') {
        return new Date(value).toLocaleDateString('es-ES')
      }
      
      if (column.format === 'datetime') {
        return new Date(value).toLocaleString('es-ES')
      }
      
      return value
    }

    const toggleSort = (key) => {
      if (sortKey.value === key) {
        sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
      } else {
        sortKey.value = key
        sortOrder.value = 'asc'
      }
      
      emit('sort-change', { key: sortKey.value, order: sortOrder.value })
    }

    const goToPage = (page) => {
      if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page
      }
    }

    const isSelected = (item) => {
      const key = getRowKey(item)
      return selectedItems.value.some(selected => getRowKey(selected) === key)
    }

    const toggleSelect = (item) => {
      const key = getRowKey(item)
      const index = selectedItems.value.findIndex(selected => getRowKey(selected) === key)
      
      if (index > -1) {
        selectedItems.value.splice(index, 1)
      } else {
        selectedItems.value.push(item)
      }
    }

    const toggleSelectAll = () => {
      if (allSelected.value) {
        // Deseleccionar todos los elementos visibles
        paginatedData.value.forEach(item => {
          const key = getRowKey(item)
          const index = selectedItems.value.findIndex(selected => getRowKey(selected) === key)
          if (index > -1) {
            selectedItems.value.splice(index, 1)
          }
        })
      } else {
        // Seleccionar todos los elementos visibles
        paginatedData.value.forEach(item => {
          if (!isSelected(item)) {
            selectedItems.value.push(item)
          }
        })
      }
    }

    // Watchers
    watch(selectedItems, (newVal) => {
      emit('update:selected', newVal)
    }, { deep: true })

    watch(searchQuery, () => {
      currentPage.value = 1
    })

    watch(selectedStatus, () => {
      currentPage.value = 1
    })

    watch(itemsPerPage, () => {
      currentPage.value = 1
    })

    return {
      searchQuery,
      selectedStatus,
      sortKey,
      sortOrder,
      currentPage,
      itemsPerPage,
      selectedItems,
      filteredData,
      sortedData,
      totalItems,
      totalPages,
      totalColumns,
      startItem,
      endItem,
      paginatedData,
      visiblePages,
      allSelected,
      getNestedValue,
      getRowKey,
      formatCellValue,
      toggleSort,
      goToPage,
      isSelected,
      toggleSelect,
      toggleSelectAll
    }
  }
}
</script>

<style scoped>
.admin-table {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}
</style>
