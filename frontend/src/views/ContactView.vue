<!--
  ContactView - Vista de contacto
  Información de contacto y formulario
-->
<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Hero Section -->
    <section class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h1 class="text-4xl lg:text-5xl font-bold text-black mb-4">
            Contáctanos
          </h1>
          <p class="text-lg text-gray-600 max-w-2xl mx-auto">
            Estamos aquí para ayudarte. Ponte en contacto con nosotros para cualquier consulta
          </p>
        </div>
      </div>
    </section>

    <!-- Información de contacto -->
    <section class="py-16 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-16">
          <!-- Ubicación -->
          <div class="bg-white p-8 rounded-2xl shadow-lg text-center">
            <div class="w-16 h-16 bg-black rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-black mb-2">Ubicación</h3>
            <p class="text-gray-600">
              Calle Principal 123<br>
              Centro de la Ciudad<br>
              Bogotá, Colombia
            </p>
          </div>

          <!-- Teléfono -->
          <div class="bg-white p-8 rounded-2xl shadow-lg text-center">
            <div class="w-16 h-16 bg-black rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-black mb-2">Teléfono</h3>
            <p class="text-gray-600">
              <a href="tel:+573001234567" class="hover:text-black transition-colors">
                +57 300 123 4567
              </a><br>
              <a href="tel:+5716012345" class="hover:text-black transition-colors">
                +57 (1) 601 2345
              </a>
            </p>
          </div>

          <!-- Email -->
          <div class="bg-white p-8 rounded-2xl shadow-lg text-center">
            <div class="w-16 h-16 bg-black rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-black mb-2">Email</h3>
            <p class="text-gray-600">
              <a href="mailto:info@lowbarber.com" class="hover:text-black transition-colors">
                info@lowbarber.com
              </a><br>
              <a href="mailto:reservas@lowbarber.com" class="hover:text-black transition-colors">
                reservas@lowbarber.com
              </a>
            </p>
          </div>
        </div>

        <!-- Formulario de contacto y mapa -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <!-- Formulario de contacto -->
          <div>
            <h2 class="text-3xl font-bold text-black mb-6">
              Envíanos un mensaje
            </h2>
            <form @submit.prevent="submitContact" class="space-y-6">
              <!-- Información personal -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-black mb-2">
                    Nombre *
                  </label>
                  <input
                    v-model="form.name"
                    type="text"
                    required
                    class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-black focus:border-transparent"
                    placeholder="Tu nombre completo"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-black mb-2">
                    Teléfono
                  </label>
                  <input
                    v-model="form.phone"
                    type="tel"
                    class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-black focus:border-transparent"
                    placeholder="+57 300 123 4567"
                  />
                </div>
              </div>

              <!-- Email -->
              <div>
                <label class="block text-sm font-medium text-black mb-2">
                  Email *
                </label>
                <input
                  v-model="form.email"
                  type="email"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-black focus:border-transparent"
                  placeholder="tu@email.com"
                />
              </div>

              <!-- Asunto -->
              <div>
                <label class="block text-sm font-medium text-black mb-2">
                  Asunto *
                </label>
                <select
                  v-model="form.subject"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-black focus:border-transparent"
                >
                  <option value="">Selecciona un asunto</option>
                  <option value="reserva">Consulta sobre reservas</option>
                  <option value="servicios">Información sobre servicios</option>
                  <option value="productos">Consulta sobre productos</option>
                  <option value="reclamo">Reclamo o queja</option>
                  <option value="sugerencia">Sugerencia</option>
                  <option value="otro">Otro</option>
                </select>
              </div>

              <!-- Mensaje -->
              <div>
                <label class="block text-sm font-medium text-black mb-2">
                  Mensaje *
                </label>
                <textarea
                  v-model="form.message"
                  required
                  rows="6"
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-black focus:border-transparent"
                  placeholder="Escribe tu mensaje aquí..."
                ></textarea>
              </div>

              <!-- Botón de envío -->
              <div>
                <button
                  type="submit"
                  :disabled="isSubmitting"
                  class="w-full bg-black text-white px-8 py-4 rounded-xl font-medium hover:bg-gray-800 transition-all duration-200"
                >
                  {{ isSubmitting ? 'Enviando...' : 'Enviar Mensaje' }}
                </button>
              </div>
            </form>
          </div>

          <!-- Mapa e información adicional -->
          <div class="space-y-6">
            <!-- Mapa placeholder -->
            <div class="aspect-video bg-gray-200 rounded-2xl overflow-hidden">
              <div class="w-full h-full bg-gradient-to-br from-gray-100 to-gray-300 flex items-center justify-center">
                <div class="text-center text-gray-500">
                  <svg class="w-16 h-16 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                  </svg>
                  <p class="text-sm">Mapa de ubicación</p>
                  <p class="text-xs mt-1">Calle Principal 123, Centro</p>
                </div>
              </div>
            </div>

            <!-- Horarios detallados -->
            <div class="bg-white p-6 rounded-2xl shadow-lg">
              <h3 class="text-xl font-semibold text-black mb-4">
                Horarios de Atención
              </h3>
              <div class="space-y-3">
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">Lunes</span>
                  <span class="text-black font-medium">9:00 AM - 7:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">Martes</span>
                  <span class="text-black font-medium">9:00 AM - 7:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">Miércoles</span>
                  <span class="text-black font-medium">9:00 AM - 7:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">Jueves</span>
                  <span class="text-black font-medium">9:00 AM - 7:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">Viernes</span>
                  <span class="text-black font-medium">9:00 AM - 7:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">Sábado</span>
                  <span class="text-black font-medium">9:00 AM - 5:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-gray-600">Domingo</span>
                  <span class="text-black font-medium">10:00 AM - 3:00 PM</span>
                </div>
              </div>
            </div>

            <!-- Redes sociales -->
            <div class="bg-white p-6 rounded-2xl shadow-lg">
              <h3 class="text-xl font-semibold text-black mb-4">
                Síguenos en Redes Sociales
              </h3>
              <div class="flex space-x-4">
                <a href="#" class="w-12 h-12 bg-black rounded-lg flex items-center justify-center text-white hover:bg-gray-800 transition-colors">
                  <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
                  </svg>
                </a>
                <a href="#" class="w-12 h-12 bg-black rounded-lg flex items-center justify-center text-white hover:bg-gray-800 transition-colors">
                  <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                  </svg>
                </a>
                <a href="#" class="w-12 h-12 bg-black rounded-lg flex items-center justify-center text-white hover:bg-gray-800 transition-colors">
                  <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.885 3.488"/>
                  </svg>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'ContactView',
  data() {
    return {
      isSubmitting: false,
      form: {
        name: '',
        phone: '',
        email: '',
        subject: '',
        message: ''
      }
    }
  },
  methods: {
    async submitContact() {
      this.isSubmitting = true
      
      try {
        // Simular envío del formulario
        await new Promise(resolve => setTimeout(resolve, 2000))
        
        // Aquí iría la lógica para enviar el mensaje al backend
        console.log('Mensaje enviado:', this.form)
        
        // Mostrar mensaje de éxito
        alert('¡Mensaje enviado exitosamente! Te responderemos pronto.')
        
        // Resetear formulario
        this.resetForm()
        
      } catch (error) {
        console.error('Error al enviar mensaje:', error)
        alert('Hubo un error al enviar tu mensaje. Por favor, intenta nuevamente.')
      } finally {
        this.isSubmitting = false
      }
    },
    resetForm() {
      this.form = {
        name: '',
        phone: '',
        email: '',
        subject: '',
        message: ''
      }
    }
  }
}
</script>
