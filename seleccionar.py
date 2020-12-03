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
        path += "\\"
        path = path[-2::]
    else:
        path += "/"
    path += "index.pickle"
    index = None

    if os.path.isfile(path):
        index = pickle.load(path)
    else:
        index = create_index(path)

    return index


def create_index(path):
    content = os.listdir(path)
    files = []

    for file in content:
        if os.path.isfile(os.path.join(path, file)) and file.endswith('.pdf') or file.endswith('.txt'):
            files.append(file)

    # todo craete inverted index with the list of  files

    INDEX = {}
    return INDEX


if __name__ == '__main__':
    search_index(os.getcwd())