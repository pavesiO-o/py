# cria um algoritimo q recebe 3 lados de jm triangulo e classifica entre
# aisoceles = 2 lados iguais
# escaleno = 3 lados diferentes
# equilatero = 3 lados iguais
# nao triangulo = 1 lado > q a some de 2 lados

lado1 = int(input('digite o tamanho do lado:'))
lado2 = int(input('digite o tamanho do lado:'))
lado3 = int(input('digite o tamanho do lado:'))

if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado2 + lado1:
    print('nao é um triangulo')
elif lado1 == lado2 and lado2 == lado3:
    print('triangulo equilatero')
elif lado1 != lado2 and lado1 != lado3:
    print('triangulo isoceles')
else:
    print('triangulo escaleno')