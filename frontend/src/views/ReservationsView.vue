<!--
  ReservationsView - Vista de reservas estilo Figma v2
  Página de reservas con diseño tipo checkout
-->
<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-gray-50 to-slate-100">
    <!-- Header mejorado -->
    <div class="bg-white shadow-sm border-b">
      <div class="container mx-auto px-6 py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-r from-gray-900 to-gray-700 rounded-xl flex items-center justify-center">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
            <div>
              <h1 class="text-xl font-bold text-gray-900">Low Barber Shop</h1>
              <p class="text-sm text-gray-500">Reserva tu cita perfecta</p>
            </div>
          </div>
          <div class="flex items-center space-x-2">
            <div class="flex items-center space-x-1 text-sm text-gray-500">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              <span>Horario: 9:00 AM - 6:00 PM</span>
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
            <div class="w-8 h-8 bg-gray-900 text-white rounded-full flex items-center justify-center text-sm font-semibold">1</div>
            <span class="text-sm font-medium text-gray-900">Seleccionar</span>
          </div>
          <div class="w-16 h-0.5 bg-gray-200"></div>
          <div class="flex items-center space-x-2">
            <div class="w-8 h-8 bg-gray-200 text-gray-500 rounded-full flex items-center justify-center text-sm font-semibold">2</div>
            <span class="text-sm text-gray-500">Confirmar</span>
          </div>
        </div>
      </div>
    </div>

    <div class="container mx-auto px-6 py-8">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Columna principal -->
        <div class="lg:col-span-2 space-y-8">

          <!-- Selección de barbero -->
          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
            <div class="px-6 py-5 bg-gradient-to-r from-gray-50 to-white">
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-xl flex items-center justify-center">
                  <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                  </svg>
                </div>
                <div>
                  <h2 class="text-xl font-bold text-gray-900">Selecciona un barbero</h2>
                  <p class="text-sm text-gray-600">Elige el profesional que prefieras</p>
                </div>
              </div>
            </div>
            <div class="px-6 pb-6">
              <div class="relative">
                <select
                  v-model="selectedBarber"
                  class="w-full px-4 py-4 bg-gray-50 border-2 border-gray-100 rounded-xl text-gray-700 font-medium appearance-none focus:outline-none focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-all duration-200 hover:border-gray-200"
                >
                  <option :value="null" class="text-gray-500">Selecciona un barbero</option>
                  <option 
                    v-for="barber in barbers" 
                    :key="barber.id" 
                    :value="barber"
                    class="text-gray-700"
                  >
                    {{ barber.name }} - {{ barber.specialty }}
                  </option>
                </select>
                <div class="absolute inset-y-0 right-0 flex items-center pr-4 pointer-events-none">
                  <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                  </svg>
                </div>
              </div>
              <div v-if="selectedBarber" class="mt-4 p-4 bg-blue-50 rounded-xl border border-blue-100">
                <div class="flex items-center space-x-3">
                  <div class="w-12 h-12 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-full flex items-center justify-center">
                    <span class="text-white font-semibold text-sm">{{ selectedBarber.name.split(' ').map(n => n[0]).join('') }}</span>
                  </div>
                  <div>
                    <h3 class="font-semibold text-gray-900">{{ selectedBarber.name }}</h3>
                    <p class="text-sm text-gray-600">{{ selectedBarber.specialty }}</p>
                    <div class="flex items-center mt-1">
                      <svg class="w-4 h-4 text-[var(--color-barber-gold)] mr-1" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                      </svg>
                      <span class="text-sm text-gray-600">{{ selectedBarber.experience }}+ años de experiencia</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Selección de servicio -->
          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
            <div class="px-6 py-5 bg-gradient-to-r from-gray-50 to-white">
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl flex items-center justify-center">
                  <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                </div>
                <div>
                  <h2 class="text-xl font-bold text-gray-900">Selecciona un servicio</h2>
                  <p class="text-sm text-gray-600">Elige el servicio que necesitas</p>
                </div>
              </div>
            </div>
            <div class="px-6 pb-6">
              <div class="relative">
                <select
                  v-model="selectedService"
                  class="w-full px-4 py-4 bg-gray-50 border-2 border-gray-100 rounded-xl text-gray-700 font-medium appearance-none focus:outline-none focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-all duration-200 hover:border-gray-200"
                >
                  <option :value="null" class="text-gray-500">Selecciona un servicio</option>
                  <option 
                    v-for="service in services" 
                    :key="service.id" 
                    :value="service"
                    class="text-gray-700"
                  >
                    {{ service.name || 'Sin nombre' }} - {{ service.duration || 0 }}min - Bs {{ service.price || 0 }}
                  </option>
                </select>
                <div class="absolute inset-y-0 right-0 flex items-center pr-4 pointer-events-none">
                  <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                  </svg>
                </div>
              </div>
              <div v-if="selectedService" class="mt-4 p-4 bg-green-50 rounded-xl border border-green-100">
                <div class="flex items-center justify-between">
                  <div>
                    <h3 class="font-semibold text-gray-900">{{ selectedService.name }}</h3>
                    <p class="text-sm text-gray-600">{{ selectedService.category }}</p>
                  </div>
                  <div class="text-right">
                    <div class="text-lg font-bold text-gray-900">Bs {{ selectedService.price }}</div>
                    <div class="text-sm text-gray-600">{{ selectedService.duration }} minutos</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Selección de fecha y hora -->
          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
            <div class="px-6 py-5 bg-gradient-to-r from-gray-50 to-white">
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 bg-gradient-to-r from-purple-500 to-indigo-500 rounded-xl flex items-center justify-center">
                  <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                  </svg>
                </div>
                <div>
                  <h2 class="text-xl font-bold text-gray-900">Selecciona fecha y hora</h2>
                  <p class="text-sm text-gray-600">Elige el momento perfecto para tu cita</p>
                </div>
              </div>
            </div>
            <div class="px-6 pb-6">
              <!-- Selector de hora -->
              <div class="relative">
                <select
                  v-model="selectedTime"
                  class="w-full px-4 py-4 bg-gray-50 border-2 border-gray-100 rounded-xl text-gray-700 font-medium appearance-none focus:outline-none focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-all duration-200 hover:border-gray-200"
                  :disabled="!selectedBarber || !selectedService || !selectedDate"
                >
                  <option value="">
                    {{ !selectedBarber || !selectedService || !selectedDate 
                       ? 'Selecciona barbero, servicio y fecha primero' 
                       : 'Selecciona una hora' }}
                  </option>
                  <option v-for="time in availableTimes" :key="time" :value="time">
                    {{ time }}
                  </option>
                </select>
                <div class="absolute inset-y-0 right-0 flex items-center pr-4 pointer-events-none">
                  <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                  </svg>
                </div>
              </div>
              <!-- Calendario -->
              <div class="bg-gray-50 rounded-xl p-6 mb-6 border border-gray-100">
                <div class="flex items-center justify-between mb-6">
                  <button @click="previousMonth" class="p-2 hover:bg-white hover:shadow-sm rounded-xl transition-all duration-200">
                    <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                    </svg>
                  </button>
                  <h3 class="text-lg font-bold text-gray-900">{{ currentMonth }}</h3>
                  <button @click="nextMonth" class="p-2 hover:bg-white hover:shadow-sm rounded-xl transition-all duration-200">
                    <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                    </svg>
                  </button>
                </div>
                
                <div class="grid grid-cols-7 gap-2 mb-4">
                  <div v-for="day in weekDays" :key="day" class="text-center text-xs font-semibold text-gray-500 p-2 uppercase tracking-wide">
                    {{ day }}
                  </div>
                </div>
                
                <div class="grid grid-cols-7 gap-2">
                  <button
                    v-for="date in currentMonthDates"
                    :key="date"
                    @click="selectDate(date)"
                    :disabled="!date || isPastDate(date)"
                    :class="[
                      'p-3 text-center text-sm rounded-xl transition-all duration-200 font-medium',
                      selectedDate === date 
                        ? 'bg-gradient-to-r from-gray-900 to-gray-700 text-white shadow-lg transform scale-105' 
                        : !date || isPastDate(date)
                        ? 'text-gray-300 cursor-not-allowed'
                        : 'text-gray-700 hover:bg-white hover:shadow-sm cursor-pointer',
                      !date ? 'invisible' : ''
                    ]"
                  >
                    {{ date }}
                  </button>
                </div>
              </div>
              
              <!-- Información de disponibilidad -->
              <div v-if="selectedBarber && selectedService && selectedDate" class="mt-4 p-4 bg-purple-50 rounded-xl border border-purple-100">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 bg-gradient-to-r from-purple-500 to-indigo-500 rounded-full flex items-center justify-center flex-shrink-0">
                    <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                  </div>
                  <div>
                    <div class="font-semibold text-gray-900">{{ availableTimes.length }} horarios disponibles</div>
                    <div class="text-sm text-gray-600">Para {{ selectedService.name }} ({{ selectedService.duration }} minutos)</div>
                    <div v-if="availableTimes.length === 0" class="mt-2 text-sm text-red-600 font-medium">
                      ⚠️ No hay horarios disponibles para este día. Prueba otra fecha.
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Panel lateral de resumen -->
        <div class="lg:col-span-1">
          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 sticky top-8 overflow-hidden">
            <!-- Loading state -->
            <div v-if="loading" class="text-center py-12">
              <div class="animate-spin rounded-full h-10 w-10 border-2 border-gray-200 border-t-gray-900 mx-auto"></div>
              <p class="text-gray-500 mt-4 font-medium">Cargando datos...</p>
            </div>
            
            <!-- Content -->
            <div v-else>
              <!-- Header del resumen -->
              <div class="px-6 py-5 bg-gradient-to-r from-gray-50 to-white border-b border-gray-100">
                <h3 class="text-lg font-bold text-gray-900">Resumen de tu reserva</h3>
                <p class="text-sm text-gray-600">Revisa los detalles antes de continuar</p>
              </div>
              
              <div class="p-6">
                <!-- Información del barbero y servicio -->
                <div class="flex items-start justify-between mb-6">
                  <div class="flex-1">
                    <div class="space-y-4">
                      <!-- Barbero -->
                      <div class="flex items-center space-x-3">
                        <div class="w-12 h-12 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-full flex items-center justify-center">
                          <span class="text-white font-semibold text-sm">
                            {{ selectedBarber ? selectedBarber.name.split(' ').map(n => n[0]).join('') : '?' }}
                          </span>
                        </div>
                        <div>
                          <div class="text-sm font-medium text-gray-500">Barbero</div>
                          <div class="font-semibold text-gray-900">
                            {{ selectedBarber?.name || 'Selecciona un barbero' }}
                          </div>
                          <div class="text-sm text-gray-500">
                            {{ selectedBarber?.specialty || '' }}
                          </div>
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
                          <div class="font-semibold text-gray-900">
                            {{ selectedService?.name || 'Selecciona un servicio' }}
                          </div>
                          <div class="text-sm text-gray-500">
                            {{ selectedService?.category || '' }}
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Información de la cita -->
                <div class="space-y-3 mb-6 p-4 bg-gray-50 rounded-xl">
                  <div class="flex justify-between items-center">
                    <div class="flex items-center space-x-2">
                      <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                      </svg>
                      <span class="text-gray-600 font-medium">Fecha</span>
                    </div>
                    <span class="text-gray-900 font-semibold">{{ formatSelectedDate() }}</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <div class="flex items-center space-x-2">
                      <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                      </svg>
                      <span class="text-gray-600 font-medium">Hora</span>
                    </div>
                    <span class="text-gray-900 font-semibold">{{ selectedTime || 'Selecciona una hora' }}</span>
                  </div>
                  <div class="flex justify-between items-center" v-if="selectedService">
                    <div class="flex items-center space-x-2">
                      <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                      </svg>
                      <span class="text-gray-600 font-medium">Duración</span>
                    </div>
                    <span class="text-gray-900 font-semibold">{{ selectedService.duration }} min</span>
                  </div>
                </div>

                <!-- Resumen del pedido -->
                <div class="border-t border-gray-100 pt-6">
                  <h4 class="text-base font-bold text-gray-900 mb-4">Detalles del precio</h4>
                  <div class="space-y-3">
                    <div class="flex justify-between items-center">
                      <span class="text-gray-600">{{ selectedService?.name || 'Servicio' }}</span>
                      <span class="text-gray-900 font-medium">{{ selectedService?.duration || '30' }} min</span>
                    </div>
                    <div class="flex justify-between items-center">
                      <span class="text-gray-600">Precio del servicio</span>
                      <span class="text-gray-900 font-medium">Bs {{ selectedService?.price || 25 }}</span>
                    </div>
                    <div class="border-t border-gray-200 pt-3">
                      <div class="flex justify-between items-center">
                        <span class="text-lg font-bold text-gray-900">Total</span>
                        <span class="text-xl font-bold text-gray-900">Bs {{ calculateTotal() }}</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Botón de continuar -->
                <button
                  @click="proceedToConfirmation"
                  :disabled="!canReserve"
                  class="w-full mt-6 bg-gradient-to-r from-gray-900 to-gray-700 text-white py-4 rounded-xl font-semibold text-lg hover:from-gray-800 hover:to-gray-600 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 transform hover:scale-[1.02] shadow-lg"
                >
                  {{ canReserve ? 'Continuar a confirmación' : 'Complete todos los campos' }}
                </button>
                
                <div class="mt-4 text-center">
                  <p class="text-xs text-gray-500">
                    Al continuar, podrás revisar y confirmar tu reserva
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { serviceService, barberService, reservationService } from '../services/index.js'

export default {
  name: 'ReservationsView',
  data() {
    return {
      selectedBarber: null,
      selectedService: null,
      selectedDate: null,
      selectedTime: '',
      loading: true,
      error: null,
      weekDays: ['D', 'L', 'M', 'M', 'J', 'V', 'S'],
      currentMonthIndex: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      barbers: [],
      services: [],
      existingReservations: [], // Reservas existentes desde el backend
      baseAvailableTimes: [
        '09:00', '09:30', '10:00', '10:30',
        '11:00', '11:30', '12:00', '12:30',
        '13:00', '13:30', '14:00', '14:30',
        '15:00', '15:30', '16:00', '16:30',
        '17:00', '17:30', '18:00'
      ]
    }
  },
  computed: {
    currentMonth() {
      const months = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
      ];
      return `${months[this.currentMonthIndex]} ${this.currentYear}`;
    },
    currentMonthDates() {
      return this.generateCalendarDates(this.currentMonthIndex, this.currentYear);
    },
    canReserve() {
      return this.selectedBarber && this.selectedService && this.selectedDate && this.selectedTime;
    },
    
    availableTimes() {
      if (!this.selectedBarber || !this.selectedDate || !this.selectedService) {
        return this.baseAvailableTimes;
      }
      
      return this.getAvailableTimesForBarberAndDate(
        this.selectedBarber.id, 
        this.selectedDate, 
        this.selectedService.duration
      );
    }
  },
  watch: {
    selectedBarber() {
      this.watchSelections();
    },
    selectedDate() {
      this.watchSelections();
    },
    selectedService() {
      this.watchSelections();
    }
  },
  async mounted() {
    await this.loadData()
  },
  methods: {
    async loadData() {
      this.loading = true
      this.error = null
      
      try {
        console.log('🔄 Cargando datos para reservas...')
        
        // Cargar servicios
        try {
          const services = await serviceService.getServices()
          console.log('📡 Respuesta de servicios:', services)
          
          if (services && Array.isArray(services)) {
            this.services = services.map(service => ({
              id: service.id,
              name: service.name || service.nombre,
              price: parseFloat(service.price || service.precio || 0),
              duration: service.duration || service.duracion || 30,
              description: service.description || service.descripcion,
              category: service.category || service.categoria
            }))
            console.log('✅ Servicios cargados:', this.services)
          } else {
            throw new Error('Formato de respuesta no válido')
          }
        } catch (error) {
          console.log('⚠️ Error cargando servicios:', error.message)
          this.loadFallbackServices()
        }
        
        // Cargar barberos
        try {
          const barbersResponse = await barberService.getBarbers()
          console.log('📡 Respuesta de barberos:', barbersResponse)
          
          const barbers = barbersResponse.barbers || barbersResponse.data || barbersResponse
          if (barbers && Array.isArray(barbers)) {
            this.barbers = barbers.map(barber => ({
              id: barber.id,
              name: barber.nombre,
              specialty: barber.especialidad || 'Barbero profesional',
              experience: barber.experiencia_anos,
              description: barber.descripcion,
              available: barber.disponible,
              activo: barber.activo
            }))
            console.log('✅ Barberos cargados:', this.barbers)
          } else {
            throw new Error('Formato de respuesta no válido')
          }
        } catch (error) {
          console.log('⚠️ Error cargando barberos:', error.message)
          this.loadFallbackBarbers()
        }
        
        // Cargar reservas existentes desde el backend
        await this.loadExistingReservations()
        
      } catch (error) {
        console.error('💥 Error cargando datos:', error)
        this.error = 'Error al cargar datos del servidor'
        this.loadFallbackData()
      } finally {
        this.loading = false
      }
    },
    
    async loadExistingReservations() {
      try {
        console.log('🔄 Cargando reservas existentes desde el backend...')
        
        const response = await reservationService.getReservations()
        console.log('📡 Respuesta del backend de reservas:', response)
        
        if (response && (response.reservations || response.data)) {
          const reservations = response.reservations || response.data || response
          
          // Mapear reservas del backend al formato que necesita el frontend
          this.existingReservations = reservations.map(reservation => {
            // Extraer fecha y hora de diferentes formatos posibles
            let date, time, duration
            
            if (reservation.fecha_reserva) {
              date = reservation.fecha_reserva
            } else if (reservation.fecha_hora) {
              const fechaHora = new Date(reservation.fecha_hora)
              date = fechaHora.toISOString().split('T')[0] // YYYY-MM-DD
              time = fechaHora.toTimeString().slice(0, 5) // HH:MM
            }
            
            if (reservation.hora_inicio) {
              time = reservation.hora_inicio.slice(0, 5) // HH:MM
            }
            
            // Obtener duración del servicio
            if (reservation.service && reservation.service.duracion) {
              duration = reservation.service.duracion
            } else if (reservation.servicio && reservation.servicio.duracion) {
              duration = reservation.servicio.duracion
            } else {
              duration = 30 // Default fallback
            }
            
            const startMinutes = this.timeToMinutes(time)
            const endMinutes = startMinutes + duration
            
            return {
              barberId: reservation.barber_id || reservation.barbero_id,
              date: date,
              time: time,
              duration: duration,
              endTime: this.minutesToTime(endMinutes)
            }
          }).filter(res => res.barberId && res.date && res.time) // Filtrar entradas válidas
          
          console.log('✅ Reservas existentes procesadas:', this.existingReservations)
        } else {
          console.log('⚠️ No hay reservas existentes o respuesta vacía')
          this.existingReservations = []
        }
        
      } catch (error) {
        console.warn('⚠️ Error cargando reservas del backend, usando datos de fallback:', error)
        
        // Fallback con reservas simuladas para desarrollo
        this.existingReservations = [
          {
            barberId: 1, // Pedro Barbero
            date: '2025-08-05',
            time: '10:00',
            duration: 45, // Corte + Barba
            endTime: '10:45'
          },
          {
            barberId: 1, // Pedro Barbero  
            date: '2025-08-05',
            time: '14:30',
            duration: 30, // Corte de cabello
            endTime: '15:00'
          },
          {
            barberId: 2, // Otro barbero
            date: '2025-08-05', 
            time: '11:00',
            duration: 20, // Arreglo de barba
            endTime: '11:20'
          }
        ]
        console.log('📅 Usando reservas de fallback:', this.existingReservations)
      }
    },
    
    loadFallbackServices() {
      console.log('⚠️ Cargando servicios de fallback')
      this.services = [
        { id: 1, name: 'Corte de Cabello', price: 25, duration: 30, category: 'Cabello' },
        { id: 2, name: 'Arreglo de Barba', price: 15, duration: 20, category: 'Barba' },
        { id: 3, name: 'Corte + Barba', price: 35, duration: 45, category: 'Paquete' },
        { id: 4, name: 'Lavado de Cabello', price: 10, duration: 15, category: 'Cabello' }
      ]
      console.log('✅ Servicios de fallback cargados:', this.services)
    },
    
    loadFallbackBarbers() {
      this.barbers = [
        { id: 1, name: 'Pedro Barbero', specialty: 'Cortes modernos y barba', experience: 5 },
        { id: 2, name: 'Carlos Estilista', specialty: 'Estilos clásicos', experience: 8 },
        { id: 3, name: 'Juan Experto', specialty: 'Barbería tradicional', experience: 10 }
      ]
    },
    
    loadFallbackData() {
      this.loadFallbackServices()
      this.loadFallbackBarbers()
    },
    generateCalendarDates(month, year) {
      const firstDay = new Date(year, month, 1);
      const lastDay = new Date(year, month + 1, 0);
      const startDate = firstDay.getDay();
      const daysInMonth = lastDay.getDate();
      
      const dates = [];
      
      // Espacios vacíos al inicio
      for (let i = 0; i < startDate; i++) {
        dates.push(null);
      }
      
      // Días del mes
      for (let day = 1; day <= daysInMonth; day++) {
        dates.push(day);
      }
      
      // Completar la cuadrícula con espacios vacíos
      while (dates.length < 42) {
        dates.push(null);
      }
      
      return dates;
    },
    selectDate(date) {
      if (!date || this.isPastDate(date)) return;
      this.selectedDate = date;
    },
    
    isPastDate(date) {
      if (!date) return false;
      const today = new Date();
      const selectedDate = new Date(this.currentYear, this.currentMonthIndex, date);
      
      // Resetear horas para comparar solo fechas
      today.setHours(0, 0, 0, 0);
      selectedDate.setHours(0, 0, 0, 0);
      
      return selectedDate < today;
    },
    previousMonth() {
      if (this.currentMonthIndex === 0) {
        this.currentMonthIndex = 11;
        this.currentYear--;
      } else {
        this.currentMonthIndex--;
      }
    },
    nextMonth() {
      if (this.currentMonthIndex === 11) {
        this.currentMonthIndex = 0;
        this.currentYear++;
      } else {
        this.currentMonthIndex++;
      }
    },
    formatSelectedDate() {
      if (!this.selectedDate) return 'Selecciona una fecha';
      const months = [
        'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
        'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
      ];
      return `${this.selectedDate} de ${months[this.currentMonthIndex]} de ${this.currentYear}`;
    },
    calculateTotal() {
      if (!this.selectedService) return '0.00';
      return this.selectedService.price.toFixed(2);
    },
    
    proceedToConfirmation() {
      console.log('🔄 proceedToConfirmation llamado');
      console.log('canReserve:', this.canReserve);
      console.log('selectedBarber:', this.selectedBarber);
      console.log('selectedService:', this.selectedService);
      console.log('selectedDate:', this.selectedDate);
      console.log('selectedTime:', this.selectedTime);
      
      if (!this.canReserve) {
        alert('Por favor complete todos los campos requeridos');
        return;
      }
      
      try {
        // Preparar datos de la reserva para pasar a la siguiente página
        const reservationData = {
          barber: this.selectedBarber,
          service: this.selectedService,
          date: this.formatDateForComparison(this.selectedDate),
          time: this.selectedTime,
          dateFormatted: this.formatSelectedDate(),
          subtotal: this.selectedService.price,
          total: parseFloat(this.calculateTotal())
        };
        
        console.log('🚀 Navegando a confirmación con datos:', reservationData);
        
        // Guardar datos en sessionStorage para pasar entre páginas
        sessionStorage.setItem('reservationData', JSON.stringify(reservationData));
        
        // Navegar a la página de confirmación
        this.$router.push('/reservas/confirmacion');
        
      } catch (error) {
        console.error('❌ Error en proceedToConfirmation:', error);
        alert('Error al procesar la reserva. Inténtalo de nuevo.');
      }
    },
    
    // Método legacy mantenido por compatibilidad
    async makeReservation() {
      if (!this.canReserve) {
        alert('Por favor complete todos los campos requeridos');
        return;
      }
      
      this.loading = true;
      
      try {
        const reservationDate = this.formatDateForComparison(this.selectedDate);
        const startMinutes = this.timeToMinutes(this.selectedTime);
        const endMinutes = startMinutes + this.selectedService.duration;
        
        // Preparar datos para el backend según formato esperado
        const reservationData = {
          barbero_id: this.selectedBarber.id, // Formato snake_case para backend
          servicio_id: this.selectedService.id,
          fecha_reserva: reservationDate, // YYYY-MM-DD
          hora_inicio: this.selectedTime + ':00', // HH:MM:SS
          notas: `Reserva creada desde la aplicación web. Servicio: ${this.selectedService.name}`
        };
        
        console.log('📡 Enviando reserva al backend:', reservationData);
        
        // Llamada real al backend
        const response = await reservationService.createReservation(reservationData);
        console.log('✅ Reserva creada exitosamente:', response);
        
        // Agregar la nueva reserva a las existentes para actualizar la disponibilidad
        this.existingReservations.push({
          barberId: this.selectedBarber.id,
          date: reservationDate,
          time: this.selectedTime,
          duration: this.selectedService.duration,
          endTime: this.minutesToTime(endMinutes)
        });
        
        // Preparar información para mostrar al usuario
        const reservation = {
          barberId: this.selectedBarber.id,
          barber: this.selectedBarber.name,
          barberSpecialty: this.selectedBarber.specialty,
          serviceId: this.selectedService.id,
          service: this.selectedService.name,
          date: this.formatSelectedDate(),
          time: this.selectedTime,
          duration: this.selectedService.duration,
          subtotal: this.selectedService.price,
          total: this.calculateTotal(),
          total: this.calculateTotal(),
          id: response.id || response.data?.id // ID de la reserva del backend
        };
        
        console.log('📅 Reservas actualizadas:', this.existingReservations);
        
        // Mostrar confirmación de éxito
        alert(`🎉 ¡Reserva confirmada exitosamente!

📅 ${reservation.date} a las ${reservation.time}
💈 Barbero: ${reservation.barber}
✂️ Servicio: ${reservation.service}
⏰ Duración: ${reservation.duration} minutos

💰 Total: Bs ${reservation.total}

🆔 ID de reserva: ${reservation.id}
¡Nos vemos pronto en Low Barber!`);
        
        // Limpiar formulario
        this.resetForm();
        
      } catch (error) {
        console.error('💥 Error al crear reserva:', error);
        
        // Manejo de errores específicos
        let errorMessage = '❌ Error al crear la reserva. ';
        
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
    },
    
    resetForm() {
      this.selectedBarber = null;
      this.selectedService = null;
      this.selectedDate = null;
      this.selectedTime = '';
    },
    
    getAvailableTimesForBarberAndDate(barberId, date, serviceDuration) {
      if (!barberId || !date || !serviceDuration) {
        return this.baseAvailableTimes;
      }
      
      const selectedDateStr = this.formatDateForComparison(date);
      console.log(`🔍 Calculando horarios disponibles para barbero ${barberId} el ${selectedDateStr} (servicio: ${serviceDuration}min)`);
      
      // Obtener reservas del barbero para la fecha seleccionada
      const barberReservations = this.existingReservations.filter(reservation => 
        reservation.barberId === barberId && reservation.date === selectedDateStr
      );
      
      console.log(`📋 Reservas existentes del barbero:`, barberReservations);
      
      // Filtrar horarios disponibles
      const availableTimes = this.baseAvailableTimes.filter(time => {
        return this.isTimeSlotAvailable(time, serviceDuration, barberReservations);
      });
      
      console.log(`✅ Horarios disponibles:`, availableTimes);
      return availableTimes;
    },
    
    isTimeSlotAvailable(startTime, serviceDuration, existingReservations) {
      const startMinutes = this.timeToMinutes(startTime);
      const endMinutes = startMinutes + serviceDuration;
      
      // Verificar si el servicio cabe antes del cierre (18:00 = 1080 minutos)
      if (endMinutes > this.timeToMinutes('18:00')) {
        return false;
      }
      
      // Verificar conflictos con reservas existentes
      for (const reservation of existingReservations) {
        const reservationStart = this.timeToMinutes(reservation.time);
        const reservationEnd = reservationStart + reservation.duration;
        
        // Verificar si hay solapamiento
        if (startMinutes < reservationEnd && endMinutes > reservationStart) {
          console.log(`❌ Conflicto: ${startTime}-${this.minutesToTime(endMinutes)} solapa con ${reservation.time}-${this.minutesToTime(reservationEnd)}`);
          return false;
        }
      }
      
      return true;
    },
    
    timeToMinutes(timeStr) {
      const [hours, minutes] = timeStr.split(':').map(Number);
      return hours * 60 + minutes;
    },
    
    minutesToTime(minutes) {
      const hours = Math.floor(minutes / 60);
      const mins = minutes % 60;
      return `${hours.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}`;
    },
    
    formatDateForComparison(date) {
      // Convertir fecha del calendario a formato YYYY-MM-DD
      const year = this.currentYear;
      const month = (this.currentMonthIndex + 1).toString().padStart(2, '0');
      const day = date.toString().padStart(2, '0');
      return `${year}-${month}-${day}`;
    },
    
    // Watchers para recalcular horarios cuando cambie barbero, fecha o servicio
    watchSelections() {
      // Limpiar hora seleccionada si ya no está disponible
      if (this.selectedTime && !this.availableTimes.includes(this.selectedTime)) {
        this.selectedTime = '';
        console.log('⚠️ Hora seleccionada ya no disponible, limpiando selección');
      }
    }
  }
}
</script>