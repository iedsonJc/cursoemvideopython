#Escreva um programa que faça o computador pensar em um número de 0 a 5 e peça para o usuário
# tentar dscobrir qual foi o número escolhido pelo computador, o programa devera mostrar se o usuário acertou ou não
from random import randint
print('-=-' * 6,'tente a sorte','-=-' * 6)
esc = int(input('Tente acertar  escolha um número de 0 a 5: '))
sort = randint(0,5)
print('O computador escolheu {}'.format(sort))
if esc == sort:
    print('Parabéns você acertou! ')
else:
    print('Que pena você errou!')