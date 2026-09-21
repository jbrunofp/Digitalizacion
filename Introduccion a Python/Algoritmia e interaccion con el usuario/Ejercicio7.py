"""GESTION DE NOTAS"""

alumnos = "start"
nombres = []
notas = []

while alumnos[0] != "FIN":
    print("Ingresa el nombre de un alumno y sus notas: ")
    alumnos = input().upper().split()

    if alumnos[0] != "FIN":
        nombres.append(alumnos[0])
        print(nombres)
        notas.append(list(map(float, alumnos[1:])))
        print(notas)

i = 0
for nombre in nombres:
    print(f"""--------------------\nNombre: {nombres[i]}
Nota media: {sum(notas[i])/len(notas)}
Nota alta: {max(notas[i])}
Nota baja: {min(notas[i])}""")
    i += 1
