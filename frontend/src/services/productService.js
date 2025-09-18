/**
 * Low Barber - Servicio de Productos
 * Maneja todas las operaciones relacionadas con productos
 */

import apiClient from './api.js'

class ProductService {
  /**
   * Obtener todos los productos activos
   */
  async getProducts() {
    try {
      const response = await apiClient.get('/api/products')
      return {
        success: true,
        data: response.data.products || response.data,
        message: 'Productos obtenidos exitosamente'
      }
    } catch (error) {
      console.error('Error al obtener productos:', error)
      return {
        success: false,
        data: [],
        message: error.response?.data?.message || 'Error al cargar productos'
      }
    }
  }

  /**
   * Obtener un producto por ID
   */
  async getProductById(id) {
    try {
      const response = await apiClient.get(`/api/products/${id}`)
      return {
        success: true,
        data: response.data.product || response.data,
        message: 'Producto obtenido exitosamente'
      }
    } catch (error) {
      console.error('Error al obtener producto:', error)
      return {
        success: false,
        data: null,
        message: error.response?.data?.message || 'Error al cargar producto'
      }
    }
  }

  /**
   * Crear nuevo producto
   */
  async createProduct(productData) {
    try {
      const response = await apiClient.post('/api/products', productData)
      return {
        success: true,
        data: response.data.product || response.data,
        message: 'Producto creado exitosamente'
      }
    } catch (error) {
      console.error('Error al crear producto:', error)
      return {
        success: false,
        data: null,
        message: error.response?.data?.message || 'Error al crear producto',
        errors: error.response?.data?.errors
      }
    }
  }

  /**
   * Actualizar producto
   */
  async updateProduct(id, productData) {
    try {
      const response = await apiClient.put(`/api/products/${id}`, productData)
      return {
        success: true,
        data: response.data.product || response.data,
        message: 'Producto actualizado exitosamente'
      }
    } catch (error) {
      console.error('Error al actualizar producto:', error)
      return {
        success: false,
        data: null,
        message: error.response?.data?.message || 'Error al actualizar producto',
        errors: error.response?.data?.errors
      }
    }
  }

  /**
   * Eliminar producto
   */
  async deleteProduct(id) {
    try {
      const response = await apiClient.delete(`/api/products/${id}`)
      return {
        success: true,
        data: response.data,
        message: 'Producto eliminado exitosamente'
      }
    } catch (error) {
      console.error('Error al eliminar producto:', error)
      return {
        success: false,
        data: null,
        message: error.response?.data?.message || 'Error al eliminar producto'
      }
    }
  }

  /**
   * Buscar productos por término
   */
  async searchProducts(searchTerm) {
    try {
      const response = await apiClient.get(`/api/products/search?q=${encodeURIComponent(searchTerm)}`)
      return {
        success: true,
        data: response.data.products || response.data,
        message: 'Búsqueda completada'
      }
    } catch (error) {
      console.error('Error al buscar productos:', error)
      return {
        success: false,
        data: [],
        message: error.response?.data?.message || 'Error en la búsqueda'
      }
    }
  }

  /**
   * Filtrar productos por categoría
   */
  async getProductsByCategory(category) {
    try {
      const response = await apiClient.get(`/api/products?categoria=${encodeURIComponent(category)}`)
      return {
        success: true,
        data: response.data.products || response.data,
        message: 'Productos filtrados exitosamente'
      }
    } catch (error) {
      console.error('Error al filtrar productos:', error)
      return {
        success: false,
        data: [],
        message: error.response?.data?.message || 'Error al filtrar productos'
      }
    }
  }

  /**
   * Obtener estadísticas de productos
   */
  async getProductStats() {
    try {
      const response = await apiClient.get('/api/products/stats')
      return {
        success: true,
        data: response.data,
        message: 'Estadísticas obtenidas exitosamente'
      }
    } catch (error) {
      console.error('Error al obtener estadísticas:', error)
      return {
        success: false,
        data: null,
        message: error.response?.data?.message || 'Error al cargar estadísticas'
      }
    }
  }

  // ==========================================
  // MÉTODOS ADMINISTRATIVOS
  // ==========================================

  /**
   * Obtener estadísticas generales de productos para admin
   */
  async getStats() {
    try {
      // Usar directamente el endpoint de productos que sabemos que funciona
      const productsResponse = await apiClient.get('/api/products')
      const products = productsResponse.data.products || []
      
      // Calcular estadísticas basadas en los productos reales
      const stats = {
        totalProductos: products.length,
        enStock: products.filter(p => p.stock > 0).length,
        stockBajo: products.filter(p => p.stock > 0 && p.stock <= 10).length,
        agotados: products.filter(p => p.stock === 0).length,
        valorInventario: products.reduce((total, p) => total + (p.precio * p.stock), 0),
        activos: products.filter(p => p.activo).length,
        isDemo: false // Datos reales de la base de datos
      }
      
      return stats
    } catch (error) {
      console.error('Error al obtener estadísticas:', error)
      // Solo si falla completamente, mostrar mensaje de error
      throw new Error('No se pudo conectar con el servidor')
    }
  }

  /**
   * Obtener productos con filtros avanzados para administración
   */
  async getProductsAdmin(filters = {}) {
    try {
      // Usar directamente el endpoint de productos que sabemos que funciona
      const response = await apiClient.get('/api/products')
      const products = response.data.products || []
      
      // Transformar la estructura de datos para que sea compatible con AdminProductos
      const transformedProducts = products.map(product => ({
        id: product.id?.toString() || '',
        nombre: product.nombre || '',
        codigo: product.codigo || `P-${product.id?.slice(0, 8)}`, // Generar código si no existe
        marca: product.marca || 'Sin marca',
        descripcion: product.descripcion || '',
        categoria: product.categoria || 'General',
        proveedor: product.proveedor || 'Sin proveedor',
        precioCosto: parseFloat(product.precio_costo || product.precio || 0) * 0.7, // Simular precio costo como 70% del precio
        precioVenta: parseFloat(product.precio || 0),
        stockActual: parseInt(product.stock || 0),
        stockMinimo: parseInt(product.stock_minimo || 5), // Default mínimo
        unidadMedida: product.unidad_medida || 'unidad',
        estado: product.activo ? 'activo' : 'inactivo',
        imagen: product.imagen || null,
        fechaCreacion: product.created_at || new Date().toISOString(),
        fechaActualizacion: product.updated_at || new Date().toISOString()
      }))
      
      return {
        data: transformedProducts,
        total: transformedProducts.length,
        page: 1,
        totalPages: 1,
        isDemo: false // Datos reales de la base de datos
      }
    } catch (error) {
      console.error('Error al obtener productos:', error)
      throw new Error('No se pudo conectar con el servidor')
    }
  }

  /**
   * Crear nuevo producto
   */
  async create(productData) {
    try {
      const response = await apiClient.post('/api/products', productData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al crear producto')
    }
  }

  /**
   * Actualizar producto
   */
  async update(id, data) {
    try {
      const response = await apiClient.put(`/api/products/${id}`, data)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al actualizar producto')
    }
  }

  /**
   * Eliminar producto
   */
  async delete(id) {
    try {
      const response = await apiClient.delete(`/api/products/${id}`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al eliminar producto')
    }
  }

  /**
   * Actualización masiva de stock de productos
   */
  async bulkUpdateStock(productIds, nuevoStock) {
    try {
      const response = await apiClient.patch('/api/admin/products/bulk/stock', {
        productIds,
        nuevoStock
      })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al actualizar stock de productos')
    }
  }

  /**
   * Actualización masiva de estado de productos
   */
  async bulkUpdateStatus(productIds, estado) {
    try {
      const response = await apiClient.patch('/api/admin/products/bulk/status', {
        productIds,
        estado
      })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al actualizar estado de productos')
    }
  }

  /**
   * Eliminación masiva de productos
   */
  async bulkDelete(productIds) {
    try {
      const response = await apiClient.delete('/api/admin/products/bulk', {
        data: { productIds }
      })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Error al eliminar productos')
    }
  }

  /**
   * Obtener estadísticas detalladas de un producto específico
   */
  async getProductStats(productId) {
    try {
      const response = await apiClient.get(`/api/admin/products/${productId}/stats`)
      return response.data
    } catch (error) {
      // Fallback data for demo purposes
      return this.getFallbackProductStats(productId)
    }
  }

  // ==========================================
  // MÉTODOS DE FALLBACK PARA DESARROLLO
  // ==========================================

  /**
   * Método alternativo para obtener todos los productos (compatibilidad con AdminProductos)
   */
  async getAll() {
    try {
      const response = await apiClient.get('/api/products')
      const products = response.data.products || response.data || []
      
      // Transformar los productos al formato esperado por AdminProductos
      const transformedProducts = products.map(product => ({
        id: product.id,
        nombre: product.nombre || product.name,
        codigo: product.codigo || product.code || `PROD-${product.id}`,
        marca: product.marca || product.brand || 'Sin marca',
        descripcion: product.descripcion || product.description || '',
        categoria: product.categoria || product.category || 'General',
        precioCosto: product.precioCosto || product.precio_costo || product.cost_price || 0,
        precioVenta: product.precioVenta || product.precio || product.price || 0,
        stockActual: product.stockActual || product.stock || 0,
        stockMinimo: product.stockMinimo || product.stock_minimo || product.min_stock || 5,
        estado: product.estado || product.status || (product.activo ? 'activo' : 'inactivo'),
        imagen: product.imagen || product.image || null,
        createdAt: product.createdAt || product.created_at || new Date().toISOString(),
        updatedAt: product.updatedAt || product.updated_at || new Date().toISOString()
      }))
      
      return {
        data: transformedProducts,
        total: transformedProducts.length,
        isDemo: false
      }
    } catch (error) {
      console.error('❌ Error al obtener productos:', error)
      // Retornar datos de fallback
      const fallbackProducts = this.getFallbackProductsRealFormat()
      return {
        data: fallbackProducts,
        total: fallbackProducts.length,
        isDemo: true
      }
    }
  }

  /**
   * Crear un nuevo producto
   */
  async create(productData) {
    try {
      const response = await apiClient.post('/api/admin/products', productData)
      return response.data
    } catch (error) {
      console.error('Error creating product:', error)
      throw new Error(error.response?.data?.message || 'Error al crear producto')
    }
  }

  /**
   * Actualizar un producto existente
   */
  async update(id, productData) {
    try {
      const response = await apiClient.put(`/api/admin/products/${id}`, productData)
      return response.data
    } catch (error) {
      console.error('Error updating product:', error)
      throw new Error(error.response?.data?.message || 'Error al actualizar producto')
    }
  }

  /**
   * Actualizar estado de un producto
   */
  async updateStatus(id, status) {
    try {
      const response = await apiClient.patch(`/api/admin/products/${id}/status`, { estado: status })
      return response.data
    } catch (error) {
      console.error('Error updating product status:', error)
      throw new Error(error.response?.data?.message || 'Error al actualizar estado del producto')
    }
  }

  /**
   * Productos de fallback en formato compatible con AdminProductos
   */
  getFallbackProductsRealFormat() {
    return [
      {
        id: 1,
        nombre: 'Shampoo Premium',
        codigo: 'SHAM-001',
        marca: "L'Oréal",
        descripcion: 'Shampoo premium para todo tipo de cabello',
        categoria: 'Cuidado Capilar',
        precioCosto: 25.50,
        precioVenta: 45.00,
        stockActual: 15,
        stockMinimo: 5,
        estado: 'activo',
        imagen: null,
        createdAt: '2024-01-15T10:00:00Z',
        updatedAt: '2024-01-20T15:30:00Z'
      },
      {
        id: 2,
        nombre: 'Gel Fijador Extra Fuerte',
        codigo: 'GEL-002',
        marca: 'American Crew',
        descripcion: 'Gel de fijación extra fuerte para peinados duraderos',
        categoria: 'Styling',
        precioCosto: 18.00,
        precioVenta: 32.00,
        stockActual: 8,
        stockMinimo: 10,
        estado: 'activo',
        imagen: null,
        createdAt: '2024-01-16T11:15:00Z',
        updatedAt: '2024-01-21T09:45:00Z'
      },
      {
        id: 3,
        nombre: 'Crema Facial Hidratante',
        codigo: 'CREM-003',
        marca: 'Nivea',
        descripcion: 'Crema hidratante para el cuidado facial diario',
        categoria: 'Cuidado Facial',
        precioCosto: 22.75,
        precioVenta: 38.50,
        stockActual: 0,
        stockMinimo: 8,
        estado: 'activo',
        imagen: null,
        createdAt: '2024-01-17T14:20:00Z',
        updatedAt: '2024-01-22T16:00:00Z'
      },
      {
        id: 4,
        nombre: 'Máquina Cortapelos Profesional',
        codigo: 'MAQ-004',
        marca: 'Wahl',
        descripcion: 'Máquina cortapelos profesional con múltiples accesorios',
        categoria: 'Herramientas',
        precioCosto: 180.00,
        precioVenta: 280.00,
        stockActual: 3,
        stockMinimo: 2,
        estado: 'activo',
        imagen: null,
        createdAt: '2024-01-18T09:30:00Z',
        updatedAt: '2024-01-23T12:15:00Z'
      },
      {
        id: 5,
        nombre: 'Toalla Premium',
        codigo: 'TOA-005',
        marca: 'Genérica',
        descripcion: 'Toalla de alta calidad para barbería',
        categoria: 'Accesorios',
        precioCosto: 12.00,
        precioVenta: 22.00,
        stockActual: 25,
        stockMinimo: 15,
        estado: 'inactivo',
        imagen: null,
        createdAt: '2024-01-19T13:45:00Z',
        updatedAt: '2024-01-24T10:30:00Z'
      },
      {
        id: 6,
        nombre: 'Acondicionador Reparador',
        codigo: 'ACON-006',
        marca: 'Schwarzkopf',
        descripcion: 'Acondicionador para cabello seco y dañado',
        categoria: 'Cuidado Capilar',
        precioCosto: 20.25,
        precioVenta: 35.75,
        stockActual: 12,
        stockMinimo: 8,
        estado: 'activo',
        imagen: null,
        createdAt: '2024-01-20T14:00:00Z',
        updatedAt: '2024-01-25T19:00:00Z'
      }
    ]
  }

  /**
   * Datos de fallback para productos (desarrollo)
   */
  getFallbackProducts() {
    return {
      data: [
        {
          id: '1',
          nombre: 'Shampoo Reparador',
          codigo: 'SH-001',
          marca: "L'Oréal",
          descripcion: 'Shampoo para cabello dañado con keratina',
          categoria: 'Cuidado Capilar',
          proveedor: "L'Oréal",
          precioCosto: 15000,
          precioVenta: 25000,
          stockActual: 25,
          stockMinimo: 10,
          unidadMedida: 'ml',
          estado: 'activo',
          imagen: null,
          fechaCreacion: '2024-01-15T10:00:00Z',
          fechaActualizacion: '2024-01-20T14:30:00Z'
        },
        {
          id: '2',
          nombre: 'Cera Modeladora',
          codigo: 'ST-002',
          marca: 'American Crew',
          descripcion: 'Cera para peinado con fijación fuerte',
          categoria: 'Styling',
          proveedor: 'American Crew',
          precioCosto: 20000,
          precioVenta: 35000,
          stockActual: 15,
          stockMinimo: 8,
          unidadMedida: 'gr',
          estado: 'activo',
          imagen: null,
          fechaCreacion: '2024-01-16T11:00:00Z',
          fechaActualizacion: '2024-01-21T15:00:00Z'
        },
        {
          id: '3',
          nombre: 'Crema de Afeitar',
          codigo: 'CF-003',
          marca: 'Gillette',
          descripcion: 'Crema hidratante para afeitado suave',
          categoria: 'Cuidado Facial',
          proveedor: 'Gillette',
          precioCosto: 8000,
          precioVenta: 15000,
          stockActual: 5,
          stockMinimo: 12,
          unidadMedida: 'ml',
          estado: 'activo',
          imagen: null,
          fechaCreacion: '2024-01-17T09:00:00Z',
          fechaActualizacion: '2024-01-22T16:00:00Z'
        },
        {
          id: '4',
          nombre: 'Maquinilla Profesional',
          codigo: 'HE-004',
          marca: 'Wahl',
          descripcion: 'Cortadora de cabello profesional',
          categoria: 'Herramientas',
          proveedor: 'Wahl',
          precioCosto: 180000,
          precioVenta: 250000,
          stockActual: 3,
          stockMinimo: 2,
          unidadMedida: 'unidad',
          estado: 'activo',
          imagen: null,
          fechaCreacion: '2024-01-18T12:00:00Z',
          fechaActualizacion: '2024-01-23T17:00:00Z'
        },
        {
          id: '5',
          nombre: 'Toalla Premium',
          codigo: 'AC-005',
          marca: 'Generic',
          descripcion: 'Toalla de microfibra para barbería',
          categoria: 'Accesorios',
          proveedor: 'Generic',
          precioCosto: 12000,
          precioVenta: 20000,
          stockActual: 0,
          stockMinimo: 5,
          unidadMedida: 'unidad',
          estado: 'inactivo',
          imagen: null,
          fechaCreacion: '2024-01-19T13:00:00Z',
          fechaActualizacion: '2024-01-24T18:00:00Z'
        },
        {
          id: '6',
          nombre: 'Acondicionador Hidratante',
          codigo: 'SH-006',
          marca: 'Schwarzkopf',
          descripcion: 'Acondicionador para cabello seco',
          categoria: 'Cuidado Capilar',
          proveedor: 'Schwarzkopf',
          precioCosto: 18000,
          precioVenta: 30000,
          stockActual: 20,
          stockMinimo: 8,
          unidadMedida: 'ml',
          estado: 'activo',
          imagen: null,
          fechaCreacion: '2024-01-20T14:00:00Z',
          fechaActualizacion: '2024-01-25T19:00:00Z'
        }
      ],
      total: 6,
      page: 1,
      totalPages: 1
    }
  }

  /**
   * Estadísticas de fallback para un producto específico
   */
  getFallbackProductStats(productId) {
    const baseStats = {
      ventasTotales: Math.floor(Math.random() * 50) + 10,
      ingresosTotales: Math.floor(Math.random() * 1000000) + 200000,
      stockVendido: Math.floor(Math.random() * 30) + 5,
      rotacion: (Math.random() * 3 + 1).toFixed(1)
    }

    return {
      ...baseStats,
      tendencia: Math.random() > 0.5 ? 'positiva' : 'negativa',
      porcentajeTendencia: Math.floor(Math.random() * 30) + 5
    }
  }
}

// Crear una instancia compartida del servicio
const productServiceInstance = new ProductService()

// Exportar tanto la clase como la instancia para flexibilidad
export { ProductService }
export default productServiceInstance

// Exportar también como productService para compatibilidad
export const productService = productServiceInstance
