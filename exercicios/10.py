#algoritmo que ler o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos
import time
lista_pesos=[]

for contador in range(1,6,1):
    try:
        kg=float(input(f'digite o  peso(KG) da {contador} pessoa:\n'))
        if kg>500:
            print('peso desconsiderado\n')
            continue
        lista_pesos.append(kg)
        #mostrar a ordem de posicao de cada um dos pesos com os seus pesos ao lado
        #nisso depois que eu pegar esses valores e meter nessas variaveis ver agora uma forma de fazer condicional em cima para puder ter o maior ou o menor valor, ou ate mesmo utilizar uma funcao do python que parece que tem especifica para isso        
    except ValueError:
        print('tipo de entrada de dados invalida:\n')


#agora iremos saber qual foi o maior peso digitado e o menor peso
#sem precisar utilizar em if e else ou for com contadores

#utilizando funcoes max e min para lista
#obs: nao sao restritas a listas, podem ser usadas emm qualquer iteravel ou em multiplos valores passados diretamente

#-listas;tuplas;conjuntos;dicionarios;com multiplos argumentos diretamente;em strings


maior_peso=max(lista_pesos)
menor_peso=min(lista_pesos)

print(f'os pesos coletados foram:{lista_pesos}')
time.sleep(2)
print('*'*20)
print(f'o maior peso foi: {maior_peso}\n e o menor foi:{menor_peso}')