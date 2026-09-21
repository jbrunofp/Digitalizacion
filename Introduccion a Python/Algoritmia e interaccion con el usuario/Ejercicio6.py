"NUMEROS PRIMOS EN UN RANGO"

import math


def is_cousin(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limite = int(math.isqrt(number))

    for i in range(3, limite + 1, 2):
        if number % i == 0:
            return False
    return True


print("Ingrese dos números: ", end="")
first_number, second_number = list(map(int, input().split()))

for number in range(first_number, second_number):
    if is_cousin(number):
        print(number)
