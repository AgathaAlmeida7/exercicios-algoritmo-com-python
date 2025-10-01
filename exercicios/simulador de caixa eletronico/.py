#programa que simula o funcionamento de um caixa eletronico. no inicio,pergunte ao usuario qual sera o valor a ser sacado(numero inteiro) e o programa vai informar quantas cedulas de cada valor sera entregues

#OBS:CONSIDERE QUE O CAIXA POSSUI CEDULAS DE 50,20,10 E 1 REAL 

print('---'*10)
print('BEM VINDO AO CAIXA VIRTUAL')
print('---'*10)


cedulas=[50,20,10,1]
while True:
    try:
        valor_de_saque=int(input('digite qual valor voce quer sacar.. obs:so pode ser valor inteiro:\n'))
    except ValueError:
        print('entrada de dados invalida:\n')

        #eu tava pensando em criar uma lista que essa lista ja me deixa guardar esses numeros ai: 50,20,10,1

        #porem , uma obs: esses numeros estarao nalista porem aparece la so uma vez..... 

        #dps de que o usuario dizer o valor que ele quer, eu vou pegar esse valor e vou começar a dividir pelas cedulas e uso a funcao do python que so me permita o inteiro de resultado , o liquido da divisa. se nao for exato eu tentarei ir para o proximo numero que seaprox

#OBS: A ORDEM DA LISTA INFLUENCIA DIRETAMENTE NA LOGICA DO SAQUE 

# O SEGREDO AQUI É UTILIZAR A DIVISAO INTEIRA // PARA SABER QUANTAS DAQUELA CEDULA VAO SER USADAS

#AUTOMATIZANDO O ACESSO DE QUAIS CEDULAS DA LISTA
#PERCORRER A LISTA COM O LOOP FOR PEGANDO CADA CEDULA DE FORMA AUTOMATICA

    for cedula in cedulas:
#percorra cada valor dentro da lista cedulas, e em cada volta do loop,me entregue esse valor dentro da variavel chamada cedula

        qtd=valor_de_saque//cedula
