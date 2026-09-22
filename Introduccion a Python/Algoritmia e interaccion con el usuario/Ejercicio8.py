""" JUEGO DE ADIVINANZA   """
import random

secret_number= random.randint(0, 100)
answer = -1
print(secret_number)

while answer != secret_number:
    print("Introduce un número entre 0 y 100: ", end= "")
    answer= int(input())
    if answer < secret_number:
        print(f"Es mayor.")
    elif answer > secret_number:
        print(f"Es menor.")

print("¡¡¡ Enhorabuena, GANASTE !!!")
