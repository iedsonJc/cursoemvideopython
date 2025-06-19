print('-=-=-=-=-=IJCSERV-=-=-=-=-=-')
valcompra = prod1000 = prodmp = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço do produto: R$ '))
    valcompra += preço
    cont += 1
    if preço > 1000:
        prod1000 += 1
    if cont == 1 or preço < prodmp:
        prodmp = preço
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f"""O total de produtos {cont} 
Valor da compra : {valcompra}
Produtos com preço maior que R$1000: {prod1000}
Produto mais parato foi {barato}: {prodmp}""")
