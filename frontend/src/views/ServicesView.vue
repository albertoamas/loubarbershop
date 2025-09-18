<!--
  ServicesView - Vista de servicios rediseñada
  Página moderna que muestra todos los servicios disponibles con diseño premium
-->
<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Hero Section Mejorado con variables CSS v4 -->
    <section class="bg-[var(--color-barber-primary)] py-16 md:py-20 relative overflow-hidden">
      <!-- Elementos decorativos de fondo -->
      <div class="absolute inset-0">
        <div class="absolute top-10 left-10 w-32 h-32 bg-[var(--color-barber-gold)]/10 rounded-full blur-xl"></div>
        <div class="absolute bottom-10 right-10 w-48 h-48 bg-[var(--color-barber-gold)]/5 rounded-full blur-2xl"></div>
        <div class="absolute top-1/2 left-1/4 w-16 h-16 bg-white/10 rounded-full blur-lg"></div>
      </div>
      
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <div class="text-center">
          <!-- Logo/Nombre con estilo mejorado -->
          <div class="mb-6">
            <div class="inline-flex items-center justify-center px-4 py-2 bg-[var(--color-barber-gold)] text-[var(--color-barber-primary)] rounded-full text-sm font-bold mb-4 shadow-lg">
              ✂️ Low BarberShop
            </div>
            <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold text-white mb-4 leading-tight">
              Nuestros 
              <span class="bg-gradient-to-r from-[var(--color-barber-gold)] to-yellow-300 bg-clip-text text-transparent">
                Servicios
              </span>
            </h1>
          </div>
          
          <!-- Descripción mejorada -->
          <p class="text-gray-300 max-w-3xl mx-auto text-lg md:text-xl leading-relaxed">
            Experiencias únicas de cuidado masculino con técnicas profesionales y productos premium
          </p>
          
          <!-- Estadísticas rápidas -->
          <div class="grid grid-cols-3 gap-4 md:gap-8 max-w-2xl mx-auto mt-12">
            <div class="text-center">
              <div class="text-2xl md:text-3xl font-bold text-[var(--color-barber-gold)] mb-1">15+</div>
              <div class="text-gray-300 text-sm md:text-base">Años</div>
            </div>
            <div class="text-center">
              <div class="text-2xl md:text-3xl font-bold text-[var(--color-barber-gold)] mb-1">5★</div>
              <div class="text-gray-300 text-sm md:text-base">Calidad</div>
            </div>
            <div class="text-center">
              <div class="text-2xl md:text-3xl font-bold text-[var(--color-barber-gold)] mb-1">100%</div>
              <div class="text-gray-300 text-sm md:text-base">Satisfacción</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Loading State Mejorado -->
    <div v-if="loading" class="flex flex-col justify-center items-center py-24">
      <div class="relative">
        <div class="animate-spin rounded-full h-16 w-16 border-4 border-gray-200"></div>
        <div class="animate-spin rounded-full h-16 w-16 border-4 border-[var(--color-barber-primary)] border-t-transparent absolute inset-0"></div>
      </div>
      <p class="text-gray-600 text-lg font-medium mt-6">Cargando servicios profesionales...</p>
    </div>

    <!-- Error State Mejorado -->
    <div v-if="error" class="text-center py-24">
      <div class="max-w-md mx-auto">
        <div class="w-16 h-16 bg-yellow-100 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-3">Error al cargar servicios</h3>
        <p class="text-gray-600 mb-6">{{ error }}</p>
        <button 
          @click="loadServices" 
          class="bg-[var(--color-barber-primary)] text-white px-8 py-3 rounded-lg hover:bg-[var(--color-barber-gold)] transition-all duration-200 transform hover:scale-105 shadow-lg"
        >
          Reintentar
        </button>
      </div>
    </div>

    <!-- Sección de estadísticas modernizada -->
    <section v-if="!loading && !error" class="py-12 bg-gradient-to-br from-white to-gray-50 border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Título de la sección -->
        <div class="text-center mb-10">
          <div class="inline-flex items-center justify-center px-4 py-2 bg-[var(--color-barber-primary)] text-white rounded-full text-sm font-medium mb-4">
            📊 Nuestros Números
          </div>
          <h2 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">
            Confianza que Habla por Sí Sola
          </h2>
          <div class="w-16 h-1 bg-gradient-to-r from-[var(--color-barber-gold)] to-yellow-300 mx-auto rounded-full"></div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Servicios Disponibles -->
          <div class="group text-center bg-white rounded-3xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 border border-gray-100">
            <div class="w-16 h-16 bg-gradient-to-br from-[var(--color-barber-primary)] to-gray-700 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <div class="text-4xl lg:text-5xl font-bold text-[var(--color-barber-primary)] mb-2 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
              {{ allServices.length }}
            </div>
            <div class="text-sm lg:text-base text-gray-600 font-medium tracking-wide uppercase">
              Servicios Profesionales
            </div>
            <p class="text-gray-500 text-sm mt-2">
              Especializados en cuidado masculino
            </p>
          </div>
          
          <!-- Satisfacción Garantizada -->
          <div class="group text-center bg-white rounded-3xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 border border-gray-100">
            <div class="w-16 h-16 bg-gradient-to-br from-[var(--color-barber-gold)] to-yellow-400 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <div class="text-4xl lg:text-5xl font-bold text-[var(--color-barber-primary)] mb-2 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
              100%
            </div>
            <div class="text-sm lg:text-base text-gray-600 font-medium tracking-wide uppercase">
              Satisfacción Garantizada
            </div>
            <p class="text-gray-500 text-sm mt-2">
              O te devolvemos tu dinero
            </p>
          </div>
          
          <!-- Calificación Promedio -->
          <div class="group text-center bg-white rounded-3xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 border border-gray-100">
            <div class="w-16 h-16 bg-gradient-to-br from-green-500 to-emerald-600 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
              </svg>
            </div>
            <div class="flex items-center justify-center mb-2">
              <span class="text-4xl lg:text-5xl font-bold text-[var(--color-barber-primary)] group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">5</span>
              <div class="flex items-center ml-2">
                <svg v-for="star in 5" :key="star" class="w-6 h-6 text-[var(--color-barber-gold)]" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                </svg>
              </div>
            </div>
            <div class="text-sm lg:text-base text-gray-600 font-medium tracking-wide uppercase">
              Calificación Promedio
            </div>
            <p class="text-gray-500 text-sm mt-2">
              Basado en +500 reseñas
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Grid de servicios modernizado -->
    <section v-if="!loading && !error" class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Título de la sección -->
        <div class="text-center mb-16">
          <div class="inline-flex items-center justify-center px-4 py-2 bg-[var(--color-barber-gold)] text-[var(--color-barber-primary)] rounded-full text-sm font-bold mb-4 shadow-lg">
            ✂️ Servicios Premium
          </div>
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Elige Tu Experiencia Perfecta
          </h2>
          <div class="w-20 h-1 bg-gradient-to-r from-[var(--color-barber-gold)] to-yellow-300 mx-auto rounded-full mb-6"></div>
          <p class="text-gray-600 max-w-2xl mx-auto text-lg">
            Desde cortes clásicos hasta tratamientos premium, cada servicio está diseñado para realzar tu mejor versión
          </p>
        </div>

        <!-- Mensaje cuando no hay servicios -->
        <div v-if="allServices.length === 0" class="text-center py-20">
          <div class="max-w-md mx-auto">
            <div class="w-24 h-24 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-8">
              <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-gray-900 mb-4">Próximamente</h3>
            <p class="text-gray-600 mb-8 leading-relaxed">
              Estamos preparando nuestros servicios premium para ti.<br>
              Muy pronto tendrás disponible toda nuestra gama de tratamientos.
            </p>
          </div>
        </div>

        <!-- Grid de servicios -->
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 lg:gap-10">
          <div
            v-for="service in allServices"
            :key="service.id"
            class="group transform transition-all duration-300 hover:-translate-y-2"
          >
            <ServiceCard 
              :service="service"
              @select-service="handleServiceSelection"
              class="h-full shadow-lg hover:shadow-2xl transition-shadow duration-300"
            />
          </div>
        </div>
      </div>
    </section>

    <!-- Sección de información adicional modernizada -->
    <section class="py-20 bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 relative overflow-hidden">
      <!-- Elementos decorativos de fondo -->
      <div class="absolute inset-0">
        <div class="absolute top-10 left-10 w-32 h-32 bg-white/5 rounded-full blur-xl"></div>
        <div class="absolute bottom-10 right-10 w-48 h-48 bg-[var(--color-barber-gold)]/10 rounded-full blur-2xl"></div>
        <div class="absolute top-1/2 left-1/4 w-16 h-16 bg-white/10 rounded-full blur-lg"></div>
      </div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <!-- Contenido principal -->
          <div>
            <div class="mb-8">
              <div class="inline-flex items-center justify-center px-4 py-2 bg-[var(--color-barber-gold)] text-[var(--color-barber-primary)] rounded-full text-sm font-bold mb-6 shadow-lg">
                🏆 Excelencia Comprobada
              </div>
              <h2 class="text-4xl lg:text-5xl font-bold text-white mb-6 leading-tight">
                ¿Por qué elegir 
                <span class="bg-gradient-to-r from-[var(--color-barber-gold)] to-yellow-300 bg-clip-text text-transparent">
                  Low Barber?
                </span>
              </h2>
              <p class="text-gray-300 text-lg leading-relaxed">
                Más que un corte de cabello, ofrecemos una experiencia premium que combina tradición, innovación y atención personalizada.
              </p>
            </div>

            <div class="space-y-8">
              <!-- Barberos Profesionales -->
              <div class="flex items-start space-x-6 group">
                <div class="flex-shrink-0">
                  <div class="w-16 h-16 bg-gradient-to-br from-[var(--color-barber-primary)] to-gray-700 rounded-2xl flex items-center justify-center backdrop-blur-sm border border-white/10 group-hover:scale-110 transition-transform duration-300">
                    <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                  </div>
                </div>
                <div>
                  <h3 class="text-xl font-bold text-white mb-3 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
                    Barberos Profesionales
                  </h3>
                  <p class="text-gray-300 leading-relaxed">
                    Nuestro equipo cuenta con más de 15 años de experiencia y formación continua en las últimas tendencias y técnicas especializadas.
                  </p>
                </div>
              </div>
              
              <!-- Productos Premium -->
              <div class="flex items-start space-x-6 group">
                <div class="flex-shrink-0">
                  <div class="w-16 h-16 bg-gradient-to-br from-[var(--color-barber-gold)] to-yellow-500 rounded-2xl flex items-center justify-center backdrop-blur-sm border border-white/10 group-hover:scale-110 transition-transform duration-300">
                    <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/>
                    </svg>
                  </div>
                </div>
                <div>
                  <h3 class="text-xl font-bold text-white mb-3 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
                    Productos Premium
                  </h3>
                  <p class="text-gray-300 leading-relaxed">
                    Utilizamos únicamente productos de las mejores marcas internacionales que cuidan tu cabello y piel con ingredientes de primera calidad.
                  </p>
                </div>
              </div>
              
              <!-- Horarios Flexibles -->
              <div class="flex items-start space-x-6 group">
                <div class="flex-shrink-0">
                  <div class="w-16 h-16 bg-gradient-to-br from-blue-600 to-indigo-700 rounded-2xl flex items-center justify-center backdrop-blur-sm border border-white/10 group-hover:scale-110 transition-transform duration-300">
                    <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                  </div>
                </div>
                <div>
                  <h3 class="text-xl font-bold text-white mb-3 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
                    Horarios Flexibles
                  </h3>
                  <p class="text-gray-300 leading-relaxed">
                    Reserva tu cita en el horario que mejor se adapte a tu rutina diaria. Abierto de lunes a sábado con horarios extendidos.
                  </p>
                </div>
              </div>

              <!-- Ambiente Exclusivo -->
              <div class="flex items-start space-x-6 group">
                <div class="flex-shrink-0">
                  <div class="w-16 h-16 bg-gradient-to-br from-purple-600 to-pink-600 rounded-2xl flex items-center justify-center backdrop-blur-sm border border-white/10 group-hover:scale-110 transition-transform duration-300">
                    <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
                    </svg>
                  </div>
                </div>
                <div>
                  <h3 class="text-xl font-bold text-white mb-3 group-hover:text-[var(--color-barber-gold)] transition-colors duration-300">
                    Ambiente Exclusivo
                  </h3>
                  <p class="text-gray-300 leading-relaxed">
                    Disfruta de un ambiente masculino sofisticado y relajante, diseñado especialmente para tu comodidad y privacidad.
                  </p>
                </div>
              </div>
            </div>

            <!-- Call to Action -->
            <div class="mt-12 pt-8 border-t border-white/20">
              <div class="flex flex-col sm:flex-row gap-4">
                <button class="flex-1 bg-[var(--color-barber-gold)] text-[var(--color-barber-primary)] px-8 py-4 rounded-2xl font-bold hover:bg-yellow-300 transition-all duration-200 transform hover:scale-105 shadow-lg">
                  Reservar Ahora
                </button>
                <button class="flex-1 bg-transparent border-2 border-white/30 text-white px-8 py-4 rounded-2xl font-bold hover:bg-white/10 transition-all duration-200">
                  Ver Horarios
                </button>
              </div>
            </div>
          </div>

          <!-- Imagen/Estadísticas -->
          <div class="relative">
            <div class="bg-gradient-to-br from-white/10 to-white/5 backdrop-blur-sm border border-white/20 rounded-3xl p-8 shadow-2xl">
              <!-- Estadísticas Grid -->
              <div class="grid grid-cols-2 gap-8 mb-8">
                <div class="text-center">
                  <div class="text-4xl font-bold text-white mb-2">15+</div>
                  <div class="text-gray-300 text-sm">Años de experiencia</div>
                </div>
                <div class="text-center">
                  <div class="text-4xl font-bold text-white mb-2">2K+</div>
                  <div class="text-gray-300 text-sm">Clientes satisfechos</div>
                </div>
                <div class="text-center">
                  <div class="text-4xl font-bold text-white mb-2">95%</div>
                  <div class="text-gray-300 text-sm">Clientes recurrentes</div>
                </div>
                <div class="text-center">
                  <div class="text-4xl font-bold text-white mb-2">24h</div>
                  <div class="text-gray-300 text-sm">Respuesta promedio</div>
                </div>
              </div>
              
              <!-- Separador -->
              <div class="border-t border-white/20 mb-8"></div>
              
              <!-- Contacto rápido -->
              <div class="text-center">
                <h4 class="text-lg font-bold text-white mb-6">¿Necesitas ayuda personalizada?</h4>
                <div class="space-y-4">
                  <div class="flex items-center justify-center space-x-3">
                    <div class="w-10 h-10 bg-[var(--color-barber-gold)] rounded-full flex items-center justify-center">
                      <svg class="w-5 h-5 text-[var(--color-barber-primary)]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                      </svg>
                    </div>
                    <span class="text-white font-medium">+591 77872911</span>
                  </div>
                  <div class="flex items-center justify-center space-x-3">
                    <div class="w-10 h-10 bg-green-500 rounded-full flex items-center justify-center">
                      <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/>
                        <path d="M11.893 0C5.333 0 0 5.333 0 11.893c0 2.096.547 4.142 1.588 5.946L.057 24l6.305-1.654C8.098 23.5 10.059 24 12.05 24c6.557 0 11.890-5.335 11.893-11.892C23.946 5.651 18.61.344 12.05.343 11.997.343 11.945.343 11.893 0z"/>
                      </svg>
                    </div>
                    <span class="text-white font-medium">WhatsApp</span>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Elemento decorativo -->
            <div class="absolute -bottom-6 -right-6 w-24 h-24 bg-[var(--color-barber-gold)]/20 rounded-full blur-2xl"></div>
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
