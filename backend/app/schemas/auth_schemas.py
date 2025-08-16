"""
Schemas de validación para la autenticación
"""

from marshmallow import Schema, fields, validate, ValidationError, validates, validates_schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import User, UserRole
import re

class EnumField(fields.Field):
    """Campo personalizado para serializar enums correctamente"""
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.value if hasattr(value, 'value') else str(value)

class UserRegistrationSchema(Schema):
    """Schema para registro de usuarios"""
    nombre = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    email = fields.Email(required=True)
    telefono = fields.Str(validate=validate.Length(max=20), allow_none=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
    password_confirmation = fields.Str(required=True)
    rol = fields.Str(validate=validate.OneOf([role.value for role in UserRole]), 
                     missing=UserRole.CLIENTE.value)
    
    @validates('email')
    def validate_email_unique(self, email):
        """Validar que el email sea único"""
        if User.find_by_email(email):
            raise ValidationError('Este email ya está registrado.')
    
    @validates_schema
    def validate_password_match(self, data, **kwargs):
        """Validar que las contraseñas coincidan"""
        if data.get('password') != data.get('password_confirmation'):
            raise ValidationError('Las contraseñas no coinciden.', 'password_confirmation')
    
    @validates_schema
    def validate_phone_format(self, data, **kwargs):
        """Validar formato del teléfono"""
        if data.get('telefono'):
            phone_pattern = re.compile(r'^\+?[\d\s\-\(\)]{7,20}$')
            if not phone_pattern.match(data['telefono']):
                raise ValidationError('Formato de teléfono inválido.', 'telefono')

class UserLoginSchema(Schema):
    """Schema para login de usuarios"""
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class UserProfileSchema(SQLAlchemyAutoSchema):
    """Schema para perfil de usuario (sin password)"""
    class Meta:
        model = User
        load_instance = True
        exclude = ('password_hash',)
    
    # Campos de solo lectura
    id = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    rol = EnumField(dump_only=True)

class UserUpdateSchema(Schema):
    """Schema para actualizar perfil de usuario"""
    nombre = fields.Str(validate=validate.Length(min=2, max=100))
    telefono = fields.Str(validate=validate.Length(max=20), allow_none=True)
    
    @validates_schema
    def validate_phone_format(self, data, **kwargs):
        """Validar formato del teléfono"""
        if data.get('telefono'):
            phone_pattern = re.compile(r'^\+?[\d\s\-\(\)]{7,20}$')
            if not phone_pattern.match(data['telefono']):
                raise ValidationError('Formato de teléfono inválido.', 'telefono')

class ChangePasswordSchema(Schema):
    """Schema para cambio de contraseña"""
    current_password = fields.Str(required=True)
    new_password = fields.Str(required=True, validate=validate.Length(min=6))
    new_password_confirmation = fields.Str(required=True)
    
    @validates_schema
    def validate_password_match(self, data, **kwargs):
        """Validar que las contraseñas nuevas coincidan"""
        if data.get('new_password') != data.get('new_password_confirmation'):
            raise ValidationError('Las contraseñas nuevas no coinciden.', 'new_password_confirmation')

# Instancias de los schemas para uso en las rutas
user_registration_schema = UserRegistrationSchema()
user_login_schema = UserLoginSchema()
user_profile_schema = UserProfileSchema()
user_update_schema = UserUpdateSchema()
change_password_schema = ChangePasswordSchema()
