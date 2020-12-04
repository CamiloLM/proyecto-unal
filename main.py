from seleccionar import select_dir, search_index
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
            index_created = search_index(directory)
            if index_created:
                print("El directorio ha sido seleccionado")
            else:
                print("Hubo un error con el directorio")

    elif case == "2":
        if not os.path.isdir(directory):
            print('''No se ha seleccionado un directorio.
            Intente otra vez despues de ingresar un directorio.''')
            continue
        else:
            if directory:
                result = search_book()
                print("""
                Que accion desea realizar?\n
                1. Abrir un archivo\n
                2. Volver al menu de inicio""")
                OPC = input()
                if OPC == "1":
                  if len(result)==1:
                        title = result[0]
                        path = os.path.join(directory, title)
                        print(path)
                        os.startfile(path)
                  if len(result)!=1:    
                        print("Escriba el indice del libro que desea abrir")
                        book_index = int(input())
                        title = result[book_index - 1]
                        path = os.path.join(directory, title)
                        print(path)
                        os.startfile(path)
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
