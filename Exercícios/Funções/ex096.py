#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
#terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m²')

print('    Controle de Terreno')
print('-=-'*10)
l = float(input('Qual a lagura do terreno em metros: '))
c = float(input('Qual o comprimento do terreno em metros: '))

area(l, c)