"""Números pares e impares"""

print("Ingresa una lista de números separados por espacios: ", end="")
numbers = input("")
numbers = numbers.split(" ")
list = []
for number in numbers:
    list.append(int(number))
for number in list:
    print(f"{number} es par" if number % 2 == 0 else f"{number} es impar")


""" Correcion """

numeros = list(map(int, input("Introduce una lista de números separados por espacios: ").split()))
pares=[n for n in numeros if n%2==0]
impares=[n for n in numeros if n%2!=0]

print(f"Pares: {pares}\nImpares: {impares}")