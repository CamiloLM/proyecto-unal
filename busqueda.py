from pickle import load


def search_book():
    index = load(open("index.pickle", "rb"))
    search = list(map(str.lower, input().split()))
    result = []
    for key in index:
        for words in search:
            if words == set():
                pass
            elif words in index[key] and len(result) <= 20:
                if key not in result:
                    result.append(key)
    if result:
        for i in range(len(result)):
            print(i+1, result[i])
        return result
    else:
        print("No se encontro ningun libro")
        return False
