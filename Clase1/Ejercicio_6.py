# Escribir una funcion que reciba una lista de tuplas, por ejemplo:
# [('Geroge','4312 Abbey Road', 22),('John','54 Love Ave', 21)]
# Una tupla se escribe con ()
import csv

Data = [('Name','Address','Age'),('Geroge','4312 Abbey Road', 22),('John','54 Love Ave', 21)]

myFile = open('Ejercicio6.csv','w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(Data)

print('completado')


