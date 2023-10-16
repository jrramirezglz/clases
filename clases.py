class humano:

    def __init__(self, nombre, edad, ocupacion):
        self.name = nombre
        self.age = edad
        self.ocupation = ocupacion
    
    def presentate(self):
        print('hola mi nombre es', self.name, 'tengo', self.age, 'y soy', self.ocupation)
    
