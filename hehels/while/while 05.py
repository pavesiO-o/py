from random import randint

numeropc = randint(1,100)

while True:
    numero = int(input('de um palpite de numero'))
    if numero == numeropc:
        print('vc acertou o numero!!!')
        break
    elif numero < numeropc:
        print('o numero é maior que o seu palpite')
    else:
        print('o numero é menor que o seu palpite')
print('o numero era:', numeropc)