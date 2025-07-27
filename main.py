
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

    # Crear equipos de ejemplo (necesitan 11 jugadores, esto es solo un placeholder)
    # Asumo que el Agente 2 creará la lógica para generar equipos completos
    equipo_a = Team("Equipo A", [jugador1, jugador3, jugador4, jugador5] + [Player(f"JugadorA{i}", "DEF", {}) for i in range(7)]) # Placeholder
    equipo_b = Team("Equipo B", [jugador2] + [Player(f"JugadorB{i}", "MED", {}) for i in range(10)]) # Placeholder

    # Crear y simular un partido
    partido = Match(equipo_a, equipo_b)
    partido.iniciar_partido()
