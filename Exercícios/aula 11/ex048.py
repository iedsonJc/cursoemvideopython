print('===SOMA de Impares NÚMEROS MUTILPLOS DE 3====')
cont = 0
soma = 0
print('Essa é a soma entre números multiplos de 3 entre 1 e 500:')
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valor solicitados é {}'.format(cont, soma))
print('=======FIM======')