from biblioteca import *

biblioteca = Biblioteca()
socio = Socio(30331261,"Matias",4804828,"Av Siempreviva 1234")
biblioteca.alta_nuevo_socio(socio)
#print(biblioteca.contiene_socio(30331261))

#print(biblioteca.buscar_socio(30331261))

biblioteca.baja_socio(30331261)
#print(biblioteca.contiene_socio(30331261))

libro = Libros("Frankestein","Terror",1885)
biblioteca.alta_nuevo_libro(libro)
#print(biblioteca.contiene_libro("Frankestein"))
#print(biblioteca.buscar_libro("Frankestein"))
#biblioteca.baja_pelicula("Frankestein")
#print(videoclub.contiene_libro("Frankestein"))
biblioteca.alquilar_pelicula("Frankestein",30331261)
#print(biblioteca.buscar_libro("Frankestein"))

#print(socio == socio)
socio2 = Socio(40331261,"Natanael",3515645489,"Nueva cordoba")
print(socio == socio2)
print(socio < socio2)
print(socio <= socio2)
print(socio != socio2)
print(socio > socio2)
print(socio >= socio2)
