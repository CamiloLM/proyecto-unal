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
        print("Estos son los resultados:")
        for i in range(len(result)):
            print("Indice {}: {}".format(i + 1, result[i]))
        print()

        while True:
            print("Que accion desea realizar?")
            print("\t1. Abrir un archivo")
            print("\t2. Volver al menu de inicio")
            option = input()
            if option == "1":
                start_file(result)
                break
            if option == "2":
                break
            else:
                print("Opcion incorrecta. Intete otra vez")
    else:
        print("No se encontro ningun libro")
        print("Desea realizar una nueva busqueda? s/n")
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
    print("El documento se esta abriendo")
    startfile(path.join(getcwd(), title))


def validate(user_input):
    """Verifica que el texto de entrada sea correcto"""

    list_words = user_input.split()
    validated = True

    while validated:
        if list_words:
            for word in list_words:
                if word.isalpha() and len(word) > 1:
                    validated = False
                else:
                    validated = True
                    print("No ingrese caracteres especiales, intente de nuevo")
                    list_words = input().split()
        else:
            print("Entrada incorrecta, intente de nuevo")
            list_words = input().split()
    
    for i in range(len(list_words)):
        list_words[i] = list_words[i].lower()
        a, b = "áéíóúü", "aeiouu"
        for j in range(6):
            if a[j] in list_words[i]:
                list_words[i] = list_words[i].replace(a[j], b[j])
    
    return list_words
