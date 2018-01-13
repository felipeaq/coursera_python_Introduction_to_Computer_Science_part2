def incomodam(n):
    if n>0:
        return incomodam(n-1)+'incomodam '
    else:
        return ''


def elefantes(n):
    n-=1
    if n>2:
        return elefantes(n)+'\n'+str(n)+' elefantes incomodam muita gente'+'\n'+str(n+1)+' elefantes '+incomodam(n+1)+'muito mais'
    elif n==2:
        return ('Um elefante incomoda muita gente'+'\n'+'2 elefantes incomodam incomodam muito mais'+'\n2 elefantes incomodam muita gente\n'+str(n+1)+' elefantes '+incomodam(n+1)+'muito mais')
    else:
        return ''
    return ''

if __name__=='__main__':
    print (elefantes(4))
