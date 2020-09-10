class Sensor:
    def __init__(self,id):
        self.id = id
    def read_file(self,file_name):
        with open(file_name,"r") as f:
            return float(f.read())
    def get_value(self):
        return 0

class Sensortemperatura(Sensor):

    def __init__(self,id):
        super().__init__(id)

    def get_value(self):
        #construir el path al sensor segun mi numero de sensor
        #llamar a read file
        #ajuste del valor leido
        path = "/tmp/temp{}.data".format(self.id)
        valor = self.read_file(path)
        if valor < 0:
            valor = 0.0
        return valor

class Sensorhumedad(Sensor):
    
    def __init__(self,id):
        super().__init__(id)

    def get_value(self):
        #construir el path al sensor segun mi numero de sensor
        #llamar a read file
        #ajuste del valor leido
        path = "/tmp/hum{}.data".format(self.id)
        valor = self.read_file(path)
        return valor/10.0