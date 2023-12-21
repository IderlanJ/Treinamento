import random

players = ['Bob','Beater','Aphelian','Nono','Rhyan','Indra','Siix','Zangado','Chacal','Look','Muca']
sorteados = []

while len(sorteados) < 5 and players:
    sorteado = random.choice(players)
    sorteados.append(sorteado)
    players.remove(sorteado)

print('Os nomes sorteados foram:', sorteados)





