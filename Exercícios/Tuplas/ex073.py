times = ('Flamengo','Cruzeiro','Bragantino','Palmeiras','Fluminense',
         'Botafogo','Bahia','Mirassol','Atlético-MG','Ceará SC','Corinthians',
         'Grêmio','São Paulo','Internacional','Vasco da Gama','EC Vitória',
         'Fortaleza','Santos','Juventude','Sport Recife')
print('-=-'*15)
print(f'Lista de time do Brasileirão {times}')
print('-=-'*15)
print(f'OS 5 primeiros colocados: {times[0:5]}')
print('-=-'*15)
print(f'Os 4 ultimos colocados: {times[-4:]}')
print('-=-'*15)
print(f'Os times em ordem alfabetica:{sorted(times)}')
print(f'O Sport Recife esta na {times.index('Sport Recife')+1}ª posição')
