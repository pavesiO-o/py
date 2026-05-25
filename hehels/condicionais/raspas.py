nome1 = len(input('degite um nome: '))
nome2 = len(input('degite um nome: '))
nome3 = len(input('degite um nome: '))
nome4 = len(input('degite um nome: '))
media = nome1+nome2+nome3+nome4

if media>7:
    print('q nome grande')
elif media>5:
    print('q nome medio')
else:
    print('q nome pequeno')
print('a media de caracteres foi' media)