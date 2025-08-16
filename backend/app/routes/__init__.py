"""
Rutas y endpoints para la aplicación Low Barber
"""

from .auth import auth_bp
from .stats import stats_bp

__all__ = [
    'auth_bp',
    'stats_bp'
]
