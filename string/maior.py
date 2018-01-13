def menor_nome(nomes):
    nome=nomes[0]
    for i in nomes:
        if len(i.strip())<len(nome.strip()):
            nome= i
    return nome.strip().capitalize()

if __name__=='__main__':
    print (menor_nome(['maria', ' josé ', '   PAULO', 'Catarina   ']))
