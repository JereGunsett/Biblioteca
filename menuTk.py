from random import randint 
from tkinter import *
from biblioteca import *


def menu(opc):
    
    biblioteca = Biblioteca()
    opcion = 0
    opcion = opc
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
            socio = biblioteca.buscar_socio(dni)
            biblioteca.baja_socio(socio)
            print("Socio dado de baja")
    if opcion == 3:
        titulo = input("Titulo: ")
        genero = input("Genero: ")
        anio = input("Anio: ")
        libro = Libros(titulo,genero,anio)
        if biblioteca.contiene_libro(libro.titulo):
            print("El libro ya existe")
        else:
            biblioteca.alta_nuevo_libro(libro)
            print("Libro agregado")
    if opcion == 4:
        dni = input("Titulo:")
        if not biblioteca.contiene_libro(dni):
            print("El libro no existe")
        else:
            biblioteca.baja_libro(socio)
            print("El libro ha sido dado de baja")
    if opcion == 5:
        titulo = input("Titulo: ")
        dni = input("DNI socio: ")
        if biblioteca.contiene_libro() and biblioteca.contiene_socio():
            biblioteca.alquilar_libro(titulo,dni)
        else:
            print("No se pudo alquilar el libro")
    if opcion == 6:
        titulo = input("Titulo: ")
        if not biblioteca.contiene_libro(titulo):
            print("El libro no existe")
        else:
            biblioteca.devolver_libro(titulo)
            print("El libro a sido devuelto")
    if opcion == 7:
        guardar_archivo(biblioteca)
    if opcion == 8:
        biblioteca = leer_archivo(biblioteca)
        print(biblioteca.__str__())
    if opcion == 9:
        return exit
        
    ejecutar()
    
def ejecutar():
    root = Tk(className='- Nuestra Biblioteca')
    root.geometry("400x215")
    v = IntVar()

    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))


    Radiobutton(root, text='(1) Dar de alta nuevo socio', variable=v, value=1,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(2) Dar de baja socio', variable=v, value=2,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(3) Dar de alta nuevo libro', variable=v, value=3,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(4) Dar de baja libro', variable=v, value=4,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(5) Alquilar libro', variable=v, value=5,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(6) Devolver libro', variable=v, value=6,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(7) Guardar archivo', variable=v, value=7,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(8) Leer archivo', variable=v, value=8,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(9) Salir', variable=v, value=9,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    root.config(bg=color)
    root.mainloop()
    menu(v.get())

root = Tk(className='- Nuestra Biblioteca')
root.geometry("400x215")
v = IntVar()

color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))


Radiobutton(root, text='(1) Dar de alta nuevo socio', variable=v, value=1,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(2) Dar de baja socio', variable=v, value=2,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(3) Dar de alta nuevo libro', variable=v, value=3,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(4) Dar de baja libro', variable=v, value=4,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(5) Alquilar libro', variable=v, value=5,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(6) Devolver libro', variable=v, value=6,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(7) Guardar archivo', variable=v, value=7,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(8) Leer archivo', variable=v, value=8,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(9) Salir', variable=v, value=9,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))

root.config(bg=color)

root.mainloop()

menu(v.get())