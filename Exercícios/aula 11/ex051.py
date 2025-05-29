#Progreção Aritmetica
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('          PA')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = p + (10 - 1) * r
for c in range(p, decimo, r):
    print(c, end='-> ')
print('Acabou')