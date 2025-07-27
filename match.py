
# clitest/match.py
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

        # La lógica principal de la simulación irá aquí

        self.finalizar_partido()

    def finalizar_partido(self):
        resultado = f"Final del partido: {self.equipo_local.nombre} {self.marcador[self.equipo_local.nombre]} - {self.marcador[self.equipo_visitante.nombre]} {self.equipo_visitante.nombre}"
        self.log_eventos.append(resultado)
        print(resultado)

    def __str__(self):
        return f"Partido entre {self.equipo_local} y {self.equipo_visitante}"
