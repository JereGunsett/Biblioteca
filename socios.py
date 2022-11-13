class Socio():
    def __init__(self,dni,nombre,apellido,telefono):
        self.dni =dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        
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
        return "DNI: {0}\nNombre: {1}\nApellido: {2}\nTelefono {3}\n" \
            .format(self.dni,self.nombre,self.apellido,self.telefono)
