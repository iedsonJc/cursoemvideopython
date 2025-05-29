#comparador de númeos
print("==="*7,'Comparador de números inteiros','==='*7)
n1 = int(input('Digite o primeiro valor número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
else:
    print('Não existe número maior, os números são iguais!')
