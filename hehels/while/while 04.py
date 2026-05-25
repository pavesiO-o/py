# crie um algoritimo que recebe varios nomes
# quantas letras
# ao final exibe quantas vogais e quantas consoantes foram digitadas
# para parar o usuario informa "parar"
vogais = 'aeiou'
vogaln = 0
consoante = 0
while True:
    nome = str(input('digite um nome: ')).lower()
    if nome == 'parar':
        break
    for letras in nome:
        if letras in vogais:
            vogaln += 1
        else:
            consoante += 1
print(f'''letras digitadas:{vogaln + consoante}
vogais digitadas:{vogaln}
consoantes digitadas:{consoante}''')