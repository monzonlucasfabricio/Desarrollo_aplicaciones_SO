from sensores import Sensortemperatura,Sensorhumedad

s = Sensortemperatura(0)
h = Sensorhumedad(0)

##valor = s.read_file("/tmp/temp0.data") MAL
valor = s.get_value()
print("lei valor de temperatura:"+str(valor))

valor = h.get_value()
print("lei valor de humedad:"+str(valor))



