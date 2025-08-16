"""
Esquemas para Productos - Low Barber
"""

from marshmallow import Schema, fields, validates, ValidationError, validate

class ProductCreateSchema(Schema):
    """Schema para crear un producto"""
    nombre = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    descripcion = fields.Str(required=True, validate=validate.Length(min=10, max=500))
    precio = fields.Decimal(required=True, validate=validate.Range(min=0))
    stock = fields.Int(required=True, validate=validate.Range(min=0))
    imagen = fields.Str(required=False, validate=validate.Length(max=255))
    activo = fields.Bool(required=False, missing=True)

class ProductUpdateSchema(Schema):
    """Schema para actualizar un producto"""
    nombre = fields.Str(required=False, validate=validate.Length(min=2, max=100))
    descripcion = fields.Str(required=False, validate=validate.Length(min=10, max=500))
    precio = fields.Decimal(required=False, validate=validate.Range(min=0))
    stock = fields.Int(required=False, validate=validate.Range(min=0))
    imagen = fields.Str(required=False, validate=validate.Length(max=255))
    activo = fields.Bool(required=False)

class ProductResponseSchema(Schema):
    """Schema para respuesta de producto"""
    id = fields.Str(dump_only=True)
    nombre = fields.Str(dump_only=True)
    descripcion = fields.Str(dump_only=True)
    precio = fields.Decimal(dump_only=True)
    stock = fields.Int(dump_only=True)
    imagen = fields.Str(dump_only=True)
    activo = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

# Instancias de los esquemas
product_create_schema = ProductCreateSchema()
product_update_schema = ProductUpdateSchema()
product_response_schema = ProductResponseSchema()
products_response_schema = ProductResponseSchema(many=True)
