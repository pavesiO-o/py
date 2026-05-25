# crie um algoritimo que recebe 10 numeros e retorna
# a soma entre eles
# a media aritimetica simples
# quantos eram pares
# quantos eram impares
# quantos zeros
# maior valor
# menor valor



impar, zeros, par, soma, negativo, positivo = 0


for i in range(10):
    if i == 0:
        numero = int(input('digita um numero ai: '))
        maior = numero
        menor = numero

    else:
        numero = int(input('digita um numero ai: '))
        soma += numero

        if numero >= maior:
            maior = numero

        if numero <= menor:
            menor = numero

        if numero % 2 == 0:
            par +=  1
        else:
            impar += 1

        if numero > 0:
            positivo += 1
        elif numero < 0:
            negativo += 1
        else:
            zeros += 1

print('soma',soma)
print('media', soma/10)
print('tem isso de numero par:', par)
print('tem isso de numero impar:', impar)
print ('tem isso de zero:',zeros)
print ('o maior numero foi', maior)
print ('o menor foi', menor)


