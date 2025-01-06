 # Rock, Paper and Scissors Game
import random

def get_choices():
    player_choice = input('Enter a choice (rock, paper, scissors): ')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {
        'player': player_choice,
        'computer': computer_choice
    }
    return choices

def check_win(player, computer):
    print(f'You chose: {player}, Computer chose: {computer}')
    if player == computer:
        return 'It is a tie'
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes scissors! you win!'
        else:
            return 'Paper covers rock! you lose.'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers rock! you Win!'
        else:
            return 'Scissors cuts paper! you lose.'
    elif player == 'scissors':
        if computer == 'paper':
            return 'Scissors cuts paper! you Win!'
        else:
            return 'Rock smashes scissors! you lose.'
        
choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)
