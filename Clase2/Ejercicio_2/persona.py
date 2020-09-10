class Persona:

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