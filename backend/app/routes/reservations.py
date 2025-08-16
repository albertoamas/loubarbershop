"""
Rutas para la gestión de reservas - Low Barber
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, date, time, timedelta
from marshmallow import ValidationError

from app.models import Reservation, User, Barber, Service, ReservationStatus
from app.models.base import db
from app.schemas.reservation_schemas import (
    reservation_create_schema, reservation_update_schema, reservation_status_update_schema,
    reservation_response_schema, reservations_response_schema,
    availability_query_schema, availability_response_schema
)
from app.utils import admin_required, get_current_user

# Crear blueprint
reservations_bp = Blueprint('reservations', __name__)

@reservations_bp.route('', methods=['GET'])
def get_reservations():
    """Obtener reservas (filtros por usuario/barbero/fecha)"""
    try:
        # **TEMPORAL: Sin autenticación para pruebas**
        # current_user = get_current_user()
        
        # Parámetros de consulta
        barbero_id = request.args.get('barbero_id')
        fecha_inicio = request.args.get('fecha_inicio')
        fecha_fin = request.args.get('fecha_fin')
        estado = request.args.get('estado')
        
        # Construir query base
        query = Reservation.query
        
        # **TEMPORAL: Mostrar todas las reservas para admins**
        # Los admins ven todas las reservas (sin filtro adicional)
        
        # Aplicar filtros adicionales
        if barbero_id:
            query = query.filter_by(barber_id=barbero_id)
        
        if fecha_inicio:
            fecha_inicio_obj = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            query = query.filter(Reservation.fecha_reserva >= fecha_inicio_obj)
        
        if fecha_fin:
            fecha_fin_obj = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
            query = query.filter(Reservation.fecha_reserva <= fecha_fin_obj)
        
        if estado:
            try:
                estado_enum = ReservationStatus(estado)
                query = query.filter_by(estado=estado_enum)
            except ValueError:
                return jsonify({'error': 'Estado de reserva inválido'}), 400
        
        # Ordenar por fecha y hora
        reservas = query.order_by(Reservation.fecha_reserva.desc(), Reservation.hora_inicio.desc()).all()
        
        # Mapear las reservas con información completa
        reservas_data = []
        for reserva in reservas:
            reserva_dict = reservation_response_schema.dump(reserva)
            
            # Agregar información del barbero
            if reserva.barbero:
                reserva_dict['barbero_nombre'] = reserva.barbero.nombre
                reserva_dict['barbero_especialidad'] = reserva.barbero.especialidad
            
            # Agregar información del servicio
            if reserva.servicio:
                reserva_dict['servicio_nombre'] = reserva.servicio.nombre
                reserva_dict['servicio_precio'] = float(reserva.servicio.precio)
                reserva_dict['servicio_duracion'] = reserva.servicio.duracion
            
            reservas_data.append(reserva_dict)
        
        return jsonify({
            'data': reservas_data,
            'total': len(reservas_data),
            'isDemo': False
        }), 200
        
    except Exception as e:
        print(f"Error en get_reservations: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@reservations_bp.route('', methods=['POST'])
@jwt_required()
def create_reservation():
    """Crear una nueva reserva"""
    try:
        current_user = get_current_user()
        print(f"🔍 DEBUG: Usuario actual: {current_user.email} (ID: {current_user.id})")
        print(f"🔍 DEBUG: Datos recibidos: {request.json}")
        
        # Validar datos de entrada
        try:
            data = reservation_create_schema.load(request.json)
            print(f"🔍 DEBUG: Datos validados: {data}")
        except ValidationError as e:
            print(f"❌ DEBUG: Error de validación: {e.messages}")
            return jsonify({
                'error': 'Error de validación',
                'message': 'Los datos enviados no son válidos',
                'validation_errors': e.messages
            }), 400
        
        # Verificar que el barbero exista y esté disponible
        barbero = Barber.query.get(data['barbero_id'])
        print(f"🔍 DEBUG: Barbero encontrado: {barbero.nombre if barbero else 'None'}")
        if barbero:
            print(f"🔍 DEBUG: Barbero - Disponible: {barbero.disponible}, Activo: {barbero.activo}")
        
        if not barbero:
            return jsonify({'error': 'Barbero no encontrado'}), 404
        
        if not barbero.disponible or not barbero.activo:
            return jsonify({'error': 'El barbero no está disponible'}), 400
        
        # Verificar que el servicio exista y esté activo
        servicio = Service.query.get(data['servicio_id'])
        print(f"🔍 DEBUG: Servicio encontrado: {servicio.nombre if servicio else 'None'}")
        if servicio:
            print(f"🔍 DEBUG: Servicio - Activo: {servicio.activo}")
        
        if not servicio:
            return jsonify({'error': 'Servicio no encontrado'}), 404
        
        if not servicio.activo:
            return jsonify({'error': 'El servicio no está disponible'}), 400
        
        # Calcular hora de fin basada en la duración del servicio
        datetime_inicio = datetime.combine(data['fecha_reserva'], data['hora_inicio'])
        datetime_fin = datetime_inicio + timedelta(minutes=servicio.duracion)
        hora_fin = datetime_fin.time()
        
        # Crear la reserva
        reserva = Reservation(
            user_id=current_user.id,
            barber_id=data['barbero_id'],
            service_id=data['servicio_id'],
            fecha_reserva=data['fecha_reserva'],
            hora_inicio=data['hora_inicio'],
            cliente_nombre=current_user.nombre,
            cliente_email=current_user.email,
            cliente_telefono=current_user.telefono,
            notas=data.get('notas')
        )
        
        # Establecer hora de fin y precio
        reserva.hora_fin = hora_fin
        reserva.precio_final = servicio.precio
        
        db.session.add(reserva)
        db.session.commit()
        
        return jsonify({
            'message': 'Reserva creada exitosamente',
            'reserva': reservation_response_schema.dump(reserva)
        }), 201
        
    except ValidationError as e:
        return jsonify({
            'error': 'Datos de entrada inválidos',
            'details': e.messages
        }), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@reservations_bp.route('/<reservation_id>', methods=['GET'])
@jwt_required()
def get_reservation(reservation_id):
    """Obtener una reserva específica"""
    try:
        current_user = get_current_user()
        
        reserva = Reservation.query.get(reservation_id)
        if not reserva:
            return jsonify({'error': 'Reserva no encontrada'}), 404
        
        # Verificar permisos
        if current_user.rol.value == 'cliente' and reserva.user_id != current_user.id:
            return jsonify({'error': 'No tienes permisos para ver esta reserva'}), 403
        
        if current_user.rol.value == 'barbero':
            barbero = Barber.query.filter_by(user_id=current_user.id).first()
            if not barbero or reserva.barber_id != barbero.id:
                return jsonify({'error': 'No tienes permisos para ver esta reserva'}), 403
        
        return jsonify({
            'reserva': reservation_response_schema.dump(reserva)
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@reservations_bp.route('/<reservation_id>', methods=['PUT'])
@jwt_required()
def update_reservation(reservation_id):
    """Actualizar una reserva"""
    try:
        current_user = get_current_user()
        
        reserva = Reservation.query.get(reservation_id)
        if not reserva:
            return jsonify({'error': 'Reserva no encontrada'}), 404
        
        # Solo el cliente propietario o admins pueden actualizar
        if current_user.rol.value == 'cliente' and reserva.user_id != current_user.id:
            return jsonify({'error': 'No tienes permisos para actualizar esta reserva'}), 403
        
        # Solo se pueden actualizar reservas pendientes
        if reserva.estado != ReservationStatus.PENDIENTE:
            return jsonify({'error': 'Solo se pueden actualizar reservas pendientes'}), 400
        
        # Validar datos
        data = reservation_update_schema.load(request.json)
        
        # Si se cambia fecha u hora, validar disponibilidad
        if 'fecha_reserva' in data or 'hora_inicio' in data:
            nueva_fecha = data.get('fecha_reserva', reserva.fecha_reserva)
            nueva_hora = data.get('hora_inicio', reserva.hora_inicio)
            
            # Recalcular hora_fin si cambió la hora_inicio
            if 'hora_inicio' in data:
                servicio = Service.query.get(reserva.service_id)
                datetime_inicio = datetime.combine(nueva_fecha, nueva_hora)
                datetime_fin = datetime_inicio + timedelta(minutes=servicio.duracion)
                hora_fin = datetime_fin.time()
            else:
                hora_fin = reserva.hora_fin
            
            # Validar disponibilidad (excluyendo la reserva actual)
            disponible, mensaje = Reservation.validar_disponibilidad(
                reserva.barber_id, nueva_fecha, nueva_hora, hora_fin, reserva.id
            )
            
            if not disponible:
                return jsonify({'error': mensaje}), 400
            
            # Actualizar hora_fin si cambió hora_inicio
            if 'hora_inicio' in data:
                reserva.hora_fin = hora_fin
        
        # Actualizar campos
        for field, value in data.items():
            setattr(reserva, field, value)
        
        db.session.commit()
        
        return jsonify({
            'message': 'Reserva actualizada exitosamente',
            'reserva': reservation_response_schema.dump(reserva)
        }), 200
        
    except ValidationError as e:
        return jsonify({
            'error': 'Datos de entrada inválidos',
            'details': e.messages
        }), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@reservations_bp.route('/<reservation_id>/cancel', methods=['POST'])
@jwt_required()
def cancel_reservation(reservation_id):
    """Cancelar una reserva"""
    try:
        current_user = get_current_user()
        
        reserva = Reservation.query.get(reservation_id)
        if not reserva:
            return jsonify({'error': 'Reserva no encontrada'}), 404
        
        # Verificar si se puede cancelar
        puede_cancelar, mensaje = reserva.puede_cancelar(current_user)
        if not puede_cancelar:
            return jsonify({'error': mensaje}), 400
        
        # Cancelar la reserva
        reserva.cancelar()
        
        return jsonify({
            'message': 'Reserva cancelada exitosamente',
            'reserva': reservation_response_schema.dump(reserva)
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@reservations_bp.route('/<reservation_id>/confirm', methods=['POST'])
@jwt_required()
def confirm_reservation(reservation_id):
    """Confirmar una reserva (solo barberos y admins)"""
    try:
        current_user = get_current_user()
        
        reserva = Reservation.query.get(reservation_id)
        if not reserva:
            return jsonify({'error': 'Reserva no encontrada'}), 404
        
        # Verificar si se puede confirmar
        puede_confirmar, mensaje = reserva.puede_confirmar(current_user)
        if not puede_confirmar:
            return jsonify({'error': mensaje}), 400
        
        # Confirmar la reserva
        reserva.confirmar()
        
        return jsonify({
            'message': 'Reserva confirmada exitosamente',
            'reserva': reservation_response_schema.dump(reserva)
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@reservations_bp.route('/<reservation_id>/complete', methods=['POST'])
@jwt_required()
def complete_reservation(reservation_id):
    """Completar una reserva (solo barberos y admins)"""
    try:
        current_user = get_current_user()
        
        reserva = Reservation.query.get(reservation_id)
        if not reserva:
            return jsonify({'error': 'Reserva no encontrada'}), 404
        
        # Solo barberos asignados o admins pueden completar
        if current_user.rol.value == 'barbero':
            barbero = Barber.query.filter_by(user_id=current_user.id).first()
            if not barbero or reserva.barber_id != barbero.id:
                return jsonify({'error': 'Solo puedes completar tus propias reservas'}), 403
        elif current_user.rol.value != 'admin':
            return jsonify({'error': 'No tienes permisos para completar reservas'}), 403
        
        # Solo se pueden completar reservas confirmadas o en proceso
        if reserva.estado not in [ReservationStatus.CONFIRMADA, ReservationStatus.EN_PROCESO]:
            return jsonify({'error': 'Solo se pueden completar reservas confirmadas o en proceso'}), 400
        
        # Obtener precio final si se envía
        data = request.get_json() or {}
        precio_final = data.get('precio_final')
        notas_barbero = data.get('notas_barbero')
        
        # Completar la reserva
        reserva.completar(precio_final)
        
        if notas_barbero:
            reserva.notas_barbero = notas_barbero
            db.session.commit()
        
        return jsonify({
            'message': 'Reserva completada exitosamente',
            'reserva': reservation_response_schema.dump(reserva)
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500

@reservations_bp.route('/availability', methods=['GET'])
def get_availability():
    """Consultar disponibilidad de un barbero en una fecha"""
    try:
        # Validar parámetros
        barbero_id = request.args.get('barbero_id')
        fecha_str = request.args.get('fecha')
        
        if not barbero_id or not fecha_str:
            return jsonify({
                'error': 'Se requieren los parámetros barbero_id y fecha'
            }), 400
        
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({
                'error': 'Formato de fecha inválido. Use YYYY-MM-DD'
            }), 400
        
        # Validar que el barbero exista
        barbero = Barber.query.get(barbero_id)
        if not barbero:
            return jsonify({'error': 'Barbero no encontrado'}), 404
        
        if not barbero.disponible:
            return jsonify({
                'fecha': fecha.isoformat(),
                'barbero_id': barbero_id,
                'barbero_nombre': barbero.nombre,
                'disponible': False,
                'mensaje': 'El barbero no está disponible'
            }), 200
        
        # Obtener reservas del barbero en esa fecha
        reservas = Reservation.get_disponibilidad_barbero(barbero_id, fecha)
        
        # Crear lista de horarios ocupados
        horarios_ocupados = []
        for reserva in reservas:
            horarios_ocupados.append({
                'hora_inicio': reserva.hora_inicio.strftime('%H:%M'),
                'hora_fin': reserva.hora_fin.strftime('%H:%M') if reserva.hora_fin else None,
                'reserva_id': reserva.id,
                'estado': reserva.estado.value
            })
        
        # Generar horarios disponibles (cada 30 minutos de 9:00 a 18:00)
        horarios_disponibles = []
        hora_actual = time(9, 0)  # 9:00 AM
        hora_limite = time(18, 0)  # 6:00 PM
        
        while hora_actual < hora_limite:
            # Verificar si este horario está ocupado
            ocupado = False
            for reserva in reservas:
                if reserva.hora_inicio <= hora_actual < (reserva.hora_fin or time(hora_actual.hour + 1, hora_actual.minute)):
                    ocupado = True
                    break
            
            if not ocupado:
                horarios_disponibles.append({
                    'hora': hora_actual.strftime('%H:%M'),
                    'disponible': True
                })
            
            # Avanzar 30 minutos
            minutos = hora_actual.minute + 30
            hora = hora_actual.hour
            if minutos >= 60:
                minutos -= 60
                hora += 1
            hora_actual = time(hora, minutos)
        
        return jsonify({
            'fecha': fecha.isoformat(),
            'barbero_id': barbero_id,
            'barbero_nombre': barbero.nombre,
            'disponible': True,
            'horarios_ocupados': horarios_ocupados,
            'horarios_disponibles': horarios_disponibles
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error interno del servidor',
            'message': str(e)
        }), 500
