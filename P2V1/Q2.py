cont = 0
for i in range(8):
    timecasa = int(input('Placar do time da casa: '))
    timefora = int(input('Placar do time de fora: '))

    if timecasa > timefora:
        print('O time da casa pontuou 3 pontos.')
        cont += 3
        print(f'O time da casa está com {cont} pontos.')
    elif timefora > timecasa:
        print('O time da casa pontuou 0 pontos.')
        cont += 0
        print(f'O time da casa está com {cont} pontos.')
    elif timecasa == timefora:
        print('O time da casa pontuou 1 ponto.')
        cont += 1
        print(f'O time da casa está com {cont} pontos.')

print(f'A pontuação total foi igual a {cont}.')