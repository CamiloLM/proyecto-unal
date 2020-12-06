from seleccionar import select_dir, search_index
from busqueda import search_book
from os import getcwd
from time import sleep

print("╔" + "═"*34 + "╗")
print("║ Bienvenido al Motor de Busqueda. ║")
print("╚" + "═"*34 + "╝\n")
directory = False

while True:
    print("Seleccione la opcion que desea realizar:")
    print("\t1. Ingresar directorio de busqueda.")
    print("\t2. Realizar una busqueda.")
    print("\t3. Creditos.")
    print("\t4. Salir del programa.")
    case = input()

    if case == "1":
        print("Ingrese la ruta del directorio que desea usar:")
        directory = select_dir(input())

        if directory:
            index_created = search_index(getcwd())
            if index_created:
                print("El directorio se ha seleccionado correctamente\n")
            else:
                print("Hubo un error con el directorio")

    elif case == "2":
        if not directory:
            print("No se ha seleccionado un directorio.")
            print("Intente otra vez despues de ingresar un directorio.")
        else:
            search_book()

    elif case == "3":
        print("Este programa fue desarrollado por:")
        print("\tMaria Jose Jara Herrera.")
        print("\tCamilo Londoño Moreno.")
        print("\tSergio Alexander Parada Amarillo.")
        print()

    elif case == "4":
        print("Hasta Luego.")
        sleep(1)
        break

    else:
        print("Entrada incorrecta. Intente otra vez.")
