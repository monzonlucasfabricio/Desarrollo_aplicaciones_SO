from persona import Persona

p = Persona("Lucas",45)
p1 = Persona("Juan",16)

p.print_persona();
p1.print_persona();

if(p.es_mayor_de_edad()):
    print("Es mayor de edad")
