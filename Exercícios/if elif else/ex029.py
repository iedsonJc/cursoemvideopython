#Faça um programa que mede a felocidade de um carro, onde se o carro passar de 80km sera multado em
# R$7 reias para cada km acima dos 80km
print('-=-' * 11)
vel = float(input('Qual a velocidade do carro? '))
prec = (vel - 80)*7
if vel > 80:
    print('Sua velocidade foi de {}km/h'.format(vel))
    print('Você excedeu o limite da via, sera multado em R$7 reias por cada km acima de 80km')
    print('O valor da sua multa é de R${:.2f}'.format(prec))
else:
    print('Sua velocidade foi  de {}km/h'.format(vel))
    print('Você não sera multado')
    print('Continue assim')
print('===========Bom dia!!===========')