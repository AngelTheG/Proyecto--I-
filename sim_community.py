"""
Este es el objeto comunidad, aquí se realiza la creación de la
población, incluyendo los grupos cercanos de cada uno de los 
habitantes de la comunidad

"""

from random import choice
from sim_citizen import Citizen

class Community():
    def __init__(self, name,
                       population,
                       promContact,
                       probContact,
                       initialInfected,
                       disease,
                       gui):

        # Variables por Definición 
        self.name = name
        self.population = population
        self.promContact = promContact
        self.probContact = probContact
        self.initialInfected = initialInfected
        self.disease = disease
        self.gui = gui

        # Variables por Asignación
        self.citizens = []
        self.step = 0
        self.log = []

        # GUI - Actualizar estado en ventana
        subtitle = self.name + " - Generando Población"
        self.gui.header.set_subtitle(subtitle)

        # Generar Población
        for id_number in range(self.population):
            self.citizens.append(Citizen(id_number=id_number,
                                         community=self,
                                         disease =self.disease))

        # GUI - Actualizar estado en ventana
        subtitle = self.name + " - Creando Círculos Cercanos"
        self.gui.header.set_subtitle(subtitle)

        # Generar conexiónes cercanas (Círculo de conocidos o amigos)
        for citizen in self.citizens:
            
            circleIsNotCreated = True
            i = 0
            while circleIsNotCreated:               
                if citizen.enough_buddies():
                    circleIsNotCreated = False
                    
                
                possibleBuddy = choice(self.citizens)
                
                if not possibleBuddy.enough_buddies():
                    if not possibleBuddy in citizen.get_buddies():
                        
                        if possibleBuddy.get_id() != citizen.get_id():
                            citizen.add_buddy(possibleBuddy)
                            possibleBuddy.add_buddy(citizen)
                if i == self.promContact:
                    break
                
        # TEMP - Imprimir lista de amigos por consola
        for citizen in self.citizens:
            print("El ciudadano ",citizen.get_id()," tiene como amigos a: [", end="")
            for buddy in citizen.get_buddies():
                print(" ",buddy.get_id()," ",end="")
            print("]")
        
        ###

        # GUI - Actualizar estado en ventana
        subtitle = self.name + " - Infectando a la comunidad"
        self.gui.header.set_subtitle(subtitle)
        
        # Infección inicial
        for i in range(self.initialInfected):

            while True:
                patient0 = choice(self.citizens)
                if not patient0.get_status():
                    patient0.infect(step=0)
                    break
        
        # GUI - Actualizar estado en ventana
        subtitle = self.name + " - Creada correctamente"
        self.gui.header.set_subtitle(subtitle)

    # FUN - Dar un paso (Actualizar simulación)
    def take_step(self):
        
        self.step += 1
        active_cases = 0
        healed_cases = 0
        dead_cases = 0

        # GUI - Actualizar estado en ventana
        subtitle = self.name+" - Simulando paso ["+str(self.step)+"]"
        self.gui.header.set_subtitle(subtitle)

        for citizen in self.citizens:
            if citizen.get_status():
                citizen.infect_buddies()
                for i in range(self.promContact):
                    contact = choice(self.citizens)
                    contact.attempt_infect()
                citizen.evolve()

        # Actualizacion de registro de datos
        for citizen in self.citizens:
            if citizen.get_status():
                active_cases += 1
            else:
                if citizen.get_inmune():
                    if citizen.is_alive():
                        healed_cases += 1
                    else:
                        dead_cases += 1
                
            

        log_step = [self.step,
                    active_cases,
                    self.disease.get_cases(),
                    dead_cases,
                    healed_cases]

        self.log.append(log_step)

    """ GETTERS """
    def get_name(self):
        return self.name

    def get_promContact(self):
        return self.promContact

    def get_step(self):
        return self.step

    def get_log(self):
        return self.log
