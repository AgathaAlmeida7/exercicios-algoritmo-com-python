#algoritmo que mostra na tela todos os numeros pares

#que estao no intervalo entre 1 e 50


# a restrição para um numero ser par é que seu ultimo algarismo
#termine em 0,2,4,6,8
#ou tambem contando de 2 em 2 
#teria diferença no fim essas duas formas de saber se um numero é par,gostaria de saber a abordagem de cada casos desses,
#para esse meu codigo a 2 abordagem que é a melhor

#eu vou criar uma condicao que valida se um numero é par ou n, e meter dentro 


for pares in range(1,51,1):
    if pares%2==0:
        print(pares)
        
    