#programa que ler o nome,idade,sexo de 4 pessoas. no final do programa mostre:

#a media de idade do grupo;
#o nome do homem mais velho
#quantas mulheres tem menos de 20 anos?
lista_das_idades=[]
lista_dos_nomes=[]
lista_dos_sexo=[]

for contador in range(4):
    try:
        nome_da_pessoa=input(f'digite o nome da pessoa{contador}').lower().strip().isalpha()
        if "" in nome_da_pessoa:
            continue
        lista_dos_nomes.append(nome_da_pessoa)        
        idade=int(input(f'qual a idade da pessoa:{contador}'))
        if idade<0 and idade>110:
            print('entrada de idades invalidas\n')
            continue
        lista_das_idades.append(idade)
        sexo=input('Digite qual é o seu SEXO(F/M)').lower()
        #usar uma condicional if junto com o operador de pertinencia in ou uma comparação simples com ==
        if sexo!="f" and sexo !="m":
            print('entrada invalida para o sexo. Digite novamente\n')
            continue
        lista_dos_sexo.append(sexo)
        #DEPOIS LEVAR EM CONSIDERAÇÃO QUE PODE TER IDADES IGUAIS   
        if sexo=="m":
            maior_idade=max(lista_das_idades)
            posicao_da_idade=lista_das_idades.index(maior_idade)
            posicao_do_nome=lista_dos_nomes.index(nome_da_pessoa)
        ########################################################
        #ENTENDER ESSA LOGICA AQUI, PARA PEGAR A IDADE,MOSTRAR O NOME DA PESSOA DO SEXO MASCULINO QUE TEM A MAIOR IDADE.
        #TBM DPS FAZER UMA VALIDAÇÇAO PARA CASO TENHA MAIS DE UM HOMEM COM A MESMA IDADE, COMO SERIA O CRITERIO....
        #PARAMOS AQUI PARA FAZER A VALIDAÇAO#
        ######################################################
            



         #eu tou entrando aqui pq eu tenho que ver so se o sexo for igual m, 
        #como tambem é str vai entrar toda aquela validação
        print(f'A pessoa {contador} se chama:{nome_da_pessoa} tem a idade:{idade} e é do sexo:{sexo}')
       

    except ValueError:
        print('entrada invalida')
        continue
  

#media de idade do grupo

media_total_do_grupo_das_idades=sum(lista_das_idades)/len(lista_das_idades)
#obs:nao darpara dividir uma variavel de lista por um numero
#a forma correta é calcular a media com os agregadores da linguagem python

#sum()->soma todos os elementos numericos da lista;
#len()->retorna a quantidade de elementos da lista;
#->dividindo a soma pelo tamanho da lista voce obtem a media;


        





#desafio hard do programa 