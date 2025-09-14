#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
#como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
#pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    """
    realiza a análise de ano atual e de nascimento de uma pessoal e retorna se ele deve votar ou não
    :param ano: ano de nascimento
    :return: se o voto é obrigatório, opcional ou negado
    """
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Sua idade é {idade}, não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Sua idade é {idade}: VOTO OPCIONAL'
    else:
        return f'Sua idade é {idade}: VOTO OBRGATÓRIO'


print('=-='*10)
nome = str(input('Nome: '))
ano_nasc = int(input('ano de nascimento: '))
print(f'Olá, {nome}')
print(f'{voto(ano_nasc)}')