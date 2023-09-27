# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Fortaleza.

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
         'Athetico-PR', 'Atletico-MG', 'Fortaleza', 'São Paulo', 'America-MG',
         'Botafogo', 'Santos', 'Goias', 'Bragantino', 'Coritiba', 'Cuiaba',
         'Ceara', 'Atletico-GO', 'Avai', 'Juventude')
print('-=-' * 12)
print(f'Lista de times do Brasileirão 2022: {times}')
print('-=-' * 12)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=-' * 12)
print(f'Os 4 últimos são {times[-4:]}')
print('-=-' * 12)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-' * 12)
print(f'O Fortaleza está na {times.index("Fortaleza") + 1}ª posição')
