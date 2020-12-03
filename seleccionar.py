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
  if platform == "win32":
    path += "\ "
    path = path[-2::]
  else:
    path += "/"
  UBICACION = path+"index.pickle"
  INDEX = None
  
  if os.path.isfile(UBICACION):
    INDEX = pickle.load(UBICACION)
  else:
    INDEX = create_index(path)

  return INDEX
  
def create_index(path):
  CONTENIDOS = os.listdir(path)
  ARCHIVOS = []

  for fichero in CONTENIDOS:
    if os.path.isfile(os.path.join(path, fichero)) and ((fichero.endswith('.pdf')) or (fichero.endswith('.txt'))):
      ARCHIVOS.append(fichero)

  # Crear indice con la lista de ARCHIVOS 
  
  INDEX = {}
  return INDEX

if __name__ == '__main__':
  search_index(os.getcwd())