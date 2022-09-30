import random
import os
from unidecode import unidecode

def run():
    try:
        with open("./palabras.txt", "r", encoding="utf-8") as f:
            words = [i for i in f]
            word_selected = (random.choice(words).replace("\n", ""))
            word_selected = unidecode(word_selected)
            word = dict(enumerate(word_selected))
            os.system("clear")
            print("""""" + "_ " * len(word))
            word_user = [i.replace(i, "") for i in word.values()]
            attempt = int(input("""
                [0] Para ingresar una letra.
                [1] Para arriesgar por una palabra.
                Porfavor ingrese un comando valido 0 o 1.
            """))
            if(attempt == 0):
                while word_selected != "".join(word_user):
                    attempt = input("Ingrese una letra: ")[:1]
                    for k, v in word.items():
                        if attempt == v:
                            word[k] = ""
                            word_user[k] = attempt 
                            msj = ""
                            for l in word_user:
                                msj += "_ " if l == "" else f"{l} "
                            os.system("clear")
                            print(msj)
            elif(attempt == 1): 
                attempt = input("Ingrese la palabra: ")
                return print("WOOOOOOW, lo lograste... COMO????? Ganaste de manera excepcional!") if attempt == word_selected else print("Lo siento, has perdido.")
            else:
                return print("Comando invalido, lo siento")
            return print("Felicidades! Has ganado el juego!") 
    except ValueError as ve:
        print(ve) 


if __name__ == "__main__":
    run()