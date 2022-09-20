'''
Assignment: Tic-Tac-Toe.py
Author: Paul McBride
'''
print()

def who_won(game, user):
    winner = ''
    if game[0] == user and game[1] == user and game[2] == user:
        winner = 'win'
    elif game[3] == user and game[4] == user and game[5] == user:
        winner = 'win'
    elif game[6] == user and game[7] == user and game[8] == user:
        winner = 'win'
    elif game[0] == user and game[3] == user and game[6] == user:
        winner = 'win'
    elif game[1] == user and game[4] == user and game[7] == user:
        winner = 'win'
    elif game[2] == user and game[5] == user and game[8] == user:
        winner = 'win'
    elif game[0] == user and game[4] == user and game[8] == user:
        winner = 'win'
    elif game[2] == user and game[4] == user and game[6] == user:
        winner = 'win'
    return winner
def main():
    game = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    user_x = ''
    user_o = ''
    user_turn = 0
    x = 'x'
    o = 'o'
    while user_x != 'win' or user_o != 'win':
        turn_number = user_turn % 2     
        print()
        print(f'{game[0]}|{game[1]}|{game[2]}')
        print('-+-+-')
        print(f'{game[3]}|{game[4]}|{game[5]}')
        print('-+-+-')
        print(f'{game[6]}|{game[7]}|{game[8]}')
        
        if turn_number == 0:
            user_input_x = int(input("X's turn, please pick an available square (1-9): "))
            x_square = user_input_x - 1
            if user_input_x < 1 or user_input_x > 9:
                print('That is not a valid square number')
            elif game[x_square] == 'x' or game[x_square] == 'o':
                print('That square is already taken')
                print()
            elif game[x_square] != 'x' or game[x_square] != 'o':            
                game[x_square] = 'x'
                user_turn += 1
            elif user_input_x == "I am the winner":
                print('Congradulations to x for the Win!')
                print(f'{game[0]}|{game[1]}|{game[2]}')
                print('-+-+-')
                print(f'{game[3]}|{game[4]}|{game[5]}')
                print('-+-+-')
                print(f'{game[6]}|{game[7]}|{game[8]}')
                break
        if turn_number != 0:
            user_input_o = int(input("O's turn, please pick an available square (1-9): "))
            o_square = user_input_o - 1
            if user_input_o < 1 or user_input_o > 9:
                print('That is not a valid square number')
            elif game[o_square] == 'x' or game[o_square] == 'o':
                print('That square is already taken')
                print()
            elif game[o_square] != 'x' or game[o_square] != 'o':            
                game[o_square] = 'o'
                user_turn += 1
            elif user_input_o == "I am the winner":
                print('Congradulations to O for the Win!')
                print(f'{game[0]}|{game[1]}|{game[2]}')
                print('-+-+-')
                print(f'{game[3]}|{game[4]}|{game[5]}')
                print('-+-+-')
                print(f'{game[6]}|{game[7]}|{game[8]}')
                break
        print()
        user_x = who_won(game, x)
        user_o = who_won(game, o)
        
        
        if user_o == 'win':
            print('Congradulations to O for the Win!')
            print(f'{game[0]}|{game[1]}|{game[2]}')
            print('-+-+-')
            print(f'{game[3]}|{game[4]}|{game[5]}')
            print('-+-+-')
            print(f'{game[6]}|{game[7]}|{game[8]}')
            break
        elif user_x == 'win':
            print('Congradulations to X for the Win!')
            print(f'{game[0]}|{game[1]}|{game[2]}')
            print('-+-+-')
            print(f'{game[3]}|{game[4]}|{game[5]}')
            print('-+-+-')
            print(f'{game[6]}|{game[7]}|{game[8]}')
            break
            
        if game[0] != 1 and game[1] != 2 and game[2] != 3 and game[3] != 4 and game[4] != 5 and game[5] != 6 and game[6] != 7 and game[7] != 8 and game[8] != 9:
            print()
            print('There is no winner, game over.')
            print(f'{game[0]}|{game[1]}|{game[2]}')
            print('-+-+-')
            print(f'{game[3]}|{game[4]}|{game[5]}')
            print('-+-+-')
            print(f'{game[6]}|{game[7]}|{game[8]}')
            break
                
main()