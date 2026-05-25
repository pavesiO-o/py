# crie um algoritimo que recebe um numero indeterminado de valores
# ao final diz quantos numeros eram positivos e quantos eram negativos
# para encenrrar o programa o usuario digita 0
positivo = 0
negativo = 0
while True:
    numero = int(input('digite um numero'))
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
    else:
        break
print(positivo,'positivos e ', negativo, 'negativos')