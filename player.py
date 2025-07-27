class Player:
    def __init__(self, nombre, posicion, stats):
        self.nombre = nombre
        self.posicion = posicion # Ej: "PO", "DEF", "MED", "DEL"
        self.stats = {
            "tiro": stats.get("tiro", 50),
            "pase": stats.get("pase", 50),
            "velocidad": stats.get("velocidad", 50),
            "defensa": stats.get("defensa", 50),
            "parada": stats.get("parada", 50) # Solo para porteros
        }

    def __str__(self):
        return f"{self.nombre} ({self.posicion})"

    def get_info(self):
        info = f"Nombre: {self.nombre}, Posición: {self.posicion}"
        for stat, value in self.stats.items():
            info += f", {stat.capitalize()}: {value}"
        return info

    def get_valor_ataque(self):
        # Ejemplo de cálculo, puedes ajustarlo
        return (self.stats.get("tiro", 0) * 0.6) + (self.stats.get("pase", 0) * 0.4)

    def get_valor_defensa(self):
        # Ejemplo de cálculo, puedes ajustarlo
        return (self.stats.get("defensa", 0) * 0.7) + (self.stats.get("velocidad", 0) * 0.3)