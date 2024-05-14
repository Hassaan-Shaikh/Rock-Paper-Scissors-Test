import random

is_game_running = True
rps_choices = {
    "Rock" : 1,
    "Paper" : -1,
    "Scissors" : 0
    }

def round_result(player_card, ai_card):
    return player_card - ai_card

def get_player_choice():
    player_choice = input("Choose 'Rock', 'Paper' or 'Scissors': ")
    if player_choice not in rps_choices:
        print("Invalid choice, fool!")
    else:
        return player_choice

def get_ai_choice():
    return random.choice(list(rps_choices.keys()))

def play_round():
    p_choice = ""
    while(p_choice not in rps_choices):
        p_choice = get_player_choice()
    a_choice = get_ai_choice()
    print("Player chooses {}.".format(p_choice))
    print("The AI chooses {}.".format(a_choice))
    res = round_result(rps_choices[p_choice], rps_choices[a_choice])
    if res == 0:
        print("No winner this round.")
    elif res == -1 or res == 2:
        print("The AI wins this round!")
    elif res == 1 or res == -2:
        print("The Player wins this round!")

while(is_game_running):
    play_round()
    wants_to_quit = input("Enter 'Y' to stop playing. Leave blank to continue: ")
    is_game_running = not wants_to_quit.lower() == "y"
    print()
