"""
Modelo de Producto para el sistema Low Barber
"""

from .base import db, BaseModel

class Product(BaseModel):
    """Modelo de Producto"""
    __tablename__ = 'products'
    
    # Información del producto
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    
    # Inventario
    stock = db.Column(db.Integer, default=0, nullable=False)
    stock_minimo = db.Column(db.Integer, default=5, nullable=False)
    
    # Categoría y marca
    categoria = db.Column(db.String(50), nullable=True)
    marca = db.Column(db.String(50), nullable=True)
    
    # Estado del producto
    activo = db.Column(db.Boolean, default=True, nullable=False)
    destacado = db.Column(db.Boolean, default=False, nullable=False)
    
    # Imagen del producto
    imagen_url = db.Column(db.String(255), nullable=True)
    
    # SKU del producto
    sku = db.Column(db.String(50), unique=True, nullable=True)
    
    def __init__(self, nombre, precio, stock=0, descripcion=None, categoria=None, marca=None, activo=True, imagen=None):
        super().__init__()
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion
        self.categoria = categoria
        self.marca = marca
        self.activo = activo
        self.imagen = imagen
    
    def to_dict(self):
        """Convierte el producto a diccionario"""
        data = super().to_dict()
        data.update({
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': float(self.precio) if self.precio else 0,
            'stock': self.stock,
            'stock_minimo': self.stock_minimo,
            'categoria': self.categoria,
            'marca': self.marca,
            'activo': self.activo,
            'destacado': self.destacado,
            'imagen_url': self.imagen_url,
            'sku': self.sku,
            'disponible': self.stock > 0,
            'stock_bajo': self.stock <= self.stock_minimo
        })
        return data
    
    @classmethod
    def get_active_products(cls):
        """Obtiene productos activos"""
        return cls.query.filter_by(activo=True).all()
    
    @classmethod
    def get_featured_products(cls):
        """Obtiene productos destacados"""
        return cls.query.filter_by(activo=True, destacado=True).all()
    
    @classmethod
    def get_by_category(cls, categoria):
        """Obtiene productos por categoría"""
        return cls.query.filter_by(activo=True, categoria=categoria).all()
    
    @classmethod
    def get_low_stock_products(cls):
        """Obtiene productos con stock bajo"""
        return cls.query.filter(cls.activo == True, cls.stock <= cls.stock_minimo).all()
    
    def update_stock(self, cantidad):
        """Actualiza el stock del producto"""
        self.stock += cantidad
        if self.stock < 0:
            self.stock = 0
        self.save()
        return self.stock
    
    def __repr__(self):
        return f'<Product {self.nombre}>'
