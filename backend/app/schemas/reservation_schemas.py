"""
Esquemas para Reservas - Low Barber
"""

from marshmallow import Schema, fields, validates, ValidationError, validate, post_load
from datetime import datetime, date, time, timedelta
from app.models import ReservationStatus

class ReservationCreateSchema(Schema):
    """Schema para crear una reserva"""
    barbero_id = fields.Str(required=True, validate=validate.Length(equal=36))
    servicio_id = fields.Str(required=True, validate=validate.Length(equal=36))
    fecha_reserva = fields.Date(required=True)
    hora_inicio = fields.Time(required=True)
    notas = fields.Str(required=False, validate=validate.Length(max=500))
    
    # Campos de información del cliente (opcionales - si no se envían, se usan los del usuario autenticado)
    cliente_nombre = fields.Str(required=False, validate=validate.Length(min=2, max=100))
    cliente_telefono = fields.Str(required=False, validate=validate.Length(max=20))
    cliente_email = fields.Email(required=False, validate=validate.Length(max=120))
    
    @validates('fecha_reserva')
    def validate_fecha_reserva(self, value):
        """Valida que la fecha no sea en el pasado"""
        if value < date.today():
            raise ValidationError('La fecha de reserva no puede ser en el pasado.')
    
    @validates('hora_inicio')
    def validate_hora_inicio(self, value):
        """Valida que la hora esté en horario de trabajo"""
        # Horario de trabajo: 9:00 AM a 6:00 PM
        if value < time(9, 0) or value > time(18, 0):
            raise ValidationError('La hora debe estar entre 9:00 AM y 6:00 PM.')
    
    @post_load
    def validate_disponibilidad(self, data, **kwargs):
        """Valida disponibilidad del barbero después de cargar todos los datos"""
        from app.models import Reservation, Service
        
        # Obtener duración del servicio para calcular hora_fin
        servicio = Service.query.get(data['servicio_id'])
        if not servicio:
            raise ValidationError({'servicio_id': ['Servicio no encontrado.']})
        
        if not servicio.activo:
            raise ValidationError({'servicio_id': ['El servicio no está disponible.']})
        
        # Calcular hora de fin
        datetime_inicio = datetime.combine(data['fecha_reserva'], data['hora_inicio'])
        datetime_fin = datetime_inicio + timedelta(minutes=servicio.duracion)
        hora_fin = datetime_fin.time()
        
        # Validar disponibilidad del barbero
        disponible, mensaje = Reservation.validar_disponibilidad(
            data['barbero_id'], 
            data['fecha_reserva'], 
            data['hora_inicio'], 
            hora_fin
        )
        
        if not disponible:
            raise ValidationError({'hora_inicio': [mensaje]})
        
        # Validar horario de trabajo del barbero
        valido, mensaje = Reservation.validar_horario_trabajo(
            data['barbero_id'], 
            data['fecha_reserva'], 
            data['hora_inicio'], 
            hora_fin
        )
        
        if not valido:
            raise ValidationError({'hora_inicio': [mensaje]})
        
        # Validar que sea en el futuro con tiempo mínimo
        valido, mensaje = Reservation.validar_fecha_futura(data['fecha_reserva'], data['hora_inicio'])
        if not valido:
            raise ValidationError({'fecha_reserva': [mensaje]})
        
        return data

class ReservationUpdateSchema(Schema):
    """Schema para actualizar una reserva"""
    fecha_reserva = fields.Date(required=False)
    hora_inicio = fields.Time(required=False)
    notas = fields.Str(required=False, validate=validate.Length(max=500))
    notas_barbero = fields.Str(required=False, validate=validate.Length(max=500))
    precio_final = fields.Decimal(required=False, validate=validate.Range(min=0))
    
    @validates('fecha_reserva')
    def validate_fecha_reserva(self, value):
        """Valida que la fecha no sea en el pasado"""
        if value < date.today():
            raise ValidationError('La fecha de reserva no puede ser en el pasado.')

class ReservationStatusUpdateSchema(Schema):
    """Schema para actualizar el estado de una reserva"""
    estado = fields.Str(required=True, validate=validate.OneOf([e.value for e in ReservationStatus]))
    notas_barbero = fields.Str(required=False, validate=validate.Length(max=500))
    precio_final = fields.Decimal(required=False, validate=validate.Range(min=0))

class ReservationResponseSchema(Schema):
    """Schema para respuesta de reserva"""
    id = fields.Str(dump_only=True)
    fecha_reserva = fields.Date(dump_only=True)
    hora_inicio = fields.Time(dump_only=True)
    hora_fin = fields.Time(dump_only=True)
    estado = fields.Method("get_estado", dump_only=True)
    notas = fields.Str(dump_only=True)
    notas_barbero = fields.Str(dump_only=True)
    precio_final = fields.Decimal(dump_only=True)
    cliente_nombre = fields.Str(dump_only=True)
    cliente_telefono = fields.Str(dump_only=True)
    cliente_email = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    # Información relacionada
    barbero = fields.Method("get_barbero_info")
    servicio = fields.Method("get_servicio_info")
    
    def get_estado(self, obj):
        return obj.estado if obj.estado else None
    
    def get_barbero_info(self, obj):
        if obj.barbero:
            return {
                'id': obj.barbero.id,
                'nombre': obj.barbero.nombre,
                'especialidad': obj.barbero.especialidad
            }
        return None
    
    def get_servicio_info(self, obj):
        if obj.servicio:
            return {
                'id': obj.servicio.id,
                'nombre': obj.servicio.nombre,
                'precio': float(obj.servicio.precio) if obj.servicio.precio else None,
                'duracion': obj.servicio.duracion
            }
        return None

class AvailabilityQuerySchema(Schema):
    """Schema para consultar disponibilidad"""
    barbero_id = fields.Str(required=True, validate=validate.Length(equal=36))
    fecha = fields.Date(required=True)
    
    @validates('fecha')
    def validate_fecha(self, value):
        """Valida que la fecha no sea en el pasado"""
        if value < date.today():
            raise ValidationError('No se puede consultar disponibilidad en fechas pasadas.')

class AvailabilityResponseSchema(Schema):
    """Schema para respuesta de disponibilidad"""
    fecha = fields.Date(dump_only=True)
    barbero_id = fields.Str(dump_only=True)
    barbero_nombre = fields.Str(dump_only=True)
    horarios_ocupados = fields.List(fields.Dict(), dump_only=True)
    horarios_disponibles = fields.List(fields.Dict(), dump_only=True)

# Instancias de los esquemas
reservation_create_schema = ReservationCreateSchema()
reservation_update_schema = ReservationUpdateSchema()
reservation_status_update_schema = ReservationStatusUpdateSchema()
reservation_response_schema = ReservationResponseSchema()
reservations_response_schema = ReservationResponseSchema(many=True)
availability_query_schema = AvailabilityQuerySchema()
availability_response_schema = AvailabilityResponseSchema()
