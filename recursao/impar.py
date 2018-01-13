def encontra_impares(lista):
    x = []
    if len(lista) > 0:
        n = lista.pop(0)
        if n % 2 != 0:
            x.append(n)
        x = x + encontra_impares(lista)
    return x



if __name__=='__main__':
    print (encontra_impares([1,2,3,4,5,5]))
