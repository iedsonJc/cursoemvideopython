#Crie um programa que leia um número e diga se ele é impar ou par
num = int(input('Digite o número: '))
print('-=-' * 20)
par = num % 2
if par == 0:
    print('O número que você digitou é Par')
else:
    print('O número que você digitou é Impar')