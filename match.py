
# clitest/match.py
import random
from team import Team
from config import DURACION_PARTIDO

class Match:
    def __init__(self, equipo_local, equipo_visitante, score_label=None, event_text=None):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.minuto_actual = 0
        self.marcador = {equipo_local.nombre: 0, equipo_visitante.nombre: 0}
        self.log_eventos = []
        self.score_label = score_label
        self.event_text = event_text

    def _update_gui(self, event_message=None):
        if self.score_label:
            self.score_label.config(text=f"{self.equipo_local.nombre} {self.marcador[self.equipo_local.nombre]} - {self.marcador[self.equipo_visitante.nombre]} {self.equipo_visitante.nombre}")
        if self.event_text and event_message:
            self.event_text.insert("end", event_message + "\n")
            self.event_text.see("end") # Auto-scroll to the end


    def iniciar_partido(self):
        self.log_eventos.append("¡Comienza el partido!")
        self._update_gui("¡Comienza el partido!")

        for self.minuto_actual in range(1, DURACION_PARTIDO + 1):
            # Lógica de eventos por minuto
            self.log_eventos.append(f"Minuto {self.minuto_actual}")
            self._update_gui(f"Minuto {self.minuto_actual}")
            # Simulación de eventos (muy básica por ahora)
            # Lógica de eventos
            if random.random() < 0.05: # Oportunidad de gol
                self._simular_oportunidad_gol()
            elif random.random() < 0.03: # Oportunidad de falta
                self._simular_falta()
            elif random.random() < 0.02: # Oportunidad de pase exitoso
                self._simular_pase_exitoso()
            elif random.random() < 0.01: # Oportunidad de regate exitoso
                self._simular_regate_exitoso()

        self.log_eventos.append("Tiempo reglamentario cumplido.")
        self._update_gui("Tiempo reglamentario cumplido.")

    def _simular_oportunidad_gol(self):
        equipo_atacante = random.choice([self.equipo_local, self.equipo_visitante])
        equipo_defensor = self.equipo_visitante if equipo_atacante == self.equipo_local else self.equipo_local

        atacante = equipo_atacante.get_mejor_atacante()
        portero_defensor = equipo_defensor.get_portero()

        probabilidad_gol = (atacante.get_valor_ataque() - portero_defensor.stats.get("parada", 50)) / 100.0
        probabilidad_gol = max(0.01, min(0.99, probabilidad_gol))

        if random.random() < probabilidad_gol:
            self.marcador[equipo_atacante.nombre] += 1
            evento = f"Minuto {self.minuto_actual}: ¡GOL de {equipo_atacante.nombre} (anotado por {atacante.get_descripcion_corta()})! Marcador: {self.equipo_local.nombre} {self.marcador[self.equipo_local.nombre]} - {self.marcador[self.equipo_visitante.nombre]} {self.equipo_visitante.nombre}"
            self.log_eventos.append(evento)
            self._update_gui(evento)
        else:
            evento = f"Minuto {self.minuto_actual}: Ocasión fallida de {equipo_atacante.nombre}. El portero {portero_defensor.get_descripcion_corta()} detuvo el disparo de {atacante.get_descripcion_corta()}."
            self.log_eventos.append(evento)
            self._update_gui(evento)

    def _simular_falta(self):
        equipo_infractor = random.choice([self.equipo_local, self.equipo_visitante])
        jugador_infractor = equipo_infractor.get_jugador_aleatorio()
        evento = f"Minuto {self.minuto_actual}: Falta de {jugador_infractor.get_descripcion_corta()} ({equipo_infractor.nombre})."
        self.log_eventos.append(evento)
        self._update_gui(evento)

    def _simular_pase_exitoso(self):
        equipo_pasador = random.choice([self.equipo_local, self.equipo_visitante])
        jugador_pasador = equipo_pasador.get_jugador_aleatorio()
        evento = f"Minuto {self.minuto_actual}: Pase exitoso de {jugador_pasador.get_descripcion_corta()} ({equipo_pasador.nombre})."
        self.log_eventos.append(evento)
        self._update_gui(evento)

    def _simular_regate_exitoso(self):
        equipo_regateador = random.choice([self.equipo_local, self.equipo_visitante])
        jugador_regateador = equipo_regateador.get_jugador_aleatorio()
        evento = f"Minuto {self.minuto_actual}: Regate exitoso de {jugador_regateador.get_descripcion_corta()} ({equipo_regateador.nombre})."
        self.log_eventos.append(evento)
        self._update_gui(evento)

    def finalizar_partido(self):
        resultado = f"Final del partido: {self.equipo_local.nombre} {self.marcador[self.equipo_local.nombre]} - {self.marcador[self.equipo_visitante.nombre]} {self.equipo_visitante.nombre}"
        self.log_eventos.append(resultado)
        self._update_gui(resultado)

        self._update_gui(f"\n--- Resumen del Partido ---")
        self._update_gui(f"Marcador Final: {self.equipo_local.nombre} {self.marcador[self.equipo_local.nombre]} - {self.marcador[self.equipo_visitante.nombre]} {self.equipo_visitante.nombre}")

        posesion_local = self.equipo_local.get_posesion_simulada()
        posesion_visitante = 100 - posesion_local # Asumimos que la suma es 100
        self._update_gui(f"Posesión: {self.equipo_local.nombre} {posesion_local}% - {self.equipo_visitante.nombre} {posesion_visitante}%")

        self._update_gui("\nJugadores del Partido:")
        self._update_gui(f"{self.equipo_local.nombre}: {', '.join(self.equipo_local.get_nombres_jugadores())}")
        self._update_gui(f"{self.equipo_visitante.nombre}: {', '.join(self.equipo_visitante.get_nombres_jugadores())}")

        self._update_gui("\nEventos del Partido:")
        for evento in self.log_eventos:
            self._update_gui(evento)

    def __str__(self):
        return f"Partido entre {self.equipo_local} y {self.equipo_visitante}"
