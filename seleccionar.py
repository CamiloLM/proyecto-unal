import os
import pickle
from sys import platform

def select_dir(path):
  """ Cambia el directorio a la direccion ingresada"""
  if os.path.isdir(path):
    os.chdir(path)
    return os.getcwd()
  else:
    print("El directorio no existe.")
    return False


def search_index(path):
  """ Comprueba si ya existe un indice o no """
  UBICACION = path
  if platform == "win32":
    UBICACION += "\index.pickle"
  else:
    UBICACION += "/index.pickle"
  
  if os.path.isfile(UBICACION):
    return UBICACION
    #INDEX = pickle.load(index.pickle)
  else:
    print("No")
    #Crear el indice
  

if __name__ == '__main__':
  search_index(os.getcwd())