#algoritmo que calcula a soma entre todos os numeros impares

#que sao multiplos de tres e que se encontrar no intervalo de 1
#ate500


#fazer um intervalo de 1 ate 500

#nisso abrir a restrição de que quando for
#  
#impares e multiplos de 3, eu posso somar e dps mostrar na tela quanto que deu

#basicamente eu vou mostrar na tela os numeros que de 1 a 500 sao tanto multiplos de 3 e impares
#e nisso dps fazer a soma total disso

#acredito que nao precisa mostrar de 1 a 500 nao, fica muito grande


for intervalo in range(1,500,1):
    if intervalo%2!=0 and intervalo%3==0:
        print(intervalo)
    
    #para um numero ser impar ele tem que o seu modulo ser diferente de 0
    #e para um numero ser multiplo 3, a sua divisao por 3 tem que ser 0

    