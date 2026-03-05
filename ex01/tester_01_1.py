from S1E7 import Baratheon, Lannister
"""Importamos las clases Baratheon y Lannister y así podremos crear
personjes (objetos) de esas familias"""

Robert = Baratheon("Robert")
"""
Esto hace varias cosas automáticamente:
1. Se crea un nuevo objeto
2. Se llama a Baratheon.__init__
3. Dentro de ese método:
    - Se llama a Character.__init__
    - Se guardan los atributos:
        first_name = "Robert"
        is_alive = True
        family_name = "Baratheon"
        eyes = "brown"
        hairs = "dark
"""

print(Robert.__dict__)  # __dict__ es un diccionario interno donde Python 
""" Guardará todos los datos del objeto: 
{
    'first_name': 'Robert',
    'is_alive': True,
    'family_name': 'Baratheon',
    'eyes': 'brown',
    'hairs': 'dark'
}"""

print(Robert.__str__)   # mostramos solo la función asociada al objeto
# print(Robert.__str__()) # así llamamos a la func __str__() y muestra el resultado: Vector: ('Baratheon', 'brown', 'dark')

print(Robert.__repr__)  # no se ejecuta repr, solo muestra el método ligado al objeto

print(Robert.is_alive)  # muestra el estado de vida antes de morir, el personaje empieza vivo pq is_alive=true or defecto
Robert.die()            # llamamos al método die y se jecuta, con lo que cambia el estado del objeto a False
print(Robert.is_alive)

print(Robert.__doc__ )   # Esto imprime el docstring de la clase Baratheon:
print("---")            


Cersei = Lannister("Cersei")    # igual que antes pero ahora de la familia Lannister
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")

# Ahora crearemos otro Lannister llamado Jaine pero con el @calssmethod que definimos
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")

"""
Expected output:
$> python tester.py

{'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
<bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
Vector: ('Baratheon', 'brown', 'dark')
<bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
True
False
Representing the Baratheon family.
---
{'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}
<bound method Lannister.__str__ of Vector: ('Lannister', 'blue', 'light')>
True
---
Name : ('Jaine', 'Lannister'), Alive : True
$>
"""
