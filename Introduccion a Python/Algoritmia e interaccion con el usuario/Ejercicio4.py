""" Calculadora básica """

print("Introduce una operacion básica (+ - / *): ", end="")
operacion= input()
operacion = operacion.strip().replace(" ","")

numbers= operacion.split("+" or "-" or "/" or "*")
first_number= int(numbers[0])
second_number= int(numbers[1])

match operacion[operacion.find("+" or "-" or "/" or "*")]:
    case "+":
        print(f"Su suma es: {first_number+second_number} ")
    case "-":
        print(f"Su resta es: {first_number-second_number} ")
    case "*":
        print(f"Su multiplicación es: {first_number*second_number} ")
    case "/":
        print(f"Su división es: {first_number/second_number} ")