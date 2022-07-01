"""
Nuestro pobresillo ciudadano, compuesto de 6 funciones, las primeras 2
relacionadas con la creación de grupos cercanos y las otras 4 relacionadas con la infección
de grupos cercanos e infección como tal
"""

from random import randrange

class Citizen():
    def __init__(self,id_number,
                      community,
                      disease):
        
        # Variables por definición
        self.id_number = id_number
        self.community = community
        self.disease = disease
        self.status = False
        self.inmune = False
        self.infection_date = "Nunca fué infectado"
        self.isAlive = True

        # Variables por Asignación
        self.buddies = []

    # Fun - Añadir Amigo
    def add_buddy(self, buddy):
        self.buddies.append(buddy)

    # Fun - Comprobar espacio para amigos
    def enough_buddies(self):
        if len(self.buddies) < self.community.get_promContact():
            return False
        else:
            return True

    # Fun - Infectar
    def infect(self,step):
        self.infection_date = step
        self.inmune = True
        self.status = True
        self.disease.add_infection()
        print("Ciudadano [",self.id_number,"] infectado en el paso: ",self.infection_date)
    
    # FUN - Intentar infeccion
    def attempt_infect(self):
        attempt_randnumber = randrange(100)
        if not self.inmune:
            if attempt_randnumber < self.disease.get_prob():
                self.infect(self.community.get_step())

    # Fun - Infectar grupo cercano
    def infect_buddies(self):
        for buddy in self.buddies:
            buddy.attempt_infect()

    # Fun - Actualizar estado infeccioso del ciudadano
    def evolve(self):
        if self.status:
            if self.community.get_step()-self.infection_date >= self.disease.get_stepsEvolution():
                attempt_randnumber = randrange(100)
                self.status = False
                if attempt_randnumber < 50:
                    self.isAlive = False

    """ GETTERS """
    def get_id(self):
        return self.id_number

    def get_buddies(self):
        return self.buddies

    def get_status(self):
        return self.status

    def get_inmune(self):
        return self.inmune

    def is_alive(self):
        return self.isAlive
