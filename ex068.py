from random import randint
print('=' * 30)
print('    JOGO DO PAR OU ÍMPAR')
print('=' * 30)
cont = 0
while True:
    player = int(input('Digite um valor: '))
    escolha = str(input('Você quer PAR OU ÍMPAR [P/I]: ')).strip()
    computador = randint(1, 10)
    soma = computador + player
    if soma % 2 == 0 and escolha in 'Pp':
        print(f'Você jogou {player} e o computador {computador}. O total é {soma} que é PAR!')
        print('Você ganhou.')
        cont += 1
        print('=' * 30)
        print('    Vamos jogar novamente.')
        print('=' * 30)
    elif soma % 2 != 0 and escolha in 'Ii':
        print(f'Você jogou {player} e o computador {computador}. O total é {soma} que é ÍMPAR!')
        print('Você ganhou.')
        cont += 1
        print('=' * 30)
        print('    Vamos jogar novamente.')
        print('=' * 30)
    elif soma % 2 == 0 and escolha in 'Ii':
        print(f'Você jogou {player} e o computador {computador}. O total é {soma} que é PAR!')
        print('GAMER OVER.')
        print('=' * 30)
        break
    elif soma % 2 != 0 and escolha in 'Pp':
        print(f'Você jogou {player} e o computador {computador}. O total é {soma} que é ÍMPAR!')
        print('GAME OVER.')
        print('=' * 30)
        break

print(f'Fim de jogo. Você ganhou {cont} vezes.')
print('=' * 30)
