def maiusculas(stringa):
    nova=''
    for i in stringa:
        if ord(i)>=64 and ord(i)<=90:
            nova+=i
    return nova
if __name__=='__main__':
    print(maiusculas('Programamos em python 2?'))
    print(maiusculas('Programamos em Python 3.'))
# deve devolver 'PP'

    print(maiusculas('PrOgRaMaMoS em python!'))
# deve devolver 'PORMMS'
