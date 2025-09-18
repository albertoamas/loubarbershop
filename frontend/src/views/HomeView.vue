<!--
  HomeView - Vista principal/inicio
  Página de bienvenida con información general de la barbería
  Actualizada para usar Tailwind CSS v4 con clases estándar
-->
<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Panel de Pruebas de Desarrollo (temporal) -->
    <div v-if="showDevPanel" class="bg-[color-mix(in_srgb,var(--color-barber-gold),white_80%)] border-l-4 border-[var(--color-barber-gold)] p-4 mb-4">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between">
          <div class="flex">
            <div class="flex-shrink-0">
              <svg class="h-5 w-5 text-[var(--color-barber-gold)]" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
              </svg>
            </div>
            <div class="ml-3">
              <p class="text-sm text-[color-mix(in_srgb,var(--color-barber-gold),black_20%)]">
                <strong>Panel de Desarrollo:</strong> Haz clic en los botones para probar el panel administrativo
              </p>
            </div>
          </div>
          <div class="flex items-center space-x-2">
            <button
              @click="loginAsAdmin"
              class="bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded text-sm font-medium transition-colors"
            >
              🔑 Login Admin
            </button>
            <button
              @click="loginAsBarber"
              class="bg-green-600 hover:bg-green-700 text-white px-3 py-1 rounded text-sm font-medium transition-colors"
            >
              ✂️ Login Barbero
            </button>
            <button
              @click="loginAsClient"
              class="bg-purple-600 hover:bg-purple-700 text-white px-3 py-1 rounded text-sm font-medium transition-colors"
            >
              👤 Login Cliente
            </button>
            <button
              @click="logout"
              class="bg-red-600 hover:bg-red-700 text-white px-3 py-1 rounded text-sm font-medium transition-colors"
            >
              🚪 Logout
            </button>
            <button
              @click="showDevPanel = false"
              class="text-[color-mix(in_srgb,var(--color-barber-gold),black_20%)] hover:text-[var(--color-barber-gold)] text-sm"
            >
              ✕
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Hero Section -->
    <HeroComponent />

    <!-- Sección de servicios destacados -->
    <section class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Encabezado -->
        <div class="text-center mb-12">
          <div class="inline-flex items-center justify-center px-4 py-2 bg-[var(--color-barber-primary)] text-white rounded-full text-sm font-medium mb-4">
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            Nuestros Servicios
          </div>
          <h2 class="text-4xl font-bold text-black mb-4">
            Servicios Profesionales
          </h2>
          <div class="w-16 h-0.5 bg-[var(--color-barber-primary)] mx-auto mb-4"></div>
          <p class="text-lg text-gray-600">
            Transformamos tu imagen con los mejores servicios
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
          <ServiceCard 
            v-for="service in featuredServices" 
            :key="service.id"
            :service="service"
            @select-service="handleServiceSelection"
          />
        </div>

        <div class="text-center">
          <RouterLink to="/servicios" class="bg-[var(--color-barber-primary)] text-white px-6 py-3 rounded-xl font-medium hover:bg-[var(--color-barber-gold)] transition-all duration-200 inline-block">
            Ver Todos los Servicios
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- Sección de productos destacados -->
    <section class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <div class="inline-flex items-center justify-center px-4 py-2 bg-[var(--color-barber-primary)] text-white rounded-full text-sm font-medium mb-4">
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M9 1L5 3l4 2 4-2-4-2z"/>
            </svg>
            Productos Premium
          </div>
          <h2 class="text-4xl font-bold text-black mb-4">
            Productos Recomendados
          </h2>
          <div class="w-16 h-0.5 bg-[var(--color-barber-primary)] mx-auto mb-4"></div>
          <p class="text-lg text-gray-600 max-w-2xl mx-auto">
            Los mejores productos para el cuidado personal, seleccionados por nuestros expertos
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-10 mb-12">
          <ProductCard 
            v-for="product in featuredProducts" 
            :key="product.id"
            :product="product"
            @view-product="handleProductView"
          />
        </div>

        <div class="text-center">
          <RouterLink to="/productos" class="bg-[var(--color-barber-primary)] text-white px-6 py-3 rounded-xl font-medium hover:bg-[var(--color-barber-gold)] transition-all duration-200 inline-block">
            Ver Todos los Productos
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- Sección de testimonio -->
    <section class="py-16 bg-gray-800 text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-4xl mx-auto text-center">
          <blockquote class="text-2xl lg:text-3xl font-light text-gray-200 mb-8 italic">
            "La mejor experiencia de barbería que he tenido. El ambiente es increíble y 
            la atención al detalle es excepcional. Definitivamente mi lugar favorito."
          </blockquote>
          <div class="flex items-center justify-center">
            <div class="w-16 h-16 bg-gray-600 rounded-full mr-4"></div>
            <div class="text-left">
              <p class="font-semibold text-white">Carlos Mendoza</p>
              <p class="text-gray-300">Cliente frecuente</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Sección de ubicación y contacto -->
    <section class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <!-- Información de contacto -->
          <div>
            <h2 class="text-3xl lg:text-4xl font-bold text-black mb-6">
              Visítanos
            </h2>
            <p class="text-lg text-gray-600 mb-8">
              Estamos ubicados en el corazón de la ciudad, con fácil acceso y estacionamiento disponible.
            </p>
            
            <div class="space-y-4 mb-8">
              <div class="flex items-center space-x-4">
                <div class="w-12 h-12 bg-[var(--color-barber-primary)] rounded-lg flex items-center justify-center">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="font-semibold text-black">Dirección</h3>
                  <p class="text-gray-600">Ramón rojas entre Bolívar y Domingo Paz, Tarija</p>
                </div>
              </div>
              
              <div class="flex items-center space-x-4">
                <div class="w-12 h-12 bg-[var(--color-barber-primary)] rounded-lg flex items-center justify-center">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="font-semibold text-black">Teléfono</h3>
                  <p class="text-gray-600">+591 77872911</p>
                </div>
              </div>
              
              <div class="flex items-center space-x-4">
                <div class="w-12 h-12 bg-[var(--color-barber-primary)] rounded-lg flex items-center justify-center">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="font-semibold text-black">Horarios</h3>
                  <p class="text-gray-600">Lun - Vie: 9:00 - 19:00</p>
                </div>
              </div>
            </div>
            
            <div class="flex flex-col sm:flex-row gap-4">
              <RouterLink to="/contacto" class="bg-[var(--color-barber-primary)] text-white px-6 py-3 rounded-xl font-medium hover:bg-[var(--color-barber-gold)] transition-all duration-200 inline-block text-center">
                Contactar
              </RouterLink>
              <RouterLink to="/reservas" class="bg-gray-200 text-black px-6 py-3 rounded-xl font-medium hover:bg-gray-300 transition-all duration-200 inline-block text-center">
                Reservar Cita
              </RouterLink>
            </div>
          </div>

          <!-- Mapa de Google Maps -->
          <div class="aspect-video lg:aspect-square rounded-lg overflow-hidden shadow-lg">
            <iframe 
              src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3711.4175878900796!2d-64.7398365!3d-21.5305211!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x940647cc75c5b92f%3A0x33dd9a29dd3859da!2sLou%20Barbershop!5e0!3m2!1ses-419!2sbo!4v1752882019980!5m2!1ses-419!2sbo" 
              width="100%" 
              height="100%" 
              style="border:0;" 
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade"
              class="w-full h-full"
            ></iframe>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import HeroComponent from '@/components/HeroComponent.vue'
import ServiceCard from '@/components/ServiceCard.vue'
import ProductCard from '@/components/ProductCard.vue'
import { authService } from '@/services/authService.js'

export default {
  name: 'HomeView',
  components: {
    HeroComponent,
    ServiceCard,
    ProductCard
  },
  data() {
    return {
      showDevPanel: false, // Panel de desarrollo desactivado - ahora usar login real
      featuredServices: [
        {
          id: 1,
          name: 'Corte de Cabello',
          description: 'Corte de cabello clásico o moderno adaptado a tu estilo personal con técnicas profesionales.',
          price: 50.00,
          duration: 45,
          popular: true,
          icon: 'scissors',
          features: ['Estilo clásico o moderno', 'Técnicas profesionales'],
          tags: ['Clásico', 'Moderno']
        },
        {
          id: 2,
          name: 'Barba',
          description: 'Arreglo y perfilado profesional de barba con productos de calidad y técnicas especializadas.',
          price: 40.00,
          duration: 30,
          popular: false,
          icon: 'user',
          features: ['Perfilado preciso', 'Aceites naturales'],
          tags: ['Barba', 'Styling']
        },
        {
          id: 5,
          name: 'Servicio Completo',
          description: 'Servicio premium que incluye corte de cabello, arreglo de barba y perfilado de cejas.',
          price: 80.00,
          duration: 75,
          popular: false,
          recommended: true,
          icon: 'sparkles',
          features: ['Corte + Barba + Cejas', 'Servicio premium'],
          tags: ['Premium', 'Completo', 'VIP']
        }
      ],
      featuredProducts: [
        {
          id: 1,
          name: 'Pomada Fijadora',
          description: 'Pomada de alta calidad para un peinado duradero y con brillo natural.',
          price: 35.00,
          brand: 'Premium Hair',
          category: 'Styling',
          stock: 15,
          rating: 4.5,
          featured: true,
          tags: ['Fijación', 'Brillo']
        },
        {
          id: 3,
          name: 'Aceite para Barba',
          description: 'Aceite nutritivo para barba que suaviza y da brillo natural.',
          price: 45.00,
          brand: 'Beard Master',
          category: 'Barba',
          stock: 12,
          rating: 4.8,
          tags: ['Barba', 'Nutritivo']
        }
      ]
    }
  },
  methods: {
    handleServiceSelection(service) {
      console.log('Servicio seleccionado:', service)
      // Aquí podrías manejar la lógica adicional para la selección del servicio
    },
    handleProductView(product) {
      console.log('Ver producto:', product)
      // Aquí podrías manejar la lógica para ver los detalles del producto
    },
    
    // Métodos para el panel de desarrollo
    async loginAsAdmin() {
      try {
        const result = await authService.loginAsAdmin()
        alert('✅ Logueado como Administrador\n\n🎯 Ahora puedes acceder al Panel Admin haciendo clic en el botón azul "Panel Admin" en el navbar superior.')
        console.log('Login admin exitoso:', result)
      } catch (error) {
        alert('❌ Error al hacer login como admin: ' + error.message)
        console.error('Error:', error)
      }
    },
    
    loginAsBarber() {
      try {
        const result = authService.loginAsBarber()
        alert('✅ Logueado como Barbero\n\n✂️ Perfil de barbero activado.')
        console.log('Login barbero exitoso:', result)
      } catch (error) {
        alert('❌ Error al hacer login como barbero: ' + error.message)
      }
    },
    
    loginAsClient() {
      try {
        const result = authService.loginAsClient()
        alert('✅ Logueado como Cliente\n\n👤 Perfil de cliente activado.')
        console.log('Login cliente exitoso:', result)
      } catch (error) {
        alert('❌ Error al hacer login como cliente: ' + error.message)
      }
    },
    
    logout() {
      try {
        authService.logout()
        alert('🚪 Sesión cerrada exitosamente')
        console.log('Logout exitoso')
      } catch (error) {
        alert('❌ Error al cerrar sesión: ' + error.message)
      }
    }
  }
}
</script>
