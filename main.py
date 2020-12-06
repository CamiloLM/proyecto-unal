from seleccionar import select_dir, search_index
from busqueda import search_book
from os import getcwd

continuar = True
print('Inicio del programa')

directory = False

while continuar:
    print("""
        Bienvenido al Motor De Busqueda. \n
        Seleccione la opcion que desea seleccionar: \n
        \t 1. Ingresar directorio de busqueda.
        \t 2. Realizar una busqueda.
        \t 3. Creditos.
        \t 4. Salir del programa.\n""")
    case = input()

    if case == "1":
        print("Ingrese la ruta del directorio:")
        directory = select_dir(input())

        if directory:
            index_created = search_index(getcwd())
            if index_created:
                print("El directorio ha sido seleccionado")
            else:
                print("Hubo un error con el directorio")

    elif case == "2":
        if not directory:
            print("""No se ha seleccionado un directorio.
            Intente otra vez despues de ingresar un directorio.""")
        else:
            search_book()

    elif case == "3":
        print("""Este programa fue desarrollado por: 
            \t Maria Jose Jara Herrera.
            \t Camilo Londoño Moreno.
            \t Sergio Alexander Parada Amarillo.\n""")

    elif case == "4":
        print("Hasta Luego.")
        break

    else:
        print("Entrada incorrecta. Intente otra vez.")

print("Fin del programa")
