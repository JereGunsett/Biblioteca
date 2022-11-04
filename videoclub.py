import pickle #libreria para guardar y recuperar informacion
from listas import *
from libros import *
from socios import *

class Biblioteca:
    def __init__(self):
        self.socios = []
        self.libros = []
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
    
    def contiene_libro(self,titulo):
        esta = False
        for libro in self.libros:
            if libro.titulo == titulo:
                esta = True
        return esta
    def buscar_libro(self,titulo):
        esta = False
        for libro in self.libros:
            if libro.titulo == titulo:
                devolver = libro
        return devolver
    def alta_nuevo_libro(self,libro)->None:
        self.libros.append(libro)
        
    def baja_libro(self,titulo)->None:
        libro = self.buscar_libro(titulo)
        self.libros.remove(libro)
        
    def alquilar_libro(self,titulo,dni):
        for libro in self.libros:
            if libro.titulo == titulo and libro.alquilada == None:
                libro.alquilada = dni
                
    def devolver_libro(self,titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.alquilada != None:
                libro.alquilada = None
         
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
            autor = input("Autor: ")
            libro = Libros(titulo,genero,autor)
            if videoclub.contiene_libro(libro.titulo):
                print("El libro ya existe")
            else:
                videoclub.alta_nueva_pelicula(libro)
                print("Libro agregado")
        if opcion == 4:
            dni = input("Titulo:")
            if videoclub.contiene_pelicula(dni):
                print("El libro no existe")
            else:
                videoclub.baja_pelicula(socio)
                print("El libro ha sido dado de baja")
        if opcion == 5:
            titulo = input("Titulo: ")
            dni = input("DNI socio: ")
            if videoclub.contiene_pelicula() and videoclub.contiene_socio():
                videoclub.alquilar_pelicula(titulo,dni)
            else:
                print("No se pudo alquilar el libro")
        if opcion == 6:
            titulo = input("Titulo: ")
            if not videoclub.contiene_pelicula(titulo):
                print("El Libro no existe")
            else:
                videoclub.devolver_pelicula(titulo)
                print("El Libro ha sido devuelto")
        if opcion == 7:
            guardar_archivo(videoclub)
        if opcion == 8:
            videoclub = leer_archivo(videoclub)
        print("Socios: ", len(videoclub.socios))
        print("Peliculas: ", len(videoclub.peliculas))

