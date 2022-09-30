
#! ENTORNO VIRTUAL

"""
? Similitudes con JS

pip -> npm
requeriments.txt -> package.json
venv -> node modules
"""


"""
* mkdir x
* git init
* python3 -m venv venv  
? venv = virtual enviroment
* en linux --> source venv/bin/activate  <-- se activa el entorno virtual
* alias avenv="source venv/bin/activate" <-- cada vez que se ejecute avenv se activara el entorno virtual
? escribir constantemente ese comando para activar y desactivar el env puede ser molesto, por lo que se puede crear un alias
* deactivate <--- se desactiva el entorno virtual
"""

#! What is PIP?
#* Package Installer for Python
#* pip ---> python | npm ---> JavaScript
#* requeriments.txt | package.json 

#? Commands

# pip freeze | pip3 freeze     <---- muestra los modulos instalados en el entorno virtual
# pip install x      <---- instala el/los modulos solicitados
# pip freeze > requeriments.txt      <--- guarda las dependencias a utilizar para el proyecto
# cat requeriments.txt        <--- podemos ver las dependencias alojadas en el archivo 
# pip install -r requeriments.txt     <--- instala las dependencias necesarias

#! Lists and Dicts

def run():
    list1 = [{"name": "Owen", "lastName": "Bonoris"}]
    for i in list1:
        print("The list/arr has:", i)
        for key, value in i.items():
            print(f"The dictionary/obj has: {key} ---> {value}")

if __name__ == "__main__":
    run()

#* List Comprehensions

def list_nums():
    nums = []
    for i in range(1, 101):
        if i**2 % 3 != 0:
            nums.append(i**2)
    print(f"List of the first 100 natural numbers ^ 2:", nums)


def list_nums_comprehensions():
    nums = [ i**2 for i in range(1, 101) if i % 3 != 0]
    print(f"List of the first 100 natural numbers ^ 2:", nums)

# [ element for element in iterable  if condition ]
"""|______| |______________________| |___________|
      |                  |                   |
      V                  V                   |
    lo que va        De donde se sacan        --->  Condición para 
    a quedar en      los elementos, sea             filtrar (opcional)
    la lista         un rango u otra list
"""
def reto():
    squares = [i for i in range (1, 100000) if i % 36 == 0]
    print(squares)


#* Dictionary Comprehensions

def dic_comprehensions():
    dic = {i: i**2 for i in range(1, 101) if i % 3 != 0}
    print(dic)

# [ key: value for value in iterable  if condition ]
"""|___||______| |______________________| |___________|
     |      |                  |                   |
     V      V                  V                   |
    key  lo que va        De donde se sacan        --->  Condición para 
         a quedar en      los elementos, sea             filtrar (opcional)
         value del dic    un rango u otra list
"""

import math

def reto2():
    dic = {i: round(math.sqrt(i), 2) for i in range(1, 100000)}
    print(dic)
    

#! Funciones anónimas:

# en python tmb se las conoce como "lambda"
# y a diferencia de js no se puede tener mas de una linea de codigo.

palindrome = lambda string: string.replace(" ", "").lower() == string.replace(" ", "").lower()[::-1] 
#funcion palindroma anonima
palindrome("Ana") # True
palindrome("Azul luza") # True
palindrome("Diego") # False

#! High order functions: filter, map y reduce

# Una funcion de orden superior es una funcion que recibe como parametro un callback, es decir, otra función

#* FILTER

nums_to_filter = [1, 4, 5, 6, 9, 13, 19, 21]

odd = [i for i in nums_to_filter if i % 2 != 0]

odd2 = list(filter(lambda num: num % 2 != 0, nums_to_filter))

# la funcion de orden superior filter recibe en primer lugar una funcion, en este ej lambda y como segundo parametro
# un iterable (en python un iterable es todo aquello que se puede devolver), esta funcion retorna un iterador por lo que
# se tendra que convertir en lista

#* MAP

nums_to_map = [1, 2, 3, 4, 5]

raiseds = [i**2 for i in nums_to_map]

raiseds2 = list(map(lambda num: num**2, nums_to_map))

#* REDUCE

from functools import reduce

nums_to_reduce = [2, 2, 2, 2, 2]

reducers = reduce(lambda num1, num2: num1 * num2, nums_to_reduce)


#! Manejo de errores

# traceback 
"""
Traceback (most recent call last):              3 <-- De donde parte el error
File "<stdin>", line 1, in <module>             2 <-- Archivo donde se produjo, linea y modulo
ZeroDivisionError: division by zero             1 <-- Exepción 
"""

# SyntaxError --> reconoce el error y no llega a ejecutarse el codigo

# Cuando se eleva el error es que, el programa rompe en algun punto del mismo, por ejemplo una funcion, automaticamente si el error
# no se capturo el mismo se eleva a una función padre. Si llegase a la función principal sin ser tratado o manejado el programa
# dejara de correr

# Exception ---> se ejecuta el programa y en un momento rompe y se eleva.
#* Ejemplos:
# Keyboardinterrupt --> Ctrl + c --> eleva la exepcion.
# KeyError ---> acceder a una key de un diccionario inexistente.
# IndexError ---> Intento de acceso a un indice inexistente.
# FileNotFoundError ---> Cuando se intenta abrir un archivo q no existe.
# ZeroDivisionError ---> Error al tratar de dividir por 0.
# ImportError -----> Error al intentar importar un modulo y se genera un error.

#! Debugging

# Herramienta Run and Debug, play, pausa, entrar a la función, breackpoint

#! Manejo de exepciones

"""
#*  try, except

def palindrome(string):
    return string == string[::-1]


print(palindrome(1))


Traceback (most recent call last):
File "main.py", line 5, in <module>
    print(palindrome(1))
File "main.py", line 2, in palindrome
    return string == string[::-1]
TypeError: "int" objects is not subscriptable


#*  try:
#*      print(palindrome(1))
#*  except TypeError:
#*      print("Solo se pueden ingresar palabras")

El try es como en js para intentar correr algo mientras que el except captura en caso de que ocurra un TypeError

#* Raise

Si el usuario ejecutase incluso con el try except con un str vacio "" seria un error sin serlo
"""

def palindrome_raise(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresa una cadena vacía")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


try:
    print(palindrome(1))
except TypeError:
    print("Solo se pueden ingresar palabras")

# raise viene de elevar, basicamente se el str ingresado es un str vacio se eleva un error y se lo captura en la linea 207,
# se le cambia el nombre y se lo maneja de la manera deseada

#* Finally

# Se utiliza para cerrar archivos, cerrar una conexión a una db o liberar recursos externos

#   try:
#       f = open("archivo.txt")
#   finally:
#       f.close()


# Ejemplo manejo de errores:


def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError("Porfavor ingresa un número positivo.")
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)


def run2():
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            print(divisors(num) or "No se pudo realizar la operación.") 
        except ValueError:
            print("Debes ingresar un número")
         

if __name__ == "__main__":
    run2()


#! Assert statements

# afirmaciones en Python
"""
        Código
          |
          V
    Assert statement
          |
    --------------
    |            |
    V            V
  Error       Código
"""

#*  assert condicion, mensaje de error   -----> afirmo que la condición es verdadera, si no mensaje de error


def palindrome_assert(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacía"
    return string == string[::-1]


print(palindrome_assert(""))

# AssertionError: No se puede ingresar una cadena vacía

def divisors3(num):
    divisors = []
    for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
    return divisors


def run3():
    while True:
        num = input("Ingrese un numero: ")
        assert num.isnumeric() and int(num) >= 0, "El dato ingresado tiene que ser un número positivo"
        print(divisors3(int(num)) or "No se pudo realizar la operación.") 
         

if __name__ == "__main__":
    run3()


#! Archivos

"""
Texto:   <---- lo que se va a utilizar
.xml
.json
.txt
.css
.py
.js
.csv
Binarios:
.png
.jpg
.dll
.mp3
.mp4
.avi
"""

#* R --> Lectura
#* W --> Escritura (sobrescribe)
#* A --> Escritura (agregar alfinal)

with open("./rute/del/archivo.txt", "r") as f:
    pass



def read():
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        numbers = [int(l) for l in f]
    print(numbers)


def write():
    pass 


def run4():
    pass 


if __name__ == "__main__":
    run4()