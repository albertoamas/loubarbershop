"""
Esquemas para Barberos - Low Barber
"""

from marshmallow import Schema, fields, validates, ValidationError, validate
from app.models import UserRole

class BarberCreateSchema(Schema):
    """Schema para crear un barbero"""
    nombre = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    email = fields.Email(required=True)
    telefono = fields.Str(required=False, validate=validate.Length(max=20))
    password = fields.Str(required=True, validate=validate.Length(min=6))
    password_confirmation = fields.Str(required=True)
    especialidad = fields.Str(required=True, validate=validate.Length(min=5, max=200))
    descripcion = fields.Str(required=False)
    experiencia_anos = fields.Int(required=False, missing=0)
    disponible = fields.Bool(required=False, missing=True)
    
    @validates('email')
    def validate_email(self, value):
        from app.models import User
        if User.query.filter_by(email=value).first():
            raise ValidationError('Este email ya está registrado.')

    # Nota: La validación de password_confirmation se hace en el endpoint
    pass

class BarberUpdateSchema(Schema):
    """Schema para actualizar un barbero"""
    nombre = fields.Str(required=False, validate=validate.Length(min=2, max=100))
    telefono = fields.Str(required=False, validate=validate.Length(max=20))
    especialidad = fields.Str(required=False, validate=validate.Length(min=5, max=200))
    descripcion = fields.Str(required=False)
    experiencia_anos = fields.Int(required=False)
    disponible = fields.Bool(required=False)
    activo = fields.Bool(required=False)
    horario_trabajo = fields.Dict(required=False)

class BarberResponseSchema(Schema):
    """Schema para respuesta de barbero"""
    id = fields.Str(dump_only=True)
    nombre = fields.Str(dump_only=True)  # Nombre del barbero directamente
    especialidad = fields.Str(dump_only=True)
    descripcion = fields.Str(dump_only=True)
    experiencia_anos = fields.Int(dump_only=True)
    disponible = fields.Bool(dump_only=True)
    activo = fields.Bool(dump_only=True)  # Campo activo faltante
    user_id = fields.Str(dump_only=True)
    horario_trabajo = fields.Dict(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    # Campos del usuario asociado
    email = fields.Method("get_email")
    telefono = fields.Method("get_telefono")
    
    def get_email(self, obj):
        return obj.usuario.email if obj.usuario else None
    
    def get_telefono(self, obj):
        return obj.usuario.telefono if obj.usuario else None

# Instancias de los esquemas
barber_create_schema = BarberCreateSchema()
barber_update_schema = BarberUpdateSchema()
barber_response_schema = BarberResponseSchema()
barbers_response_schema = BarberResponseSchema(many=True)
