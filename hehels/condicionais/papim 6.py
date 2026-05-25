# criar um programa que recebe 4 numero de notas
# o numero totald de aulas e o numero de preseças
# o programa deve calcular a media e a frequencia
# e apos isso informar se foi aprovado e reprovado

nota1 = float(input('digite a nota1: '))
nota2 = float(input('digite a nota2: '))
nota3 = float(input('digite a nota3: '))
nota4 = float(input('digite a nota4: '))
aulas = int(input('digite o numero de aulas: '))
presenca = int(input('digite o numero de aulas que foram participadas: '))
media = (nota1+nota2+nota3+nota4)/4
freq = (presenca/aulas)

if media>=6 and freq>=0.75:
    print('aprovado')
else:
    print('reprovado')