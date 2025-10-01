#programa queler dois numeros inteiros e compare-os,mostrando uma msg na tela.

#O primeiro valor é MAIOR
#O segundo valor é  MAIOR
#nao existe valormaior,os dois sao iguais

n1=int(input('digite um numero:\n'))
n2=int(input('digite outro numero:\n'))

if n1>n2:
    print('o numero {} ele é MAIOR que o numero {}'.format(n1,n2))
elif n2>n1:
    print('o numero {} ele é MAIOR  que o numero {}'. format(n2,n1))
else:
    print('nao existe  valor maior,ambos sao iguais {} {}'.format(n1,n2))