import random
from src.exceptions import LongitudInvalidaError, ContrasenaInvalidaError

class Contrasena:
    """Clase responsable de la abstracción, encapsulamiento y validación de contraseñas."""
    
    # Lista exacta de caracteres especiales solicitada en la guía de la UNAD
    CARACTERES_ESPECIALES: str = "¿i?=)(/**+-%&$#!."

    def __init__(self, longitud: int):
        if longitud < 8:
            raise LongitudInvalidaError("La longitud mínima permitida es de 8 caracteres.")
        
        self.__longitud: int = longitud
        self.__valor: str = self.__generar_y_validar()

    @property
    def valor(self) -> str:
        """Encapsulamiento: Permite leer la contraseña (get) pero no modificarla externamente."""
        return self.__valor

    def __generar_y_validar(self) -> str:
        """Genera una contraseña aleatoria sin patrones repetidos y que cumpla la guía."""
        intentos = 0
        while intentos < 100:  # Límite seguro para evitar bucles infinitos
            mayusculas = "ABCDEFGHIJKLMNPQRSTUVWXYZ"
            minusculas = "abcdefghijklmnpqrstuvwxyz"
            numeros = "1234567890"
            
            # Aseguramos al menos un elemento de cada grupo obligatorio
            password_pool = [
                random.choice(mayusculas),
                random.choice(minusculas),
                random.choice(numeros),
                random.choice(self.CARACTERES_ESPECIALES)
            ]
            
            # Combinamos todo el universo de caracteres posibles
            universo_completo = mayusculas + minusculas + numeros + self.CARACTERES_ESPECIALES
            
            # Filtramos caracteres que ya usamos para evitar repeticiones accidentales
            universo_filtrado = [c for c in universo_completo if c not in password_pool]
            
            caracteres_restantes = self.__longitud - len(password_pool)
            if caracteres_restantes > len(universo_filtrado):
                raise LongitudInvalidaError("Longitud excesiva para generar caracteres sin repetir.")
                
            password_pool.extend(random.sample(universo_filtrado, caracteres_restantes))
            
            # Mezclamos completamente para eliminar cualquier orden predecible
            random.shuffle(password_pool)
            candidata = "".join(password_pool)
            
            # Validación rigurosa antes de retornarla
            if self.validar_estricto(candidata):
                return candidata
            intentos += 1
            
        raise ContrasenaInvalidaError("No se pudo generar una contraseña válida en los intentos del sistema.")

    @classmethod
    def validar_estricto(cls, password: str) -> bool:
        """Verifica de manera algorítmica que la cadena cumpla las condiciones de la guía."""
        if len(password) < 8:
            return False
        if len(password) != len(set(password)):  # Valida que no haya caracteres repetidos
            return False
            
        tiene_mayuscula = any(c.isupper() for c in password)
        tiene_minuscula = any(c.islower() for c in password)
        tiene_numero = any(c.isdigit() for c in password)
        tiene_especial = any(c in cls.CARACTERES_ESPECIALES for c in password)
        
        return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial