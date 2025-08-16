"""
Modelo de Servicio para el sistema Low Barber
"""

from .base import db, BaseModel

# Tabla de asociación para la relación many-to-many entre barberos y servicios
barber_services = db.Table('barber_services',
    db.Column('barber_id', db.String(36), db.ForeignKey('barbers.id'), primary_key=True),
    db.Column('service_id', db.String(36), db.ForeignKey('services.id'), primary_key=True)
)

class Service(BaseModel):
    """Modelo de Servicio"""
    __tablename__ = 'services'
    
    # Información del servicio
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    duracion = db.Column(db.Integer, nullable=False)  # Duración en minutos
    
    # Estado del servicio
    activo = db.Column(db.Boolean, default=True, nullable=False)
    popular = db.Column(db.Boolean, default=False, nullable=False)
    
    # Categoría del servicio
    categoria = db.Column(db.String(50), nullable=True)
    
    # Imagen del servicio
    imagen_url = db.Column(db.String(255), nullable=True)
    
    # Relaciones (sin backref para evitar conflictos)
    # reservas se acceden via Reservation.query.filter_by(service_id=...)
    barberos = db.relationship('Barber', secondary=barber_services, back_populates='servicios')
    
    def __init__(self, nombre, precio, duracion, descripcion=None, categoria=None, activo=True, imagen_url=None):
        super().__init__()
        self.nombre = nombre
        self.precio = precio
        self.duracion = duracion
        self.descripcion = descripcion
        self.categoria = categoria
        self.activo = activo
        self.imagen_url = imagen_url
    
    def to_dict(self):
        """Convierte el servicio a diccionario"""
        data = super().to_dict()
        data.update({
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': float(self.precio) if self.precio else 0,
            'duracion': self.duracion,
            'activo': self.activo,
            'popular': self.popular,
            'categoria': self.categoria,
            'imagen_url': self.imagen_url,
            'barberos_count': len(self.barberos) if self.barberos else 0
        })
        return data
    
    @classmethod
    def get_active_services(cls):
        """Obtiene servicios activos"""
        return cls.query.filter_by(activo=True).all()
    
    @classmethod
    def get_popular_services(cls):
        """Obtiene servicios populares"""
        return cls.query.filter_by(activo=True, popular=True).all()
    
    @classmethod
    def get_by_category(cls, categoria):
        """Obtiene servicios por categoría"""
        return cls.query.filter_by(activo=True, categoria=categoria).all()
    
    def get_reservas(self):
        """Obtiene todas las reservas de este servicio"""
        from .reservation import Reservation
        return Reservation.query.filter_by(service_id=self.id).order_by(Reservation.fecha_reserva.desc()).all()
    
    def __repr__(self):
        return f'<Service {self.nombre}>'
