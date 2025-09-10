#programa que ler duas notas de um aluno e calcula sua media,mostrando uma msg no final de acordo com a media atinginda.

#- a baico de 5,reprovado
#media entre 5 e 6.9,recuperação
#media 7 ou superior,aprovado


nota01=float(input('digite a sua primeira nota:\n'))
nota02=float(input('digite a sua segunda nota:\n'))

media=(nota01+nota02)/2

if media<5:
    print('voce tirou {},voce esta: (REPROVADO(A))'.format(media))
elif media>=5 and media<=6.9:
    print('sua nota foi: {}, voce esta de (RECUPERAÇÃO)'.format(media))
else:
    print('sua nota foi{},voce esta (APROVADO(A))'.format(media))