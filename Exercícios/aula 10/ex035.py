#face um programa que leia tres retas e diga se essas retas pode formar um triângulo
print('==='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo!')