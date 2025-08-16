// Test de transformación de datos
const testProducts = [
  {
    "activo": true,
    "created_at": "2025-08-01T17:11:11.890904",
    "descripcion": "Shampoo premium para todo tipo de cabello con ingredientes naturales",
    "id": "151a673f-9be2-4e50-b63b-f4f1bb7ba1e0",
    "nombre": "Shampoo Premium",
    "precio": "15.99",
    "stock": 50,
    "updated_at": "2025-08-01T17:11:11.890904"
  }
];

// Aplicar la misma transformación que en productService
const transformedProducts = testProducts.map(product => ({
  id: product.id?.toString() || '',
  nombre: product.nombre || '',
  codigo: product.codigo || `P-${product.id?.slice(0, 8)}`,
  marca: product.marca || 'Sin marca',
  descripcion: product.descripcion || '',
  categoria: product.categoria || 'General',
  proveedor: product.proveedor || 'Sin proveedor',
  precioCosto: parseFloat(product.precio_costo || product.precio || 0) * 0.7,
  precioVenta: parseFloat(product.precio || 0),
  stockActual: parseInt(product.stock || 0),
  stockMinimo: parseInt(product.stock_minimo || 5),
  unidadMedida: product.unidad_medida || 'unidad',
  estado: product.activo ? 'activo' : 'inactivo',
  imagen: product.imagen || null,
  fechaCreacion: product.created_at || new Date().toISOString(),
  fechaActualizacion: product.updated_at || new Date().toISOString()
}));

console.log('Producto original:', JSON.stringify(testProducts[0], null, 2));
console.log('Producto transformado:', JSON.stringify(transformedProducts[0], null, 2));
