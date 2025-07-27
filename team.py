from player import Player

class Team:
    def __init__(self, nombre, jugadores):
        self.nombre = nombre
        if len(jugadores) != 11:
            raise ValueError("Un equipo debe tener exactamente 11 jugadores.")
        self.jugadores = jugadores

    def __str__(self):
        return self.nombre