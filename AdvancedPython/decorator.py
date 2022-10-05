from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): # <-- no importa la cantidad de args ni la de args nombrados
        inital_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elaped = final_time - inital_time
        time_elaped = time_elaped.total_seconds()
        print(f"Pasaron {time_elaped} segundos")
    return wrapper


def decorator_custom(message):
    def decorator(func):
        print(f"{message}:")
        def wraper(*args, **kwargs):
            print("Funcion decorada :D")
            func(*args, **kwargs)
        return wraper
    return decorator


@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    print(a + b)

@execution_time
def saludo(nombre="Owen"): 
    print(f"Hola {nombre}!")

@decorator_custom("Este mensaje es ejemplo de la personalizacion que puede recibir un decorador")
def multiply(a: int, b: int) -> int:
    print(f"The result of {a} x {b} = {a*b}")
    return a * b


def run():
   # random_func()
   # suma(2, 2)
   # saludo("Awas")
    multiply(43, 4312)


if __name__ == "__main__":
    run()