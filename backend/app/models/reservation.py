"""
Modelo de Reserva para el sistema Low Barber
"""

from datetime import datetime, timedelta
from enum import Enum
from .base import db, BaseModel

class ReservationStatus(Enum):
    """Estados de las reservas"""
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    EN_PROCESO = "en_proceso"
    COMPLETADA = "completada"
    CANCELADA = "cancelada"
    NO_ASISTIO = "no_asistio"

class Reservation(BaseModel):
    """Modelo de Reserva"""
    __tablename__ = 'reservations'
    
    # Relaciones con otras entidades
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    barber_id = db.Column(db.String(36), db.ForeignKey('barbers.id'), nullable=False)
    service_id = db.Column(db.String(36), db.ForeignKey('services.id'), nullable=False)
    
    # Relaciones explícitas hacia otros modelos (sin backrefs)
    cliente = db.relationship('User', foreign_keys=[user_id])
    barbero = db.relationship('Barber', foreign_keys=[barber_id])
    servicio = db.relationship('Service', foreign_keys=[service_id])
    
    # Información de la reserva
    fecha_reserva = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=True)
    
    # Estado de la reserva
    estado = db.Column(db.Enum(ReservationStatus), default=ReservationStatus.PENDIENTE, nullable=False)
    
    # Información adicional
    notas = db.Column(db.Text, nullable=True)
    precio_final = db.Column(db.Numeric(10, 2), nullable=True)
    
    # Datos de contacto (por si cambian)
    cliente_nombre = db.Column(db.String(100), nullable=False)
    cliente_telefono = db.Column(db.String(20), nullable=True)
    cliente_email = db.Column(db.String(120), nullable=False)
    
    # Timestamps específicos
    fecha_confirmacion = db.Column(db.DateTime, nullable=True)
    fecha_completacion = db.Column(db.DateTime, nullable=True)
    fecha_cancelacion = db.Column(db.DateTime, nullable=True)
    
    def __init__(self, user_id, barber_id, service_id, fecha_reserva, hora_inicio, 
                 cliente_nombre, cliente_email, cliente_telefono=None, notas=None):
        self.user_id = user_id
        self.barber_id = barber_id
        self.service_id = service_id
        self.fecha_reserva = fecha_reserva
        self.hora_inicio = hora_inicio
        self.cliente_nombre = cliente_nombre
        self.cliente_email = cliente_email
        self.cliente_telefono = cliente_telefono
        self.notas = notas
    
    def to_dict(self):
        """Convierte la reserva a diccionario"""
        data = super().to_dict()
        data.update({
            'user_id': self.user_id,
            'barber_id': self.barber_id,
            'service_id': self.service_id,
            'fecha_reserva': self.fecha_reserva.isoformat() if self.fecha_reserva else None,
            'hora_inicio': self.hora_inicio.strftime('%H:%M') if self.hora_inicio else None,
            'hora_fin': self.hora_fin.strftime('%H:%M') if self.hora_fin else None,
            'estado': self.estado.value if self.estado else None,
            'notas': self.notas,
            'precio_final': float(self.precio_final) if self.precio_final else None,
            'cliente_nombre': self.cliente_nombre,
            'cliente_telefono': self.cliente_telefono,
            'cliente_email': self.cliente_email,
            'fecha_confirmacion': self.fecha_confirmacion.isoformat() if self.fecha_confirmacion else None,
            'fecha_completacion': self.fecha_completacion.isoformat() if self.fecha_completacion else None,
            'fecha_cancelacion': self.fecha_cancelacion.isoformat() if self.fecha_cancelacion else None
        })
        return data
    
    def confirmar(self):
        """Confirma la reserva"""
        self.estado = ReservationStatus.CONFIRMADA
        self.fecha_confirmacion = datetime.utcnow()
        self.save()
    
    def completar(self, precio_final=None):
        """Completa la reserva"""
        self.estado = ReservationStatus.COMPLETADA
        self.fecha_completacion = datetime.utcnow()
        if precio_final:
            self.precio_final = precio_final
        self.save()
    
    def cancelar(self):
        """Cancela la reserva"""
        self.estado = ReservationStatus.CANCELADA
        self.fecha_cancelacion = datetime.utcnow()
        self.save()
    
    @classmethod
    def get_by_user(cls, user_id):
        """Obtiene reservas de un usuario"""
        return cls.query.filter_by(user_id=user_id).order_by(cls.fecha_reserva.desc()).all()
    
    @classmethod
    def get_by_barber(cls, barber_id):
        """Obtiene reservas de un barbero"""
        return cls.query.filter_by(barber_id=barber_id).order_by(cls.fecha_reserva.desc()).all()
    
    @classmethod
    def get_by_date_range(cls, fecha_inicio, fecha_fin):
        """Obtiene reservas en un rango de fechas"""
        return cls.query.filter(
            cls.fecha_reserva >= fecha_inicio,
            cls.fecha_reserva <= fecha_fin
        ).order_by(cls.fecha_reserva, cls.hora_inicio).all()
    
    @classmethod
    def get_disponibilidad_barbero(cls, barbero_id, fecha):
        """Obtiene las reservas activas de un barbero en una fecha específica"""
        return cls.query.filter_by(
            barber_id=barbero_id,
            fecha_reserva=fecha
        ).filter(
            cls.estado.in_([
                ReservationStatus.PENDIENTE, 
                ReservationStatus.CONFIRMADA, 
                ReservationStatus.EN_PROCESO
            ])
        ).order_by(cls.hora_inicio).all()
    
    @classmethod
    def validar_disponibilidad(cls, barbero_id, fecha, hora_inicio, hora_fin, reserva_id=None):
        """Valida si un barbero está disponible en un horario específico"""
        # Obtener reservas activas del barbero en esa fecha
        reservas_existentes = cls.get_disponibilidad_barbero(barbero_id, fecha)
        
        # Excluir la reserva actual si estamos editando
        if reserva_id:
            reservas_existentes = [r for r in reservas_existentes if r.id != reserva_id]
        
        # Convertir strings a time objects si es necesario
        if isinstance(hora_inicio, str):
            hora_inicio = datetime.strptime(hora_inicio, '%H:%M').time()
        if isinstance(hora_fin, str):
            hora_fin = datetime.strptime(hora_fin, '%H:%M').time()
        
        # Verificar solapamiento con cada reserva existente
        for reserva in reservas_existentes:
            reserva_inicio = reserva.hora_inicio
            reserva_fin = reserva.hora_fin
            
            # Si la reserva no tiene hora_fin, usar hora_inicio + 1 hora (default)
            if not reserva_fin:
                datetime_inicio = datetime.combine(fecha, reserva_inicio)
                datetime_fin = datetime_inicio + timedelta(hours=1)
                reserva_fin = datetime_fin.time()
            
            # Verificar solapamiento: hay conflicto si NO es cierto que termina antes de que empiece la otra O empieza después de que termine la otra
            if not (hora_fin <= reserva_inicio or hora_inicio >= reserva_fin):
                return False, f"Conflicto de horario: El barbero ya tiene una reserva de {reserva_inicio.strftime('%H:%M')} a {reserva_fin.strftime('%H:%M')}"
        
        return True, "Horario disponible"
    
    @classmethod
    def validar_horario_trabajo(cls, barbero_id, fecha, hora_inicio, hora_fin):
        """Valida que la reserva esté dentro del horario de trabajo del barbero"""
        from .barber import Barber
        
        barbero = Barber.query.get(barbero_id)
        if not barbero:
            return False, "Barbero no encontrado"
        
        if not barbero.disponible:
            return False, "El barbero no está disponible"
        
        # TODO: Implementar validación de horario_trabajo cuando se defina la estructura
        # Por ahora asumimos horario de 9:00 a 18:00
        horario_inicio = datetime.strptime("09:00", "%H:%M").time()
        horario_fin = datetime.strptime("18:00", "%H:%M").time()
        
        if isinstance(hora_inicio, str):
            hora_inicio = datetime.strptime(hora_inicio, '%H:%M').time()
        if isinstance(hora_fin, str):
            hora_fin = datetime.strptime(hora_fin, '%H:%M').time()
        
        if hora_inicio < horario_inicio or hora_fin > horario_fin:
            return False, f"La reserva debe estar entre {horario_inicio.strftime('%H:%M')} y {horario_fin.strftime('%H:%M')}"
        
        return True, "Horario válido"
    
    @classmethod
    def validar_fecha_futura(cls, fecha, hora_inicio):
        """Valida que la reserva sea en el futuro"""
        ahora = datetime.now()
        
        if isinstance(hora_inicio, str):
            hora_inicio = datetime.strptime(hora_inicio, '%H:%M').time()
        
        fecha_hora_reserva = datetime.combine(fecha, hora_inicio)
        
        if fecha_hora_reserva <= ahora:
            return False, "No se pueden hacer reservas en el pasado"
        
        # Validar tiempo mínimo de anticipación (30 minutos)
        if fecha_hora_reserva - ahora < timedelta(minutes=30):
            return False, "Debe hacer la reserva con al menos 30 minutos de anticipación"
        
        return True, "Fecha válida"
    
    def puede_cancelar(self, usuario_actual):
        """Verifica si una reserva puede ser cancelada"""
        # Solo el cliente, el barbero asignado o un admin pueden cancelar
        barbero_usuario = None
        if usuario_actual.rol.value == 'barbero':
            from .barber import Barber
            barbero_usuario = Barber.query.filter_by(user_id=usuario_actual.id).first()
        
        tiene_permiso = (
            usuario_actual.id == self.user_id or  # Es el cliente
            usuario_actual.rol.value == 'admin' or  # Es admin
            (barbero_usuario and barbero_usuario.id == self.barber_id)  # Es el barbero asignado
        )
        
        if not tiene_permiso:
            return False, "No tienes permisos para cancelar esta reserva"
        
        # No se puede cancelar si ya está completada
        if self.estado == ReservationStatus.COMPLETADA:
            return False, "No se puede cancelar una reserva completada"
        
        # No se puede cancelar si ya está cancelada
        if self.estado == ReservationStatus.CANCELADA:
            return False, "La reserva ya está cancelada"
        
        # Verificar tiempo mínimo (2 horas antes para clientes, barberos pueden cancelar hasta 30 min antes)
        ahora = datetime.now()
        fecha_hora_reserva = datetime.combine(self.fecha_reserva, self.hora_inicio)
        
        tiempo_minimo = timedelta(hours=2)  # Default para clientes
        if usuario_actual.rol.value in ['barbero', 'admin']:
            tiempo_minimo = timedelta(minutes=30)  # Más flexible para barberos/admins
        
        if fecha_hora_reserva - ahora < tiempo_minimo:
            horas = tiempo_minimo.total_seconds() / 3600
            return False, f"No se puede cancelar con menos de {horas} horas de anticipación"
        
        return True, "Reserva puede ser cancelada"
    
    def puede_confirmar(self, usuario_actual):
        """Verifica si una reserva puede ser confirmada"""
        # Solo barberos o admins pueden confirmar
        if usuario_actual.rol.value not in ['barbero', 'admin']:
            return False, "Solo barberos y administradores pueden confirmar reservas"
        
        # Si es barbero, solo puede confirmar sus propias reservas
        if usuario_actual.rol.value == 'barbero':
            from .barber import Barber
            barbero_usuario = Barber.query.filter_by(user_id=usuario_actual.id).first()
            if not barbero_usuario or barbero_usuario.id != self.barber_id:
                return False, "Solo puedes confirmar tus propias reservas"
        
        # Solo se pueden confirmar reservas pendientes
        if self.estado != ReservationStatus.PENDIENTE:
            return False, f"No se puede confirmar una reserva en estado: {self.estado.value}"
        
        return True, "Reserva puede ser confirmada"
    
    def calcular_hora_fin_desde_servicio(self):
        """Calcula la hora de fin basada en la duración del servicio"""
        if self.hora_fin:
            return  # Ya tiene hora de fin
        
        from .service import Service
        servicio = Service.query.get(self.service_id)
        if servicio and servicio.duracion:
            # Convertir a datetime para hacer cálculos
            datetime_inicio = datetime.combine(self.fecha_reserva, self.hora_inicio)
            datetime_fin = datetime_inicio + timedelta(minutes=servicio.duracion)
            self.hora_fin = datetime_fin.time()
    
    def __repr__(self):
        return f'<Reservation {self.cliente_nombre} - {self.fecha_reserva}>'
