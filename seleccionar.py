import os
import pickle


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
    index = None
    test = os.path.join(path,"index.pickle")
    print(path, test)

    if os.path.isfile(test):
        index = pickle.load(open(test, "rb"))
    else:
        index = create_index(path,test)

    return index


def create_index(path, test):
    content = os.listdir(path)
    files = []

    for file in content:
        if (os.path.isfile(os.path.join(path, file))) and (file.endswith('.pdf') or file.endswith('.txt')):
            files.append(file)

    index = {}

    for file in files:
        if file.endswith('.txt'):
            words = words_txt(os.path.join(path,file))
            index[file] = words
        elif file.endswith('.pdf'):
            pass

    fichero = open(test, "wb")
    pickle.dump(index, fichero)
    fichero.close()
    
    return index


def words_txt(file_path):
    with open(file_path, "r") as f:
        words = set()
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
        return words


if __name__ == '__main__':
    search_index(os.getcwd())