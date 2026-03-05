from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

"""La salida quedaría así:
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', '_eyes': 'brown', '_hairs': 'dark'}
blue
light
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', '_eyes': 'blue', '_hairs': 'light'}

Por qué:
Internamente el objeto queda
{
  'first_name': 'Joffrey',
  'is_alive': True,
  'family_name': 'Baratheon',
  '_eyes': 'brown',
  '_hairs': 'dark'
}

first_name: se pasa como argumento al constructor.
is_alive: valor por defecto True.
family_name: definido por la clase King (Baratheon).
_eyes: atributo “protegido”, valor inicial "brown".
_hairs: atributo “protegido”, valor inicial "dark".

con:
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")

Los setters actualizan los atributos protegidos:
set_eyes("blue") → cambia _eyes de "brown" a "blue"
set_hairs("light") → cambia _hairs de "dark" a "light"

y con los getters hacemos la lectura:
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
esto da como resultado: blue
                        light

Y para ver el resultado final del objeto después de los cambios:
    print(Joffrey.__dict__)
"""