#Números Primos
print('-=-=-=-=Númeoros Primos-=-=-=-=-')
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1:32m',end='')
        tot += 1
    else:
        print('\033[1:34m',end='')
    print('{}'.format(c),end='')
print('\n\033[mO número {} é divisivel {} vezes.'.format(num,tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')