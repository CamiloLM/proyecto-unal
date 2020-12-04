from seleccionar import select_dir
from busqueda import search_book
import os

continuar = True
print('Inicio del programa')

directory = " "

while continuar:
    print("""
    Bienvenido al Motor De Busqueda. \n
    Seleccione la opcion que desea seleccionar: \n
    \t 1. Ingresar directorio de busqueda.
    \t 2. Realizar una busqueda.
    \t 3. Creditos.
    \t 4. Salir del programa.""")
    case = input()

    if case == "1":
        directory = select_dir(input("Ingrese el directorio: "))
        if directory:
            print(directory)
            

        OPC = input("Desea volver al inicio? (s/n): ")
        if OPC == "s":
            continue
        elif OPC == "n":
            OPC = input("Desea salir del programa? (s/n): ")
            if OPC == "s":
                print("Hasta Luego.")
                break
            elif OPC == "n":
                continue

    elif case == "2":
        if not os.path.isdir(directory):
            print('''No se ha seleccionado un directorio.
            Intente otra vez despues de ingresar un directorio.''')
            continue
        else:
            main = os.listdir(directory)
            for i in range(len(main)):
                print(main[i])
            print("Ingrese las palabras a buscar en los documentos: ")

            result = search_book()

            if main:
                print("Que accion desea realizar?")
                print("1. Abrir un archivo")
                print("2. Volver al menu de inicio")
                OPC = input()
                if OPC == "1":
                    print("Por favor, ingrese el indice del archivo que quiera abrir")
                    file = int(input())
                    os.startfile(os.path.join(directory, result[file]))
                elif OPC == "2":
                    continue
            else:
                print("El indice no se ha creado correctamente")

    elif case == "3":
        print("""
        Programa Creado Por: 
        \t Maria Jose Jara Herrera.
        \t Camilo Londoño Moreno.
        \t Sergio Alexander Parada Amarillo.
        """)

        OPC = input("Desea volver al inicio? (s/n): ")
        if OPC == "s":
            continue
        elif OPC == "n":
            OPC = input("Desea salir del programa? (s/n): ")
            if OPC == "s":
                print("Hasta Luego.")
                break
            elif OPC == "n":
                continue

    elif case == "4":
        OPC = input("Desea salir del programa? (s/n): ")
        if OPC == "s":
            print("Hasta Luego.")
            break
        elif OPC == "n":
            continue

    else:
        print("Entrada incorrecta. Intente otra vez.")

print("Fin del programa")
