"""Números pares e impares"""
print("Ingresa una lista de números separados por espacios:", end="")
numbers = input("")
numbers= numbers.split(" ")
list= []
for number in numbers:
    list.append(int(number))
for number in list:
    print(f"{number} es par" if number % 2 == 0 else f"{number} es impar")