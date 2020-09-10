class Persona:
    MAYORIA_EDAD = 18

    def __init__(self,nombre,edad):
        self.set_nombre(nombre)
        self.set_edad(edad)

    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def set_edad(self,edad):
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad

    def print_persona(self):
        print("{},{}".format(self.__nombre,self.__edad))

    def es_mayor_de_edad(self):
        if self.get_edad() > Persona.MAYORIA_EDAD:
            return True 
        return False

    @staticmethod 
    def print_personas(personas):
        for p in personas:
            print(p.get_nombre()+",edad:"+str(p.get_edad()))


    @staticmethod
    def dump_csv(nombre_archivo,personas):
        line = "nombre,edad\n"
        print(line)
        for p in personas:
            line = p.get_nombre()+","+str(p.get_edad())+"\n"
            print(line)
