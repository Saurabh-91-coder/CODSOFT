# Rock-Paper-Scissors Game
# TASK 3
# User Input: Prompt the user to choose rock, paper, or scissors.
# Computer Selection: Generate a random choice (rock, paper, or scissors) for
# the computer.
# Game Logic: Determine the winner based on the user's choice and the
# computer's choice.
# Rock beats scissors, scissors beat paper, and paper beats rock.
# Display Result: Show the user's choice and the computer's choice.
# Display the result, whether the user wins, loses, or it's a tie.
# Score Tracking (Optional): Keep track of the user's and computer's scores for
# multiple rounds.
# Play Again: Ask the user if they want to play another round.
# User Interface: Design a user-friendly interface with clear instructions and
# feedback.


'''
1 for rock 

-1 for paper 

0 for scissors


'''


import random

user_dict = {"r": 1, "p": -1, "s": 0}
user_reverse_dict = {1: "Rock", -1: "Paper", 0: "Scissors"}
'''
Rock beats scissors,  1 and 0
scissors beat paper,  0 and -1
and paper beats rock, -1 and 1
    
'''

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif (computer_choice == -1 and user_choice == 1) or \
         (computer_choice == 1 and user_choice == 0) or \
         (computer_choice == 0 and user_choice == -1):
        return "You win!"

    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nWelcome to Rock-Paper-Scissors Game!")
        print("Choose one: 'r' for rock, 'p' for paper, 's' for scissors")
        user_str = input("Your choice: ").lower()
        
        while user_str not in user_dict:
            print("Invalid choice. Please choose 'r' for rock, 'p' for paper, or 's' for scissors.")
            user_str = input("Your choice: ").lower()
        
        user_choice = user_dict[user_str]
        computer_choice = random.choice([-1, 0, 1])
        
        user_choice_str = user_reverse_dict[user_choice]
        computer_choice_str = user_reverse_dict[computer_choice]
        
        print(f"\nYour choice: {user_choice_str}")
        print(f"Computer's choice: {computer_choice_str}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        
        play_again = input("\nDo you want to play again? (Y/N): ").lower()
        if play_again != 'y':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()



