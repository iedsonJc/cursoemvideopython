#Aprovado ou não
print('==='*6,'Aprovado ou Reprovado?','==='*6)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = ((n1 + n2 + n3) / 3)
print('Sua media é {:.1f}'.format(media))
if media < 5:
    print('\033[1:31m','Reprovado','\033[m')
elif media >= 7:
    print('\033[1:32m','Aprovado','\033[m')
elif 5 <= media < 7:
    print('\033[1:34m','Recuperação','\033[m')
print('==='*6,'FIM','==='*6)