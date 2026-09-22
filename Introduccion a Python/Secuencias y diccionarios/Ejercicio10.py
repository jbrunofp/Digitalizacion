""" TUPLAS Y COORDENADAS """
import math

print("Ingresa el primer punto (x/y): ", end= "")
p1 = list(map(int, input().split()))

print("Ingresa el segundo punto (x/y): ", end= "")
p2 = list(map(int, input().split()))

euclidian_distance= math.sqrt(math.pow((p2[0]-p1[0]), 2) + math.pow((p2[1]-p1[1]), 2))

print(f"La distancia euclidiana de los puntos {p1} y {p2} es: {euclidian_distance}.")