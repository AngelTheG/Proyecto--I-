"""
Este es el entorno del simulador, aquí se llevan a cabo todos los los
procesos relacionados con la simulación, carga de datos y generación
de resultados

"""

class Simulation():
    def __init__(self, community):
        self.community = community
    
    def run(self,steps):
        for i in range(int(steps)):
            self.community.take_step()
