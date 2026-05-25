# crie um algoritimo que:
# solicita quantos numeros que armazenar
# solicita os numeros que serao armazenados
# exibe todos ao final
lista = []

inputs = int(input('quantos numeros tu quer digitar?: '))

for i in range (inputs):
    numeros = int(input('digite um numero: '))
    lista.append(numeros)
print (f'total: {sum(lista)}')
print (f'maximo: {max(lista)}')
print (f'minimo: {min(lista)}')
print (f'media: {sum(lista)/len(lista)}')