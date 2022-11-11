from biblioteca import *

biblioteca = Biblioteca()
socio = Socio(30331261,"Matias","Botero",4804828)
biblioteca.alta_nuevo_socio(socio)
print(biblioteca.contiene_socio(30331261))

print(biblioteca.buscar_socio(30331261))

biblioteca.baja_socio(30331261)

if biblioteca.contiene_socio(30331261) == False:
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

