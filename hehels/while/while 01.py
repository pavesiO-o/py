# numero = 1
# while numero <=10:
#     print(numero)
#     numero += 1

# criar um algoritimo que recebe varios numeros e só para quando a soma deles for maior que 100

soma = 0
while True:
    numero = int(input('digita um numero: '))
    soma += numero
    if soma == 50 or soma > 100:
        break
print('o seu numero ficou:', soma)