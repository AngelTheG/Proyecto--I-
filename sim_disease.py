"""
Esta es el objeto enfermedad, más que nada un contenedor de atributos

"""

class Disease():
    def __init__(self, probInfection,
                       stepsEvolution):
        
        self.probInfection = probInfection
        self.stepsEvolution = stepsEvolution

        self.cases = 0

    # Fun - Añadir caso
    def add_infection(self):
        self.cases += 1

    """ GETTERS """
    def get_prob(self):
        return self.probInfection
    
    def get_stepsEvolution(self):
        return self.stepsEvolution

    def get_cases(self):
        return self.cases