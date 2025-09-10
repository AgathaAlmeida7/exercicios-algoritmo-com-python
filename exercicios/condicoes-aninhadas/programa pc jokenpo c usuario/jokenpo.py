#pedra papel e tesoura. 
#eu irei escolher se eu serei  tesoura ou papel. 
# o outro sera o pc, nisso irei fazer o time com a palvra 'jo/ken/po' e depois disso usar a biblioteca do phyton de numero//palavra aleatoria (a favor do pc) e dps pedindo uma entrada de dados minha e nisso vendo quem ganhou pela força da escolha e nisso mostrar


#######from time import sleep #######

#biblioteca de tempo do phyton, que com a função sleep vai fazer com que algo //algum 
# comando do codigo der uma 'dormida' de um 'comando para o outro'

#PARA A GERAÇÃO DE NUMEROS ALEATORIOS NO PHYTON, PODE-SE USAR A BIBLIOTECA RANDOM. QUE É PARTE DE UMA BIBLIOTECA PADRAO DO PHYTON

#A BIBLIOTECA RANDOM CONTEM FUNÇÕES PARA GERAR NUMEROS ALEATORIOS INTEIROS,NUMEROS DE PONTO FLUTUANTE E OUTRAS FORMAS DE ALEATORIEDADE.

######from random import randint######

#AS PRINCIPAIS FUNÇÕES DA BIBLIOTECA RANDOM PARA GERAR NUMEROS ALEATORIOS

print('SEJA BEM VINDO, AO JOGO (PAPEL E TESOURA)\n')
print('VOCE USUARIO IRÁ JOGAR COM O PC, COM ISSO VOCE IRA ESCOLHER O NUMERO REPRESENTANTE DE QUAL VOCE QUER SER (PAPEL OU TESOURA, COM ISSO O PC SERÁ O OPOSTO),POREM VOCES IRAO ESCOLHER AO MESMO TEMPO, E COM ISSO IREMOS VER QUEM FOI QUE GANHOU O JOGO ou QUEM EMPATOU O JOGO!:\n')
print('BOA SORTE!!!!!!\n')

print('[1]: escolha caso voce queira ser o [PAPEL]:\n')
print('[2]: escolha caso voce queira ser a [TESOURA]:\n')
print('CASO DÊ (EMPATE) IRÁ SER REPETIDO A JOGADA:\n')
print('AO TODO SERÁ 5 JOGADAS, IREMOS VER QUEM GANHOU MAIS\n')

opcaousuario=int(input('digite a opção de jogo que voce quer:\n'))

from random import randint

opcaopc=randint(1,2) 

#TENHO QUE VER QUE O NUMERO 2 TEM QUE SER O PRIORIZADO, E ENTENDER SE O PCVAI REALMENTE ENTENDER ISSO AI,CASO NAO, EU TENHO QUE FAZER ALGO PARA QUE ELE REALMENTE SAIBAA    

#OBS: PELO QUE EU PERCEBO O MAIS INDICADO AQUI PARA CHEGARMOS AO QUE REALMENTE QUEREMOS É A UTILIZAÇÃO DO 'AND' DO QUE O 'OR' ACHO QUE NAO DARIA CERTO A FUNCIONALIDADE COM O 'OR'.

if opcaousuario==1 and opcaopc==1:
    print(' o usuario digitou {} e o pc digitou {}, logo resultou em um (EMPATE)'.format(opcaousuario,opcaopc))
#ai aqui como deu empate ela iria fazer algo para que isso aqui fosse repetido novamente
#ai creio que entratia a estrutura de repetição do-while
elif opcaousuario==2 and opcaopc==1:
    print('o usuario digitou {} e o pc digitou{}, logo resultou em (USUARIO) como o campeao dessa rodada'.format(opcaousuario,opcaopc))
elif opcaousuario==1 and opcaopc==2:
    print('o usuario digitou{} e o pc digitou {}, logo resultou em (pc) commo o campeao dessa rodada'.format(opcaousuario,opcaopc))
else:
    print(' o usuario digitou {} e o pc digitou {}, logo resultou ambos empatados!'.format(opcaousuario,opcaopc))

