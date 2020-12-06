from os import path, chdir, listdir
from pickle import dump
import fitz


def select_dir(dir_path):
    """ Cambia el directorio a la direccion ingresada"""
    if path.isdir(dir_path):
        chdir(dir_path)
        return True
    else:
        print("El directorio no existe.")
        return False


def search_index(dir_path):
    """ Comprueba si ya existe un indice o no """
    index_path = path.join(dir_path, "index.pickle")

    if path.isfile(index_path):
        return True
    else:
        create_index(dir_path, index_path)
        return True


def words_txt(file_path):
    """Crea un conjunto con el contenido de un archivo txt"""
    words = set()
    try:
        with open(file_path, "r") as f:
            for line in f:
                for word in line.split():
                    word = word.lower()
                    word = word.strip(".,:;-—¿?'()«»¡!")
                    if word.isalpha():
                        a, b = "áéíóúü", "aeiouu"
                        for i in range(6):
                            if a[i] in word:
                                word = word.replace(a[i], b[i])
                        if len(word) > 1:
                            words.add(word)
    except UnicodeDecodeError:
        print("Hay un error en el archivo", file_path)
    return words


def words_pdf(filepath):
    """Crea un conjunto con el contenido de un archivo pdf"""
    words = set()
    with fitz.open(filepath) as doc:
        for page in doc:
            page_words = page.getText().split()
            for word in page_words:
                word = word.lower()
                word = word.strip(".,:;-—¿?'()«»¡!")
                if word.isalpha():
                    a, b = 'áéíóúü', 'aeiouu'
                    for i in range(6):
                        if a[i] in word:
                            word = word.replace(a[i], b[i])
                    if len(word) > 1:
                        words.add(word)
    return words


def create_index(dir_path, index_path):
    """Crea un indice inverso con el contenido de los libros"""
    content = listdir(dir_path)
    files = []

    for file in content:
        if (path.isfile(path.join(dir_path, file))) and (file.endswith('.pdf') or file.endswith('.txt')):
            files.append(file)

    index = {}
    print("Por favor, espere un momento...")

    for file in files:
        if file.endswith('.txt'):
            words = words_txt(path.join(dir_path, file))
            index[file] = words
        elif file.endswith('.pdf'):
            words = words_pdf(path.join(dir_path, file))
            index[file] = words
            pass

    with open(index_path, "wb") as f:
        dump(index, f)
    del index
