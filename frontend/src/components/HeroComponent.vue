<!--
  Hero Section - Sección principal de presentación
  Actualizado para usar Tailwind CSS v4 con clases estándar
-->
<template>
  <section class="relative bg-gray-100 overflow-hidden">
    <!-- Contenido principal -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="py-20 lg:py-32">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <!-- Contenido de texto -->
          <div class="text-center lg:text-left">
            <!-- Badge premium -->
            <div class="inline-flex items-center justify-center px-4 py-2 bg-black text-white rounded-full text-sm font-medium mb-6 heartbeat">
              <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 16 16">
                <path d="M3.5 3.5c-.614-.884-.074-1.962.858-2.5L8 7.226 11.642 1c.932.538 1.472 1.616.858 2.5L8.81 8.61l1.556 2.661a2.5 2.5 0 1 1-.794.637L8 9.73l-1.572 2.177a2.5 2.5 0 1 1-.794-.637L7.19 8.61 3.5 3.5zm2.5 10a1.5 1.5 0 1 0-3 0 1.5 1.5 0 0 0 3 0zm7 0a1.5 1.5 0 1 0-3 0 1.5 1.5 0 0 0 3 0z"/>
              </svg>
              BARBERÍA PREMIUM
            </div>

            <h1 class="text-4xl lg:text-6xl font-bold text-black mb-8 leading-tight">
              Estilo y Confianza
              <br>
              <span class="text-black">en Cada Corte</span>
            </h1>

            <!-- Separadores decorativos -->
            <div class="flex items-center justify-center lg:justify-start mb-8">
              <div class="w-40 h-0.5 bg-black"></div>
              <div class="w-8 h-8 mx-6 flex items-center justify-center">
                <svg class="w-6 h-6 text-black" fill="currentColor" viewBox="0 0 16 16">
                  <path d="M3.5 3.5c-.614-.884-.074-1.962.858-2.5L8 7.226 11.642 1c.932.538 1.472 1.616.858 2.5L8.81 8.61l1.556 2.661a2.5 2.5 0 1 1-.794.637L8 9.73l-1.572 2.177a2.5 2.5 0 1 1-.794-.637L7.19 8.61 3.5 3.5zm2.5 10a1.5 1.5 0 1 0-3 0 1.5 1.5 0 0 0 3 0zm7 0a1.5 1.5 0 1 0-3 0 1.5 1.5 0 0 0 3 0z"/>
                </svg>
              </div>
              <div class="w-40 h-0.5 bg-black"></div>
            </div>

            <p class="text-lg lg:text-xl text-gray-600 mb-8 max-w-lg mx-auto lg:mx-0">
              En <span class="font-semibold text-black">Lou Barbershop</span> ofrecemos el mejor servicio de barbería 
              con estilo moderno y ambiente acogedor. Nuestros barberos 
              expertos harán que luzcas y te sientas mejor.
            </p>
            
            <!-- Botones de acción -->
            <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <RouterLink to="/reservas" class="bg-black text-white text-lg px-8 py-4 rounded-xl font-medium hover:bg-gray-800 transition-all duration-200 inline-block text-center">
                Reservar Cita
              </RouterLink>
              <RouterLink to="/servicios" class="bg-gray-200 text-black text-lg px-8 py-4 rounded-xl font-medium hover:bg-gray-300 transition-all duration-200 inline-block text-center">
                Ver Servicios
              </RouterLink>
            </div>
          </div>

          <!-- Imagen/Gráfico -->
          <div class="relative">
            <div class="aspect-square lg:aspect-[4/3] bg-gray-200 rounded-2xl overflow-hidden shadow-lg">
              <!-- Logo de la barbería -->
              <img 
                src="@/assets/images/logo-barber.jpg" 
                alt="Logo Low Barber - Barbería Premium"
                class="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
                @error="handleImageError"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Sección de características -->
  <section class="py-16 bg-gray-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Encabezado -->
      <div class="text-center mb-12">
        <div class="inline-flex items-center justify-center px-4 py-2 bg-black text-white rounded-full text-sm font-medium mb-6">
          <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
          </svg>
          ¿Por qué elegirnos?
        </div>
        <h2 class="text-4xl font-bold text-black mb-4">
          Excelencia en Cada Detalle
        </h2>
        <div class="w-16 h-0.5 bg-black mx-auto mb-4"></div>
        <p class="text-lg text-gray-600">
          Descubre lo que nos hace únicos en cada servicio que ofrecemos
        </p>
      </div>

      <!-- Características -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Característica 1 -->
        <div class="bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-2 text-center">
          <div class="w-20 h-20 bg-yellow-500 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1m4 0h1m-6 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-black mb-4">Barberos Expertos</h3>
          <p class="text-gray-600 mb-6 leading-relaxed">
            Nuestro equipo está formado por profesionales con años de experiencia en las últimas tendencias y técnicas de corte.
          </p>
          <div class="flex items-center justify-center text-sm bg-yellow-50 rounded-lg p-3">
            <svg class="w-4 h-4 text-yellow-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
            </svg>
            <span class="text-gray-700 font-medium">Certificados profesionales</span>
          </div>
        </div>

        <!-- Característica 2 -->
        <div class="bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-2 text-center">
          <div class="w-20 h-20 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-black mb-4">Reserva Online</h3>
          <p class="text-gray-600 mb-6 leading-relaxed">
            Agenda tu cita en minutos desde cualquier dispositivo y a cualquier hora. Sistema moderno y fácil de usar.
          </p>
          <div class="flex items-center justify-center text-sm bg-blue-50 rounded-lg p-3">
            <svg class="w-4 h-4 text-blue-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            <span class="text-gray-700 font-medium">Disponible 24/7</span>
          </div>
        </div>

        <!-- Característica 3 -->
        <div class="bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-2 text-center">
          <div class="w-20 h-20 bg-green-600 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-black mb-4">Satisfacción Garantizada</h3>
          <p class="text-gray-600 mb-6 leading-relaxed">
            Tu satisfacción es nuestra prioridad. Nos aseguramos de que salgas feliz con tu nuevo look y experiencia.
          </p>
          <div class="flex items-center justify-center text-sm bg-green-50 rounded-lg p-3">
            <svg class="w-4 h-4 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            <span class="text-gray-700 font-medium">100% de satisfacción</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeroComponent',
  methods: {
    handleImageError(event) {
      // Si la imagen no carga, mostrar un placeholder
      event.target.style.display = 'none'
      event.target.parentElement.innerHTML = `
        <div class="w-full h-full bg-gray-300 flex items-center justify-center">
          <div class="text-center">
            <svg class="w-16 h-16 text-gray-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            <p class="text-gray-500 text-sm font-medium">Low Barbershop</p>
            <p class="text-gray-400 text-xs">Imagen no disponible</p>
          </div>
        </div>
      `
    }
  }
}
</script>

<style scoped>
.heartbeat {
  animation: heartbeat 3s ease-in-out infinite;
}

@keyframes heartbeat {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}
</style>
