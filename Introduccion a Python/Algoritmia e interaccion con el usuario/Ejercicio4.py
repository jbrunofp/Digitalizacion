""""Ordenacion de palabras"""
print("Ingresa ua frase: ", end="")
phrase= input()
sorted_phrase_abc= sorted(phrase.split(), key=str.casefold)
sorted_phrase_123= sorted(phrase.split(), key=str.__len__)
ordered_phrase_abc=""
ordered_phrase_123=""

for word in sorted_phrase_abc:
    ordered_phrase_abc += word + " "
ordered_phrase_abc = ordered_phrase_abc.strip()

for word in sorted_phrase_123:
    ordered_phrase_123 += word + " "
ordered_phrase_123 = ordered_phrase_123.strip()

print(f"Su frase ordenada alfabeticamente es: {ordered_phrase_abc}")
print(f"Su frase ordenada alfabeticamente es: {ordered_phrase_123}")