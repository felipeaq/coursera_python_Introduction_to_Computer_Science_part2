def ordenada(lista):
    for i in range(len(lista)-2):
        if not (lista[i]<=lista[i+1]):
            return False
    return True

if __name__=='__main__':
    print (ordenada([5,4,2,5,6,7]))
    print (ordenada([2,3,4,5,6]))
