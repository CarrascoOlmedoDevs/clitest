
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
            # Lógica de gol más sofisticada
            if random.random() < 0.05: # 5% de probabilidad de que haya una "oportunidad" de gol
                equipo_atacante = random.choice([self.equipo_local, self.equipo_visitante])
                equipo_defensor = self.equipo_visitante if equipo_atacante == self.equipo_local else self.equipo_local

                atacante = equipo_atacante.get_mejor_atacante()
                portero_defensor = equipo_defensor.get_portero()

                # Calcular la probabilidad de gol basada en estadísticas
                probabilidad_gol = (atacante.get_valor_ataque() - portero_defensor.stats.get("parada", 50)) / 100.0
                probabilidad_gol = max(0.01, min(0.99, probabilidad_gol)) # Asegurar que esté entre 0.01 y 0.99

                if random.random() < probabilidad_gol:
                    self.marcador[equipo_atacante.nombre] += 1
                    evento = f"¡GOL de {equipo_atacante.nombre} (anotado por {atacante.nombre})! Marcador: {self.equipo_local.nombre} {self.marcador[self.equipo_local.nombre]} - {self.marcador[self.equipo_visitante.nombre]} {self.equipo_visitante.nombre}"
                    self.log_eventos.append(evento)
                    print(evento)
                else:
                    evento = f"Ocasión fallida de {equipo_atacante.nombre}. El portero {portero_defensor.nombre} detuvo el disparo de {atacante.nombre}."
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
