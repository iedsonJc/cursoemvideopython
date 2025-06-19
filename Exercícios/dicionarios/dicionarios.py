#   DICIONÁRIOS
dados = dict()
#    OU
# dados = {}

#adiciona dados
dados['nome'] = 'Iêdson'
dados['idade'] = 28
dados['sexo'] = 'M'
print(dados)

#remover dados
del dados['sexo']


#valor, cahave e item
filme = {'titulo':'Star wars',
         'ano':1977,
         'diretor':'George lucas'
        }

print(filme.values()) #mostra os valores
print(filme.keys()) #mostra as chaves
print(filme.items()) #mosta os itens
print(f'O {dados["nome"]} tem {dados["idade"]} anos')

for k,v in filme.items(): #O "k" é a chave, "v" valor
    print(f'O {k} é {v}')
for v in filme.values():#valor
    print(v)
for k in filme.keys():#cahves
    print(k)
for i in filme.items():#itens
    print(i)

locadoura = {'titulo':'Star wars',
             'ano':1977,
             'diretor':'George lucas',
             'titulo':'Avengers',
             'ano':2012,
              'diretor':'Joss Whedon'
            }
print(locadoura[0]['ano'])
print(locadoura[1]['titulo'])

#adicionando dicionários dentro de listas
brasil = []
estado1 = {'uf':'Perambuco','sigla':'PE'}
estado2 = {'uf':'Paraiba','sigla':'PR'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

estado = dict()
Brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Ferativa: '))
    estado['aigla'] = str(input('Sigla do Estado: '))
    Brasil.append(estado.copy())
for e in brasil: #laaço da lista
    for v in e.values(): #laço do dicionário
        print(v, end= ' ')
print()

#dicionario vazio = sorted(dicionário.items() ,key=itemgetter(1), reverse=True)