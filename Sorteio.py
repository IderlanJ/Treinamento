import random

players = ['Bob', 'Beater', 'Aphelian', 'Nono', 'Rhyan', 'Indra', 'Siix', 'Zangado', 'Chacal', 'Look', 'Muca', 'Kauan','Noelle','Carlos','Luis','Iderlan','Rafael','Lucas','Luciana','Marcos']

# Verifica se há pelo menos 5 jogadores na lista
if len(players) >= 5:
    random.shuffle(players)  # Embaralha a lista original

    num_lists = len(players) // 5  # Número de listas de 5 jogadores
    rest = len(players) % 5  # Quantidade de jogadores restantes

    for i in range(num_lists):
        start = i * 5
        end = start + 5
        sorted_players = players[start:end]
        print(f'Time {i + 1}:', sorted_players)

    if rest > 0:
        print(f'Jogadores restantes: {players[-rest:]}')
else:
    print('Não há jogadores suficientes para fazer o sorteio.')



