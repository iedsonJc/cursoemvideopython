#valor de desconto
print('==='*6,'COMPRA','==='*6)
preco = float(input('Preço: '))
print("""Qual forma de pagamento?
[1]AVISTA Dinheiro/Cheque
[2]CARTÃO 1x com 5% de desconto
[3]Cartão 2x sem desconto
[4]Cartão 3x ou mais com 20x de Juros""")
escolha = int(input('Escolha: '))
if escolha == 1:
    print('Desconto de 10%')
    preco = preco - (10 / 100 * preco)
    print('Valor a ser pago com 10% de desconto R${}'.format(preco))
elif escolha == 2:
    print('Desconto de 5%')
    preco = preco - (5 / 100 * preco)
    print('Valor a ser pago com 5% de desconto: R${}'.format(preco))
elif escolha == 3:
    print('Percentoal normal')
    print('valor a ser pago é R${}'.format(preco))
elif escolha == 4:
    print('20% de juros')
    total = preco + (20 / 100 * preco)
    parcela = int(input('Quantas vezes: '))
    tolpar = total / parcela
    print('Você vai pagar {}x de R${}'.format(parcela,tolpar))
    print('Valor a ser pago no final com 20% de juros: R${}'.format(total))
print("======Volte sempre====")