class Libro:
    isbn = 0

    def __init__(self):
        print(f"Ingresa el nombre del libro: ")
        self.nombre = input()
        print(f"Ingresa el nombre del autor: ")
        self.autor = input()
        print(f"Ingresa el genero del libro: ")
        self.genero = input()
        Libro.isbn += 1

    def __str__(self):
        return f"""{self.nombre}
-----------------------------
{self.autor}
{self.genero}
-----------------------------
"""
