#algoritmo que ler uma frase qualquer e diga se ele é um palindromo. desconsiderando espaços

#palavras que de frente para tras é a mesma coisa


#PELO QUE EU ENTENDI AQUI EU VOU TER QUE PEDIR UMA FRASE QUALQUER AO MEU USUARIO
#COM BASE NISSO, VALIDAR PARA QUE REALMENTE SEJA STRING, VALIDAR AQUELAS COISAS DE STRING, CONSIDERAR QUE VAI TER DETERMINADOS ESPAÇOS NO MEIO, E COM BASE NESSES ESPAÇOS VAO SER CONTADOS QUANTAS PALAVRAS TEM AQUELA DETERMINADA FRASE
#NESSA CONTAGEM VAI TER QUE TER UMA LOGICA QUE CONSIDERE A FRASE, ACHO QUE PRA ISSO VAI TER QUE TIRAR OU DESCONSIDERAR ESSES ESPAÇOS DO MEIO
#UM PALINDROMO, BASICAMENTE EU VOU PEGAR ESSA FRASE, E VOU EMBARALHAR ESSA FRASE, E NESSE RESULTADO DO EMBARALHO DA FRASE EU VOU COMPARAR SE É IGUAL A FRASE PADRAO,SE FOR É UM PALINDROMO, SE NAO NAO É UM PALINDDROMO


#EXISTE NO PYTHON ALGUMA FUNCAO DE STRING, OU ALGUMA FUNCAO PROPRIAMENTE DITA QUE PEGUE UM RESULTADE DE UMA VARIAVEL, NO CASO UMA FRASE DE UMA VARIAVEL E FAÇA COM QUE ELA VIRE O CONTRARIO? A FRASE FIQUE AO CONTRARIO?

#DESTRINCHANDO  A LOGICA DO CODIGO


#basicamente aqui lidamos com uma variavel de string,sequencia de caractere
#no python existe varias maneiras de se manipular uma string,uma delas e exatamente inverter essa string. transformando essa frase de tras para frente.

#isso ocorre pq no python uma string pode ser acessada como uma lista de caracteres, onde cada posicao passa por um indice. o conceito de fatiamento de string, vai me permitir extrair partes especificias da string, inclusive ordem inversa

while True:
    try:
        frase=input('digite uma frase:\n').strip().lower()
        #validar primeiro se ta vazio ou nao
        if len(frase)==0 or len(frase)<3:
            print('voce nao digitou de acordo com a quantidade que tem que possuir essa palavra:\n')
        elif  "  " in frase :
            print('nao se pode ter espaços mais de uma vez nas palavras da frase')
            continue
        #aqui vai entrar a validação para que reforce que o programa so tenha letras do alfabeto e espaços
        

    
            #para eu percorrer uma string e fazer determinados acessos de validações, eu terei que criar um loop em python
            #dentro de um loop é possivel chamar metodos de string para checar o tipo do caractere.isso vai permitir se aquela  frase vai se manter ou nao.
         
            
        #obs: metodo count() sempre vai precisar de um argumento para saber o que ele deve contar.o certo para esse caso aqui é a funcao len((nome da variavel que eu quero))
        #len()-> retorna quantos elementos existem  na string ou lista no total,independente do valor deles
        #ele nao se importa com quais letras aparecem,apenas conta a quantidade total de caracteres
        #count() será uma contagem especifica,conta quantas vezes um elemento ou substring especifica aparece
        #len()->tamanho especifico da string//lista
        #count()-> quantas vezes um elemento especifico aparece
        frase_limpa=""
        for c in frase:
            if c.isalpha():
                frase_limpa+=c




        frase_padrao=frase
        frase_inversao=frase_limpa[::-1]
#eu so preciso garantir que essa string é string de letras , n um numero ou caractere que vai se tornar uma string
        if frase_inversao==frase_padrao:
            print(f'a frase padrao é:{frase_padrao}\n e ela invertida fica:{frase_inversao}')
            print('(((É UM PALINDROMO)))!\n')
        else:
            print(f'a frase padrao é:{frase_padrao}\n e ela invertida fica:{frase_inversao}')
            print('(((NÃO é UM  PALINDROMO)))!\n')


        

        #verificar se todos os caracteres sao letras dessa variavel

        #tipo pode espaços no meio, ate pq frases tem espaços no meio, e a gente vai contato as palavras de uma frases pelos espaços que sao dados no meio

        #






        #validar que realmente é frase, letra de alfabeto,e nao caracteres,numeros que viraram string por causa do imput
        #e tambemm fazer uma validação para que 

        break
    except ValueError:
        print('entrada invalida')


