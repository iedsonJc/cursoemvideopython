#faça um programa que leia 3 números e diga qual o maior e o menor número
print('===='*10)
n1 = float(input('Digite primeiro número: '))
n2 = float(input('Digite segundo número: '))
n3 = float(input('Digite terceiro número: '))
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
print('O número maior é {}'.format(maior))
print('O número menor é {}'.format(menor))