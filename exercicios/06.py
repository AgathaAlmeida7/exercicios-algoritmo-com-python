#algoritmo que ler o primeiro termo
#e uma razao de uma PA
#no final, mostre os 10 primeiros termos dessa progressao


#SEQUENCIA DE NUMEROS EM CADA TERMO A PARTIR DO SEGUNDO É OBTIDO SOMANDO(SUBTRAINDO) UM MESMO NUMERO AO TERMO ANTERIOR

#O NUMERO QUE TANTO SE ADICIONA OU DIMINUI, É SEMPRE CHAMADO DE RAZAO DE UMA PA

while True:
    try:
        primeiro_termo=int(input('digite qual sera o primeiro termo da PA:\n'))
        razao_pa=int(input('digite qual sera a RAZAO dessa PA:\n'))
        break
    except ValueError:
        print('entrada de dados invalida')
#tem que pensar que o usuario ele pode quebrar 
#a forma que é a ok para se validar



#o numero passado aqui nao é a quantidade e sim limite
##0a 10
for contador in range(1,11):
    termo=primeiro_termo+(contador-1)*razao_pa
    print(f'{contador}º termo:{termo}')




    #quando utilizamos apenas um numero, o range entende que: -o inicio sera 0 , nao e 1
    #o passo sera 1
    #ele ira ate o numero anterior informado

    


















    #entender oque ta acontecendo por tras dessalogica aqui

#DEPOIS RETORNAR PARA AQUI 
