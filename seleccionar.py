import os
import pickle
import fitz


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
    index_created = False
    test = os.path.join(path, "index.pickle")
    print(path, test)

    if os.path.isfile(test):
        index_created = True
    else:
        create_index(path,test)
        index_created = True
    return index_created


def create_index(path, test):
    content = os.listdir(path)
    files = []

    for file in content:
        if (os.path.isfile(os.path.join(path, file))) and (file.endswith('.pdf') or file.endswith('.txt')):
            files.append(file)

    index = {}

    for file in files:
        if file.endswith('.txt'):
            words = words_txt(os.path.join(path, file))
            index[file] = words
        elif file.endswith('.pdf'):
            words = words_pdf(os.path.join(path, file))
            index[file] = words
            pass

    fichero = open(test, "wb")
    pickle.dump(index, fichero)
    fichero.close()
    del(index)


def words_txt(file_path):
    words = set()
    try:
        with open(file_path, "r") as f:
            for line in f:
                for line in f:
                    for word in line.split():
                        word = word.lower()
                        word = word.strip(".,:;-—¿?'()«»¡!")
                        if not word.isnumeric():
                            a,b = 'áéíóúü','aeiouu'
                            for i in range(len(a)):
                                if a[i] in word:
                                    word = word.replace(a[i], b[i])
                            if len(word) > 1:
                                words.add(word)
    except UnicodeDecodeError:
        print("Hay un error en el archivo", file_path)
    return words


  ###busca una palabra especifica en todos los PDF###


def words_pdf(filepath):
    words = set()
    with fitz.open(filepath ) as doc:
        for page in doc:
            page_words = page.getText().split()
            for word in page_words:
                word = word.lower()
                word = word.strip(".,:;-—¿?'()«»¡!")
                if not word.isnumeric():
                    a, b = 'áéíóúü', 'aeiouu'
                    for i in range(len(a)):
                        if a[i] in word:
                            word = word.replace(a[i], b[i])
                    if len(word) > 1:
                        words.add(word)
    return words



if __name__ == '__main__':
    pass