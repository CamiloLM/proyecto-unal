from pickle import load


def buscar_libro(path):
    index = load(open("index.pickle", "rb"))
    busqueda = list(map(str.lower, input().split()))
    resultado = []
    for key in index:
        for palabras in busqueda:
            if palabras in index[key] and len(resultado) <= 20:
                if key not in resultado:
                    resultado.append(key)           
    if resultado:
        for i in range(len(resultado)):
            print(i, resultado[i])
        return resultado
    else:
        print("No se encontro ningun libro")
        return False
 