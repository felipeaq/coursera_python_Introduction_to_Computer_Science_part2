def soma_lista(lista):
    if len(lista)>1:
        return lista.pop()+soma_lista(lista)
    else:
        return lista.pop()
