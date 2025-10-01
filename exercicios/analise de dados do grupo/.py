#programa que leia a idade e o sexo de varias pessoas. a cada pessoa cadastrada, o programa devera pergunta se o usuario quer ou nao continuar. no final,mostre:

#A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS?
#B)QUANTOS HOMENS FORAM CADASTRADOS
#C)QUANTAS MULHERES TEM MENOS DE 20 ANOS
#eu posso aqui utilizar o metodo que juntando com aquela variavel ja me mostra rapidamente o resultado disso auqi 

mulheres=0
homens=0
idade=0
lista_idade=[]
pessoa_posicao=[]
lista_sexo=[]
contador=0

while True:
        try:
            idade=int(input('digite a sua idade:\n'))
            if idade<0:
                print('entrada de idade invalida:\n')
                continue
            #eu tenho que criar a lista que vai ir armazenando a idade 
            lista_idade.append(idade)
        except ValueError:
            print('entrada de dados invalida\n')
            break

        while True:
                    sexo=input('Digite  o seu sexo : (F) = (FEMININO) / (M)= MASCULINO:\n').strip().upper()
        #validaçao se as letras sao somente do alfabetos 
        #cada str tem metodos que ajudam a verificar 
        #o metodo isalpha() 
                    if sexo not in["F","M"]:
        #para verificar se sexo esta entre as opcoes validas , é preciso colocar todas em uma colecao (lista, tupla ou conjunto )
                        print('a entrada de informação do sexo esta invalida:\n')
                        continue
                    lista_sexo.append(sexo)
                    break
                    #COMO SE TRATA DE ENTRADE DADOS DO TIPO STRING, EU NAO PRECISO FAZER A VALIDAÇÃO O TRY E O EXCEPT VALUEERROR 
                    #PQ O INPUT AUTOMATICAMENTE JA RECEBE ENTRADAS COMO STRING 

                

                   #contador de qual numeracao foi essa pessoa ( a partir daqui ja vou me baseando )

                   #AQU ENTRA O PONTO CHAVE , DE EU SABER SE O USUARIO QUER CONTINUAR OU NAO DIGITANDO.... 

        contador+=1
        pessoa_posicao.append(contador)
                    #ESSA LOGICA QUE EU FIZ AQUI FOI PRA LITERALMENTE DIZER ASSIM :

                    # DPS DE TER BOTADO A IDADE, E O SEXO (1) PESSOA ALI FOI REGISTRADA, E  ASSIM IRA CONTINUAR EM UM DETERMINADO LOOP DE ACORDO COM A RESPOSTA DA PESSOA .

                    #OBS: DPS AQUI EU IREI FAZER UMA 'GAMBIARRA' PARA CONTAR QUANTOS TEM, QUE TEM, E POSICOES UTILZANDO METODOS DO PYTHON

        
            
        try:
            resp=input('voce quer continuar: (Sim) ou (nao)?:\n').strip().upper()
            if resp not in ['SIM','S','N','NAO']:
                            print('entrada de resposta invalida:\n tente novamente:\n')
                            continue 
            if resp in ['SIM','S']:     
                continue
            else:
                print('programa encerrado...\n')
                break
        except ValueError:
                print('entrada de dados invalida:\n')
   
total_pessoas_mais_18=sum(1 for idade in lista_idade if idade>18 )
total_homens_cadastro=lista_sexo.count('M')
mulheres_menos_de_20=sum(1 for mulheres in lista_idade if mulheres<20 )
print(f'o total de pessoas com mais de 18 anos é de :{total_pessoas_mais_18}') 
print(f' o total de homens cadastrado nesse sistema foi de:{total_homens_cadastro}')
print(f'o total de mulheres cadastradas com menos de 20 anos nesse sistema foi de :{mulheres_menos_de_20}')                  
           
#A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS?-OKAY

#B)QUANTOS HOMENS FORAM CADASTRADOS-OKAY

#C)QUANTAS MULHERES TEM MENOS DE 20 ANOS-okay

#eu posso aqui utilizar o metodo que juntando com aquela variavel ja me mostra rapidamente o resultado disso auqi 
               

#agora quando o programa acabar eu vou entrar e fazer a llogica para conseguir coletar essa informações aqui e mostrar


#para eu coletar quantas pessoas tem mais de 18 anos, eu vou ter que ir na variavel de  lista de idade, e la fazer a coletar das idades que estao inseridas  e ver quantos +18 aparecem

#EXTRAINDO INFORMACAO DA LISTA DEPOIS DE TER PREENCHIDO ELA
#irei percorrer a lista

#UMA CONDICAO APLICADA A CADA ITEM DA LISTA.
#PARA CADA IDADE EM LISTA_IDADE , EU IREI VERIFICAR SE ELA É MAIOR QUE 18 , E CONTAR QUANTAS ATENDEM A ISSO

#QUANTO SE QUER CONTAR BASEANDO-SE EM UMA CONDICAO, O JEITOE PERCORRER A LISTA E APLICAR ESSA CONDICAO A CADA ITEM.



                    

    


   
