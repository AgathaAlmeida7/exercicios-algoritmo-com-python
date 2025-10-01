#algoritmo que ler seis numeros inteiros
#e mostre a soma apenas daqueles que forem pares
#se o valor digitado for impar,desconsidere-o

#inves de pedir 6 numeros inteiros de forma individual
#eu posso pedir esses 6 numeros uitilizanod o for
#porem criando uma restrição que tem que ser do tipo inteiro

soma=0#procurar entender melhor a logica disso aqui


for contagem in range(1, 7, 1):
    try:
        valor_numero = int(input('digite o valor:\n'))
        # caso eu venha a colocar um break ele já para total na condição, e não posso
        if valor_numero % 2 == 0:
            soma += valor_numero
            #para eu saber quais foram os pares
            #criar uma lista
           
            print(f'este foi o {contagem}º valor digitado {valor_numero}')
        else:
            continue
    except ValueError:
        print('tipo de entrada inválida\n')
        continue


soma_total=soma
print('e a soma total desses numeros resultou em:{}'.format(soma_total))
    #caso o tipo de dado nao seja de fato inteiro, ele vai entra nessa condicao, para eu querer forçar dnv mandar ate ser o certo como aqui nao se tem while true, eu vou ter que meter um continue



#ESTÁ TOTALMENTE ATENDENDO  AO QUE O USUARIO PEDIU,POREM TEM UMA FORMA MELHOR DE PROFISSIONALIZAR O CODIGO

#DOS 6 NUMEROS QUAIS FORAM OS QUE SAO PARES E IMPARES E MOSTRAR AS QUANTIDADES

#MELHORA DA EXPERIENCIA DO USUARIO
#FEEDBACK CLARO
#CODIGOMAIS COMPLETO

#COMO QUE PODE SER CRIADO ESSA LOGICA DE ALGORITMO

#DURANTE A LEITURA DOS 6 NUMEROS,ARMAZENAR OS PARES EM UMA LISTA E OS IMPARES EM OUTRA LISTA 

#DEPOIS EXIBIR 

#QUAIS OS NUMEROS PARES E A SUA QUANTIDADE(PARA A QUANITDADE TEM FUNCAOO DO PYTHON QUE JA ME ENTREGA ISSO NA BOA, DE STR)
#QUAIS FORAM IMPARES E SUA QUANTIDADE
#A SOMA TOTAL DOS PARES

