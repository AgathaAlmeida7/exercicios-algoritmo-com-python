print('DESCUBRA O SEU IMC, E VEJA EM QUAL CATEGORIA VOCE ESTÁ:\n\n')

peso=float(input('digite quanto voce tem de peso(KG);\n'))
altura=float(input('digite quanto voce tem de altura (metro):\n'))


imc=peso/ (altura**altura)

if imc<18.5:
    print('o seu peso é {:.2f} e a sua altura é {:.2f} resultando no imc = {}, consequentemente, voce está (ABAIXO DO PESO)'.format(peso,altura,imc))
elif imc>18.5 and imc<=24.9:
   print('o seu peso é {:.2f} e a sua altura é {:.2f} resultando no imc = {}, consequentemente, voce está (PESO NORMAL)'.format(peso,altura,imc))
elif imc>25 and imc<=29.9:
    print('o seu peso é {:.2f} e a sua altura é {:.2f} resultando no imc = {}, consequentemente, voce está (SOBREPESO)'.format(peso,altura,imc))
elif imc>30 and imc<=34.9:
     print('o seu peso é {:.2f} e a sua altura é {:.2f} resultando no imc = {}, consequentemente, voce está (OBESIDADE GRAU 1)'.format(peso,altura,imc))
elif imc>35 and imc<=39.9:
    print('o seu peso é {:.2f} e a sua altura é {:.2f} resultando no imc = {}, consequentemente, voce está (OBESIDADE GRAU 2)'.format(peso,altura,imc))
else:
    print('o seu peso é {:.2f} e a sua altura é {:.2f} resultando no imc = {}, consequentemente, voce está (OBESIDADE GRAU 3)'.format(peso,altura,imc))