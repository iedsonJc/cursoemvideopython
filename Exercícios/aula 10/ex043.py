#Calculo de imc]
print('==='*6,'IMC','==='*6)
peso = float(input('Peso Kg: '))
alutra = float(input('Altura m: '))
imc = peso / (alutra ** 2)
print('Seu Imc: {:.2f}'.format(imc))
if imc < 18.5 :
    print('\033[1::46mAbaixo do peso!\033[m')
elif 18.5 <= imc < 25:
    print('\033[1::42mPeso ideal!\033[m')
elif 25 <= imc < 30:
    print('\033[1::45mSobrepeso!\033[m')
elif 30 <= imc < 40:
    print('\033[1::43mObesidade!\033[m')
else:
    print('\033[1::41mObseidade morbida\033[m')