from datetime import date
from time import sleep

print('-=-'*4,'Contagem Regreciva','-=-'*4)
ano = date.today().year
print('Contagem regreciva para {}'.format(ano))
for c in range(10,-1, -1):
    sleep(0.5)
    print(c,end=(' '))
print('\n🎇=====FELIZ ANO NOVO====🎇')
