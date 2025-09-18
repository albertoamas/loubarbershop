<!--
  AboutView - Vista de información sobre la barbería
  Página que muestra la historia, misión y equipo de Lou Barbershop
-->
<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Hero Section -->
    <section class="py-24 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h1 class="text-4xl lg:text-5xl font-bold text-black mb-4">
            Sobre Lou Barbershop
          </h1>
          <p class="text-lg text-gray-600 max-w-3xl mx-auto">
            Conoce nuestra historia, nuestra pasión por el arte de la barbería y el equipo 
            que hace posible cada experiencia única.
          </p>
        </div>
      </div>
    </section>

    <!-- Nuestra Historia -->
    <section class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 class="text-3xl lg:text-4xl font-bold text-black mb-6">
              Nuestra Historia
            </h2>
            <div class="space-y-4 text-gray-600 leading-relaxed">
              <p>
                Lou Barbershop nació con la visión de revivir la tradición clásica de la barbería 
                masculina, combinándola con las técnicas y estilos más modernos. Desde nuestros 
                inicios, hemos mantenido el compromiso de ofrecer no solo un corte de cabello, 
                sino una experiencia completa de cuidado personal.
              </p>
              <p>
                Nuestro fundador, inspirado por las barberías tradicionales europeas, decidió 
                crear un espacio donde cada hombre pudiera sentirse cómodo, relajado y 
                completamente atendido por profesionales que entienden la importancia de 
                la imagen personal.
              </p>
              <p>
                Hoy, somos reconocidos como una de las barberías premium de la ciudad, 
                manteniendo siempre nuestros valores de calidad, profesionalismo y 
                atención personalizada.
              </p>
            </div>
          </div>
          <div class="aspect-video lg:aspect-square bg-gray-200 rounded-2xl overflow-hidden shadow-lg">
            <div class="w-full h-full bg-gradient-to-br from-gray-100 to-gray-300 flex items-center justify-center">
              <div class="text-center text-gray-500">
                <svg class="w-16 h-16 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
                </svg>
                <p class="text-sm">Historia de Lou Barbershop</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Misión y Valores -->
    <section class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl lg:text-4xl font-bold text-black mb-4">
            Nuestra Misión y Valores
          </h2>
          <p class="text-lg text-gray-600">
            Los principios que guían nuestro trabajo diario
          </p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Misión -->
          <div class="bg-white p-8 rounded-2xl shadow-lg text-center">
            <div class="w-16 h-16 bg-[var(--color-barber-primary)] rounded-full flex items-center justify-center mx-auto mb-6">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-black mb-4">Misión</h3>
            <p class="text-gray-600 leading-relaxed">
              Brindar servicios de barbería de la más alta calidad, creando experiencias 
              únicas que fortalezcan la confianza y el estilo personal de cada cliente.
            </p>
          </div>

          <!-- Calidad -->
          <div class="bg-white p-8 rounded-2xl shadow-lg text-center">
            <div class="w-16 h-16 bg-[var(--color-barber-gold)] rounded-full flex items-center justify-center mx-auto mb-6">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-black mb-4">Calidad</h3>
            <p class="text-gray-600 leading-relaxed">
              Utilizamos solo productos premium y técnicas profesionales para garantizar 
              resultados excepcionales en cada servicio que ofrecemos.
            </p>
          </div>

          <!-- Pasión -->
          <div class="bg-white p-8 rounded-2xl shadow-lg text-center">
            <div class="w-16 h-16 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-6">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-black mb-4">Pasión</h3>
            <p class="text-gray-600 leading-relaxed">
              Cada corte es una obra de arte. Nuestro equipo vive y respira la barbería, 
              manteniéndose siempre actualizado con las últimas tendencias.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Nuestro Equipo -->
    <section class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl lg:text-4xl font-bold text-black mb-4">
            Nuestro Equipo
          </h2>
          <p class="text-lg text-gray-600">
            Conoce a los maestros barberos que harán realidad tu estilo ideal
          </p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Barbero 1 -->
          <div class="bg-white p-6 rounded-2xl shadow-lg text-center">
            <div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4 overflow-hidden">
              <div class="w-full h-full bg-gradient-to-br from-gray-100 to-gray-300 flex items-center justify-center">
                <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
              </div>
            </div>
            <h3 class="text-xl font-semibold text-black mb-2">Carlos Rodríguez</h3>
            <p class="text-sm text-[var(--color-barber-gold)] font-medium mb-3">Maestro Barbero - 15 años</p>
            <p class="text-gray-600 text-sm leading-relaxed">
              Especialista en cortes clásicos y modernos. Su experiencia y técnica 
              refinada lo convierten en uno de los barberos más solicitados.
            </p>
          </div>

          <!-- Barbero 2 -->
          <div class="bg-white p-6 rounded-2xl shadow-lg text-center">
            <div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4 overflow-hidden">
              <div class="w-full h-full bg-gradient-to-br from-gray-100 to-gray-300 flex items-center justify-center">
                <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
              </div>
            </div>
            <h3 class="text-xl font-semibold text-black mb-2">Miguel Torres</h3>
            <p class="text-sm text-blue-600 font-medium mb-3">Barbero Senior - 10 años</p>
            <p class="text-gray-600 text-sm leading-relaxed">
              Experto en afeitado clásico y styling de barba. Su precisión y 
              atención al detalle garantizan resultados perfectos.
            </p>
          </div>

          <!-- Barbero 3 -->
          <div class="bg-white p-6 rounded-2xl shadow-lg text-center">
            <div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4 overflow-hidden">
              <div class="w-full h-full bg-gradient-to-br from-gray-100 to-gray-300 flex items-center justify-center">
                <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
              </div>
            </div>
            <h3 class="text-xl font-semibold text-black mb-2">Andrés Gómez</h3>
            <p class="text-sm text-green-600 font-medium mb-3">Barbero Junior - 5 años</p>
            <p class="text-gray-600 text-sm leading-relaxed">
              Especialista en tendencias actuales y estilos juveniles. Su creatividad 
              y energía aportan frescura a cada servicio.
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'AboutView'
}
</script>
