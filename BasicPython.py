
""" 
Comentarios en bloque de python
"""

# comentarios en linea de python 

"""
!  >>>>>>>>>>  Diferencias contra JS  <<<<<<<<<<<
 
console.log() --->  print()

var/let/const nombre = "Owen" ---->  nombre = "Owen

var nombreOwen = "Owen" ----> nombre_owen = "Owen"

true ---> True
false ---> False

&&  ---->  and
||  ---->  or
"!   --->  not
== | ===  ---->  ==
" != | !== ----> !=

condicion ? true : false  ----> true if condicion else false

.toUpperCase() ----> .upper()
.trim() ---> strip()
"nashe".length ----> len("nashe")
.slice(0,3) ---> [0:3]


let nombre = "owen"                     nombre = owen
`Hola ${}!`           ------------>     f'Hola {nombre}'

const limite = 100    ------------>     LIMITE = 100

new Array() ----> list()
"""

21 / 5  # eso devuelve 4.2
21 // 5 # eso devuelve 4, se queda con la parte entera
21 % 5 # eso devuelve 1
22 ** 5 # eso devuelve 32, potencia

input("Ingresa un dato boludito: ")  # <--- input lee un dato recibido 

int("43") # <--- convierte el contenido de () en numero
float() # <---- convierte el contenido de () en numer decimal 
str(43) # <--- convierte el contenido de () en string 

nombre = input("¿Cual es tu nombre?: ").capitalize() # primera letra en mayuscula
nombre = input("¿Cual es tu nombre?: ").strip() # elimina espacios basura
pass # <-- para "pasar" codigo, es decir, dejar ese espacio para escribir posteriormente

#* SLICES:
"NASHE".lower() # <--- pasa todo a minuscula
"NASHE".replace("S", "Z") # <--- remplaza todas las S por Z ---> NAZHE
"owen"[0:3] # <--- corta el str desde el indice 0 hasta el 2 inclusibe ---> owe
"owen"[:3] # <--- corta el str desde el indice 0 hasta el 2 inclusibe ---> owe
"owen"[1:] # <--- corta el str desde el indice 1 hasta el ultimo ---> wen
"owencitobro"[0::2] # <-- corta el str desde el inidice 0 hasta el ultimo de 2 en 2 --> oectbo
"owen"[::] # <-- desde el indice 0 al final ---> owen
"owen"[::-1] # <--- desde el inidice 0 al final a la inversa ---> newo
#*

# TODO  Primer mini programa en python: "Conversor de monedas"

#! FUNCIONES

def conversor():
    dolar = 280
    pesos = int(input("Cuantos pesos argentinos desea cambiar?"))
    dolares = round(pesos / dolar, 2) 
    return "Tienes " + str(dolares) + " U$D"

def conversorArs(dolar):
    peso = 280
    pesos = round(dolar * peso, 2)
    return "Tienes " + str(pesos) + " AR$"

#! CONDICIONALES

def condicionales():
    edad = int(input("Cuantos años tienes? "))
    if edad > 18:
        return "Sos mayor de edad."
    elif edad == 18:
        return "Sos mayor de pedo."
    else:
        return "Sos menor de edad."


def conversor_universal(moneda, valor_dolar):
    pesos = int(input("Ahora porfavor ingrese la cantidad de pesos " + moneda +  " que desea transformar: "))
    return "Usted tiene " + str(round(pesos / valor_dolar, 2)) + " U$D"

def conversor_moneda():
    pais = input("""
    Bienvenido al conversor de monedas!

    1- Argentina
    2- Colombia
    3- Mexico

    Por favor ingrese el numero de su país: """)
    if pais == "1":
        return conversor_universal("argentinos", 280)
    elif pais == "2":
        return conversor_universal("colombianos", 3875)
    elif pais == '3':
        return conversor_universal("mexicanos", 20.31)
    else:
        return "Porfavor ingrese una opción valida"

# función principal que va a ser la que va a correr el programa al principio
# por convensión se utiliza una funcion llamada run o main
def run(): 
    word = input("Porfavor ingrese una palabra: ").replace(" ", "").lower()
    return "Tu palabra es un palíndromo" if word == word[::-1] else "Tu palabra no es un palíndromo"

###############################################

if __name__ == "__main__" :
    run()

# entry point de un programa de python
# cuando python se encuentra con este punto empieza a correr todo lo que viene debajo

##############################################

#! BUCLES

#? WHILE

def intento():
    i = 0
    LIMITE = 100
    while(i < LIMITE): # while i < 100:
        if i % 2 == 0:
            print("2 elevado a " + str(i) + " es igual a: " + str(2**i))
            i += 1
        else:
            i += 1


def recursividad(num):
    i = num
    if i == 100:
        return
    else:
        print("2 elevado a " + str(i) + " es igual a: " + str(2**i))
        recursividad(i + 1)


#? FOR

def ciclo_for():
    for i in range(1000):
        print(i)


def tablas_multiplicar():
    tabla = int(input("Porfavor ingrese la tabla que desea aprender: "))
    print(f"TABLA DEL {tabla}")
    for i in range(11):
        print(f'{tabla} x {i} = {tabla*i}')

#* Recorrer un str

def main():
    nombre = input("Porfavor ingrese su nombre: ")
    for letra in nombre:
        print(letra)

if __name__ == "__main__":
    main()


#* Interrupciones del ciclo

def conti():
    for i in range(101):
        if i % 2 != 0:
            continue
        else:
            print(i)


def breakk():
    for i in range(101):
        if i == 50:
            break
        print(i)


def tarea():
    i = 0
    while i < 101:
        if i == 50:
            continue
        print(f"yo, numero {i} no soy el 50")
        i += 1


#! CALLBACKS

def cb(fn):
    num = int(input("Porfavor ingrese un numero: "))
    return fn(num)


def cb_fn(num):
    return f"El numero ingresado elevado a la 10 es igual a {num**10}"    
# if __name__ == "__main__":
#     pass


#! LISTAS (Arrays de toda la vida)

mult = [1]
objetos = [1, 2, 3, 4, 5]
objetos2 = [8, 9, 10]
objetos.append(6) # <-- agrega al final el dato pasado
objetos.pop(0) # <-- elimina el indice 0 del array, si no le pasamos el indice, elimina el ultimo
objetos.count(3) # <-- recorre la lista y retorna la cantidad de valores que coinciden con el dato de parametro
objetos.remove(2) # <-- elimina el primer dato encontrado con el valor ingresado
objetos[::-1] # <-- invierte la lista
mult * 6 # = [1, 1, 1, 1, 1, 1]  

objetos + objetos2 # <-- concatena las listas


#! TUPLAS 
# cuando hacemos bucles para recorrer, es más rapido con las tuplas
# estas son INMUTABLES, es decir no se pueden modificar, solo reasignar

mi_tupla = (1, 2, 3, 4, 5)

# la coma es obligatoria, incluso si fuera un solo dato
tupla = (1,)

# acceder a las posiciones
mi_tupla[0]

# concatenar tuplas 

mi_tupla += tupla

mi_tupla.count(1) # <-- recorre la lista y retorna la cantidad de valores que coinciden con el dato de parametro
mi_tupla.index(1) # <-- retorna el indice en el que se encuentra el primer valor que coincide con el ingresado

#! DICCIONARIOS (Objetos de toda la vida)

def diccionarios():
    diccionario = {
        "name": "Owen",
        "surname": "Bonoris",
        "age": 19,
        "profession": "Full Stack Developer"
    }
    print(diccionario["name"])
    print(diccionario["surname"])
    print(diccionario["age"])

    for keyss in diccionario.keys():
        print(keyss) # name, surname, age, profession

    for valuess in diccionario.values():
        print(valuess) # "Owen", "Bonoris", 19, "Full Stack Developer"

    for keyss, valuess in diccionario.items():
        print(f"{keyss}: {valuess}") # "name: Owen",  "surname: Bonoris", "age: 19", "profession: Full Stack Developer"


if __name__ == "__main__":
    diccionarios()


#!###########################################333

#? Ejercicio de primalidad hecho por mi:

def isprimo():
    numero = int(input("Porfavor ingrese un numero para saber si es primo o no: "))
    for divisor in range(1, numero + 1):
        resultado = numero % divisor
        if resultado == 0 and divisor != numero and divisor != 1:
            return f"El numero {numero} no es un número primo!"
    return f"El numero {numero} es un número primo!" 


if __name__ == "__main__":
    isprimo()


#? Proyecto videojuego:

import random


    