"""
Esquemas para Servicios - Low Barber
"""

from marshmallow import Schema, fields, validates, ValidationError, validate

class ServiceCreateSchema(Schema):
    """Schema para crear un servicio"""
    nombre = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    descripcion = fields.Str(required=False, allow_none=True, validate=validate.Length(max=500))
    precio = fields.Decimal(required=True, validate=validate.Range(min=0), as_string=True)
    duracion = fields.Int(required=True, validate=validate.Range(min=5, max=300))  # en minutos
    categoria = fields.Str(required=False, allow_none=True, validate=validate.OneOf(['cortes', 'barbas', 'tratamientos', 'combos']))
    activo = fields.Bool(required=False, missing=True)
    popular = fields.Bool(required=False, missing=False)
    imagen_url = fields.Str(required=False, allow_none=True, validate=validate.Length(max=255))

class ServiceUpdateSchema(Schema):
    """Schema para actualizar un servicio"""
    nombre = fields.Str(required=False, validate=validate.Length(min=2, max=100))
    descripcion = fields.Str(required=False, allow_none=True, validate=validate.Length(max=500))
    precio = fields.Decimal(required=False, validate=validate.Range(min=0), as_string=True)
    duracion = fields.Int(required=False, validate=validate.Range(min=5, max=300))
    categoria = fields.Str(required=False, allow_none=True, validate=validate.OneOf(['cortes', 'barbas', 'tratamientos', 'combos']))
    activo = fields.Bool(required=False)
    popular = fields.Bool(required=False)
    imagen_url = fields.Str(required=False, allow_none=True, validate=validate.Length(max=255))
    
    # Campos adicionales del frontend que no se usan directamente
    name = fields.Str(required=False, load_only=True)
    description = fields.Str(required=False, load_only=True)
    price = fields.Decimal(required=False, load_only=True, as_string=True)
    duration = fields.Int(required=False, load_only=True)
    category = fields.Str(required=False, load_only=True)
    status = fields.Str(required=False, load_only=True)
    image = fields.Str(required=False, load_only=True)

class ServiceResponseSchema(Schema):
    """Schema para respuesta de servicio"""
    id = fields.Str(dump_only=True)
    nombre = fields.Str(dump_only=True)
    descripcion = fields.Str(dump_only=True)
    precio = fields.Decimal(dump_only=True, as_string=True)
    duracion = fields.Int(dump_only=True)
    categoria = fields.Str(dump_only=True)
    activo = fields.Bool(dump_only=True)
    popular = fields.Bool(dump_only=True)
    imagen_url = fields.Str(dump_only=True)
    barberos_count = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

# Instancias de los esquemas
service_create_schema = ServiceCreateSchema()
service_update_schema = ServiceUpdateSchema()
service_response_schema = ServiceResponseSchema()
services_response_schema = ServiceResponseSchema(many=True)
