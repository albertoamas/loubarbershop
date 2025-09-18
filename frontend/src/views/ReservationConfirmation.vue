<!--
  ReservationConfirmation - Página de confirmación de reserva
  Segunda pantalla del flujo de reservas
-->
<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-gray-50 to-slate-100">
    <!-- Header -->
    <div class="bg-white shadow-sm border-b">
      <div class="container mx-auto px-6 py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <button @click="goBack" class="p-2 hover:bg-gray-100 rounded-lg transition-colors">
              <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
              </svg>
            </button>
            <div class="w-10 h-10 bg-gradient-to-r from-gray-900 to-gray-700 rounded-xl flex items-center justify-center">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
            <div>
              <h1 class="text-xl font-bold text-gray-900">Low Barber Shop</h1>
              <p class="text-sm text-gray-500">Confirma tu reserva</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Progreso de reserva -->
    <div class="bg-white border-b">
      <div class="container mx-auto px-6 py-4">
        <div class="flex items-center justify-center space-x-8">
          <div class="flex items-center space-x-2">
            <div class="w-8 h-8 bg-green-500 text-white rounded-full flex items-center justify-center text-sm font-semibold">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
              </svg>
            </div>
            <span class="text-sm font-medium text-green-600">Seleccionar</span>
          </div>
          <div class="w-16 h-0.5 bg-gray-900"></div>
          <div class="flex items-center space-x-2">
            <div class="w-8 h-8 bg-gray-900 text-white rounded-full flex items-center justify-center text-sm font-semibold">2</div>
            <span class="text-sm font-medium text-gray-900">Confirmar</span>
          </div>
        </div>
      </div>
    </div>

    <div class="container mx-auto px-6 py-8">
      <div class="max-w-2xl mx-auto">
        <!-- Título principal -->
        <div class="text-center mb-8">
          <h2 class="text-3xl font-bold text-gray-900 mb-2">Confirma tu reserva</h2>
          <p class="text-gray-600">Revisa los detalles y completa tu información personal</p>
        </div>

        <!-- Tarjeta principal -->
        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
          <!-- Resumen de la reserva -->
          <div class="px-8 py-6 bg-gradient-to-r from-gray-50 to-white border-b border-gray-100">
            <h3 class="text-xl font-bold text-gray-900 mb-4">Resumen de tu cita</h3>
            
            <div class="grid md:grid-cols-2 gap-6">
              <!-- Información del barbero y servicio -->
              <div class="space-y-4">
                <!-- Barbero -->
                <div class="flex items-center space-x-3">
                  <div class="w-12 h-12 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-full flex items-center justify-center">
                    <span class="text-white font-semibold text-sm">
                      {{ reservationData?.barber?.name?.split(' ').map(n => n[0]).join('') || 'B' }}
                    </span>
                  </div>
                  <div>
                    <div class="text-sm font-medium text-gray-500">Barbero</div>
                    <div class="font-semibold text-gray-900">{{ reservationData?.barber?.name }}</div>
                    <div class="text-sm text-gray-600">{{ reservationData?.barber?.specialty }}</div>
                  </div>
                </div>
                
                <!-- Servicio -->
                <div class="flex items-center space-x-3">
                  <div class="w-12 h-12 bg-gradient-to-r from-green-500 to-emerald-500 rounded-full flex items-center justify-center">
                    <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                  </div>
                  <div>
                    <div class="text-sm font-medium text-gray-500">Servicio</div>
                    <div class="font-semibold text-gray-900">{{ reservationData?.service?.name }}</div>
                    <div class="text-sm text-gray-600">{{ reservationData?.service?.duration }} minutos</div>
                  </div>
                </div>
              </div>
              
              <!-- Fecha y hora -->
              <div class="space-y-4">
                <div class="p-4 bg-purple-50 rounded-xl border border-purple-100">
                  <div class="flex items-center space-x-3 mb-3">
                    <div class="w-10 h-10 bg-gradient-to-r from-purple-500 to-indigo-500 rounded-full flex items-center justify-center">
                      <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                      </svg>
                    </div>
                    <div>
                      <div class="text-sm font-medium text-gray-500">Fecha y hora</div>
                      <div class="font-semibold text-gray-900">{{ reservationData?.dateFormatted }}</div>
                      <div class="text-sm text-gray-600">{{ reservationData?.time }}</div>
                    </div>
                  </div>
                </div>
                
                <!-- Precio -->
                <div class="p-4 bg-green-50 rounded-xl border border-green-100">
                  <div class="text-sm font-medium text-gray-500 mb-2">Total a pagar</div>
                  <div class="text-2xl font-bold text-gray-900">Bs {{ reservationData?.total?.toFixed(2) }}</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Formulario de información personal -->
          <div class="px-8 py-6">
            <div class="flex items-center justify-between mb-4">
              <h4 class="text-lg font-bold text-gray-900">Información de contacto</h4>
              <div class="flex items-center space-x-2 text-sm text-green-600">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
                <span class="font-medium">Datos de tu perfil</span>
              </div>
            </div>
            
            

            <!-- Botones de acción -->
            <div class="flex gap-4 pt-4">
              <button
                type="button"
                @click="goBack"
                class="flex-1 bg-white text-gray-700 py-4 rounded-xl font-semibold border-2 border-gray-200 hover:bg-gray-50 hover:border-gray-300 transition-all duration-200"
              >
                Volver atrás
              </button>
              
              <button
                @click="confirmReservation"
                :disabled="loading || !userProfile?.nombre"
                class="flex-1 bg-gradient-to-r from-gray-900 to-gray-700 text-white py-4 rounded-xl font-semibold hover:from-gray-800 hover:to-gray-600 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 transform hover:scale-[1.02] shadow-lg relative"
              >
                <span v-if="loading" class="absolute inset-0 flex items-center justify-center">
                  <div class="animate-spin rounded-full h-5 w-5 border-2 border-white border-t-transparent"></div>
                </span>
                <span :class="{ 'opacity-0': loading }">
                  Confirmar reserva
                </span>
              </button>
            </div>
            
            <div class="text-center">
              <p class="text-xs text-gray-500">
                Al confirmar, aceptas nuestros términos y condiciones de servicio
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { reservationService, authService } from '../services/index.js'

export default {
  name: 'ReservationConfirmation',
  data() {
    return {
      reservationData: null,
      loading: false,
      userProfile: null,
      customerNotes: ''
    }
  },
  computed: {
    // Computed removido ya que no necesitamos validación de formulario
  },
  async mounted() {
    // Cargar datos del usuario autenticado
    await this.loadUserProfile();
    
    // Obtener datos de la reserva desde sessionStorage
    const storedData = sessionStorage.getItem('reservationData');
    if (storedData) {
      this.reservationData = JSON.parse(storedData);
      console.log('✅ Datos de reserva cargados:', this.reservationData);
    } else {
      // Si no hay datos, redirigir al inicio del flujo
      console.warn('⚠️ No hay datos de reserva, redirigiendo...');
      this.$router.push('/reservas');
    }
  },
  methods: {
    async loadUserProfile() {
      try {
        // Obtener perfil del usuario autenticado
        this.userProfile = await authService.getCurrentUser();
        console.log('✅ Perfil de usuario cargado:', this.userProfile);
      } catch (error) {
        console.error('❌ Error cargando perfil de usuario:', error);
        // Si no hay usuario autenticado, usar datos de fallback
        this.userProfile = {
          nombre: 'Usuario Invitado',
          telefono: 'No disponible',
          email: 'invitado@ejemplo.com'
        };
      }
    },
    
    goBack() {
      this.$router.back();
    },
    
    async confirmReservation() {
      if (!this.userProfile?.nombre) {
        alert('Error: No se pudo cargar la información del usuario');
        return;
      }
      
      this.loading = true;
      
      try {
        // Preparar datos para el backend usando datos del usuario autenticado
        const reservationRequest = {
          barbero_id: this.reservationData.barber.id,
          servicio_id: this.reservationData.service.id,
          fecha_reserva: this.reservationData.date,
          hora_inicio: this.reservationData.time + ':00',
          cliente_nombre: this.userProfile.nombre,
          cliente_telefono: this.userProfile.telefono,
          cliente_email: this.userProfile.email,
          notas: this.customerNotes.trim() || ''
        };
        
        console.log('📡 Enviando reserva al backend:', reservationRequest);
        
        // Llamada real al backend
        const response = await reservationService.createReservation(reservationRequest);
        console.log('✅ Reserva creada exitosamente:', response);
        
        // Preparar datos para la página de éxito
        const successData = {
          ...this.reservationData,
          customer: {
            name: this.userProfile.nombre,
            phone: this.userProfile.telefono,
            email: this.userProfile.email,
            notes: this.customerNotes
          },
          id: response.id || response.data?.id,
          createdAt: new Date().toISOString()
        };
        
        // Guardar datos para la página de éxito
        sessionStorage.setItem('reservationSuccess', JSON.stringify(successData));
        
        // Limpiar datos de reserva temporal
        sessionStorage.removeItem('reservationData');
        
        // Navegar a página de éxito
        this.$router.push('/reservas/exito');
        
      } catch (error) {
        console.error('💥 Error al confirmar reserva:', error);
        
        let errorMessage = '❌ Error al confirmar la reserva. ';
        
        if (error.message) {
          errorMessage += error.message;
        } else if (error.response?.data?.message) {
          errorMessage += error.response.data.message;
        } else {
          errorMessage += 'Por favor, inténtalo de nuevo más tarde.';
        }
        
        // Mostrar error específico si hay validaciones
        if (error.response?.data?.validation_errors) {
          const validationErrors = Object.values(error.response.data.validation_errors).flat();
          errorMessage += '\n\nDetalles:\n' + validationErrors.join('\n');
        }
        
        alert(errorMessage);
        
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>
