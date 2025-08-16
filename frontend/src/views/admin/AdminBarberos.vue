<!--
  AdminBarberos.vue - Gestión completa de barberos
  FASE 8.3: Rediseño minimalista y moderno
-->
<template>
  <div class="admin-barberos">
    <!-- Header con acciones -->
    <div class="admin-header">
      <div>
        <h1 class="admin-title">
          Gestión de Barberos
        </h1>
        <p class="admin-subtitle">Administra el equipo de barberos y sus horarios</p>
      </div>
      
      <div class="header-actions">
        <button
          @click="loadBarbers"
          class="btn-secondary"
        >
          Actualizar
        </button>
        <button
          @click="openCreateModal"
          class="btn-primary"
        >
          Nuevo Barbero
        </button>
      </div>
    </div>

    <!-- Estadísticas rápidas -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-content">
          <div class="stat-number">{{ stats.total || 0 }}</div>
          <div class="stat-label">Total Barberos</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-success">
        <div class="stat-content">
          <div class="stat-number">{{ stats.activos || 0 }}</div>
          <div class="stat-label">Activos</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-info">
        <div class="stat-content">
          <div class="stat-number">{{ stats.disponibles_hoy || 0 }}</div>
          <div class="stat-label">Disponibles Hoy</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/>
            <path d="M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"/>
          </svg>
        </div>
      </div>

      <div class="stat-card stat-purple">
        <div class="stat-content">
          <div class="stat-number">{{ stats.promedio_reservas || 0 }}</div>
          <div class="stat-label">Promedio Reservas</div>
        </div>
        <div class="stat-icon">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z"/>
          </svg>
        </div>
      </div>
    </div>

    <!-- Tabla de barberos -->
    <AdminTable
      title="Lista de Barberos"
      description="Gestiona todos los barberos del sistema"
      :data="filteredBarbers"
      :columns="tableColumns"
      :loading="loadingBarbers"
      :selectable="true"
      searchPlaceholder="Buscar por nombre o especialidad..."
      emptyMessage="No se encontraron barberos"
      @update:selected="selectedBarbers = $event"
    >
      <!-- Filtros personalizados -->
      <template #filters>
        <div class="filters-container">
          <select
            v-model="statusFilter"
            class="filter-select"
          >
            <option value="">Todos los estados</option>
            <option value="true">Disponibles</option>
            <option value="false">No Disponibles</option>
          </select>
          
          <select
            v-model="especialidadFilter"
            class="filter-select"
          >
            <option value="">Todas las especialidades</option>
            <option value="Especialista en cortes modernos">Cortes Modernos</option>
            <option value="Barba y Bigote">Barba y Bigote</option>
            <option value="Tratamientos">Tratamientos</option>
            <option value="Cortes Clásicos">Cortes Clásicos</option>
          </select>
        </div>
      </template>

      <!-- Celda personalizada para avatar y nombre -->
      <template #cell-nombre="{ item }">
        <div class="barbero-info">
          <div class="barbero-avatar">
            <img
              v-if="item.avatar"
              :src="item.avatar"
              :alt="item.nombre"
              class="avatar-img"
            />
            <div
              v-else
              class="avatar-placeholder"
            >
              {{ getInitials(item.nombre) }}
            </div>
          </div>
          <div class="barbero-details">
            <div class="barbero-nombre">{{ item.nombre }}</div>
            <div class="barbero-email">{{ item.email }}</div>
          </div>
        </div>
      </template>

      <!-- Celda personalizada para especialidad -->
      <template #cell-especialidad="{ item }">
        <span class="especialidad-badge">
          {{ item.especialidad }}
        </span>
      </template>

      <!-- Celda personalizada para estado -->
      <template #cell-disponible="{ item }">
        <span :class="['status-badge', item.disponible ? 'status-available' : 'status-unavailable']">
          <div class="status-dot"></div>
          {{ item.disponible ? 'Disponible' : 'No Disponible' }}
        </span>
      </template>

      <!-- Celda personalizada para horario -->
      <template #cell-horario="{ item }">
        <div class="horario-info">
          <div class="horario-time">
            {{ item.horario_inicio || '09:00' }} - {{ item.horario_fin || '18:00' }}
          </div>
          <div class="horario-days">
            {{ getWorkingDays(item.dias_trabajo) }}
          </div>
        </div>
      </template>

      <!-- Acciones por fila -->
      <template #actions="{ item }">
        <div class="action-buttons">
          <button
            @click="editBarber(item)"
            class="action-btn action-edit"
            title="Editar barbero"
          >
            Editar
          </button>
          
          <button
            @click="manageSchedule(item)"
            class="action-btn action-schedule"
            title="Gestionar horarios"
          >
            Horarios
          </button>
        </div>
      </template>

      <!-- Acciones masivas -->
      <template #bulk-actions="{ selectedItems }">
        <div class="bulk-actions">
          <button
            @click="bulkActivate(selectedItems)"
            class="bulk-btn bulk-activate"
          >
            Activar ({{ selectedItems.length }})
          </button>
          
          <button
            @click="bulkDeactivate(selectedItems)"
            class="bulk-btn bulk-deactivate"
          >
            Desactivar ({{ selectedItems.length }})
          </button>
        </div>
      </template>
    </AdminTable>

    <!-- Modal para crear/editar barbero -->
    <AdminModal
      :show="showBarberModal"
      :title="isEditing ? 'Editar Barbero' : 'Nuevo Barbero'"
      :description="isEditing ? 'Modifica los datos del barbero' : 'Crea un nuevo barbero en el sistema'"
      size="lg"
      :loading="savingBarber"
      :saveDisabled="!isBarberFormValid"
      @close="closeBarberModal"
      @save="saveBarber"
      showActions
    >
      <form @submit.prevent="saveBarber" class="space-y-6">
        <!-- Información básica -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label for="nombre" class="block text-sm font-medium text-gray-700 mb-2">
              Nombre completo *
            </label>
            <input
              id="nombre"
              v-model="barberForm.nombre"
              type="text"
              required
              class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              placeholder="Ej: Juan Pérez"
            />
          </div>

          <div>
            <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
              Email *
            </label>
            <input
              id="email"
              v-model="barberForm.email"
              type="email"
              required
              class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              placeholder="juan@ejemplo.com"
            />
          </div>

          <div>
            <label for="telefono" class="block text-sm font-medium text-gray-700 mb-2">
              Teléfono
            </label>
            <input
              id="telefono"
              v-model="barberForm.telefono"
              type="tel"
              class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              placeholder="+34 123 456 789"
            />
          </div>

          <div>
            <label for="especialidad" class="block text-sm font-medium text-gray-700 mb-2">
              Especialidad *
            </label>
            <select
              id="especialidad"
              v-model="barberForm.especialidad"
              required
              class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="">Seleccionar especialidad</option>
              <option value="Cortes Clásicos">Cortes Clásicos</option>
              <option value="Barba y Bigote">Barba y Bigote</option>
              <option value="Tratamientos">Tratamientos</option>
              <option value="Cortes Modernos">Cortes Modernos</option>
              <option value="Estilismo">Estilismo</option>
            </select>
          </div>
        </div>

        <!-- Información adicional -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label for="experiencia" class="block text-sm font-medium text-gray-700 mb-2">
              Experiencia
            </label>
            <input
              id="experiencia"
              v-model="barberForm.experiencia"
              type="text"
              class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              placeholder="Ej: 5 años"
            />
          </div>

          <div>
            <label for="disponible" class="block text-sm font-medium text-gray-700 mb-2">
              Estado
            </label>
            <select
              id="disponible"
              v-model="barberForm.disponible"
              class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            >
              <option :value="true">Disponible</option>
              <option :value="false">No Disponible</option>
            </select>
          </div>
        </div>

        <!-- Horario de trabajo -->
        <div>
          <h3 class="text-lg font-medium text-gray-900 mb-4">Horario de Trabajo</h3>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-4">
            <div>
              <label for="horario_inicio" class="block text-sm font-medium text-gray-700 mb-2">
                Hora de inicio
              </label>
              <input
                id="horario_inicio"
                v-model="barberForm.horario_inicio"
                type="time"
                class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              />
            </div>

            <div>
              <label for="horario_fin" class="block text-sm font-medium text-gray-700 mb-2">
                Hora de fin
              </label>
              <input
                id="horario_fin"
                v-model="barberForm.horario_fin"
                type="time"
                class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
          </div>

          <!-- Días de trabajo -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Días de trabajo
            </label>
            <div class="grid grid-cols-4 md:grid-cols-7 gap-2">
              <label
                v-for="day in weekDays"
                :key="day.value"
                class="flex items-center space-x-2 text-sm"
              >
                <input
                  v-model="barberForm.dias_trabajo"
                  :value="day.value"
                  type="checkbox"
                  class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
                <span>{{ day.label }}</span>
              </label>
            </div>
          </div>
        </div>
      </form>
    </AdminModal>

    <!-- Modal de confirmación para eliminar -->
    <AdminModal
      :show="showDeleteModal"
      type="confirm"
      confirmType="danger"
      title="Eliminar Barbero"
      confirmMessage="¿Estás seguro de que quieres eliminar este barbero? Esta acción no se puede deshacer."
      confirmText="Eliminar"
      cancelText="Cancelar"
      :loading="deletingBarber"
      @confirm="confirmDelete"
      @cancel="closeDeleteModal"
      showActions
    />
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import AdminCard from '@/components/admin/AdminCard.vue'
import AdminTable from '@/components/admin/AdminTable.vue'
import AdminModal from '@/components/admin/AdminModal.vue'
import AdminButton from '@/components/admin/AdminButton.vue'
import { barberService } from '@/services/barberService'

export default {
  name: 'AdminBarberos',
  components: {
    AdminCard,
    AdminTable,
    AdminModal,
    AdminButton
  },
  setup() {
    // Estado reactivo
    const loadingStats = ref(true)
    const loadingBarbers = ref(true)
    const savingBarber = ref(false)
    const deletingBarber = ref(false)
    
    const barbers = ref([])
    const selectedBarbers = ref([])
    const stats = ref({})
    const modoDemo = ref(false) // Indicador de modo demo
    
    // Filtros
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
    
    // Configuración de tabla
    const tableColumns = [
      {
        key: 'nombre',
        label: 'Barbero',
        sortable: true
      },
      {
        key: 'especialidad',
        label: 'Especialidad',
        sortable: true
      },
      {
        key: 'disponible',
        label: 'Estado',
        sortable: true
      },
      {
        key: 'horario',
        label: 'Horario'
      }
    ]
    
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
      
      if (statusFilter.value !== '') {
        const isDisponible = statusFilter.value === 'true'
        filtered = filtered.filter(barber => barber.disponible === isDisponible)
      }
      
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
        console.log('Cargando barberos...')
        const data = await barberService.getAll()
        console.log('Datos de barberos recibidos:', data)
        barbers.value = data
        modoDemo.value = false
        console.log('Barberos cargados - Total:', barbers.value.length)
      } catch (error) {
        console.error('Error cargando barberos:', error)
        // Si hay error, usar datos de fallback del servicio
        barbers.value = barberService.getFallbackBarbers()
        modoDemo.value = true
        console.log('Usando fallback - Total barberos:', barbers.value.length)
      } finally {
        loadingBarbers.value = false
      }
    }
    
    const loadStats = async () => {
      try {
        loadingStats.value = true
        console.log('Cargando estadísticas...')
        const data = await barberService.getStats()
        console.log('Datos de estadísticas procesados:', data)
        
        // El servicio ya procesa los datos correctamente
        stats.value = {
          total: data.total || 0,
          activos: data.activos || 0,
          disponibles_hoy: data.disponibles_hoy || data.activos || 0,
          promedio_reservas: data.promedio_reservas || 0
        }
        
        console.log('Estadísticas finales:', stats.value)
      } catch (error) {
        console.error('Error cargando estadísticas:', error)
        
        // Calcular estadísticas basadas en los barberos cargados
        const totalBarbers = barbers.value.length
        const activeBarberos = barbers.value.filter(b => b.disponible).length
        
        console.log('Usando fallback - Total barberos:', totalBarbers, 'Activos:', activeBarberos)
        
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
      
      // Cargar datos en el formulario
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
    
    const viewBarber = (barber) => {
      // Implementar vista detallada
      console.log('Ver barbero:', barber)
    }
    
    const manageSchedule = (barber) => {
      // Implementar gestión de horarios avanzada
      console.log('Gestionar horarios:', barber)
    }
    
    // Acciones masivas
    const bulkActivate = async (selectedItems) => {
      try {
        const promises = selectedItems.map(item => 
          barberService.update(item.id, { disponible: true })
        )
        await Promise.all(promises)
        await loadBarbers()
        await loadStats()
      } catch (error) {
        console.error('Error activando barberos:', error)
      }
    }
    
    const bulkDeactivate = async (selectedItems) => {
      try {
        const promises = selectedItems.map(item => 
          barberService.update(item.id, { disponible: false })
        )
        await Promise.all(promises)
        await loadBarbers()
        await loadStats()
      } catch (error) {
        console.error('Error desactivando barberos:', error)
      }
    }
    
    const bulkDelete = async (selectedItems) => {
      try {
        const promises = selectedItems.map(item => 
          barberService.delete(item.id)
        )
        await Promise.all(promises)
        await loadBarbers()
        await loadStats()
      } catch (error) {
        console.error('Error eliminando barberos:', error)
      }
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
        lunes: 'L',
        martes: 'M',
        miércoles: 'X',
        jueves: 'J',
        viernes: 'V',
        sábado: 'S',
        domingo: 'D',
        monday: 'L',
        tuesday: 'M',
        wednesday: 'X',
        thursday: 'J',
        friday: 'V',
        saturday: 'S',
        sunday: 'D'
      }
      
      return days.map(day => dayLabels[day] || day.charAt(0).toUpperCase()).join(', ')
    }
    
    // Lifecycle
    onMounted(async () => {
      // Cargar barberos primero, luego estadísticas
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
      selectedBarbers,
      stats,
      modoDemo,
      statusFilter,
      especialidadFilter,
      showBarberModal,
      showDeleteModal,
      isEditing,
      currentBarber,
      barberForm,
      
      // Configuración
      tableColumns,
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
      closeDeleteModal,
      confirmDelete,
      manageSchedule,
      bulkActivate,
      bulkDeactivate,
      
      // Helpers
      getInitials,
      getWorkingDays
    }
  }
}
</script>

<style scoped>
.admin-barberos {
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

/* Filtros */
.filters-container {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.filter-select {
  min-width: 200px;
  padding: 0.5rem 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  background: white;
  font-size: 0.875rem;
  color: #374151;
}

.filter-select:focus {
  outline: none;
  border-color: #000000;
  box-shadow: 0 0 0 1px #000000;
}

/* Información del barbero */
.barbero-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.barbero-avatar {
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

.barbero-details {
  min-width: 0;
}

.barbero-nombre {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.875rem;
}

.barbero-email {
  color: #6b7280;
  font-size: 0.75rem;
}

/* Badges */
.especialidad-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  background: #f3f4f6;
  color: #374151;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
  border: 1px solid #e5e7eb;
}

.status-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
  gap: 0.5rem;
}

.status-available {
  background: #d1fae5;
  color: #065f46;
  border: 1px solid #10b981;
}

.status-unavailable {
  background: #fee2e2;
  color: #991b1b;
  border: 1px solid #ef4444;
}

.status-dot {
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 50%;
}

.status-available .status-dot {
  background: #10b981;
}

.status-unavailable .status-dot {
  background: #ef4444;
}

/* Horario */
.horario-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.horario-time {
  font-weight: 500;
  color: #1f2937;
  font-size: 0.875rem;
}

.horario-days {
  color: #6b7280;
  font-size: 0.75rem;
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

.action-schedule {
  background: #ecfdf5;
  color: #065f46;
  border-color: #10b981;
}

.action-schedule:hover {
  background: #d1fae5;
  border-color: #059669;
}

/* Acciones masivas */
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

/* Responsividad */
@media (max-width: 768px) {
  .admin-barberos {
    padding: 1rem;
  }
  
  .admin-header {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .header-actions {
    justify-content: flex-end;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .filters-container {
    flex-direction: column;
  }
  
  .filter-select {
    min-width: 100%;
  }
  
  .action-buttons {
    flex-direction: column;
  }
  
  .bulk-actions {
    flex-direction: column;
  }
}
</style>
