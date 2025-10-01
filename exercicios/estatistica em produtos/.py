# programa que lê o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) QUAL É O TOTAL GASTO NA COMPRA
# B) QUANTOS PRODUTOS CUSTAM MAIS DE 1K
# C) QUAL É O NOME DO PRODUTO MAIS BARATO?

contador = 0
lista_preços_dos_produtos = []
lista_nome_dos_produtos = []

while True:

    nome_produto = input('digite o nome do produto:\n').strip().upper()
    # VERIFICAR SE A STRING CONTEM ALGUM TIPO DE ESPAÇO NO MEIO
    if " " in nome_produto:
        print('Não se pode haver espaços entre as letras do nome do produto.\n')
        continue

    # VERIFICAR PARA ACEITAR SOMENTE LETRAS DO ALFABETO
    if not nome_produto.isalpha():
        print('Entrada de dados inválida, só pode ser string do tipo letras de alfabetos.')
        continue

    lista_nome_dos_produtos.append(nome_produto)

    while True:
        try:
            preço_produto = float(input('digite o preço R$ do produto:\n'))
            if preço_produto < 0:
                print('Entrada de dados inválida:\n')
                continue
            lista_preços_dos_produtos.append(preço_produto)
            break
        except ValueError:
            print('Entrada de dados inválida:\n')

    # perguntar ao usuário se vai querer continuar ou não
    while True:
        resp_usuario = input('Você quer continuar? (SIM ou NAO):\n').strip().upper()
        if resp_usuario not in ['SIM', 'S', 'N', 'NAO']:
            print('Entrada de dados inválida, tente novamente\n')
            continue
        if resp_usuario in ['SIM', 'S']:
            break  # volta ao loop principal para cadastrar outro produto
        else:
           break              
    if resp_usuario in ['N','NAO']:
        break


# calcular resultados apenas após o usuário decidir encerrar


totalidade_do_valor_preco_dos_produtos = sum(lista_preços_dos_produtos)

# B) QUANTOS PRODUTOS CUSTAM MAIS DE 1K
for preco in lista_preços_dos_produtos:
    if preco > 1000:
        contador += 1

# C) QUAL É O NOME DO PRODUTO MAIS BARATO?
menor_preco = min(lista_preços_dos_produtos)
indice_do_menor_lista = lista_preços_dos_produtos.index(menor_preco)
nome_do_produto_mais_barato_da_lista = lista_nome_dos_produtos[indice_do_menor_lista]

# exibir resultados
print(f'O total do valor gasto na compra foi de: R${totalidade_do_valor_preco_dos_produtos:.2f}')
print(f'O total de elementos da lista que são maiores que 1k é correspondente a: {contador}')
print(f'O nome do produto mais barato dessa lista foi do preço: R${menor_preco}, que possui o nome: {nome_do_produto_mais_barato_da_lista}')
print('Programa encerrado.....\n')
