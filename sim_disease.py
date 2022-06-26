"""
Esta es el objeto enfermedad, más que nada un contenedor de atributos

"""

class Disease():
    def __init__(self, probInfection,
                       stepsEvolution):
        
        self.probInfection = probInfection
        self.stepsEvolution = stepsEvolution