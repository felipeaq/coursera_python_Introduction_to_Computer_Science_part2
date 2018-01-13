def compara(minha_matriz,mat):
    return str(len(minha_matriz))+'X'+str(len((minha_matriz[0]))) ==str(len(mat))+'X'+str(len((mat[0])))

def soma_matrizes(m1, m2):
    m3=[]
    if (not compara(m1,m2)):
        return False
    for (i) in (range(len(m1))):
        linha=[]
        for j in range(len(m1[i])):
            linha.append(m1[i][j]+m2[i][j])

        m3.append(linha)
    return m3

if __name__=='__main__':
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    print (soma_matrizes(m1,m2))
    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    print(soma_matrizes(m1, m2))
