<!--
  ServicesView - Vista de servicios
  Página que muestra todos los servicios disponibles
-->
<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Hero Section -->
    <section class="py-24 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-4">
          <h1 class="text-4xl lg:text-5xl font-bold text-black mb-4">
            Nuestros Servicios
          </h1>
          <p class="text-lg text-gray-600 max-w-3xl mx-auto">
            Ofrecemos una amplia gama de servicios profesionales para el cuidado personal masculino, 
            utilizando técnicas modernas y productos de alta calidad.
          </p>
        </div>
      </div>
    </section>

    <!-- Loading State -->
    <div v-if="loading" class="flex justify-center items-center py-16">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900"></div>
    </div>

    <!-- Error State -->
    <div v-if="error" class="text-center py-16">
      <div class="text-red-600 text-lg mb-4">{{ error }}</div>
      <button @click="loadServices" class="bg-gray-900 text-white px-6 py-2 rounded-lg hover:bg-gray-800">
        Reintentar
      </button>
    </div>

    <!-- Sección de estadísticas -->
    <section v-if="!loading && !error" class="py-8 bg-gray-100 border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
          <!-- Servicios Disponibles -->
          <div class="flex flex-col items-center">
            <div class="text-4xl lg:text-5xl font-bold text-black mb-2">
              {{ allServices.length }}
            </div>
            <div class="text-sm lg:text-base text-gray-600 font-medium tracking-wide uppercase">
              Servicios Disponibles
            </div>
          </div>
          
          <!-- Satisfacción Garantizada -->
          <div class="flex flex-col items-center">
            <div class="text-4xl lg:text-5xl font-bold text-black mb-2">
              100%
            </div>
            <div class="text-sm lg:text-base text-gray-600 font-medium tracking-wide uppercase">
              Satisfacción Garantizada
            </div>
          </div>
          
          <!-- Calificación Promedio -->
          <div class="flex flex-col items-center">
            <div class="flex items-center mb-2">
              <span class="text-4xl lg:text-5xl font-bold text-black">5</span>
              <svg class="w-8 h-8 lg:w-10 lg:h-10 text-yellow-400 ml-1" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
              </svg>
            </div>
            <div class="text-sm lg:text-base text-gray-600 font-medium tracking-wide uppercase">
              Calificación Promedio
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Grid de servicios -->
    <section v-if="!loading && !error" class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div v-if="allServices.length === 0" class="text-center py-16">
          <div class="text-gray-600 text-lg">No hay servicios disponibles en este momento.</div>
        </div>
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <ServiceCard 
            v-for="service in allServices"
            :key="service.id"
            :service="service"
            @select-service="handleServiceSelection"
          />
        </div>
      </div>
    </section>

    <!-- Sección de información adicional -->
    <section class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 class="text-3xl lg:text-4xl font-bold text-gray-900 mb-6">
              ¿Por qué elegir Low Barber?
            </h2>
            <div class="space-y-6">
              <div class="flex items-start space-x-4">
                <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="text-xl font-semibold text-gray-900 mb-2">
                    Barberos Profesionales
                  </h3>
                  <p class="text-gray-600">
                    Nuestro equipo cuenta con años de experiencia y formación continua en las últimas tendencias.
                  </p>
                </div>
              </div>
              
              <div class="flex items-start space-x-4">
                <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="text-xl font-semibold text-gray-900 mb-2">
                    Productos Premium
                  </h3>
                  <p class="text-gray-600">
                    Utilizamos únicamente productos de alta calidad que cuidan tu cabello y piel.
                  </p>
                </div>
              </div>
              
              <div class="flex items-start space-x-4">
                <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="text-xl font-semibold text-gray-900 mb-2">
                    Horarios Flexibles
                  </h3>
                  <p class="text-gray-600">
                    Reserva tu cita en el horario que mejor se adapte a tu rutina diaria.
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Imagen placeholder -->
          <div class="aspect-video lg:aspect-square bg-gray-200 rounded-lg overflow-hidden">
            <div class="w-full h-full bg-gradient-to-br from-gray-100 to-gray-300 flex items-center justify-center">
              <div class="text-center text-gray-500">
                <svg class="w-16 h-16 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
                <p class="text-sm">Imagen de servicios</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import ServiceCard from '@/components/ServiceCard.vue'
import { serviceService } from '@/services'

export default {
  name: 'ServicesView',
  components: {
    ServiceCard
  },
  data() {
    return {
      allServices: [],
      loading: true,
      error: null
    }
  },
  async mounted() {
    await this.loadServices()
  },
  methods: {
    async loadServices() {
      this.loading = true
      this.error = null
      
      try {
        // El serviceService ya procesa y adapta los datos del backend
        const services = await serviceService.getServices()
        console.log('Servicios recibidos del serviceService:', services)
        
        // Mapear los datos ya procesados al formato esperado por el frontend
        this.allServices = services.map(service => ({
          id: service.id,
          name: service.name || service.nombre || 'Servicio sin nombre',
          description: service.description || service.descripcion || 'Sin descripción disponible',
          price: service.price || service.precio ? parseFloat(service.price || service.precio) : 0,
          duration: service.duration || service.duracion || 30,
          category: service.category || service.categoria || 'General',
          popular: service.popular || service.destacado || false,
          icon: this.getServiceIcon(service.category || service.categoria || 'General'),
          features: service.caracteristicas ? service.caracteristicas.split(',') : ['Servicio profesional'],
          tags: service.tags ? service.tags.split(',') : [service.category || service.categoria || 'General']
        }))
        
        console.log('Servicios procesados para la vista:', this.allServices)
      } catch (error) {
        console.error('Error al cargar servicios:', error)
        this.error = error.message || 'Error al cargar servicios'
        
        // Fallback con servicios estáticos si falla la API
        this.allServices = [
          {
            id: 1,
            name: 'Corte de Cabello',
            description: 'Corte profesional adaptado a tu estilo personal con técnicas modernas.',
            price: 50.00,
            duration: 45,
            category: 'Cortes',
            popular: true,
            icon: 'scissors',
            features: ['Estilo clásico o moderno', 'Técnicas profesionales'],
            tags: ['Clásico', 'Moderno']
          },
          {
            id: 2,
            name: 'Barba',
            description: 'Arreglo y perfilado de barba con productos premium y acabado profesional.',
            price: 40.00,
            duration: 30,
            category: 'Barba',
            popular: true,
            icon: 'user',
            features: ['Perfilado preciso', 'Aceites naturales'],
            tags: ['Barba', 'Styling']
          },
          {
            id: 3,
            name: 'Afeitado Clásico',
            description: 'Afeitado tradicional con navaja, toallas calientes y productos hidratantes.',
            price: 60.00,
            duration: 35,
            category: 'Afeitado',
            popular: false,
            icon: 'scissors',
            features: ['Navaja tradicional', 'Toallas calientes'],
            tags: ['Tradicional', 'Premium']
          },
          {
            id: 4,
            name: 'Cejas',
            description: 'Perfilado y arreglo de cejas masculinas para un look definido y elegante.',
            price: 15.00,
            duration: 20,
            category: 'Cejas',
            popular: false,
            icon: 'user',
            features: ['Perfilado preciso', 'Acabado natural'],
            tags: ['Cejas', 'Definición']
          },
          {
            id: 5,
            name: 'Servicio Completo',
            description: 'Experiencia completa: corte de cabello, barba, cejas y acabado profesional.',
            price: 70.00,
            duration: 90,
            category: 'Completo',
            popular: false,
            recommended: true,
            icon: 'sparkles',
            features: ['Corte + Barba + Cejas', 'Servicio premium'],
            tags: ['Completo', 'Premium', 'VIP']
          }
        ]
      } finally {
        this.loading = false
      }
    },
    
    handleServiceSelection(service) {
      console.log('Servicio seleccionado:', service)
      // Redirigir a reservas con el servicio preseleccionado
      this.$router.push({
        name: 'reservations',
        query: { service: service.id }
      })
    },
    
    getServiceIcon(category) {
      const iconMap = {
        'Cabello': 'scissors',
        'Cortes': 'scissors',
        'Barba': 'user',
        'Afeitado': 'scissors',
        'Cejas': 'user',
        'Completo': 'sparkles',
        'Paquete': 'sparkles',
        'General': 'scissors'
      }
      return iconMap[category] || 'scissors'
    }
  }
}
</script>
