# crie um algoritimo que recebe 5 nome, e ao final, retorna o mais comprito e os nomes que começão com vogal
lista = []

lista_vogais = []
vogais = 'aeiou'

for _ in range (5):
    nomes = input('digite seu nome')
    lista.append(nomes)
    if nomes[0] in vogais:
        lista_vogais.append(nomes)
maior_nome = len(max(lista, key=len))

nomes_grandes = []

for nomes in lista:
    if len(nomes) == (maior_nome):
        nomes_grandes.append(nomes)
print (f'maiores nomes:{nomes_grandes}')
print (f'nomes com vogais:{lista_vogais}')
