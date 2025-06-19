#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
# usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
# a soma entre eles (desconsiderando o flag).
print('-=-'*5,'SOMANDO NÚMEROS','-=-'*5)
print('Digite os valores a seres somados, sabendo que o valor 999 irar parar o programa')
num = cont = soma = 0
while num != 999:
    num = int(input('Digite o {} valor: '.format(cont)))
    if num < 999:
        soma += num
        cont += 1
print('A quantitade de números lido foi {}'.format(cont))
print('A soma entre eles é {}'.format(soma))