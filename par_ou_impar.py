from random import randint # importando randint para o computador sortear um numero inteiro
print('=' * 30)
print('    JOGO DO PAR OU ÍMPAR')
print('=' * 30)
cont = 0
while True: # loop que roda enquanto for verdadeiro 
    player = int(input('Digite um valor: '))
    escolha = str(input('Você quer PAR OU ÍMPAR [P/I]: ')).strip() # variavéis
    computador = randint(1, 10)
    soma = computador + player
    if soma % 2 == 0 and escolha in 'Pp': # se você ganhar o loop segue
        print(f'Você jogou {player} e o computador {computador}. O total é {soma} que é PAR!')
        print('Você ganhou.')
        cont += 1
        print('=' * 30)
        print('    Vamos jogar novamente.')
        print('=' * 30)
    elif soma % 2 != 0 and escolha in 'Ii': # mesma coisa acontece aqui, se ganhar o loop segue
        print(f'Você jogou {player} e o computador {computador}. O total é {soma} que é ÍMPAR!')
        print('Você ganhou.')
        cont += 1
        print('=' * 30)
        print('    Vamos jogar novamente.')
        print('=' * 30)
    elif soma % 2 == 0 and escolha in 'Ii': # aqui temos uma parada se você perder
        print(f'Você jogou {player} e o computador {computador}. O total é {soma} que é PAR!')
        print('GAMER OVER.')
        print('=' * 30)
        break # condição de parada, se o resto da divisão da soma for igual a 0 e a escolha do player for ímpar, o programa para.
    elif soma % 2 != 0 and escolha in 'Pp': # semelhante ao de cima, porém agora ao contrário.
        print(f'Você jogou {player} e o computador {computador}. O total é {soma} que é ÍMPAR!')
        print('GAME OVER.')
        print('=' * 30)
        break

print(f'Fim de jogo. Você ganhou {cont} vezes.')
print('=' * 30)
