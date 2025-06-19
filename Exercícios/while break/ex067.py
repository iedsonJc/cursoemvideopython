#Exercício Python 67: Faça um programa que mostre a tabuada de
# vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o
# número solicitado for negativo.
print('-=-=-=-=-=Tabuada-=-=-=-=-=-=')

while True:
    num = int(input('Qual número você quer vê a tabuada: '))
    print('-=-' * 13)
    if num < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{c} x {num} = {c*num}')
    print('-=-' * 13)
print('Tabuada encerrou, volte sempre!')
print('=-=-=-=-=-=-=-=--=Fim-=-==-=-=--=-=-=-=-=')

