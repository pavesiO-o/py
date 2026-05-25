# crie um algoritimo que controle as movimentações de bolsas de sangue
# o programa deve ter as seguintes opções
#
# - doar sangue (define qual tipo e acrescente 1 unidade)
# - retirar sangue (define qual tipo e retira multiplos de 5 unidades)
# - visualizar saldo de bolsas
# - consultar movimentações de estoque

tipos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', '0+', '0-']
saldos = [10, 10, 10, 10, 10, 10, 10, 10]

while True:
    fazer = input('''oque deseja fazer?
    [1] doar sangue
    [2] pegar sangue
    [3] saldo de bolsas
    [4] sair''')
    if fazer == '1':
        tipo = input('qual seu tipo sanguineo? ').upper()
        quantidade = int(input('quantas bolsas desejadas?'))
        if tipo == 'A+':
            saldos [0] += quantidade
        elif tipo == 'A-':
            saldos [1] += quantidade
        elif tipo == 'B+':
            saldos [2] += quantidade
        elif tipo == 'B-':
            saldos [3] += quantidade
        elif tipo == 'AB+':
            saldos [4] += quantidade
        elif tipo == 'AB-':
            saldos [5] += quantidade
        elif tipo == 'O+':
            saldos [6] += quantidade
        elif tipo == '0-':
            saldos [7] += quantidade
    elif fazer == '2':
        retirada = input('qual seu tipo sanguineo? ').upper()
        quantidade = int(input('quantas bolsas desejadas?(multiplos de 5)'))
        if quantidade % 5 != 0:
            print ('numero invalido')
        else:
            if retirada == 'A+':
                saldos[1] -= quantidade
            elif retirada == 'A-':
                saldos[2] -= quantidade
            elif retirada == 'B+':
                saldos[3] -= quantidade
            elif retirada == 'B-':
                saldos[4] -= quantidade
            elif retirada == 'AB+':
                saldos[5] -= quantidade
            elif retirada == 'AB-':
                saldos[6] -= quantidade
            elif retirada == 'O+':
                saldos[7] -= quantidade
            elif retirada == '0-':
                saldos[8] -= quantidade
    elif fazer == '3':
        print (f'A+:{saldos[0]} A-:{saldos[1]} B+:{saldos[2]} B-:{saldos[3]} AB+:{saldos[4]} AB-:{saldos[5]} O+:{saldos[6]} O-:{saldos[7]}')
    else:
        break
