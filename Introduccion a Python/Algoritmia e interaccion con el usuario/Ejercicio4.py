""" Calculadora básica """

print("Introduce una operacion básica (+ - / *): ", end="")
operacion= input()
operacion = operacion.strip().replace(" ","")
operator_position= operacion.find("+" or "-" or "/" or "*")
