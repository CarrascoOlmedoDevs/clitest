import random
from player import Player
from config import POSICIONES, generar_nombre_jugador

class Team:
    def __init__(self, nombre, jugadores):
        self.nombre = nombre
        if len(jugadores) != 11:
            raise ValueError("Un equipo debe tener exactamente 11 jugadores.")
        self.jugadores = jugadores

    def __str__(self):
        return self.nombre

    @classmethod
    def generar_equipo_aleatorio(cls, nombre_equipo):
        jugadores = []
        # Portero
        jugadores.append(Player(generar_nombre_jugador(), "PO", {"parada": random.randint(70, 95)}))
        # Defensas
        for i in range(1, 5):
            jugadores.append(Player(generar_nombre_jugador(), "DEF", {"defensa": random.randint(60, 90), "velocidad": random.randint(50, 80)}))
        # Mediocentros
        for i in range(1, 4):
            jugadores.append(Player(generar_nombre_jugador(), "MED", {"pase": random.randint(60, 90), "velocidad": random.randint(50, 85)}))
        # Delanteros
        for i in range(1, 4):
            jugadores.append(Player(generar_nombre_jugador(), "DEL", {"tiro": random.randint(60, 95), "velocidad": random.randint(60, 90)}))

        return cls(nombre_equipo, jugadores)

    def get_jugador_aleatorio(self):
        return random.choice(self.jugadores)

    def get_mejor_atacante(self):
        atacantes = [p for p in self.jugadores if p.posicion in ["MED", "DEL"]]
        if not atacantes:
            return max(self.jugadores, key=lambda p: p.get_valor_ataque())
        return max(atacantes, key=lambda p: p.get_valor_ataque())

    def get_mejor_defensor(self):
        defensores = [p for p in self.jugadores if p.posicion in ["DEF", "MED"]]
        if not defensores:
            return max(self.jugadores, key=lambda p: p.get_valor_defensa())
        return max(defensores, key=lambda p: p.get_valor_defensa())

    def get_portero(self):
        for p in self.jugadores:
            if p.posicion == "PO":
                return p
        return None