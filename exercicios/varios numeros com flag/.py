#programa  que ler varios numeros inteiros pelo teclado. o programa so vai parar quando o usuario digitar o valor 999, que é a condicao de parada. no final,mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)

lista_dos_valores=[]
while True:
    try:
        valor_inteiro=int(input('digite o valor inteiro:\n'))
        if valor_inteiro!=999:
            lista_dos_valores.append(valor_inteiro)
            print(lista_dos_valores)
        else:
            print(lista_dos_valores)
            #ja que para por completo aqui, eu posso fazer os demais que so vai ser mostrado quando parar por completo

            #quantos numeros foram digitados
            total_numeros=(len(lista_dos_valores))
            #qual foi a soma entre eles , desconsiderando o flag ->bandeira:999
            soma_dos_numeros=sum(lista_dos_valores)
            break
    except ValueError:
        print('entrada de dados invalida:\n')
print(f'os numeros digitados na lista foram:{lista_dos_valores}, o total de numeros digitados foram:{total_numeros} , a soma desses numeros digitados resultou em: {soma_dos_numeros}')