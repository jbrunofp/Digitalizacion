"""Frecuencia de caracteres"""

print("Ingrese una palabra o frase: ", end="")
string = input().replace(" ", "")

letter_diccionary={}
for letter in string:
    if letter_diccionary.__contains__(letter):
        letter_diccionary[letter] = letter_diccionary[letter] +1
    else:
         letter_diccionary[letter] = 1
        
for entry in letter_diccionary:
    print(entry + ":" + str(letter_diccionary.get(entry)))