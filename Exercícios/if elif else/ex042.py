#TIdentificando Triângulos
print('==='*6,'Identificando Triângulos','==='*6)
l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
print('Os lados do triângulos {} , {} e {}'.format(l1,l2,l3))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode formar um triângulo: \033[1:32mSim\033[m')
    if l1 == l2 == l3:
        print('Tipo: Triângulo Equilatero')
        print('O triângulo equilátero é um tipo de triângulo que possui os três lados congruentes')
    elif l1 != l2 != l3 != l1:
        print('Tipo: Triângulo Escaleno')
        print('Um triângulo escaleno é definido por ter todos os seus três lados com medidas diferentes')
    else:
        print('Tipo: Triângulo Isósceles')
        print('Triângulo isósceles é um polígono que apresenta três lados, sendo, pelo menos, dois deles congruentes.')
else:
    print('\033[1:31mOs valores não podem formar um triângulo\033[m')
