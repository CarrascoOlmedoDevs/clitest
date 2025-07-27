import random

# clitest/config.py
POSICIONES = {
    "PO": "Portero",
    "DEF": "Defensa",
    "MED": "Mediocentro",
    "DEL": "Delantero"
}

DURACION_PARTIDO = 90

NOMBRES_JUGADORES = [
    "Juan", "Pedro", "Luis", "Carlos", "Miguel", "José", "Antonio", "Manuel",
    "David", "Javier", "Fernando", "Ricardo", "Sergio", "Pablo", "Diego", "Alejandro",
    "Francisco", "Daniel", "Jorge", "Roberto", "Andrés", "Gonzalo", "Alberto", "Raúl",
    "Rubén", "Iván", "Adrián", "Óscar", "Ramón", "Enrique", "Arturo", "Emilio",
    "Guillermo", "Ignacio", "Marcos", "Mario", "Álvaro", "Gabriel", "Héctor", "Julio"
]

APELLIDOS_JUGADORES = [
    "García", "Rodríguez", "Fernández", "González", "López", "Martínez", "Sánchez",
    "Pérez", "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno",
    "Muñoz", "Álvarez", "Romero", "Alonso", "Torres", "Rubio", "Serrano", "Reyes",
    "Ortiz", "Morales", "Molina", "Delgado", "Castro", "Navarro", "Vázquez", "Ramos",
    "Blanco", "Suárez", "Ortega", "Cruz", "Díez", "Cano", "Prieto", "Gil", "Vidal"
]

def generar_nombre_jugador():
    nombre = random.choice(NOMBRES_JUGADORES)
    apellido = random.choice(APELLIDOS_JUGADORES)
    return f"{nombre} {apellido}"

NOMBRES_JUGADORES = [
    "Juan", "Pedro", "Luis", "Carlos", "Miguel", "José", "Antonio", "Manuel",
    "David", "Javier", "Fernando", "Ricardo", "Sergio", "Pablo", "Diego", "Alejandro",
    "Francisco", "Daniel", "Jorge", "Roberto", "Andrés", "Gonzalo", "Alberto", "Raúl",
    "Rubén", "Iván", "Adrián", "Óscar", "Ramón", "Enrique", "Arturo", "Emilio",
    "Guillermo", "Ignacio", "Marcos", "Mario", "Álvaro", "Gabriel", "Héctor", "Julio"
]

APELLIDOS_JUGADORES = [
    "García", "Rodríguez", "Fernández", "González", "López", "Martínez", "Sánchez",
    "Pérez", "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno",
    "Muñoz", "Álvarez", "Romero", "Alonso", "Torres", "Rubio", "Serrano", "Reyes",
    "Ortiz", "Morales", "Molina", "Delgado", "Castro", "Navarro", "Vázquez", "Ramos",
    "Blanco", "Suárez", "Ortega", "Cruz", "Díez", "Cano", "Prieto", "Gil", "Vidal"
]

def generar_nombre_jugador():
    nombre = random.choice(NOMBRES_JUGADORES)
    apellido = random.choice(APELLIDOS_JUGADORES)
    return f"{nombre} {apellido}"