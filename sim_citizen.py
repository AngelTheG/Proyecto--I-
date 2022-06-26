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
            print("EVOLUCION DE LA ENFERMEDAD EN CASO DE PADECERLA")

    """ GETTERS """
    def get_id(self):
        return self.id_number

    def get_buddies(self):
        return self.buddies

    def get_status(self):
        return self.status

    def get_inmune(self):
        return self.inmune

