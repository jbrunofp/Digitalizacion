""" DICCIONARIO INVERSO """

dictionary={
    "Manzana":1,
    "Pera":2,
    "Platano":3,
}
inverted_dictionary={}

for key, valor in dictionary.items():
    inverted_dictionary[valor] = key

print(inverted_dictionary)