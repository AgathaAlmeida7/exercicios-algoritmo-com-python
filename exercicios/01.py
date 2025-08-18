#algoritmo que mostra na tela uma contagem regressiva
#para estouro de fogos de artificio. indo de 10 ate 0
#com uma pausa de 1 segundo entre eles
import time

for contagem in range(10,-1,-1):
    #a questao aqui de que nao iria imprimir nada 
    #pq eu quero fazer decrescente nao indicando o passo tb em negativo

    print(contagem)
time.sleep(3)
print('pow\n pow\npow')
