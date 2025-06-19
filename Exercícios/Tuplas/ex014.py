lanches = ('Hambuguer','Pizza','Cachorro-Quente')
for comida in lanches:
   print(f'Quero comer {comida}')
print('Comida acabou!')
print('----------------------------')
for comida in range(0, len(lanches)):
    print(f'Quero comer {lanches[comida]}!')
print('Comida Acabou!')
print('-----------------------')
for pos, comida in enumerate(lanches):
    print(f'Quero comer {comida}: {pos}')
print('Comida Acabou!')
print('-----------------=-----------------')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)