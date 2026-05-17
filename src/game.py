import json
import os
import random
from src.exceptions import TipoDatoInvalidoError, LongitudInvalidaError, ContrasenaInvalidaError
from src.password import Contrasena
from src.chests import CofreComun, CofreRaro, CofreLegendario, CofreMaldito

class JuegoCazador:
    ARCH_PUNTAJE = "high_score.json"

    def __init__(self):
        self.puntaje_actual = 0
        self.rondas_jugadas = 0
        self.record_maximo = self.__cargar_record()

    def __cargar_record(self) -> int:
        if os.path.exists(self.ARCH_PUNTAJE):
            try:
                with open(self.ARCH_PUNTAJE, "r") as f:
                    return json.load(f).get("high_score", 0)
            except Exception:
                return 0
        return 0

    def __guardar_record(self):
        if self.puntaje_actual > self.record_maximo:
            self.record_maximo = self.puntaje_actual
            try:
                with open(self.ARCH_PUNTAJE, "w") as f:
                    json.dump({"high_score": self.record_maximo}, f)
            except Exception:
                pass

    def iniciar_juego(self):
        print("==================================================")
        print("     ¡BIENVENIDO AL CAZADOR DE CONTRASEÑAS!       ")
        print(f"      Puntaje Máximo Histórico Registrado: {self.record_maximo}")
        print("==================================================")

        while True:
            self.rondas_jugadas += 1
            print(f"\n--- RONDA {self.rondas_jugadas} (Puntaje Actual: {self.puntaje_actual}) ---")
            
            entrada = input("Ingresa la longitud deseada para la contraseña (mínimo 8): ").strip()
            
            if not entrada.isdigit():
                try:
                    raise TipoDatoInvalidoError("Error: Debes ingresar un número entero válido.")
                except TipoDatoInvalidoError as e:
                    print(f"\n[⚠️ Excepción Atrapada]: {e}")
                    self.__procesar_contrasena_invalida()
                if not self.__desea_continuar(): break
                continue

            longitud = int(entrada)

            try:
                pwd_objeto = Contrasena(longitud)
                print(f"\n[🔑] Contraseña Generada Exitosamente: {pwd_objeto.valor}")
                
                cofre_obtenido = random.choice([CofreComun(), CofreRaro(), CofreLegendario()])
                puntos_ganados = cofre_obtenido.abrir()
                self.puntaje_actual += puntos_ganados
                print(f"[🎁] ¡Has abierto un {cofre_obtenido.nombre}! Obtienes +{puntos_ganados} puntos.")

            except (LongitudInvalidaError, ContrasenaInvalidaError) as e:
                print(f"\n[⚠️ Excepción Controlada]: {e}")
                self.__procesar_contrasena_invalida()

            print(f"Total acumulado: {self.puntaje_actual} puntos.")
            self.__guardar_record()
            
            if not self.__desea_continuar(): break

        print("\n==================================================")
        print(f" Rondas Completadas: {self.rondas_jugadas} | Puntaje Final: {self.puntaje_actual}")
        print("==================================================")

    def __procesar_contrasena_invalida(self):
        cofre_mal = CofreMaldito()
        penalizacion = cofre_mal.abrir()
        self.puntaje_actual += penalizacion
        print(f"[💀] ¡Se ha desatado un {cofre_mal.nombre}! Penalización: {penalizacion} puntos.")

    def __desea_continuar(self) -> bool:
        opcion = input("\n¿Deseas cazar otra contraseña? (S/N): ").strip().lower()
        return opcion in ["s", "si", ""]