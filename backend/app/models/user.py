"""
Modelo de Usuario para el sistema Low Barber
"""

from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum
from .base import db, BaseModel

class UserRole(Enum):
    """Roles de usuario en el sistema"""
    CLIENTE = "cliente"
    BARBERO = "barbero"
    ADMIN = "admin"

class User(BaseModel):
    """Modelo de Usuario"""
    __tablename__ = 'users'
    
    # Información personal
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    telefono = db.Column(db.String(20), nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Rol del usuario
    rol = db.Column(db.Enum(UserRole), default=UserRole.CLIENTE, nullable=False)
    
    # Estado del usuario
    activo = db.Column(db.Boolean, default=True, nullable=False)
    email_verificado = db.Column(db.Boolean, default=False, nullable=False)
    
    # Relaciones (sin backrefs para evitar conflictos)
    # Las relaciones inversas se definen explícitamente en cada modelo
    barbero_profile = db.relationship('Barber', foreign_keys='Barber.user_id', uselist=False, cascade='all, delete-orphan', overlaps="usuario")
    
    def __init__(self, nombre, email, password, telefono=None, rol=UserRole.CLIENTE):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.rol = rol
        self.set_password(password)
    
    def set_password(self, password):
        """Establece la contraseña hasheada"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica la contraseña"""
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """Convierte el usuario a diccionario (sin password)"""
        data = super().to_dict()
        data.update({
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'rol': self.rol.value if self.rol else None,
            'activo': self.activo,
            'email_verificado': self.email_verificado
        })
        return data
    
    @classmethod
    def find_by_email(cls, email):
        """Busca un usuario por email"""
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_by_id(cls, user_id):
        """Busca un usuario por ID"""
        return cls.query.get(user_id)
    
    def get_reservas(self):
        """Obtiene todas las reservas del usuario"""
        from .reservation import Reservation
        return Reservation.query.filter_by(user_id=self.id).order_by(Reservation.fecha_reserva.desc()).all()
    
    def es_barbero(self):
        """Verifica si el usuario es barbero"""
        return self.rol == UserRole.BARBERO
    
    def es_admin(self):
        """Verifica si el usuario es administrador"""
        return self.rol == UserRole.ADMIN
    
    def __repr__(self):
        return f'<User {self.email}>'
