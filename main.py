from seleccionar import select_dir
continuar = True
print('Inicio del programa')

DIRECTORIO = " "

while continuar:
  print("""
  Bienvenido al Motor De Busqueda. \n
  Seleccione la opcion que desea seleccionar: \n
  \t 1. Ingresar directorio de busqueda.
  \t 2. Realizar una busqueda.
  \t 3. Creditos.
  \t 4. Salir del programa.""")
  caso = int(input())
  
  if caso == 1:
    DIRECTORIO = select_dir(input("Ingrese el directorio: "))
    if DIRECTORIO != False:
      print(DIRECTORIO)
    
    OPC = input("Desea volver al inicio? (s/n): ")
    if OPC == "s": continue
    elif OPC == "n":
      OPC = input("Desea salir del programa? (s/n): ")
      if OPC == "s":
        print("Hasta Luego.")
        break
      elif OPC == "n": continue
    
    
  elif caso == 2:
    if DIRECTORIO == " ":
      print("No se ha seleccionado un directorio. Intente otra vez despues de ingresar un directorio.")
      continue
    else:
      print("Ingrese las palabras a buscar en los documentos: ")

    OPC = input("Desea volver al inicio? (s/n): ")
    if OPC == "s": continue
    elif OPC == "n":
      OPC = input("Desea salir del programa? (s/n): ")
      if OPC == "s":
        print("Hasta Luego.")
        break
      elif OPC == "n": continue
  

  elif caso == 3:
    print("""
    Programa Creado Por: 
    \t Maria Jose Jara Herrera.
    \t Camilo Londoño Moreno.
    \t Sergio Alexander Parada Amarillo.
    """)

    OPC = input("Desea volver al inicio? (s/n): ")
    if OPC == "s": continue
    elif OPC == "n":
      OPC = input("Desea salir del programa? (s/n): ")
      if OPC == "s":
        print("Hasta Luego.")
        break
      elif OPC == "n": continue
  

  elif caso == 4:
    OPC = input("Desea salir del programa? (s/n): ")
    if OPC == "s":
      print("Hasta Luego.")
      break
    elif OPC == "n": continue


  else:
    print("Entrada incorrecta. Intente otra vez.")

print("Fin del programa")

