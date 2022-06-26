"""
Este es el objeto comunidad, aquí se realiza la creación de la
población, incluyendo los grupos cercanos de cada uno de los 
habitantes de la comunidad

TO DO:
- FUN - Intentar Infección
- FUN - Intentar Infección(Grupos Cercanos)

"""

from random import randrange, choice
from sim_citizen import Citizen

class Community():
    def __init__(self, name,
                       population,
                       promContact,
                       probContact,
                       initialInfected,
                       disease):

        # Variables por Definición 
        self.name = name
        self.population = population
        self.promContact = promContact
        self.probContact = probContact
        self.initialInfected = initialInfected
        self.disease = disease
        self.citizens = []

        # Generar Población
        for id_number in range(self.population):
            self.citizens.append(Citizen(id_number=id_number,
                                         community=self,
                                         disease =self.disease))

        # Generar conexiónes cercanas (Círculo de conocidos o amigos)
        for citizen in self.citizens:
            
            circleIsNotCreated = True

            while circleIsNotCreated:               
                if citizen.enough_buddies():
                    circleIsNotCreated = False
                    
                
                possibleBuddy = choice(self.citizens)
                
                if not possibleBuddy.enough_buddies():
                    if not possibleBuddy in citizen.get_buddies():
                        
                        if possibleBuddy.get_id() != citizen.get_id():
                            citizen.add_buddy(possibleBuddy)
                            possibleBuddy.add_buddy(citizen)
            

        # DEBUG - Imprimir lista de amigos por consola
        for citizen in self.citizens:
            print("El ciudadano ",citizen.get_id()," tiene como amigos a: [", end="")
            for buddy in citizen.get_buddies():
                print(" ",buddy.get_id()," ",end="")
            print("]")
                    

    # Fun - Obtener Nombre
    def get_name(self):
        return self.name

    """ GETTERS & SETTERS """
    def get_promContact(self):
        return self.promContact