#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
#média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
#quer ou não continuar a digitar valores.
print('-=-'*5,'OPERÕES','-=-'*5)
resp = 'S'
media = soma = quant =  maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite o valor: '))
    soma += num
    quant += 1
    if quant == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()
media = soma / quant
print('Foram lidos {} com a media de {} e o menor é {} e o maior é {}.'.format(quant, media, menor, maior))
print('=-='*20)

