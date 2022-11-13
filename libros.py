class Libros():
    def __init__(self,titulo,genero,autor):
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.alquilado = None
    
    def __str__(self):
        return "Titulo: {0}\nGenero: {1}\nAño: {2}\nAlquilada: {3}" \
            .format(self.titulo,self.genero,self.autor,self.alquilado)
        #return f"Titulo: {self.titulo}\nGenero: {self.genero}\nAño: {self.anio}\nAlquilada: {self.alquilada}"

    def esta_alquilada(self):
        return self.alquilada != None
    
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