#programa que ler o ano de nascimento de um joveme informe,de acordo com sua idade

#se ele AINDA VAI SE ALISTAR  ao serviço militar

#se É A HORA DE SE ALISTAR

#SE JA PASSOU DO TEMPO DO ALISTAMENTO

#esse programa tbm devera mostrar o tempo que falta ou que passou do prazo


anonascimento=int(input('qual é o seu ano de nascimento:\n'))
#2002
from datetime import date

atual=date.today().year

idade=atual



temposepassououfalta=int(idade-idadealistamento)

if idade<18:
    print('voce tem {} anos,logo ainda chegará a sua vez de se alistar,e falta exatamente{} anos de tempo para isso\n'.format(idade,temposepassououfalta))
elif idade==18:
    print('voce tem {}anos,ja ta na hora de se alistar, e falta  exatamente {} de tempo  para isso\n'.format(idade,temposepassououfalta))
else:
    print('voce tem {} anos,ja passou da hora, e passou exatamente {} anos do tempo de alistamento\n'.format(idade,temposepassououfalta))
