
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = ((n1 + n2 + n3) / 3)
print('Sua media é {:.2f}'.format(media))
if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')