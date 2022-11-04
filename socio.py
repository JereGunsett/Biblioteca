class Socio():
    def __init__(self,dni,nombre,telefono,domicilio):
        self.dni =dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio
        
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
        return "DNI: {0}\nNombre: {1}\nTelefono: {2}\nDomicilio: {3}\n" \
            .format(self.dni,self.nombre,self.telefono,self.domicilio)
