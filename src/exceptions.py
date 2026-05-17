class JuegoException(Exception):
    """Excepción base para el proyecto de software."""
    pass

class LongitudInvalidaError(JuegoException):
    """Se lanza cuando la longitud es menor a 8."""
    pass

class TipoDatoInvalidoError(JuegoException):
    """Se lanza cuando se ingresan letras en lugar de números."""
    pass

class ContrasenaInvalidaError(JuegoException):
    """Se lanza ante fallos internos de generación."""
    pass