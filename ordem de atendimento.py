# Entrada do número de pacientes
n = int(input('pacientes: ').strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input('nome, iedade, status: ').strip().split(', ')
    idade = int(idade)

#: Ordene por prioridade: urgente > idosos > demais:
    if status == 'urgente':
        prioridade = (1, -idade)
    elif idade > 60:
        prioridade = (2, -idade)
    else:
        prioridade = (3, -idade)
    pacientes.append((prioridade, nome))
pacientes.sort()
# Exibir resultado final
print('Ordem de Atendimento:', end=' ')
print(', '.join(p[1] for p in pacientes))

