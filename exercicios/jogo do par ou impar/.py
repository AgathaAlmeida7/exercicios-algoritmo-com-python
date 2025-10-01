# programa que jogue par ou impar com o pc.
# o jogo so sera interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo

import random

lista_par = ["PAR"]
lista_impar = ["IMPAR"]
contador = 0

# Escolha do usuário: PAR ou IMPAR
while True:
    usuario_resp = input('Você quer ser IMPAR ou PAR no jogo:\n').strip().upper()
    if " " in usuario_resp:
        print('Não pode haver espaços entre as letras da palavra:\n')
        continue
    if usuario_resp not in ["IMPAR", "PAR"]:
        print('Entrada de resposta inválida:\n')
        continue
    else:
        break

print(f"Você escolheu {usuario_resp}, então o PC será o oposto!\n")

# LOOP DO JOGO
while True:
    # Pegar número do usuário
    while True:
        try:
            numero_usuario = int(input('Digite um número inteiro:\n'))
            break
        except ValueError:
            print('Entrada de dados inválida:\n')

    # Número do PC
    pc = random.randint(0, 10)

    resultado_dos_numeros_jogados = numero_usuario + pc

    # Determinar se o resultado deu PAR ou IMPAR
    if resultado_dos_numeros_jogados % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "IMPAR"

    # Mostrar jogada
    print(f"\nVocê jogou {numero_usuario}, o PC jogou {pc}.")
    print(f"Total = {resultado_dos_numeros_jogados} → {resultado}\n")

    # Verificar vitória ou derrota
    if usuario_resp == resultado:
        print("Você venceu esta rodada!\n")
        contador += 1
    else:
        print("Você perdeu!")
        print(f"Vitórias consecutivas: {contador}")
        break
