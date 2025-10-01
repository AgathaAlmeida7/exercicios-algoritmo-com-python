#algoritmo que ler o ano de nascimento de sete pessoas
#no final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores

#capturar o ano atual do sistemas, para diminuir pelo o ano das pessos e descobrir se tem menor ou maior e igual a 18 anos

from datetime import date 
import time 
#aqui esta sendo importado a classe datetime da biblioteca padrao datetime

#primeiro passo é criar a lista vazio
#acredito que a captura das 7 datas de nascimento so vai ate aqui, porem ao mesmo tempo elas nao foram guardadas, armazenadas para puder ir para a outra parte.
#ttipo, foi pedido as 7 datas, realmente seguiu o fluxo, mas nao foi armazenada(guardada as 7 datas)

anos=[]
for contador in range(1,8,1):
    try:
        ano_nascimento=int(input('digite a sua data de nascimento:\n'))
        #fazer validação que tem que ter 4 casas decimais, nem mais e nem menos. para o usuario nao querer ser engraçadinho. 
        if (len(str(ano_nascimento)))<4 or (len(str(ano_nascimento)))>4:
             print('entrada de ano invalida!\n')
        if int(ano_nascimento)<1900:
                    print('entrada invalida.')
                    continue
        anos.append(ano_nascimento)
        #vai entrar a parte de fazer a contabilização
        print('que ano a {} pessoa nasceu?: {}'.format(contador,ano_nascimento))
        #fazer a contabilização de quantas dessas sao maiores e menores de idade
        
    except ValueError:
        print('entrada invalida')
        continue


#criação de uma lista para armazenar esses 7 valores 
#estrutura de dados que serve para armazenar varios valores dentro de uma unica variavel.valores que podem ser de qualquer tipo: numeros;textos e ate outras listas;
maior_idade=0
menor_idade=0


ano_atual=date.today().year
#nao se pode extrair um inteiro de uma lista diretamente no python

#nesse caso, eu vou ter que usar esse jeito aqui :
#caso 2de solução -list comprehension

#vou precisar pegar e fazer com que gere pelo sistema o ano atual na qual estou me referindo naquele exato momento

#agora com base nisso validar quantas pessoas sao maiores e menores de idades daquelas 7 pessoas na qual tiveram os seus registros
idade_gerada = [ano_atual - int(ano_nascimento) for ano_nascimento in anos]


for c in idade_gerada:
        if c>=18:
            maior_idade+=1
        else:
            menor_idade+=1
#aqui falta ajeitar e entender a logica de fato

print(f'ao totalidade de pessoas de maiores e menores sao de:\n')
time.sleep(3)
print('---------'*20)
print(f'maiores de 18:{maior_idade}')
print(f'menos de 18:{menor_idade}')




