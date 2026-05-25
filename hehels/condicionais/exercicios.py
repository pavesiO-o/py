# crie um algoritimo que recebe uma temperatura e recebe a unidade atual,
# ele deve converter para a outra unidade,
# celcius ou farenheit

temperatura = float(input("digite a temperatura: "))
unidade = input('celcius ou farenheit F/C ').upper()
Farenheit = 'F'
Celcius = 'C'

if unidade == Farenheit:
    print('a temperatura em celcius é ', ((temperatura-32)*5)/9)
elif unidade == Celcius:
    print('a temperatura em celcius é ', (temperatura*1.8)+32)




