#faca um programa que leia o salaraio de um funcionario e calcule o seu aumento
# sendo 10% para salarios a cima de R$1250 e de 15% para salarios inferiores
salario = float(input('Qual o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))