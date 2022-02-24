from time import sleep
time = list()
dadosjogador = dict()
partidas = list()
while True:
    dadosjogador.clear()
    dadosjogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input('Quantas partidas ele jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols ele fez na {c+1} partida: ')))
    dadosjogador['gols'] = partidas[:]
    dadosjogador['total'] = sum(partidas)
    time.append(dadosjogador.copy())
    while True:
        sair = str(input('Deseja continuar? S/N ')).upper().strip()[0]
        if sair in 'SN':
            break
        print('ERRO. Digite apenas S ou N.')
    if 'N' in sair:
        break
print()
print(f'cod  ', end='')
for i in dadosjogador.keys():
    print(f'{i:<20}', end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-' * 50)
while True:
    opc = int(input('Deseja ver as estátisticas de qual jogador? [999] para parar: '))
    if opc == 999:
        print('FINALIZANDO ...')
        sleep(1)
        break
    if opc >= len(time):
        print(f'ERRO. Não existe jogador com o código {opc}.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR > {time[opc]["nome"]}:')
        for i, g in enumerate(time[opc]['gols']):
            print(f'    Na {i + 1}° partida ele fez {g} gols.')
    print('-' * 40)
print('>> VOLTE SEMPRE! <<')
