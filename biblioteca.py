import pickle #libreria para guardar y recuperar informacion
from listas import *
from libros import *
from socios import *

class Biblioteca:
    def __init__(self):
        self.socios = Lista()
        self.libros = Lista()
        
    def contiene_socio(self,dni)->bool:
        esta = False
        i = self.socios.magnitud()
        for j in range(i):
            nodo = self.socios.devolver(j)
            if nodo.dni==dni:
                esta = True            
        return esta
    
    def buscar_socio(self,dni)->object:
        devolver = None
        i = self.socios.magnitud()
        for j in range(i):
            nodo = self.socios.devolver(j)
            if nodo.dni==dni:
                devolver = nodo            
        return devolver
    
    def alta_nuevo_socio(self,socio):
        self.socios.agregar(socio)
        
    def baja_socio(self,dni):
        
        socio = self.buscar_socio(dni)
        self.socios.remover(socio)
        #indice_socio = self.socios.index(socio)
        #self.socios.pop(indice_socio)
    
    def indice_socio(self,socio)->int:
        return self.socios.indice(socio)
    
    def contiene_libro(self,titulo):
        esta = False
        i = self.libros.magnitud()
        for j in range(i):
            nodo = self.libros.devolver(j)
            if nodo.title == titulo:
                esta = True            
        return esta
    
    def buscar_libro(self,titulo):
        devolver = None
        i = self.libros.magnitud()
        for j in range(i):
            nodo = self.libros.devolver(j)
            if nodo.title==titulo:
                devolver = nodo            
        return devolver
    
    def alta_nuevo_libro(self,libro)->None:
        self.libros.agregar(libro)
        
    def baja_libro(self,titulo)->None:
        libro = self.buscar_libro(titulo)
        self.libros.remover(libro)
        
    def alquilar_libro(self,titulo,dni):
        i = self.libros.magnitud()
        for j in range(i):
            libro = self.libros.devolver(j)
            if libro.title == titulo and libro.alquilado == None:
                libro.alquilado = dni
                
    def devolver_libro(self,titulo):
        i = self.libros.magnitud()
        for j in range(i):
            libro = self.libros.devolver(j)
            if libro.title == titulo and libro.alquilado != None:
                libro.alquilado = None
                print('El libro ha sido devuelto!')
            if libro.title == titulo and libro.alquilado == None:
                print('El libro no esta alquilado!')
            
    def __str__(self):
        impresion = 'Mi Biblioteca:\n'
        if self.libros.magnitud()==0:
            impresion += 'Lamentablemente no hay libros aqui !\n'
        else:
            impresion += '+'*10 + '\nLIBROS\n'+'+'*10+'\n'
        for i in range(self.libros.magnitud()):
          libro = self.libros.devolver(i)
          impresion += libro.__str__()
        
        if self.socios.magnitud()==0:
            impresion += 'Todavia no se inscribio ningun socio !\n'
        else:
            impresion += '+'*10 + '\nSOCIOS\n'+'+'*10+'\n'
        for i in range(self.socios.magnitud()):
          socio = self.socios.devolver(i)
          impresion += socio.__str__()
        return impresion
def guardar_archivo(biblioteca,archivo="libro.pickle"):
    pickle_file = open(archivo, 'wb')
    pickle.dump(biblioteca, pickle_file)
    pickle_file.close()

def leer_archivo(biblioteca,archivo="libro.pickle"):
    pickle_file = open(archivo,'rb')
    biblioteca = pickle.load(pickle_file)
    pickle_file.close()    
    return biblioteca
    
