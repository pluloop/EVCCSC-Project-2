import random

finished = False


def display_result(user_choice):
    if user_choice == 1:
        print(f'{user_choice} chose rock!')
    elif user_choice == 2:
        print(f'{user_choice} chose paper!')
    elif user_choice == 3:
        print(f'{user_choice} chose scissors!')


def who_won(choice_player, choice_opponent):
    if choice_player == 1 and choice_opponent == 3:
        print('Player wins!')
    elif choice_player == 2 and choice_opponent == 3:
        print('Opponent wins!')
    elif choice_player == 3 and choice_opponent == 1:
        print('Opponent wins!')
    elif choice_player == 3 and choice_opponent == 2:
        print('Player wins!')
    elif choice_player == 1 and choice_opponent == 2:
        print('Opponent wins!')
    elif choice_player == 2 and choice_opponent == 1:
        print('Player wins!')
    else:
        print('Draw!')


while not finished:

    player_choice = int(input('Enter rock, paper, or scissors!: '))

    opponent_choice = random.randint(1, 4)

    display_result(player_choice)
    display_result(opponent_choice)
    who_won(player_choice, opponent_choice)

    keep_playing = input('Play again? Type Yes or No: ')

    if keep_playing == 'Yes' or keep_playing == 'yes':
        print()
        finished = False
    else:
        finished = True

print('wimpy loser')
