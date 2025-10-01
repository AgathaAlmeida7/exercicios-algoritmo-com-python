from datetime import date

cont = 1
while cont <= 5:
    try:
        anonascimento = int(input(f'Digite o ano do seu nascimento da pessoa {cont}:\n'))
        anoatual = date.today().year
        categoria = anoatual - anonascimento

        if categoria <= 9:
            print(f'Você tem {categoria} anos e se enquadra nos (MIRINS).')
        elif categoria <= 14:
            print(f'Você tem {categoria} anos e se enquadra nos (INFANTIL).')
        elif categoria <= 19:
            print(f'Você tem {categoria} anos e se enquadra nos (JUNIOR).')
        elif categoria <= 20:
            print(f'Você tem {categoria} anos e se enquadra nos (SÊNIOR).')
        else:
            print(f'Você tem {categoria} anos e se enquadra nos (MASTER).')

        cont += 1

    except ValueError:
        print('Erro: Digite um ano válido!')
