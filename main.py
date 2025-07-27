
# clitest/main.py
from player import Player
from team import Team
from match import Match

if __name__ == "__main__":
    # Crear jugadores de ejemplo
    jugador1 = Player("Messi", "DEL", {"tiro": 95, "pase": 90, "velocidad": 90})
    jugador2 = Player("Ronaldo", "DEL", {"tiro": 92, "pase": 70, "velocidad": 88})
    jugador3 = Player("Modric", "MED", {"tiro": 80, "pase": 95, "velocidad": 75})
    jugador4 = Player("Ramos", "DEF", {"tiro": 60, "pase": 70, "velocidad": 70, "defensa": 90})
    jugador5 = Player("Neuer", "PO", {"parada": 95})

    # Crear equipos de ejemplo usando la función de generación aleatoria
    equipo_a = Team.generar_equipo_aleatorio("Equipo A")
    equipo_b = Team.generar_equipo_aleatorio("Equipo B")

    # Crear y simular un partido
    partido = Match(equipo_a, equipo_b)
    partido.iniciar_partido()
