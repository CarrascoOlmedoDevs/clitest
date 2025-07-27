
# clitest/match.py
import random
from team import Team
from config import DURACION_PARTIDO

class Match:
    def __init__(self, equipo_local, equipo_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.minuto_actual = 0
        self.marcador = {equipo_local.nombre: 0, equipo_visitante.nombre: 0}
        self.log_eventos = []

    def iniciar_partido(self):
        self.log_eventos.append("¡Comienza el partido!")
        print("¡Comienza el partido!")

        for self.minuto_actual in range(1, DURACION_PARTIDO + 1):
            # Lógica de eventos por minuto
            self.log_eventos.append(f"Minuto {self.minuto_actual}")
            # Simulación de eventos (muy básica por ahora)
            if random.random() < 0.01: # 1% de probabilidad de gol por minuto
                equipo_anotador = random.choice([self.equipo_local, self.equipo_visitante])
                self.marcador[equipo_anotador.nombre] += 1
                evento = f"¡GOL de {equipo_anotador.nombre}! Marcador: {self.equipo_local.nombre} {self.marcador[self.equipo_local.nombre]} - {self.marcador[self.equipo_visitante.nombre]} {self.equipo_visitante.nombre}"
                self.log_eventos.append(evento)
                print(evento)

        self.log_eventos.append("Tiempo reglamentario cumplido.")
        print("Tiempo reglamentario cumplido.")

        self.finalizar_partido()

    def finalizar_partido(self):
        resultado = f"Final del partido: {self.equipo_local.nombre} {self.marcador[self.equipo_local.nombre]} - {self.marcador[self.equipo_visitante.nombre]} {self.equipo_visitante.nombre}"
        self.log_eventos.append(resultado)
        print(resultado)

    def __str__(self):
        return f"Partido entre {self.equipo_local} y {self.equipo_visitante}"
