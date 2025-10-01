# desenvoolver uma logica que ler opeso e a altura de uma pessoa,calcule seu imc e mostre seu status e mostre seu status ,de acordo com a tabela a baixo:

#abaixo de 18.5 : abaixo do peso
#entre 18.5 e 25: peso ideal
#25 ate 30 :sobrepeso
#30 ate 40;obesidade
#acima de 40 : obesidade morbida


kg=float(input('digite quanto de (kg)voce possue:\n'))
altura=float(input('digite quanto de (altura) você possue:\n'))


imc=kg/(altura**2)
#Em Python, o operador ** é utilizado para representar exponenciação, ou seja, ele eleva um número a uma potência.

if imc<18.5:
    print('seu imc é {} com isso voce se encontra: (ABAIXO DO PESO)'.format(imc))
elif imc>=18.5 and imc<=24.9:
    print('seu imc  é {} com isso voce se encontra: (PESO NORMAL)'.format(imc))
elif imc>=25.0 and imc<=29.9:
    print('seu imc é {} com isso voce se encontra : (SOBREPESO)'.format(imc))
elif imc>=30.0 and imc<=34.9:
    print('seu imc é {} com isso voce se encontra: (OBESIDADE GRAU 1)'.format(imc))
elif imc>=35.0 and imc<=39.9:
    print('seu imc é {} com isso voce se encontra: (OBESIDADE GRAU 2)'.format(imc))
else:
    print('seu imc é {} com isso voce se encontra: (OBESIDADE 3, MORBIDA)'.format(imc))