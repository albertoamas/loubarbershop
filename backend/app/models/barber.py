"""
Modelo de Barbero para el sistema Low Barber
"""

from .base import db, BaseModel

class Barber(BaseModel):
    """Modelo de Barbero"""
    __tablename__ = 'barbers'
    
    # Información del barbero
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(200), nullable=True)
    descripcion = db.Column(db.Text, nullable=True)
    experiencia_anos = db.Column(db.Integer, default=0)
    
    # Estado y disponibilidad
    disponible = db.Column(db.Boolean, default=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    # Relación con usuario
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    
    # Relaciones explícitas (sin backrefs conflictivos)
    usuario = db.relationship('User', foreign_keys=[user_id], overlaps="barbero_profile")
    servicios = db.relationship('Service', secondary='barber_services', back_populates='barberos')
    
    # Horarios de trabajo (JSON)
    horario_trabajo = db.Column(db.JSON, nullable=True)  # Ejemplo: {"lunes": {"inicio": "09:00", "fin": "18:00"}}
    
    def __init__(self, nombre, user_id, especialidad=None, descripcion=None, experiencia_anos=0, disponible=True):
        super().__init__()
        self.nombre = nombre
        self.user_id = user_id
        self.especialidad = especialidad
        self.descripcion = descripcion
        self.experiencia_anos = experiencia_anos
        self.disponible = disponible
    
    def to_dict(self):
        """Convierte el barbero a diccionario"""
        data = super().to_dict()
        data.update({
            'nombre': self.nombre,
            'especialidad': self.especialidad,
            'descripcion': self.descripcion,
            'experiencia_anos': self.experiencia_anos,
            'disponible': self.disponible,
            'activo': self.activo,
            'user_id': self.user_id,
            'horario_trabajo': self.horario_trabajo
        })
        return data
    
    @classmethod
    def get_available_barbers(cls):
        """Obtiene barberos disponibles y activos"""
        return cls.query.filter_by(disponible=True, activo=True).all()
    
    @classmethod
    def find_by_user_id(cls, user_id):
        """Busca un barbero por ID de usuario"""
        return cls.query.filter_by(user_id=user_id).first()
    
    def get_reservas(self):
        """Obtiene todas las reservas del barbero"""
        from .reservation import Reservation
        return Reservation.query.filter_by(barber_id=self.id).order_by(Reservation.fecha_reserva.desc()).all()
    
    def __repr__(self):
        return f'<Barber {self.nombre}>'
