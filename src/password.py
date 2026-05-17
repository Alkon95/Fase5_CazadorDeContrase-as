import random
from src.exceptions import LongitudInvalidaError, ContrasenaInvalidaError

class Contrasena:
    CARACTERES_ESPECIALES = "¿i?=)(/**+-%&$#!."

    def __init__(self, longitud: int):
        if longitud < 8:
            raise LongitudInvalidaError("La longitud mínima permitida es de 8 caracteres.")
        self.__longitud = longitud
        self.__valor = self.__generar_y_validar()

    @property
    def valor(self) -> str:
        return self.__valor

    def __generar_y_validar(self) -> str:
        intentos = 0
        while intentos < 100:
            mayusculas = "ABCDEFGHIJKLMNPQRSTUVWXYZ"
            minusculas = "abcdefghijklmnpqrstuvwxyz"
            numeros = "1234567890"
            
            password_pool = [
                random.choice(mayusculas),
                random.choice(minusculas),
                random.choice(numeros),
                random.choice(self.CARACTERES_ESPECIALES)
            ]
            
            universo_completo = mayusculas + minusculas + numeros + self.CARACTERES_ESPECIALES
            universo_filtrado = [c for c in universo_completo if c not in password_pool]
            
            caracteres_restantes = self.__longitud - len(password_pool)
            password_pool.extend(random.sample(universo_filtrado, caracteres_restantes))
            
            random.shuffle(password_pool)
            candidata = "".join(password_pool)
            
            if self.validar_estricto(candidata):
                return candidata
            intentos += 1
            
        raise ContrasenaInvalidaError("No se pudo generar una contraseña válida.")

    @classmethod
    def validar_estricto(cls, password: str) -> bool:
        if len(password) < 8 or len(password) != len(set(password)):
            return False
        tiene_mayuscula = any(c.isupper() for c in password)
        tiene_minuscula = any(c.islower() for c in password)
        tiene_numero = any(c.isdigit() for c in password)
        tiene_especial = any(c in cls.CARACTERES_ESPECIALES for c in password)
        return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial