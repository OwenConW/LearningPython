DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run(data):
    all_python_devs = [worker["name"]
                       for worker in data if worker["language"] == "python"]
    adults = list(map(lambda dic: dic["name"], filter(
        lambda people: people["age"] >= 18, data)))
    old_people = list(map(lambda worker: worker | {
                      "old": worker["age"] > 70}, data))
    """
        Lo que se hace en la linea 78 es mapear lo que nos llega por parametros en donde por cada una de las posiciones,
        se toma el diccionario y se lo une a un nuevo diccionario, dando como resultado una lista de diccionarios exactamente
        igual a los anteriores pero ahora con una nuevo par de key: value siendo este el "age": True or False
    """
    # all_platzi_workers = [worker["name"] for worker in data if worker["organization"] == "Platzi"]
    # approvedes1 = list(filter(lambda dic: dic["language"] == "python" or "javascript", data))
    # approvedes2 = [dic for dic in data if dic["language"] == "python" or "javascript"]
    # print(f"Opcion1: {approvedes1}, Opción2: {approvedes2}")
    print("""
        PYTHON DEVS:
    """)
    for dev in all_python_devs:
        print(dev)
    print("""
        ADULTS:
    """)
    for person in adults:
        print(person)


if __name__ == "__main__":
    run(DATA)
