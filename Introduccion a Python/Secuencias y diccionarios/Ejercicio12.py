"""LISTA DE DICCIONARIOS (AGENDA)"""

agenda = {}
answer = -1
while answer != 3:
    answer=-1
    
    print(f"""Añadir contacto (1).
Buscar contacto (2).
SALIR(3).""")
    
    answer = int(input("Seleccione una opcion: "))
    if answer == 1:
        print("Ingrese el nombre del usuario")
        nombre = input()
        print("Ingrese el telefono")
        telefono = int(input())
        agenda[nombre]= [telefono]
        
        
    if answer == 2:
        print("Ingrese el nombre del usuario: ")
        nombre = input()
        if nombre in agenda:
            print(f"{nombre} ha sido encontrado. ¿ Que desea realizar ?\n")
            answer=-1
            while answer != 4:
                print(f"""Consultar datos (1).
                Agregar telefono (2).
                Eliminar telefono (3).
                SALIR (4)""")
            

