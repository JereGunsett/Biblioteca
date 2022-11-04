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
    
