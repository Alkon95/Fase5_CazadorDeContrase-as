# Cazador de Contraseñas - Proyecto Final (Fase 5)

## 1. Descripción del Proyecto
Este software es una solución interactiva de consola desarrollada en el lenguaje de programación Python que simula un entorno de juego enfocado en la seguridad informática. El objetivo principal del sistema es la generación algorítmica de contraseñas robustas a partir de la longitud definida por el usuario, integrando mecánicas de gamificación mediante la apertura de cofres de recompensa o penalización según el flujo operativo.

La aplicación está diseñada bajo el paradigma de Programación Orientada a Objetos (POO) y sigue principios fundamentales de arquitectura limpia y modularidad (SOLID), lo que garantiza un código fuente escalable, mantenible y estructurado bajo estándares profesionales.

## 2. Conceptos de POO Aplicados

El desarrollo del proyecto demuestra la implementación rigurosa de los pilares de la programación orientada a objetos requeridos en la guía de aprendizaje:

1. **Abstracción y Encapsulamiento (src/password.py):** La clase Contrasena aísla la complejidad algorítmica del generador de cadenas aleatorias. Sus atributos internos (__longitud y __valor) están protegidos mediante el mecanismo de visibilidad privada de Python, exponiendo el acceso a la información de manera segura únicamente para lectura mediante decoradores @property.
2. **Herencia (src/chests.py):** Se definió una superclase abstracta denominada Cofre que actúa como plantilla base y define la estructura común para los diferentes componentes de recompensa del sistema.
3. **Polimorfismo (src/chests.py):** Las subclases CofreComun, CofreRaro, CofreLegendario y CofreMaldito heredan de la clase base e implementan de forma polimórfica sus propias versiones del método abstracto abrir(), modificando las propiedades de puntuación del juego de manera independiente y según las reglas de negocio establecidas.
4. **Gestión de Excepciones Personalizadas (src/exceptions.py):** El sistema cuenta con una jerarquía de errores propios que heredan de la clase base Exception (LongitudInvalidaError, TipoDatoInvalidoError, ContrasenaInvalidaError). Esto permite capturar fallos de entrada de datos de forma controlada sin interrumpir de manera abrupta la ejecución del intérprete.
5. **Persistencia de Datos (src/game.py):** Se incorporó un mecanismo de almacenamiento local en formato JSON para salvaguardar el puntaje máximo (High Score) obtenido por el usuario entre diferentes sesiones de ejecución.

## 3. Estructura del Repositorio

El código fuente se encuentra distribuido de forma modular en los siguientes componentes:

* src/main.py: Punto de entrada principal para la inicialización de la aplicación.
* src/game.py: Clase controladora del flujo general de las rondas, lógica del negocio y gestión de persistencia de archivos.
* src/password.py: Clase encargada de la validación estricta y construcción de contraseñas seguras sin caracteres repetidos.
* src/chests.py: Modelado polimórfico y estructural de los cofres del juego.
* src/exceptions.py: Definición de las clases de excepción personalizadas para el control de errores del software.

## 4. Requisitos e Instrucciones de Ejecución

### Requisitos Mínimos
* Sistema Operativo: Linux (Optimizado y probado en arquitecturas basadas en Debian/Ubuntu).
* Entorno de Ejecución: Python 3.10 o superior.
* Sistema de Control de Versiones: Git.

### Instrucciones de Ejecución
1. Abra la terminal de comandos en el directorio raíz del proyecto (Proyecto_Fase5_SoftwareFJ).
2. Ejecute la aplicación utilizando el sistema de módulos nativo de Python mediante el siguiente comando:
   ```bash
   python3 -m src.main