def busca(lista, elemento):
    primeiro=0
    ultimo= len(lista)-1
    while (ultimo>=primeiro):
        meio=(primeiro+ultimo)//2
        print (meio)
        if lista[meio]==elemento:
            return meio
        if elemento > lista[meio]:
            primeiro = meio + 1
        else:
            ultimo = meio-1
    return False
