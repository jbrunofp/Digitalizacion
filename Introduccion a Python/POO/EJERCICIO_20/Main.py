from Biblioteca import Biblioteca
if __name__ == "__main__":
    biblioteca = Biblioteca("Alejandría")
    while (True):
        print("""-----------------------------
        GESTIÓN DE BIBLIOTECA
1. Añadir libro
2. Eliminar libro
3. Consultar libro
4. Consultar biblioteca
-----------------------------
¿ Qué operación desea realizar ?: """)
        option = int(input())
        match option:
            case 1:
                biblioteca.añadir()
            case 2:
                biblioteca.eliminar(input("Ingresa el nombre del libro:"))
            case 3:
                biblioteca.consultar(input("Ingresa el nombre del libro:"))
            case 4:
                biblioteca.consultar_biblioteca()