<!--
  ReservationsView - Vista de reservas estilo Figma v2
  Página de reservas con diseño tipo checkout
-->
<template>
  <div class="min-h-screen bg-gray-100">
    <div class="container mx-auto px-6 py-8">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Columna principal -->
        <div class="lg:col-span-2">
          <!-- Título -->
          <h1 class="text-4xl font-bold text-gray-900 mb-8">Reserva tu cita</h1>

          <!-- Selección de barbero -->
          <div class="mb-8">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">Selecciona un barbero</h2>
            <div class="relative">
              <select
                v-model="selectedBarber"
                class="w-full px-4 py-4 bg-white border border-gray-200 rounded-xl text-gray-600 appearance-none focus:outline-none focus:ring-0 focus:border-gray-400 transition-colors"
              >
                <option :value="null">Selecciona un barbero</option>
                <option 
                  v-for="barber in barbers" 
                  :key="barber.id" 
                  :value="barber"
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
          </div>

          <!-- Selección de servicio -->
          <div class="mb-8">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">Selecciona un servicio</h2>
            <div class="relative">
              <select
                v-model="selectedService"
                class="w-full px-4 py-4 bg-white border border-gray-200 rounded-xl text-gray-600 appearance-none focus:outline-none focus:ring-0 focus:border-gray-400 transition-colors"
              >
                <option :value="null">Selecciona un servicio</option>
                <option 
                  v-for="service in services" 
                  :key="service.id" 
                  :value="service"
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
          </div>

          <!-- Selección de fecha y hora -->
          <div class="mb-8">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">Selecciona fecha y hora</h2>
            
            <!-- Calendario -->
            <div class="bg-white rounded-xl p-6 mb-6">
              <div class="flex items-center justify-between mb-6">
                <button @click="previousMonth" class="p-2 hover:bg-gray-100 rounded-lg transition-colors">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                  </svg>
                </button>
                <h3 class="text-lg font-semibold text-gray-900">{{ currentMonth }}</h3>
                <button @click="nextMonth" class="p-2 hover:bg-gray-100 rounded-lg transition-colors">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                  </svg>
                </button>
              </div>
              
              <div class="grid grid-cols-7 gap-2 mb-4">
                <div v-for="day in weekDays" :key="day" class="text-center text-sm font-medium text-gray-500 p-2">
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
                    'p-3 text-center text-sm rounded-lg transition-colors',
                    selectedDate === date 
                      ? 'bg-black text-white' 
                      : !date || isPastDate(date)
                      ? 'text-gray-300 cursor-not-allowed'
                      : 'text-gray-700 hover:bg-gray-100 cursor-pointer',
                    !date ? 'invisible' : ''
                  ]"
                >
                  {{ date }}
                </button>
              </div>
            </div>

            <!-- Selector de hora -->
            <div class="relative">
              <select
                v-model="selectedTime"
                class="w-full px-4 py-4 bg-white border border-gray-200 rounded-xl text-gray-600 appearance-none focus:outline-none focus:ring-0 focus:border-gray-400 transition-colors"
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
            
            <!-- Información de disponibilidad -->
            <div v-if="selectedBarber && selectedService && selectedDate" class="mt-3 text-sm text-gray-600">
              <div class="flex items-center gap-2">
                <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <span>{{ availableTimes.length }} horarios disponibles para {{ selectedService.name }} ({{ selectedService.duration }}min)</span>
              </div>
              <div v-if="availableTimes.length === 0" class="mt-2 text-red-600">
                ⚠️ No hay horarios disponibles para este día. Prueba otra fecha.
              </div>
            </div>
          </div>
        </div>

        <!-- Panel lateral de resumen -->
        <div class="lg:col-span-1">
          <div class="bg-white rounded-xl p-6 sticky top-8">
            <!-- Loading state -->
            <div v-if="loading" class="text-center py-8">
              <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900 mx-auto"></div>
              <p class="text-gray-500 mt-2">Cargando...</p>
            </div>
            
            <!-- Content -->
            <div v-else>
              <!-- Información del barbero y servicio -->
              <div class="flex items-center justify-between mb-6">
                <div class="flex-1">
                  <div class="text-sm text-gray-500">Barbero</div>
                  <div class="text-lg font-semibold text-gray-900">
                    {{ selectedBarber?.name || 'Selecciona un barbero' }}
                  </div>
                  <div class="text-sm text-gray-500">
                    {{ selectedBarber?.specialty || '' }}
                  </div>
                  <div class="text-sm text-gray-500 mt-2">Servicio</div>
                  <div class="text-base font-medium text-gray-900">
                    {{ selectedService?.name || 'Selecciona un servicio' }}
                  </div>
                  <div class="text-sm text-gray-500">
                    {{ selectedService?.category || '' }}
                  </div>
                </div>
                <div class="w-16 h-16 bg-gray-300 rounded-full flex items-center justify-center ml-4">
                  <svg class="w-8 h-8 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                  </svg>
                </div>
              </div>

              <!-- Información de la cita -->
              <div class="space-y-4 mb-6">
                <div class="flex justify-between">
                  <span class="text-gray-500">Fecha</span>
                  <span class="text-gray-900">{{ formatSelectedDate() }}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-500">Hora</span>
                  <span class="text-gray-900">{{ selectedTime || 'Selecciona una hora' }}</span>
                </div>
                <div class="flex justify-between" v-if="selectedService">
                  <span class="text-gray-500">Duración</span>
                  <span class="text-gray-900">{{ selectedService.duration }} min</span>
                </div>
              </div>

              <!-- Resumen del pedido -->
              <div class="border-t pt-4 mb-6">
                <h3 class="text-lg font-semibold text-gray-900 mb-4">Resumen del pedido</h3>
                <div class="space-y-2">
                  <div class="flex justify-between">
                    <span class="text-gray-600">{{ selectedService?.name || 'Servicio' }}</span>
                    <span class="text-gray-600">{{ selectedService?.duration || '30' }} min</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Subtotal</span>
                    <span class="text-gray-900">Bs {{ selectedService?.price || 25 }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Impuestos (10%)</span>
                    <span class="text-gray-900">Bs {{ calculateTax() }}</span>
                  </div>
                  <div class="border-t pt-2">
                    <div class="flex justify-between font-semibold">
                      <span class="text-gray-900">Total</span>
                      <span class="text-gray-900">Bs {{ calculateTotal() }}</span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Botón de reservar -->
              <button
                @click="makeReservation"
                :disabled="!canReserve"
                class="w-full bg-black text-white py-4 rounded-xl font-medium hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                {{ canReserve ? 'Reservar Cita' : 'Complete todos los campos' }}
              </button>
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
    calculateTax() {
      if (!this.selectedService) return '0.00';
      const tax = (this.selectedService.price * 0.10).toFixed(2);
      return tax;
    },
    calculateTotal() {
      if (!this.selectedService) return '0.00';
      const subtotal = this.selectedService.price;
      const tax = parseFloat(this.calculateTax());
      return (subtotal + tax).toFixed(2);
    },
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
          tax: this.calculateTax(),
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

💰 Subtotal: Bs ${reservation.subtotal}
📊 Impuestos: Bs ${reservation.tax}
💵 Total: Bs ${reservation.total}

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