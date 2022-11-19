from random import randint 
from tkinter import *
from biblioteca import *


def menu(opc):
    opcion = 0
    opcion = opc
    biblioteca = Biblioteca()
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
        biblioteca.ordenada()
        dni = input("DNI: ")
        socio = biblioteca.buscar_socio(dni)
        if socio != None:
            print(socio.__str__())
        else:
            print('El socio no existe')
    
    if opcion == 8:
        biblioteca.ordenada()
        titulo = input("Titulo: ")
        libro = biblioteca.buscar_libro(titulo)
        if libro != None:
            print(libro.__str__())
        else:
            print('El libro no existe')
            
    if opcion == 9:
        biblioteca.ordenada()
        guardar_archivo(biblioteca)
        print('Se ha guardado con exito!')
        
    if opcion == 10:
        biblioteca = leer_archivo(biblioteca)
        print(biblioteca.__str__())
    
    if opcion == 11:
        return exit          
        
    ejecutar()
    
def ejecutar():
    root = Tk(className='- Nuestra Biblioteca')
    root.geometry("400x251")
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
    Radiobutton(root, text='(7) Buscar socio', variable=v, value=7,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(8) Buscar libro', variable=v, value=8,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(9) Guardar archivo', variable=v, value=9,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(10) Leer archivo', variable=v, value=10,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    Radiobutton(root, text='(11) Salir', variable=v, value=11,bg=color,command=root.destroy).pack(anchor=W)
    color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    root.config(bg=color)
    root.mainloop()
    menu(v.get())

root = Tk(className='- Nuestra Biblioteca')
root.geometry("400x251")
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
Radiobutton(root, text='(7) Buscar socio', variable=v, value=7,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(8) Buscar libro', variable=v, value=8,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(9) Guardar archivo', variable=v, value=9,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(10) Leer archivo', variable=v, value=10,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
Radiobutton(root, text='(11) Salir', variable=v, value=11,bg=color,command=root.destroy).pack(anchor=W)
color = "#" + str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))

root.config(bg=color)

root.mainloop()

menu(v.get())