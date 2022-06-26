class Citizen():
    def __init__(self,id_number,
                      community,
                      disease):
        
        # Variables por definición
        self.id_number = id_number
        self.community = community
        self.disease = disease
        self.family = None
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
        if not self.inmune:
            self.infection_date = int(step)
            self.inmune = True
            self.status = True
    
    # Fun - Actualizar estado infeccioso del ciudadano
    def evolve(self):
        if self.status:
            print("EVOLUCION DE LA ENFERMEDAD EN CASO DE PADECERLA")

    """ GETTERS & SETTERS"""
    def get_id(self):
        return self.id_number

    def get_buddies(self):
        return self.buddies

