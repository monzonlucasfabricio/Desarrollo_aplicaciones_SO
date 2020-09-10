from persona import Persona

p = Persona()
p1 = Persona()

p.set_edad(45)
p1.set_edad(50)

p.set_nombre("Lucas")
p1.set_nombre("Juan")

##print("{} {}".format(p.get_nombre(),p.get_edad()))

p.print_persona();
p1.print_persona();
