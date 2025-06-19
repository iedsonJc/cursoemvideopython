n = 1
pares = impares = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0 :
           pares += 1
        else:
            impares += 1
print('Você digitou {} números pares e {} impares'.format(pares, impares))