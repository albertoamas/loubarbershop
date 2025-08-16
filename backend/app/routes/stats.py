"""
Rutas para estadísticas del panel administrativo
"""

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, Reservation, Service, Barber, UserRole, ReservationStatus, db
from sqlalchemy import func, extract, text
from datetime import datetime, timedelta
import calendar

# Crear el blueprint
stats_bp = Blueprint('stats', __name__)

@stats_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard_stats():
    """Obtener estadísticas generales del dashboard"""
    try:
        # Verificar que el usuario sea administrador
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        # Verificar que el usuario existe
        if not user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
            
        # Verificar que el usuario sea administrador
        if user.rol != UserRole.ADMIN:
            return jsonify({'error': 'Acceso denegado'}), 403

        # Obtener fecha actual
        today = datetime.now().date()
        this_month_start = today.replace(day=1)
        last_month_start = (this_month_start - timedelta(days=1)).replace(day=1)
        
        # Reservas de hoy
        try:
            reservas_hoy = Reservation.query.filter(
                Reservation.fecha_reserva == today
            ).count()
        except Exception as e:
            reservas_hoy = 0
        
        # Reservas del mes actual
        try:
            reservas_mes = Reservation.query.filter(
                Reservation.fecha_reserva >= this_month_start
            ).count()
        except Exception as e:
            reservas_mes = 0
        
        # Reservas del mes pasado para comparación
        try:
            reservas_mes_pasado = Reservation.query.filter(
                Reservation.fecha_reserva >= last_month_start,
                Reservation.fecha_reserva < this_month_start
            ).count()
        except Exception as e:
            reservas_mes_pasado = 0
        
        # Calcular porcentaje de cambio
        if reservas_mes_pasado > 0:
            cambio_reservas = ((reservas_mes - reservas_mes_pasado) / reservas_mes_pasado) * 100
        else:
            cambio_reservas = 100 if reservas_mes > 0 else 0
        
        # Ingresos del mes (simulado - necesitarías un campo de precio en reservas)
        ingresos_mes = reservas_mes * 25000  # Precio promedio simulado
        ingresos_mes_pasado = reservas_mes_pasado * 25000
        
        if ingresos_mes_pasado > 0:
            cambio_ingresos = ((ingresos_mes - ingresos_mes_pasado) / ingresos_mes_pasado) * 100
        else:
            cambio_ingresos = 100 if ingresos_mes > 0 else 0
        
        # Usuarios activos
        try:
            usuarios_activos = User.query.filter_by(activo=True).count()
        except Exception as e:
            usuarios_activos = 0
        
        # Barberos disponibles
        try:
            barberos_disponibles = Barber.query.filter_by(activo=True).count()
        except Exception as e:
            barberos_disponibles = 0
        
        stats = {
            'reservas_hoy': reservas_hoy,
            'reservas_mes': reservas_mes,
            'cambio_reservas': round(cambio_reservas, 1),
            'ingresos_mes': ingresos_mes,
            'cambio_ingresos': round(cambio_ingresos, 1),
            'usuarios_activos': usuarios_activos,
            'barberos_disponibles': barberos_disponibles,
            'ultima_actualizacion': datetime.now().isoformat()
        }
        
        return jsonify(stats), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@stats_bp.route('/reservations', methods=['GET'])
def get_reservation_stats():
    """Obtener estadísticas de reservas por período"""
    try:
        # **TEMPORAL: Sin autenticación para pruebas**
        # current_user_id = get_jwt_identity()
        # user = User.query.get(current_user_id)
        # if user.rol != UserRole.ADMIN:
        #     return jsonify({'error': 'Acceso denegado'}), 403

        # Obtener fecha actual
        today = datetime.now().date()
        
        # Estadísticas básicas
        try:
            total = Reservation.query.count()
            today_count = Reservation.query.filter(Reservation.fecha_reserva == today).count()
            
            # Contar por estado
            pending = Reservation.query.filter_by(estado=ReservationStatus.PENDIENTE).count()
            confirmed = Reservation.query.filter_by(estado=ReservationStatus.CONFIRMADA).count()  
            completed = Reservation.query.filter_by(estado=ReservationStatus.COMPLETADA).count()
            cancelled = Reservation.query.filter_by(estado=ReservationStatus.CANCELADA).count()
            
        except Exception as e:
            print(f"Error contando reservas: {e}")
            # Si no hay datos, devolver 0s
            total = 0
            today_count = 0
            pending = 0
            confirmed = 0
            completed = 0
            cancelled = 0
        
        stats = {
            'total': total,
            'today': today_count,
            'hoy': today_count,  # Alias para compatibilidad
            'pending': pending,
            'pendientes': pending,  # Alias para compatibilidad
            'confirmed': confirmed,
            'confirmadas': confirmed,  # Alias para compatibilidad
            'completed': completed,
            'completadas': completed,  # Alias para compatibilidad
            'cancelled': cancelled,
            'canceladas': cancelled,  # Alias para compatibilidad
            'isDemo': False
        }
        
        return jsonify({
            'data': stats,
            **stats  # También devolver las estadísticas en el nivel raíz
        }), 200
        
    except Exception as e:
        print(f"Error en get_reservation_stats: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@stats_bp.route('/revenue', methods=['GET'])
@jwt_required()
def get_revenue_stats():
    """Obtener estadísticas de ingresos por período"""
    try:
        # Verificar que el usuario sea administrador
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        if user.rol != UserRole.ADMIN:
            return jsonify({'error': 'Acceso denegado'}), 403

        # Obtener parámetros
        last_months = int(request.args.get('last_months', 6))
        
        # Calcular fechas
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=30 * last_months)
        
        # Obtener ingresos agrupados por mes (simulado)
        reservations_by_month = db.session.query(
            extract('year', Reservation.fecha_reserva).label('year'),
            extract('month', Reservation.fecha_reserva).label('month'),
            func.count(Reservation.id).label('count')
        ).filter(
            Reservation.fecha_reserva >= start_date
        ).group_by('year', 'month').order_by('year', 'month').all()
        
        # Formatear datos (precio promedio simulado de $25,000 por reserva)
        labels = []
        data = []
        
        for year, month, count in reservations_by_month:
            month_name = calendar.month_name[int(month)]
            labels.append(f"{month_name} {int(year)}")
            revenue = count * 25000  # Precio promedio simulado
            data.append(revenue)
        
        result = {
            'labels': labels,
            'datasets': [{
                'label': 'Ingresos ($)',
                'data': data,
                'backgroundColor': 'rgba(34, 197, 94, 0.1)',
                'borderColor': 'rgb(34, 197, 94)',
                'borderWidth': 2,
                'fill': True
            }]
        }
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@stats_bp.route('/popular-services', methods=['GET'])
@jwt_required()
def get_popular_services():
    """Obtener servicios más populares"""
    try:
        # Verificar que el usuario sea administrador
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        if user.rol != UserRole.ADMIN:
            return jsonify({'error': 'Acceso denegado'}), 403

        limit = int(request.args.get('limit', 10))
        
        # Por ahora devolvemos datos simulados ya que no tenemos la relación reserva-servicio
        popular_services = [
            {'nombre': 'Corte Clásico', 'reservas': 45, 'porcentaje': 35.2},
            {'nombre': 'Barba y Bigote', 'reservas': 32, 'porcentaje': 25.0},
            {'nombre': 'Corte Moderno', 'reservas': 28, 'porcentaje': 21.9},
            {'nombre': 'Afeitado Completo', 'reservas': 23, 'porcentaje': 18.0}
        ]
        
        return jsonify(popular_services[:limit]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@stats_bp.route('/barbers', methods=['GET'])
def get_barber_stats():
    """Obtener estadísticas de barberos"""
    try:
        # **TEMPORAL: Sin autenticación para pruebas**
        # current_user_id = get_jwt_identity()
        # user = User.query.get(current_user_id)
        # if user.rol != UserRole.ADMIN:
        #     return jsonify({'error': 'Acceso denegado'}), 403

        # Obtener barberos con sus estadísticas
        barberos = Barber.query.filter_by(activo=True).all()
        
        barber_stats = []
        for barber in barberos:
            # Contar reservas por barbero (simulado por ahora)
            reservas_count = Reservation.query.count() // len(barberos) if barberos else 0
            
            barber_stats.append({
                'id': str(barber.id),
                'nombre': barber.nombre,
                'especialidad': barber.especialidad or 'General',
                'reservas_mes': reservas_count,
                'calificacion': 4.5,  # Simulado
                'ingresos_mes': reservas_count * 25000,  # Simulado
                'activo': barber.activo
            })
        
        # Estadísticas generales de barberos
        total_barberos = Barber.query.count()
        activos = Barber.query.filter_by(activo=True).count()
        disponibles_hoy = Barber.query.filter_by(activo=True, disponible=True).count()
        
        stats_generales = {
            'total': total_barberos,
            'activos': activos,
            'inactivos': total_barberos - activos,
            'disponibles_hoy': disponibles_hoy,
            'promedio_reservas': 12,  # Simulado
            'ingresos_totales': activos * 50000,  # Simulado
            'barberos': barber_stats
        }
        
        return jsonify({
            'data': stats_generales,
            **stats_generales  # También en nivel raíz para compatibilidad
        }), 200
        
    except Exception as e:
        print(f"Error en get_barber_stats: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@stats_bp.route('/real-time', methods=['GET'])
@jwt_required()
def get_real_time_metrics():
    """Obtener métricas en tiempo real"""
    try:
        # Verificar que el usuario sea administrador
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        if user.rol != UserRole.ADMIN:
            return jsonify({'error': 'Acceso denegado'}), 403

        today = datetime.now().date()
        
        # Métricas en tiempo real
        metrics = {
            'reservas_hoy': Reservation.query.filter(
                Reservation.fecha_reserva == today
            ).count(),
            'usuarios_online': 12,  # Simulado
            'barberos_trabajando': Barber.query.filter_by(activo=True).count(),
            'ingresos_hoy': Reservation.query.filter(
                Reservation.fecha_reserva == today
            ).count() * 25000,  # Simulado
            'ocupacion_actual': 75.5,  # Simulado (%)
            'proxima_reserva': '14:30',  # Simulado
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(metrics), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
