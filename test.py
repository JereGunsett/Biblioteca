from videoclub import *

videoclub = Videoclub()
socio = Socio(30331261,"Matias",4804828,"Av Siempreviva 1234")
videoclub.alta_nuevo_socio(socio)
#print(videoclub.contiene_socio(30331261))

#print(videoclub.buscar_socio(30331261))

videoclub.baja_socio(30331261)
#print(videoclub.contiene_socio(30331261))

peli = Pelicula("Jumanji","Comedia",1995)
videoclub.alta_nueva_pelicula(peli)
#print(videoclub.contiene_pelicula("Jumanji"))
#print(videoclub.buscar_pelicula("Jumanji"))
#videoclub.baja_pelicula("Jumanji")
#print(videoclub.contiene_pelicula("Jumanji"))
videoclub.alquilar_pelicula("Jumanji",30331261)
#print(videoclub.buscar_pelicula("Jumanji"))

#print(socio == socio)
socio2 = Socio(40331261,"Natanael",3515645489,"Nueva cordoba")
print(socio == socio2)
print(socio < socio2)
print(socio <= socio2)
print(socio != socio2)
print(socio > socio2)
print(socio >= socio2)