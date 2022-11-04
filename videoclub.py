import pickle #libreria para guardar y recuperar informacion
from listas import *

class Socio():
    def __init__(self,dni,nombre,telefono,domicilio):
        self.dni =dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio
        
    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.dni<other.dni
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.dni<=other.dni
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.dni==other.dni
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.dni!=other.dni
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.dni>other.dni
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.dni>=other.dni

    def __str__(self):
        return "DNI: {0}\nNombre: {1}\nTelefono: {2}\nDomicilio: {3}\n" \
            .format(self.dni,self.nombre,self.telefono,self.domicilio)

class Videoclub:
    def __init__(self):
        self.socios = []
        self.peliculas = []
    def contiene_socio(self,dni)->bool:
        esta = False
        for socio in self.socios:
            if socio.dni == dni:
                esta = True
        return esta
    def buscar_socio(self,dni)->bool:
        devolver = None
        for socio in self.socios:
            if socio.dni == dni:
                devolver = socio
        return devolver
    def alta_nuevo_socio(self,socio):
        self.socios.append(socio)
        
    def baja_socio(self,dni):
        socio = self.buscar_socio(dni)
        self.socios.remove(socio)
        #indice_socio = self.socios.index(socio)
        #self.socios.pop(indice_socio)
    
    def contiene_pelicula(self,titulo):
        esta = False
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                esta = True
        return esta
    def buscar_pelicula(self,titulo)->"Pelicula":
        esta = False
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                devolver = pelicula
        return devolver
    def alta_nueva_pelicula(self,pelicula)->None:
        self.peliculas.append(pelicula)
        
    def baja_pelicula(self,titulo)->None:
        pelicula = self.buscar_pelicula(titulo)
        self.peliculas.remove(pelicula)
        
    def alquilar_pelicula(self,titulo,dni):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada == None:
                pelicula.alquilada = dni
                
    def devolver_pelicula(self,titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada != None:
                pelicula.alquilada = None
         
def guardar_archivo(videoclub,archivo="video.pickle"):
    pickle_file = open(archivo, 'wb')
    pickle.dump(videoclub, pickle_file)
    pickle_file.close()

def leer_archivo(videoclub,archivo="video.pickle"):
    pickle_file = open(archivo,'rb')
    videoclub = pickle.load(pickle_file)
    pickle_file.close()
    return videoclub
    
def menu():
    opcion = 0
    while opcion < 1 or opcion > 9:
        print("--")
        print("(1) Dar de alta nuevo socio")
        print("(2) Dar de baja socio")
        print("(3) Dar de alta nueva pelicula")
        print("(4) Dar de baja pelicula")
        print("(5) Alquilar película")
        print("(6) Devolver película")
        print("(7) Guardar archivo")
        print("(8) Leer archivo")
        print("(9) Salir")
        # consultar pelicula - me devuelve la informacion de la pelicula
        print("--")
        opcion = int(input("Elija una opcion: "))
        print("--")
    return opcion


if __name__ == "__main__":
    videoclub = Videoclub()
    opcion = 0
    while opcion != 9:
        opcion = menu()
        if opcion == 1:
            nombre = input("Nombre: ")
            dni = input("Dni: ")
            telefono = input("Telefono: ")
            dire = input("Dirección: ")
            socio = Socio(dni,nombre,telefono,dire)
            if videoclub.contiene_socio(socio.dni):
                print("El socio ya existe")
            else:
                videoclub.alta_nuevo_socio(socio)
                print("Socio Agregado")
        if opcion == 2:
            dni = input("Dni:")
            if videoclub.contiene_socio(dni):
                print("El socio no existe")
            else:
                videoclub.baja_socio(socio)
                print("Socio dado de baja")
        if opcion == 3:
            titulo = input("Titulo: ")
            genero = input("Genero: ")
            anio = input("Anio: ")
            peli = Pelicula(titulo,genero,anio)
            if videoclub.contiene_pelicula(peli.titulo):
                print("La peli ya existe")
            else:
                videoclub.alta_nueva_pelicula(peli)
                print("Pelicula agregada")
        if opcion == 4:
            dni = input("Titulo:")
            if videoclub.contiene_pelicula(dni):
                print("La pelicula no existe")
            else:
                videoclub.baja_pelicula(socio)
                print("Pelicula ha sido dada de baja")
        if opcion == 5:
            titulo = input("Titulo: ")
            dni = input("DNI socio: ")
            if videoclub.contiene_pelicula() and videoclub.contiene_socio():
                videoclub.alquilar_pelicula(titulo,dni)
            else:
                print("No se pudo alquilar la pelicula")
        if opcion == 6:
            titulo = input("Titulo: ")
            if not videoclub.contiene_pelicula(titulo):
                print("La pelicula no existe")
            else:
                videoclub.devolver_pelicula(titulo)
                print("Pelicula ha sido devuelta")
        if opcion == 7:
            guardar_archivo(videoclub)
        if opcion == 8:
            videoclub = leer_archivo(videoclub)
        print("Socios: ", len(videoclub.socios))
        print("Peliculas: ", len(videoclub.peliculas))

