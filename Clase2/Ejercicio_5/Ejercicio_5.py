from persona import Persona

def main():
    print("Hola mundo")

    p1 = Persona("Ernesto",34)
    p2 = Persona("Lucas",18)
    p3 = Persona("Juan",20)

    personas = []

    personas.append(p1)
    personas.append(p2)
    personas.append(p3)

    Persona.print_personas(personas)

main()