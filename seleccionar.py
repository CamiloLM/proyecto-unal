import os

def select_dir(path):
  """ Cambia el directorio a la direccion ingresada"""
  if os.path.isdir(path):
    os.chdir(path)
    return os.getcwd()
  else:
    print("El directorio no existe")
    return False
