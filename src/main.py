"""
Punto de acceso principal para ejecutar el software del proyecto final.
"""
import sys
from src.game import JuegoCazador

def main():
    juego = JuegoCazador()
    juego.iniciar_juego()

if __name__ == "__main__":
    main()