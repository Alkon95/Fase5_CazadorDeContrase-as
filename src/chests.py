from abc import ABC, abstractmethod

class Cofre(ABC):
    def __init__(self, nombre: str, modificador_puntos: int):
        self.nombre = nombre
        self.modificador_puntos = modificador_puntos

    @abstractmethod
    def abrir(self) -> int:
        pass

class CofreComun(Cofre):
    def __init__(self): super().__init__("Cofre Común", 10)
    def abrir(self) -> int: return self.modificador_puntos

class CofreRaro(Cofre):
    def __init__(self): super().__init__("Cofre Raro", 25)
    def abrir(self) -> int: return self.modificador_puntos

class CofreLegendario(Cofre):
    def __init__(self): super().__init__("Cofre Legendario", 50)
    def abrir(self) -> int: return self.modificador_puntos

class CofreMaldito(Cofre):
    def __init__(self): super().__init__("Cofre Maldito", -20)
    def abrir(self) -> int: return self.modificador_puntos