class Cuenta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.saldo - cantidad < 0:
            raise Exception(f"No cuenta con el dinero suficiente. {self.consultar()}")
        else:
            self.saldo -= cantidad

    def consultar(self):
        print(f"Su saldo es de {self.saldo}")


if __name__ == "__main__":
    cuenta = Cuenta(int(input("Ingrese la cantidad inicial de su cuenta: ")))

    while True:
        option = int(input(f"""¿Que tarea desea realizar?
1. Ingresar dinero.
2. Retirar dinero.
3.Consultar dinero
"""))
        match option:
            case 1:
                print("Ingrese la cantidad a ingresar en su cuenta: ")
                cuenta.ingresar(int(input()))
            case 2:
                print("Ingrese la cantidad a retirar en su cuenta: ")
                cuenta.retirar(int(input()))
            case 3:
                cuenta.consultar()
