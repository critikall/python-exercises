# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time do Vasco da Gama).

tabela = ('São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo', 'Grêmio',
          'Palmeiras', 'Fluminense', 'Santos', 'Ceará SC', 'Corinthians',
          'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Sport Recife',
          'Vasco da Gama', 'Fortaleza', 'Bahia', 'Goiás', 'Botafogo',
          'Coritiba')

print(f'''Os 5 primeiros colocados: {tabela[0:5]}
Os 4 últimos são: {tabela[-4:]}
Times em ordem alfabética: {sorted(tabela)}
O Vasco está na {tabela.index('Vasco da Gama')+1}ª posição''')
