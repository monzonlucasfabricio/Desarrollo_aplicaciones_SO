# Escriba una funcion que reciba un string y reemplace los espacios por un caracter que reciba por argumento.
# La funcion debera devolver el nuevo string

def recibir_string(c):
    a = input()
    b = a.replace(" ", c)
    return b

c = recibir_string("8")
print(c)

        