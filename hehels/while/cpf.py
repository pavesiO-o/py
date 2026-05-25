from random import randint


cpf = input("Informe o cpf: ")

contador1 = 10
soma1 = 0
contador2 = 11
soma2 = 0

for i in range(9):
    soma1 += int(cpf[i]) * contador1
    contador1 -= 1

for i in range(10):
    soma2 += int(cpf[i]) * contador2
    contador2 -= 1

modulo1 = 11 - (soma1 % 11)
modulo2 = 11 - (soma2 % 11)

if modulo1 > 9:
    modulo1 = 0

if modulo2 > 9:
    modulo2 = 0

if int(cpf[9]) == modulo1 and int(cpf[10]) == modulo2:
    print("cpf válido")
else:
    print("cpf invalido")

if cpf[8] == '1':
    print ('ESTADO: DF, GO, MT, MS ou TO')

if cpf[8] == '0':
    print ('ESTADO: RS')

if cpf[8] == '2':
    print ('ESTADO: PA, AM, AC, AP, RO ou RR')

if cpf[8] == '3':
    print ('ESTADO: CE, MA ou PI')

if cpf[8] == '4':
    print ('ESTADO: PE, RN, PB ou AL')

if cpf[8] == '5':
    print ('ESTADO: BA, SE')

if cpf[8] == '6':
    print ('ESTADO: MG')

if cpf[8] == '7':
    print ('ESTADO: RJ ou ES')

if cpf[8] == '8':
    print ('ESTADO: SP')

if cpf[8] == '9':
    print ('ESTADO: SC')

