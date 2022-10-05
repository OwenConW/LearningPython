"""La programación orientada a objetos tiene cuatro características principales:
Encapsulamiento. Quiere decir que oculta datos mediante código.
Abstracción. Es como se pueden representar los objetos en modo de código.
Herencia. Es donde una clase nueva se crea a partir de una clase existente.
Polimorfismo. Se refiere a la propiedad por la que es posible enviar mensajes sintácticamente iguales a objetos de tipos distintos.
En este curso, los pasos a seguir será.
Analisis
Plasmar
Programar
La mayoría solo aprende a hacer esto en un lenguajes de programación,aquí se tiene una variabilidad.
"""
#! CLASES

class Person:

    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"Hola, mi nombre es{self.name}")


class Worker:

    def __init__(self, work):
        self.profession = work

    def introduction(self):
        print(f"Soy {self.profession}")



#! Tipado estatico en PYTHON


a: int = 5
b: str = "Hola"
c: bool = True

def suma(a: int, b: int) -> int:
    return a + b



from typing import Dict, List, Tuple

positives: List[int] = [1, 2, 3, 4, 5, 6, 7]

users: Dict[str, int] = {
    "Argentina": 1,
    "Mexico": 34,
    "colombia": 45
}

countries : List[Dict[str, str]] = [
    {
        "name": "Argentina",
        "people": "45000000",
    },
    {
        "name": "Mexico",
        "people": "9000000",
    },
    {
        "name": "Colombia",
        "people": "874284184",
    }
]

numbres: Tuple[int, float, int] = (1, 0.5, 1)

coordinatesTypes = List[Dict[str, Tuple[int, int]]]

coordinates: coordinatesTypes = [
    {
        "coor1": (1, 2),
        "coor2": (3, 5)
    },
    {
        "coor1": (5, 6),
        "coor2": (2, 6)
    }
]

# Para que no ocurran flexibilidades importar el modulo "mypy"

# ejecutar mypy archivo.py --check-untyped-defs



def is_palindrome(string: str) -> bool:
    try:
        if string == "":
            raise ValueError("Se debe ingresar una palabra")
        string = string.replace(" ", "").lower()
        return string == string[::-1]
    except ValueError as ve:
        return print(ve)


def is_primo(number: int) -> bool:
    try:
        if number <= 0:
            raise ValueError("El número debe ser mayor a 0")
        divisors = [i for i in range(1, number + 1) if number % i == 0]
        return True if len(divisors) == 2 else False
    except ValueError as ve:
        return print(ve)


def run():
    word = input("Ingrese una palabra para saber si es un palindromo: ")
    try:
        number = int(input("Ahora ingrese un número para saber si es primo: "))
        if is_palindrome(word) == True or False:
            print(f"La palabra {word} es un palindromo")
        if is_primo(number) == True or False:
            print(f"El número {number} es primo")
    except ValueError:
        print("Porfavor ingresa un número")

if __name__ == "__main__":
    run()
    

#! SCOPE 

#* Una variable solo esta dispobile dentro de la región donde fue creada

#* Local Scope ---> dentro de un bloque de codigo, se la podra acceder desde unicamente el bloque donde fue creada
#* Global Scope ---> fuera de los bloques de codigo, se la podra acceder desde cualquier bloque

# Si hay global scope y local scope, se le da prioridad a la local

#! CLOSURES

#? Nested functions ---> funciones anidadas, funcion que tiene una funcion 

def main():
    closure_word = "Owen"

    def closure():
        print(closure_word)

    return closure


func_a_ejecutar = main()


del(main)


func_a_ejecutar() # Esto va a imprimir "Owen" a pesar de haber borrado la funcion en donde esta variable vivia

#* REGLAS
# Nested function
# La Nested function hace referencia a una variable de la funcion padre
# La funcion padre retorna a la funcion nested

def make_multiplier(num):
    
    def multiplier(num2):
        return num * num2

    return multiplier

por_10 = make_multiplier(10)
por_4 = make_multiplier(4)

por_4(2) # 8
por_4(6) # 24
por_10(5) # 50

por_10(por_4(2)) # 80


def make_repeater_of(n):
    def repeater(string):
        return string * n 
    
    return repeater


def make_division_by(num):
    return lambda num2: num2 / num


#! DECORADORES --> closure especial

#* Funcion que recibe como parametro una funcion y le añade y retorna una funcion diferente

def decorador(func):
    def wraper():
        print(" -- Nuevas lineas de codigo para la funcion --")
        func()
    
    return wraper


def saludo():
    print("Hola!")


saludo()
# Hola!

saludo = decorador(saludo)
saludo()
# -- Nuevas lineas de codigo para la funcion --
# Hola!

#* SUGAR SINTAX ---->  codigo embellecido para simple comprension

# |
# V

@decorador
def saludo2():
    print("Hola!")

# Example

def mayusculas(func):
    def wrpaer(text):
        return func(text).upper()
    return wrpaer


@mayusculas
def mensaje(name):
    return f"{name}, recibiste un mensaje"

print(mensaje("Owen"))

# si no se sabe la cantidad de args a pasar ---> *args, **kwargs

# se puede asignar el valor de un arg en caso de que no se pase (nombre="Owen")

#todo VER ARCHIVO DECORATOR.PY

#! ITERADORES

#* Iterables ---> objs que podemos recorrer, str, list, dict

lista = [1, 2, 3, 4, 5]
iterator = iter(lista)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break

# El ciclo for no existe en python, es sugar sintactica de este bucle infinito

#* Iterador personalizado

class EvenNumbers:
    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration

#* SUGAR SYNTAX ---> Iteradores

def my_gen():

    print("Hello world!")
    n = 0
    yield n

    print("Hello heaven!")
    n = 1
    yield n

    print("Hello hell!")
    n = 2
    yield n


a = my_gen()

print(next(a))

# generator comprehension

my_generator = (x for x in range(1, 100))

#! SETS --> Conjuntos 

#* Coleccion desordenada de elementos unicos e inmutables

my_set = {3, 4, 5}
my_set2 = {"Hola", 23.3, False, True}
my_set3 = {3, 3, 2} # <-- Aca se repite el 3, pero python borra los repetidos --> {2, 3}
my_set4 = {[1, 2, 3], 4} # <-- Python rompe ya que tiene un elemento mutable (lista)

empty_set = {}   # <--- esto es un dict

empty_set = set() # <--- esto es un set

lista = [1, 2, 3, 4, 4, 4, 5]

my_set = set(lista) # <--- {1, 2, 3, 4, 5}

# añadir un elemento a un set ---> .add(7) | .update([8, 9, 10])  

my_set.update((1, 7, 2), {6, 8})

# eliminar un elemento de un set ---> .discard(1) | .remove(2)

# la diferencia es que si intento eliminar un elemento que no existe con discard se sigue corriendo el programa, mientras que con el remove se eleva un error

# .pop()  --> borra un elemento aleatorio
# .clear() --> limpia el set

#* Operar con sets

#? Union

my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 | my_set2  # {3, 4, 5, 6, 7}

#? Interseccion

my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 & my_set2  # {5}

#? Diferencia

my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 - my_set2  # --> {3, 4}
my_set4 = my_set2 - my_set1  # --> {6, 7}

#? Diferencia simetrica

my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 ^ my_set2  # --> {3, 4, 6, 7 }


# Eliminar repetidos de una Lista

def remove_duplicate(arr):
    # without_duplicate = []
    # for i in arr:
    #     if i not in without_duplicate:
    #         without_duplicate.append(i)
    # return without_duplicate
    return list(set(arr))


#! Manejo de fechas 

import datetime

my_time = datetime.datetime.now() # ---> 2020-04-30  17:58:38.988340
my_day = datetime.datetime.today() # ----> 2020-04-30

my_day.year # ---> 2020
my_day.month # ---> 04
my_day.day # ---> 30

#formateo de fecha

#  mm/dd/yyyy
#  dd/mm/yyyy

# Tablas de valores
"""
%Y  --> Year
%m  --> Month
%d  --> Dat
%H  --> Hour
%M  --> Minute
%S  --> Second
"""

my_datetime = datetime.datetime.now()

my_str = my_datetime.strftime("%d/%m/%Y")
print(f"Formato LATAM: {my_str}")

my_str = my_datetime.strftime("%m/%d/%Y")
print(f"Formato USA: {my_str}")

# Zonas horarias

# > pip install pytz

from datetime import datetime
import pytz 

bogota_timezone = pytz.timezone("America/Bogota") # DB de pytz
bogota_date = datetime.now(bogota_timezone)

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)


