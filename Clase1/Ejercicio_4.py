# Escribir una funcion "es_par" la cual recibe un numero entero y devuelve un True si el numero es par o False
# si es impar

def es_par(a):
    if a % 2 == 0:
        return True
    else:
        return False


print(es_par(2))
print(es_par(3))
