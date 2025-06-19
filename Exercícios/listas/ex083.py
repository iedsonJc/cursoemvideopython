#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
# deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
print('-=-'*20)
print('TESTE DE ESPRESSÕES')
exp = str(input('Digite a espressão: '))
pilha = []
for simb in exp:
    if simb == '(':   #quando se achar '(' dentro da expressão se acrescenta '(' na prilha.
        pilha.append('(')
    elif simb == ')':   #quando se achar ')' dentro da expressão
        if len(pilha) > 0:  #se a quantidade de caracteres da pilha é maior que 0
            pilha.pop()   #se remove o ultimo caractere da pilha
        else:    #sea quantidade da caracteres da pilhas é menor que 0
            pilha.append(')') #se acrescenta o caractere ')'
            break
if len(pilha) == 0: #se a quantitade de caracteres dentro da pilha for igual a 0
    print('Expressão valida!')
else:
    print('Expressão invalida!')