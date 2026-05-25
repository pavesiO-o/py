
from random import randint

cabecalho = r'''
  _                              ,-==.                       
 `-)   .-.                    ||  (  (\                 .-.  
 _/,' _|_ \ .-===-., ....     ||   |\.\\           __  _|_ \ 
(___) (_)   `.___.'  `=.`''===.'  _]_]`\\ ^^^^^^^ |__| (_)    
(jokempo em hieroglifo)'''
menu = '''
Escolha sua opção
[1]pedra
[2]papel
[3]tesoura
escolha:'''
# 1 pedra
# 2 papel
# 3 tesoura

print(cabecalho)
opcao = int(input(menu))
valor = randint(1,3)


if 1<= opcao <= 3:
    print('jogada valida')
    if opcao == valor:
        print ('empate')
    elif valor == 1 and opcao == 2 or valor == 2 and opcao == 3 or valor == 3 and opcao == 1:
        print('jogador ganhou')
    else:
        print('computador ganhou')
    if opcao == 1:
        print('voce escolheu pedra')
    elif opcao == 2:
        print('voce escolheu papel')
    elif opcao == 3:
        print('voce escolheu tesoura')

    if valor == 1:
        print('computador escolheu pedra')
    elif valor == 2:
        print('computador escolheu papel')
    elif valor == 3:
        print('computador escolheu tesoura')
else:
    ('jogada invalida')
