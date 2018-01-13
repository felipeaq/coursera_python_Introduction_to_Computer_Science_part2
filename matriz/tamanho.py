def dimensoes(minha_matriz):
    print( str(len(minha_matriz))+'X'+str(len((minha_matriz[0]))))

if __name__=='__main__':
    minha_matriz = [[1], [2], [3]]
    dimensoes(minha_matriz)
    minha_matriz = [[1, 2, 3], [4, 5, 6]]
    dimensoes(minha_matriz)
