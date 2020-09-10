from persona import Persona

def main():
    p1 = Persona("Ernesto",34)
    p2 = Persona("Lucas",18)
    p3 = Persona("Juan",20)

    personas = []

    personas.append(p1)
    personas.append(p2)
    personas.append(p3)

    Persona.dump_csv("personas.csv",personas)

main()