#programa para aprovar o emprestimo bancario para a compra de uma casa. o programa vai perguntar o valor da casa,o salario do comprador e em quantos anos ele vai pagar. 

#calcule o valor da prestação mensal,sabendo que ela não pode exceder 30% do salario ou entao o emprestimo sera negado 

valorbrutodacasa=float(input('digite o valor bruto da sua casa:\n'))
salariobrutodocomprador=float(input('digite o valor do seu salario bruto:\n'))
quantosanosirapagar=int(input('digite em quantos anos voce ira pagar:\n'))

#programa que vai me dizer combase nas condições se vai aprovar a compra dessa casa ou nao no emprestimo

prestacao=valorbrutodacasa/(quantosanosirapagar*12)

max=salariobrutodocomprador-(salariobrutodocomprador*30/100)

if prestacao<=max:
    print('a sua prestação ficara de:{:.2f}  atendendo o limite maximo que  é e uma prestação de:{:.2f} do valor de prestação que voce pode pagar, baseado no valor do seu salario que é de {:.2f} (O EMPRESTIMO ESTA APROVADO)'.format(prestacao,max,salariobrutodocomprador))
else:
    print('a sua prestação ficara de {:.2f} ultrapassando ao maximo {:.2f} do valor de prestacao que voce poderia pagar,baseado no valor do seu salario de {:.2f} (O EMPRESTIMO ESTA NEGADO)'.format(prestacao,max,salariobrutodocomprador))

#A IDEIA AQUI É NEGAR UMA PRESTAÇÃO DE EMPRESTIMO QUE ULTRAPASSE 30% DO  SALARIO BRUTO DO COMPRADOR

