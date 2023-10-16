class humano:
    
    def presentate(self):
        print('hola mi nombre es', self.name, 'tengo', self.age, 'y soy', self.ocupation)
    
    def set_name(self, nombre):
        self.name = nombre

    def get_name(self):
        return self.name
    
    def set_age(self, edad):
        self.age = edad

    def get_age(self):
        return self.age
    
    def set_ocupation(self, ocupacion):
        self.ocupation = ocupacion

    def get_ocupation(self):
        return self.ocupation
    