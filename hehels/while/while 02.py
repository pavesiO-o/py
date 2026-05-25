#crie um programa que recebe um numero indeterminado de valores
# ao final exibe qual foi o maior valor
# para parar o programa o usuario informa "sair"
voltas = 0
while True:
    numero = (input('digite um numero ou sair '))
    if numero.lower() == 'sair':
        break
    if contador == 0:
        maximo = int(valor)
        contador += 1
        continue
    if int(valor) > maximo:
        maximo = int(valor)
if contador > 0:
    print (maximo)
else:
    print ('nenhum numero colocado')
