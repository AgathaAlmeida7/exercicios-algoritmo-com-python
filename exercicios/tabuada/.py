#programa que mostra a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. o programa sera interropido quando o numero solicitado for negativo.
c=0
while True:
    try:
        numero_da_tabuada=int(input('digite qual é o numero da tabuada que voce quer saber:\n'))
        while c<=10:
            valor_tabuada=numero_da_tabuada*c
            print('{}  X  {}  =  {}'.format(numero_da_tabuada,c,valor_tabuada))
            c+=+1
        #isso é a contagem para eu saber onde da contagem estou naquele determinado momento do loop
    except ValueError:
        print('entrada de dados invalida:\n')
