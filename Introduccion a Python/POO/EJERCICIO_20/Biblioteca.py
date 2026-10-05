from Libro import Libro


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros: list[Libro] = []

    def añadir(self):
        self.libros.append(Libro())

    def eliminar(self, nombre):
        for libro in self.libros:
            if libro.nombre == nombre:
                self.libros.remove(libro)

    def consultar(self, nombre):
        for libro in self.libros:
            if libro.nombre == nombre:
                print(libro)
    
    def consultar_biblioteca (self):
        for libro in self.libros:
            print(libro)
