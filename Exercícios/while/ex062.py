#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print('=-=-='*10,'PA','=-=-='*10)
primeiro = int(input('Primiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('pausa')
    mais = int(input('Você quer mostar mais alguns termos? '))

print('Progreção finalizada com {} termos mostrados'.format(total))
print('-=-=-=-=Fim-=-=-=-=-=')