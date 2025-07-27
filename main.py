
# clitest/main.py
from player import Player
from team import Team
from match import Match

import tkinter as tk
from tkinter import scrolledtext
from player import Player
from team import Team
from match import Match

def run_simulation():
    # Crear equipos de ejemplo usando la función de generación aleatoria
    equipo_a = Team.generar_equipo_aleatorio("Equipo A")
    equipo_b = Team.generar_equipo_aleatorio("Equipo B")

    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    root.title("Simulador de Fútbol 11 vs 11")

    # Etiqueta para el marcador
    score_label = tk.Label(root, text=f"{equipo_a.nombre} 0 - 0 {equipo_b.nombre}", font=("Arial", 24))
    score_label.pack(pady=10)

    # Área de texto para el log de eventos
    event_text = scrolledtext.ScrolledText(root, width=80, height=20, font=("Arial", 10))
    event_text.pack(padx=10, pady=10)

    # Crear y simular un partido, pasando las referencias de los widgets
    partido = Match(equipo_a, equipo_b, score_label=score_label, event_text=event_text)

    # Ejecutar la simulación en un hilo separado o con after para no bloquear la GUI
    # Para simplificar, lo ejecutaremos directamente y luego iniciaremos el bucle de Tkinter
    # En una aplicación real, esto se haría con root.after() o un hilo.
    partido.iniciar_partido()
    partido.finalizar_partido()

    root.mainloop()

if __name__ == "__main__":
    run_simulation()
