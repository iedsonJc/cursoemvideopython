#Desenvolva um programa que pergunte a distacia de em km de uma viagem, se km for ate 200km sera cobrado R$0,50 por km
#e R$0,49 se for acima de 200 km
print('====='*20)
km = float(input('Qual a distacia da viagem em km? '))
print('Sua viagem sera de {} km'.format(km))
if km <= 200:
    print('O preço da sua viagem sera de R${}'.format(km*0.50))
else:
    print('O valor da sua viagem sera de R${}'.format(km*0.45))