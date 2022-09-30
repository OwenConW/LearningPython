def read():
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        numbers = [int(l) for l in f]
    print("Numeros: ", numbers)


def write():
    names = ["Owen", "Agustina", "Mariano", "Facundo", "David"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for n in names:
            f.write(n)
            f.write("\n")


def run():
    write()


if __name__ == "__main__":
    run()