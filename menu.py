from biblioteca import *


def menu():
    opcion = 0
    while opcion < 1 or opcion > 9:
        print("--")
        print("(1) Dar de alta nuevo socio")
        print("(2) Dar de baja socio")
        print("(3) Dar de alta nuevo libro")
        print("(4) Dar de baja libro")
        print("(5) Alquilar libro")
        print("(6) Devolver libro")
        print("(7) Guardar archivo")
        print("(8) Leer archivo")
        print("(9) Salir")
        # consultar pelicula - me devuelve la informacion de la pelicula
        print("--")
        try:
          opcion = int(input("Elija una opcion: "))
        except:
            opcion = 0
            print('Elija un numero del 1 al 9')
        print("--")
    return opcion


if __name__ == "__main__":
    biblioteca = Biblioteca()
    opcion = 0
    while opcion != 9:
        opcion = menu()
        if opcion == 1:
            nombre = input("Nombre: ")
            dni = input("Dni: ")
            telefono = input("Telefono: ")
            dire = input("Dirección: ")
            socio = Socio(dni,nombre,telefono,dire)
            if biblioteca.contiene_socio(socio.dni):
                print("El socio ya existe")
            else:
                biblioteca.alta_nuevo_socio(socio)
                print("Socio Agregado")
        if opcion == 2:
            dni = input("Dni:")
            if not biblioteca.contiene_socio(dni):
                print("El socio no existe")
            else:
                biblioteca.baja_socio(dni)
                print("Socio dado de baja")
        if opcion == 3:
            titulo = input("Titulo: ")
            genero = input("Genero: ")
            anio = input("Anio: ")
            libro = Libros(titulo,genero,anio)
            if biblioteca.contiene_libro(libro.title):
                print("El libro ya existe")
            else:
                biblioteca.alta_nuevo_libro(libro)
                print("Libro agregado")
        if opcion == 4:
            titulo = input("Titulo:")
            if not biblioteca.contiene_libro(titulo):
                print("El libro no existe")
            else:
                biblioteca.baja_libro(titulo)
                print("El libro ha sido dado de baja")
        if opcion == 5:
            titulo = input("Titulo: ")
            dni = input("DNI socio: ")
            if biblioteca.contiene_libro(titulo) and biblioteca.contiene_socio(dni):
                biblioteca.alquilar_libro(titulo,dni)
            else:
                print("No se pudo alquilar el libro")
        if opcion == 6:
            titulo = input("Titulo: ")
            if not biblioteca.contiene_libro(titulo):
                print("El libro no existe")
            else:
                biblioteca.devolver_libro(titulo)
                
        if opcion == 7:
            guardar_archivo(biblioteca)
        if opcion == 8:
            biblioteca = leer_archivo(biblioteca)
            print(biblioteca.__str__())
        #print("Socios: ", biblioteca.socios.magnitud())
        #print("Libros: ", biblioteca.libros.magnitud())


