from pickle import load
from os import path, startfile, getcwd


def search_book():
    """Realiza la busqueda en el indice"""
    
    index = load(open("index.pickle", "rb"))
    print("Ingrese los terminos que desea buscar:")
    search = validate(input())
    result = []

    for key in index:
        for words in search:
            if words == set():
                pass
            elif words in index[key] and len(result) <= 20:
                if key not in result:
                    result.append(key)
    
    show_result(result)


def show_result(result):
    """Muestra el resultado de la busqueda"""
    if result:
        for i in range(len(result)):
            print("Indice {}: {}".format(i + 1, result[i]))
            print("""
            Que accion desea realizar?\n
            1. Abrir un archivo\n
            2. Volver al menu de inicio""")
            option = input()
            if option == "1":
                start_file(result)
    else:
        print("""
            No se encontro ningun libro\n
            Desea realizar una nueva busqueda? s/n""")
        again = input().lower()
        if again == "s":
            return search_book()


def start_file(result):
    """Inicia el arcivo indicado."""
    title = result[0]
    if len(result) > 1:
        print("Ingrese el indice del libro que desea abrir")
        book_index = int(input())
        title = result[book_index - 1]
    startfile(path.join(getcwd, title))


def validate(user_input):
    """Verifica que el texto de entrada sea correcto"""

    list_words = user_input.split()
    validate = False

    while not validate:
        if list_words:
            for word in list_words:
                if word.isalpha() and len(word) > 1:
                    validate = True
                else:
                    validate = False
                    print("No ingrese caracteres especiales, intente de nuevo")
                    list_words = input().split()
        else:
            print("Entrada incorrecta, intente de nuevo")
            list_words = input().split()
    
    for i in range(len(list_words)):
        list_words[i] = list_words[i].lower()
        a, b = 'áéíóúü', 'aeiouu'
        for j in range(6):
            if a[j] in list_words[i]:
                list_words[i] = list_words[i].replace(a[j], b[j])
    
    return list_words
