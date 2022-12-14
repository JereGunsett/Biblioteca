class Nodo:
    """Tiene un dato y una referencia al siguiente nodo"""
    dato = None #no tiene informacion
    siguiente = None # no apunta a apunta a nada

    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

class Lista():
    primero = None # Nulo lista vacia
    ultimo = None
    tamanio = 0

    def vacia(self)->bool: # devuelva si la lista esta vacia
        return self.primero == None

    def agregar(self,dato): #creo un nodo nuevo y lo agrego al principio
        nodo_nuevo = Nodo(dato)
        nodo_nuevo.siguiente = self.primero
        if self.vacia() == True:
            self.ultimo = nodo_nuevo
        self.primero = nodo_nuevo
        self.tamanio = self.tamanio + 1

    def imprimir(self): # recorro todos los nodos y los voy imprimiendo
        nodo_i = self.primero
        while nodo_i != None:
            print(nodo_i.dato)
            nodo_i = nodo_i.siguiente

    def magnitud(self)->int: #ejercicio
        """devuelve la cantidad de elementos o nodos que hay en la lsita"""
        return self.tamanio

    def buscar(self,elemento)->bool:
        nodo_i = self.primero
        encontrado = False
        while nodo_i != None:
            if nodo_i.dato == elemento:
                encontrado = True
            nodo_i = nodo_i.siguiente
        return encontrado

    def remover(self,item):
        nodo_i = self.primero # creo un nodo para recorrer
        encontrado = False # flag que indique si encontre el item
        anterior = None # otro nodo que inique cual es el anterior del actual
        if self.primero.dato == item:
            self.primero = self.primero.siguiente
            encontrado = True
        while nodo_i != None and encontrado != True:
            if nodo_i.dato == item:
                encontrado = True
                anterior.siguiente = nodo_i.siguiente
            anterior = nodo_i
            nodo_i = nodo_i.siguiente
        if self.primero == None:
            self.ultimo = None
        self.tamanio = self.tamanio - 1
    
    def agregar_final(self,e)->None:
        """O(n) -> lineal"""
        nuevo_nodo = Nodo(e) # creo un nodo nuevo
        self.tamanio = self.tamanio + 1
        if self.vacia():
            self.primero = nuevo_nodo
        else:
            nodo = self.primero # nodo es una variable aux (iterador) para ir recorriendo la lista
            while nodo.siguiente != None: # mientras no llegue al final (nodo.siguiente == None)
                nodo = nodo.siguiente
            # cuando salgo del while nodo.siguiente == None
            nodo.siguiente = nuevo_nodo
    
    def agregar_final_cte(self):
        """O(1) -> constante"""
        nuevo_nodo=Nodo()
        self.tamanio = self.tamanio + 1
        self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
    
    def agregar_indice(self, i, x):
        if (i > self.tamanio) or (i < 0):
            # error
            raise IndexError("Posici??n inv??lida")

        # Crea nuevo nodo, con x como dato:
        nuevo = Nodo(x)

        # Insertar al principio (caso particular)
        if i == 0:
            # el siguiente del nuevo pasa a ser el que era primero
            nuevo.siguiente = self.primero
            # el nuevo pasa a ser el primero de la lista
            self.primero = nuevo

        # Insertar en cualquier lugar > 0
        else:
            # Recorre la lista hasta llegar a la posici??n deseada
            n_ant = self.primero
            for pos in xrange(1,i):
                n_ant = n_ant.siguiente

            # Intercala nuevo y obtiene n_ant -> nuevo -> n_ant.prox
            nuevo.siguiente = n_ant.siguiente
            n_ant.siguiente = nuevo

        # En cualquier caso, incrementar en 1 la longitud
        self.tamanio += 1
    
    def reemplazar(self,indice,nuevo_dato):
        if indice >= 0 and indice < self.tamanio:
            actual = self.primero
            
            for i in range(indice):
                actual = actual.siguiente
            
            actual.dato = nuevo_dato
        else:
            print('indice fuera de la lista')
        
    
    def indice(self, e)->int: # es parecido a buscar
        " el m??todo de la lista toma un elemento y si se encuentra devuelve el primer ??ndice en donde se encuentra"
        nodo = self.primero
        indice = 0
        while nodo.siguiente !=None:
            if nodo.dato == e:
                return indice
            indice +=1
            nodo = nodo.siguiente
        
    def devolver(self,i:int)->object:
        "El m??todo elem toma un ??ndice i y devuelve el i-??simo elemento de la lista"
        nodo = self.primero
        d = nodo.dato
        for j in range(i):
            nodo = nodo.siguiente
        d = nodo.dato
        
        return d      
        

if __name__ == "__main__":
    # prueba nodo
    nodo1 = Nodo(98)
    nodo2 = Nodo(34)
    nodo3 = Nodo(45)
    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    print(nodo1.dato)
    print(nodo1.siguiente.dato)
    print(nodo2.siguiente.dato)
    print(nodo1.siguiente.siguiente.dato)
    print(nodo3.dato)

    #Agregar nodo al principio
    nodo0 = Nodo(15)
    nodo0.siguiente = nodo1
    print(nodo0.dato)
    print(nodo0.siguiente.siguiente.dato) #34

    # Agregar nodo al final
    nodoNuevo = Nodo(-1)
    print(nodo3.siguiente) # None -> Es el ultimo!!!
    nodo3.siguiente = nodoNuevo
    print(nodo0.siguiente.siguiente.siguiente.siguiente.dato) # -1
    
    # prueba lista
    milista = Lista()
    milista.agregar(1)
    milista.agregar(2)
    milista.agregar(3)
    milista.imprimir()
