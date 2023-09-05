import random
"""
    We Want a Rock Paper Scissors game 
    Where the user chose a choice and the computer choses another choice and then we can do the logic
"""
def play():

    choices_array = ['r','p','s']
    computer_choice = random.choice(choices_array)
    user_choice = input("""Chose Rock ('r'), 
    Paper ('p')
    and Scissors ('s') """).lower()

    if user_choice == computer_choice:
        return f"Ooh It's a tie {computer_choice} {user_choice}"
    
    elif is_win(computer_choice,user_choice):
        return "You won"

    else:
        return "Oooh you lost, the computer has won"



def is_win(computer,player):
  if (player == 'r' and computer == "s") or (player == 'p' and computer == 'r') or (player == 's' and computer =='p'):
    return True



print(play())