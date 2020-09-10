# recibir algo por teclado
import csv
import serial


encabezado = ('Nombre','Edad')
lista = []
lista.append(encabezado)

for i in range(0,5):
    nombre = input()
    edad = input()
    lista.append([nombre,edad])

myFile = open('Scripderecepcion.csv','w')
with myFile:
    write = csv.writer(myFile)
    write.writerows(lista)

print('completado')
print(lista)




