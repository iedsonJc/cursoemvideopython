#faça um programa que leia 3 números e diga qual o maior e o menor número
print('===='*10)
n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
n3 = int(input('Digite terceiro número: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O número maior é {}'.format(maior))
print('O número menor é {}'.format(menor))