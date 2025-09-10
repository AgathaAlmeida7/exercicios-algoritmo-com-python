#programa que leia um numero inteiro qualquer e peça para o usuario escolher qualserá a base de conversao:

#1- para binario
#2- para octal
#3- para hexadecimal

numero=int(input('digite um numero inteiro:\n'))

print('COM BASE NO NUMERO QUE VOCE ESCOLHEU,ESSAS SAO AS 3 FORMAS DE CONVERSÃO QUE VOCÊ PODE ESCOLHER PARA SABER COMO FICARÁ O NUMERO QUE VOCE INDICOU:\n\n')

print('DIGITE (1) CONVERTER PARA (BINARIO)')
print('DIGITE (2) CONVERTER PARA (OCTAL)')
print('DIGITE (3) CONVERTER PARA (HEXADECIMAL)')

opcao=int(input('digite o numero da opção que voce quer que seja realizado no seu numero:\n'))

#binario=bin(numero)
#octal=oct(numero)
#hexadecimal=hex(numero)
#A BRONCA AQUI É QUE EU ESTOU COMPARANDO A VARIAVEL OPCAO QUE É DO TIPO INTEIRO, DIRETAMENTE COM A FUNÇÃO BIN E A VARIAVEL NUMERO(QUE VAI RETORNAR UMA STRING) REPRESENTANDO UM NUMERO EM BINARIO O QUE NAO FAZ SENTINDO
 
if opcao==1:
    print('o numero que voce digitou {} em binario representará:\n{}'.format(numero,bin(numero)[2:]))#programa que leia um numero inteiro qualquer e peça para o usuario escolher qualserá a base de conversao:
elif opcao==2:
    print('o numero que voce digitou {} em octal representará:\n{}'.format(numero,oct(numero)[2:]))
elif opcao==3:
     print('o numero que voce digitou {} em hexadecimal representará:\n{}'.format(numero,hex(numero)[2:]))
else:
    print('informação inserida errada, so pode ser (1)/ (2) OU (3). POR FAVOR,TENTE NOVAMENTE')
