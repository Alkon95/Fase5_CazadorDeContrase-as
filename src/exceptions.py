class JuegoException(Exception):
    """Clase base para las excepciones del juego Cazador de Contraseñas."""
    pass

class LongitudInvalidaError(JuegoException):
    """Excepción lanzada cuando la longitud de la contraseña es menor a 8."""
    pass

class TipoDatoInvalidoError(JuegoException):
    """Excepción lanzada cuando el usuario ingresa un dato que no es un número."""
    pass

class ContrasenaInvalidaError(JuegoException):
    """Excepción lanzada cuando el generador no logra crear una contraseña válida."""
    pass