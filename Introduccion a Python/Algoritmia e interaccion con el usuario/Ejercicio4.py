""""Ordenacion de palabras"""
print("Ingresa ua frase: ", end="")
phrase= input()
sorted_phrase= sorted(phrase.split(), key=str.casefold)
ordered_phrase=""

for word in sorted_phrase:
    ordered_phrase += word + " "
ordered_phrase = ordered_phrase.strip()

print(f"Su frase ordenada es: {ordered_phrase}")