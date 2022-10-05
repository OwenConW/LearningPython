class Person:
    name = str

    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"Hola, mi nombre es {self.name}")


class Worker(Person):
    work = str

    def __init__(self, name, work):
        super().__init__(name)
        self.profession = work

    def presentation(self):
        self.say_hello()
        print(f"y soy {self.profession}")



def run():
    nombre = input("Porfavor ingrese su nombre: ")
    work = input("Ahora porfavor ingrese su trabajo: ")
    user = Worker(nombre, work)
    user.presentation()
    

if __name__ == "__main__":
    run()



# account.py
class Account:
    id = int
    name = str
    document = str
    email = str 
    password = str

    def __init__(self, name, document):
        self.name = name
        self.document = document 


#car.py

#from account import Account 

class Car:
    id = int
    license = str 
    driver = Account("","")
    passenger = int

    def __init__(self, license, driver):
        self.license = license
        self.driver = driver



# main.py

#from car import Car 
#from account import Account

if __name__ == "__main__":
    car = Car("AMS234", Account("Owen Bonoris", "ANDA876"))
    print(vars(car))
    print(vars(car.driver))


#! HERENCIA

class UberX(Car):
    brand = str
    model = str 

    def __init__(self, license, driver ,brand, model):
        super().__init__(license, driver)
        self.brand = brand
        self.model = model


# Public, Protected, Default, Private