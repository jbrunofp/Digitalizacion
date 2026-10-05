class Rectangulo:
    def __init__(self, largo, ancho):
        self.ancho = ancho
        self.largo = largo

    def perimetro(self):
        return self.largo * 2 + self.ancho * 2

    def area(self):
        return self.largo * self.ancho


if __name__ == "__main__":

    largo = int(input("Introduce el largo del rectángulo: "))
    ancho = int(input("Introduce el ancho del rectángulo: "))
    
    rectangulo = Rectangulo(largo, ancho)
    
    print(f"El perímetro de su rectángulo es: {rectangulo.perimetro()}\nEl área de su rectángulo es: {rectangulo.area()}")
