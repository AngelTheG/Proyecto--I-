"""
Esta es la clase "main" del simulador, o sea la encargada de administrar los datos
recolectados en la interfaz e ingresarlos en el simulador

"""
from sim_disease import Disease
from sim_community import Community
from sim_core import Simulation

class simulatorStarter():
    def __init__(self, data, steps,gui):

        # GUI - Actualizar estado en ventana
        subtitle = data[0].get_text() + " - Generando Población"
        gui.header.set_subtitle(subtitle)

        """Creación de la enferemedad"""
        obj_disease = Disease(probInfection=int(data[5].get_text()),
                                    stepsEvolution=int(data[6].get_text()))


        """Creación de la comunidad"""
        obj_community = Community(name=data[0].get_text(),
                                  population=int(data[1].get_text()),
                                  promContact=int(data[2].get_text()),
                                  probContact=int(data[3].get_text()),
                                  initialInfected=int(data[4].get_text()),
                                  disease=obj_disease,
                                  gui=gui)
        
        """Creación de la simulación"""
        self.simulator = Simulation(community=obj_community)

        self.simulator.run(steps)

        # GUI - Actualizar estado en ventana
        subtitle = data[0].get_text() + " - Mostrando resultados"
        gui.header.set_subtitle(subtitle)

    def get_log(self):
        return self.simulator.get_log()
