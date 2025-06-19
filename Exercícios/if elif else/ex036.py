#Programa para aprovação de emprestimo
from time import sleep
print('==='*10,'Emprestimo','==='*10)
print('Preencha os dados:')
nome = str(input('Digite o nome do comprador: '))
valc = float(input('Digite o valor da casa:R$'))
sal = float(input('Digite o seu salario:R$'))
anos = int(input('Digite parcelas deseja pagar: '))
prestacao = valc / (anos * 12)
minimo = sal * 30 / 100
print('=== '*7,'Resultado','==='*10)
print('Processando......')
print('Nome do comprador: {}'.format(nome))
print('Valor da casa: R${:.2f}'.format(valc))
print('Parcelas mini a pagar: {}'.format(minimo))
print('Quantidade de parcelas:R${:.2f}'.format(prestacao))
sleep(2)
if prestacao <= minimo:
    print('O valor da {:.2f} não excede 30% do seu salario'.format(prestacao))
    print('Emprestimo ','\033[1:32m','aprovado!')
else:
    print('O valor da parcela é de {:.2f} excede 30% do seu salario'.format(prestacao))
    print('Emprestimo','\033[1:31m','negado!')

