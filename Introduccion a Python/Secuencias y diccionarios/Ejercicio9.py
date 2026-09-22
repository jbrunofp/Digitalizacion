""" DICCIONARIO DE FRECUENCIAS """
print("Escribe un frase: ")
phrase = input().split()
frecuenty_dictionary={}

for word in phrase:
    if word in frecuenty_dictionary:
        frecuenty_dictionary[word] += 1
    else:
        frecuenty_dictionary[word] = 1

print(f"Frecuencias: {frecuenty_dictionary}")
