#Exercício Python 076: Crie um programa que tenha uma tupla
#única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em
# forma tabular.
print('----'*20)
print(f'{"LISTA DE PREÇO":>40}')
print('----'*20)
listagem = ('GRAFITE', 8.70,
                    'GRAFITE', 16.00,
                    'PONTA GRAFITE', 7.50,
                    'PONTA GRAFITE', 7.68,
                    'PONTA GRAFITE', 4.66,
                    'LÁPIS PRETO', 0.77,
                    'LÁTEX UNIDADE',  2.90,
                    'PONTEIRA', 0.34,
                    'COLA BASTÃO', 3.90)
for pos in range(0, len(listagem)):
    if pos %  2 == 0:
        print(f'{listagem[pos]:.<60}',  end=' ')
    else:
        print(f'R${listagem[pos]:>.2f}')
print('---'*27)
