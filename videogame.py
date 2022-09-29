import random


def run():
    numero_ran = random.randint(1, 100)
    print("""
               BIENVENIDO A ADIVINA ADIVINADOR!
    
    Este es un juego en el cual se pensara un número aleatorio
    entre el 1 y el 100  y tendras que ir adivinando, tienes 
    unicamente 10 intentos, si no lo logras perderas! Vamos?
    
    """)
    mayor = "mayor"
    menor = "menor"
    vida = 10
    numero = int(input("Porfavor intenta adivinar el número: "))
    while(vida >= 1 and numero != numero_ran):
            vida -= 1
            print(f"Ups! Lo siento... ahora tienes {vida} vidas.")
            print(f"El número pensado es {mayor if numero < numero_ran else menor} al que ingresaste. Prueba de nuevo!")
            numero = int(input("Porfavor intenta adivinar el número nuevamente: "))
    if numero == numero_ran and vida >= 1:
        print(f"Felicidades! Has ganado el juego! El número pensado era efectivamente el {numero_ran}")
    else:
        print("Ups... Te has quedado sin vidas, lo siento... tal vez la proxima?")


if __name__ == "__main__":
    run()
