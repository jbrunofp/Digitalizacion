"""LISTA DE DICCIONARIOS (AGENDA)"""

agenda : dict[str, list[int]] = {}
answer = -1
while answer != 4:
    answer = -1
    print(f"""Añadir contacto (1).
Buscar contacto (2).
Consultar agenda de contactos (3).
SALIR(4).""")

    answer = int(input("Seleccione una opcion: "))
    match answer:
        case 1:
            print("Ingrese el nombre del usuario: ")
            nombre = input()
            print("Ingrese el telefono: ")
            telefono = int(input())
            agenda[nombre] = [telefono] 

        case 2:
            print("Ingrese el nombre del usuario: ")
            nombre = input()
            if nombre in agenda:
                print(f"\n{nombre} ha sido encontrado. ¿ Que desea realizar ?\n")
                answer = -1
                while answer != 4:
                    print(f"""Consultar datos (1).
Agregar telefono (2).
Eliminar telefono (3).
SALIR (4)""")
                    answer = int(input("\nSeleccione una opcion: "))

                    match answer:
                        case 1:
                            print(nombre, agenda[nombre], "\n")
                        case 2:
                            telefono=int(input("Ingrese el nuevo teléfono: "))
                            if not agenda[nombre].__contains__(telefono):
                                agenda[nombre].append(telefono)
                            else:
                                print("El teléfono ya existe.")
                        case 3:
                            telefono= int(input("Ingresa el telefono a eliminar: "))
                            if agenda[nombre].__contains__(telefono):
                                agenda[nombre].pop(agenda[nombre].index(telefono))
                            else:
                                print("No existe el teléfono")
                answer= -1
            
        case 3:
            for nombre, telefonos in agenda.items():
                print(nombre, telefonos)