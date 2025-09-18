<!--
  ReservationSuccess - Página de confirmación exitosa
  Tercera pantalla del flujo de reservas
-->
<template>
  <div class="min-h-screen bg-gradient-to-br from-green-50 via-emerald-50 to-teal-50">
    <!-- Header -->
    <div class="bg-white shadow-sm border-b">
      <div class="container mx-auto px-6 py-4">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
          </div>
          <div>
            <h1 class="text-xl font-bold text-gray-900">Low Barber Shop</h1>
            <p class="text-sm text-gray-500">¡Reserva confirmada!</p>
          </div>
        </div>
      </div>
    </div>

    <div class="container mx-auto px-6 py-12">
      <div class="max-w-2xl mx-auto text-center">
        <!-- Icono de éxito -->
        <div class="w-24 h-24 bg-gradient-to-r from-green-500 to-emerald-500 rounded-full flex items-center justify-center mx-auto mb-8">
          <svg class="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
          </svg>
        </div>

        <!-- Mensaje de éxito -->
        <div class="mb-8">
          <h2 class="text-4xl font-bold text-gray-900 mb-4">¡Reserva confirmada!</h2>
          <p class="text-xl text-gray-600">
            Tu cita ha sido programada exitosamente. Te esperamos en Low Barber Shop.
          </p>
        </div>

        <!-- Tarjeta de detalles de la reserva -->
        <div class="bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden mb-8">
          <!-- Header de la tarjeta -->
          <div class="px-8 py-6 bg-gradient-to-r from-green-50 to-emerald-50 border-b border-gray-100">
            <h3 class="text-xl font-bold text-gray-900">Detalles de tu cita</h3>
            <p class="text-green-600 font-medium">ID: #{{ reservation?.id || '12345' }}</p>
          </div>

          <!-- Contenido de la tarjeta -->
          <div class="px-8 py-6">
            <div class="grid md:grid-cols-2 gap-8">
              <!-- Información del servicio -->
              <div class="space-y-6">
                <!-- Barbero -->
                <div class="flex items-center space-x-4">
                  <div class="w-16 h-16 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-full flex items-center justify-center">
                    <span class="text-white font-bold text-lg">
                      {{ reservation?.barber?.name?.split(' ').map(n => n[0]).join('') || 'B' }}
                    </span>
                  </div>
                  <div>
                    <div class="text-sm font-medium text-gray-500">Tu barbero</div>
                    <div class="text-lg font-bold text-gray-900">{{ reservation?.barber?.name }}</div>
                    <div class="text-sm text-gray-600">{{ reservation?.barber?.specialty }}</div>
                  </div>
                </div>
                
                <!-- Servicio -->
                <div class="flex items-center space-x-4">
                  <div class="w-16 h-16 bg-gradient-to-r from-green-500 to-emerald-500 rounded-full flex items-center justify-center">
                    <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                  </div>
                  <div>
                    <div class="text-sm font-medium text-gray-500">Servicio</div>
                    <div class="text-lg font-bold text-gray-900">{{ reservation?.service?.name }}</div>
                    <div class="text-sm text-gray-600">{{ reservation?.service?.duration }} minutos</div>
                  </div>
                </div>
              </div>
              
              <!-- Información de fecha y cliente -->
              <div class="space-y-6">
                <!-- Fecha y hora -->
                <div class="p-6 bg-purple-50 rounded-xl border border-purple-100">
                  <div class="flex items-center space-x-3 mb-3">
                    <div class="w-12 h-12 bg-gradient-to-r from-purple-500 to-indigo-500 rounded-full flex items-center justify-center">
                      <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                      </svg>
                    </div>
                    <div>
                      <div class="text-sm font-medium text-gray-500">Fecha y hora</div>
                      <div class="text-lg font-bold text-gray-900">{{ reservation?.dateFormatted }}</div>
                      <div class="text-base font-semibold text-purple-600">{{ reservation?.time }}</div>
                    </div>
                  </div>
                </div>
                
                <!-- Total pagado -->
                <div class="p-6 bg-green-50 rounded-xl border border-green-100">
                  <div class="text-center">
                    <div class="text-sm font-medium text-gray-500 mb-1">Total</div>
                    <div class="text-3xl font-bold text-gray-900">Bs {{ reservation?.total?.toFixed(2) }}</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Información del cliente -->
            <div class="mt-8 pt-6 border-t border-gray-200">
              <h4 class="text-lg font-bold text-gray-900 mb-4">Información de contacto</h4>
              <div class="grid md:grid-cols-3 gap-4">
                <div class="text-center p-4 bg-gray-50 rounded-xl">
                  <div class="text-sm text-gray-500">Nombre</div>
                  <div class="font-semibold text-gray-900">{{ reservation?.customer?.name }}</div>
                </div>
                <div class="text-center p-4 bg-gray-50 rounded-xl">
                  <div class="text-sm text-gray-500">Teléfono</div>
                  <div class="font-semibold text-gray-900">{{ reservation?.customer?.phone }}</div>
                </div>
                <div class="text-center p-4 bg-gray-50 rounded-xl" v-if="reservation?.customer?.email">
                  <div class="text-sm text-gray-500">Email</div>
                  <div class="font-semibold text-gray-900">{{ reservation?.customer?.email }}</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Información adicional -->
        <div class="bg-blue-50 rounded-2xl p-6 mb-8 border border-blue-100">
          <div class="flex items-start space-x-4">
            <div class="w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center flex-shrink-0">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
            <div class="text-left">
              <h4 class="font-bold text-gray-900 mb-2">Información importante</h4>
              <ul class="text-sm text-gray-700 space-y-1">
                <li>• Por favor, llega 5 minutos antes de tu cita</li>
                <li>• Si necesitas cancelar o reprogramar, llámanos con 24 horas de anticipación</li>
                <li>• Recuerda traer una mascarilla por protocolo sanitario</li>
                <li>• El pago se realiza al finalizar el servicio</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Información de contacto -->
        <div class="bg-gray-50 rounded-2xl p-6 mb-8">
          <h4 class="font-bold text-gray-900 mb-4">Contacto de la barbería</h4>
          <div class="grid md:grid-cols-2 gap-4">
            <div class="flex items-center space-x-3">
              <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
              </svg>
              <div>
                <div class="text-sm text-gray-500">Teléfono</div>
                <div class="font-semibold text-gray-900">+591 70123456</div>
              </div>
            </div>
            <div class="flex items-center space-x-3">
              <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              <div>
                <div class="text-sm text-gray-500">Dirección</div>
                <div class="font-semibold text-gray-900">Av. Principal #123</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Botones de acción -->
        <div class="flex flex-col sm:flex-row gap-4">
          <button
            @click="goHome"
            class="flex-1 bg-white text-gray-700 py-4 px-8 rounded-xl font-semibold border-2 border-gray-200 hover:bg-gray-50 hover:border-gray-300 transition-all duration-200"
          >
            Volver al inicio
          </button>
          
          <button
            @click="makeAnotherReservation"
            class="flex-1 bg-gradient-to-r from-gray-900 to-gray-700 text-white py-4 px-8 rounded-xl font-semibold hover:from-gray-800 hover:to-gray-600 transition-all duration-200 transform hover:scale-[1.02] shadow-lg"
          >
            Hacer otra reserva
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReservationSuccess',
  data() {
    return {
      reservation: null
    }
  },
  mounted() {
    // Obtener datos de la reserva desde sessionStorage
    const storedData = sessionStorage.getItem('reservationSuccess');
    if (storedData) {
      this.reservation = JSON.parse(storedData);
      console.log('✅ Datos de reserva exitosa cargados:', this.reservation);
      // Limpiar datos después de cargarlos
      sessionStorage.removeItem('reservationSuccess');
    } else {
      // Si no hay datos, crear datos de ejemplo para evitar errores
      console.warn('⚠️ No hay datos de reserva exitosa, usando fallback');
      this.reservation = {
        id: '12345',
        barber: { name: 'Barbero', specialty: 'Especialista' },
        service: { name: 'Servicio', duration: 30 },
        dateFormatted: 'Fecha no disponible',
        time: '00:00',
        total: 0,
        customer: { name: 'Cliente', phone: '000000000' }
      };
    }
  },
  methods: {
    goHome() {
      this.$router.push('/');
    },
    
    makeAnotherReservation() {
      this.$router.push('/reservas');
    }
  }
}
</script>
