"""
Esquemas para Servicios - Low Barber
"""

from marshmallow import Schema, fields, validates, ValidationError, validate

class ServiceCreateSchema(Schema):
    """Schema para crear un servicio"""
    nombre = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    descripcion = fields.Str(required=True, validate=validate.Length(min=10, max=500))
    precio = fields.Decimal(required=True, validate=validate.Range(min=0))
    duracion = fields.Int(required=True, validate=validate.Range(min=5, max=300))  # en minutos
    activo = fields.Bool(required=False, missing=True)

class ServiceUpdateSchema(Schema):
    """Schema para actualizar un servicio"""
    nombre = fields.Str(required=False, validate=validate.Length(min=2, max=100))
    descripcion = fields.Str(required=False, validate=validate.Length(min=10, max=500))
    precio = fields.Decimal(required=False, validate=validate.Range(min=0))
    duracion = fields.Int(required=False, validate=validate.Range(min=5, max=300))
    activo = fields.Bool(required=False)

class ServiceResponseSchema(Schema):
    """Schema para respuesta de servicio"""
    id = fields.Str(dump_only=True)
    nombre = fields.Str(dump_only=True)
    descripcion = fields.Str(dump_only=True)
    precio = fields.Decimal(dump_only=True)
    duracion = fields.Int(dump_only=True)
    activo = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

# Instancias de los esquemas
service_create_schema = ServiceCreateSchema()
service_update_schema = ServiceUpdateSchema()
service_response_schema = ServiceResponseSchema()
services_response_schema = ServiceResponseSchema(many=True)
