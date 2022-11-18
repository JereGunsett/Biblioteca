class Libros():
    def __init__(self,title,genero,autor):
        self.title = title
        self.genero = genero
        self.autor = autor
        self.alquilado = None
    
    def __str__(self):
        alquilado = ''
        if self.alquilado == None:
            alquilado = 'Sin alquilar'
        else:
            alquilado = self.alquilado
        return "Titulo: {0}\nGenero: {1}\nAño: {2}\nAlquilado: {3}\n" \
            .format(self.title,self.genero,self.autor,alquilado)
        #return f"Titulo: {self.titulo}\nGenero: {self.genero}\nAño: {self.anio}\nAlquilada: {self.alquilada}"

    def esta_alquilado(self):
        return self.alquilado != None
    
    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.title<other.title
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.title<=other.title
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.title==other.title
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.title!=other.title
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.title>other.title
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.title>=other.title