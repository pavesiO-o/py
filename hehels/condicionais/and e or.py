# nota = 7.5
# frequencia = 0.6
# if nota >= 7 and frequencia >=0.7:
#     print ('aprovado')

# crie um programa que retorna fizz ou buzz ou fizzbuzz
# quando  o numero é divisibel sem resto por 3:fizz
# quando  o numero é divisibel sem resto por 5: buzz
# quando  o numero é divisibel sem resto por 3 e 5:fizzbuzz

numero = int(input('Digite um numero: '))

if numero % 5 == 0 and numero % 3 == 0:
    print('fizzbuzz')
elif numero % 5 == 0:
    print('buzz')
elif numero % 3 == 0:
    print('fizz')
