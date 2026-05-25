# crie um algoritimo que recebe o nome de uma pessoa e classifique
# começa com vogal
# começa com consoante
# inicio e fim iguais
# inicio e fim diferentes

nome = input('digite seu nome:').lower()
vogal = 'a' or 'e' or 'i' or 'o' or 'u'

if nome[0] == vogal:
    print ('seu nome começa com vogal')
else:
    print('seu nome começa com consoante')

if nome[0] == nome[-1]:
    print('a letra inicial e final sao iguais')
else:
    print('a letra inicial e a final sao diferentes')