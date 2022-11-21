from biblioteca import *

biblioteca = Biblioteca()
socio = Socio(39445690,"Jeremias","Gunsett",3516278454)
biblioteca.alta_nuevo_socio(socio)
print(biblioteca.contiene_socio(39445690))

print(biblioteca.buscar_socio(39445690))
socio1 = biblioteca.buscar_socio(39445690)
print(socio1.__str__())

biblioteca.baja_socio(39445690)

if biblioteca.contiene_socio(39445690) == False:
    print ("El socio no se encuentra registrado") 
#print(biblioteca.contiene_socio(30331261))


socio2 = Socio(40331261,"Natanael","Perez",3515645489)
biblioteca.alta_nuevo_socio(socio2)

print(biblioteca.contiene_socio(40331261))
print(biblioteca.buscar_socio(40331261))

libro = Libros("El señor de las moscas", "Novela", "William Golding")
biblioteca.alta_nuevo_libro(libro)
print(biblioteca.buscar_libro("El señor de las moscas"))
print(biblioteca.contiene_libro("El señor de las moscas"))

libro = Libros("Las Cuevas", "Terror", "German Lopez")
libro = Libros("Risas y mas risas", "Comedia", "Marcos Rati")
libro = Libros("Aprende a decir NO", "Autoayuda", "William Golding")
libro = Libros("Padre Rico, Padre Pobre", "Economia", "Esteban Duran")
libro = Libros("El rey del Sur", "Novela", "Drake")
libro = Libros("Camino a la estabilidad emocional", "Autoayuda", "Gunsett Jeremias")

for i in range(10):
    nombre = i
    dni = int(str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)))
    telefono = i
    dire = i
    socio = Socio(dni,nombre,telefono,dire)
    if biblioteca.contiene_socio(socio.dni):
        print("El socio ya existe")
    else:
        biblioteca.alta_nuevo_socio(socio)
        print("Socio Agregado")
print(biblioteca.__str__())
print('`'*12)
biblioteca.ordenada()
print(biblioteca.__str__())


