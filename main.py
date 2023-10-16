from humanos import humano
from profesionista import profesionista
hombre= humano()
mujer = humano()
ramon = profesionista()
hombre.set_name('ramon')
hombre.set_age(32)
hombre.set_ocupation('ingeniero')

ramon.set_name('ramon')
ramon.set_age(32)
ramon.set_ocupation('ingeniero')

print(hombre.get_name())
print(hombre.get_age())
print(hombre.get_ocupation())

hombre.presentate()
ramon.curriculum()