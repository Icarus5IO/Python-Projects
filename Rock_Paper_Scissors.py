import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Game Tied"
    elif (player_choice == "Rock" and computer_choice == "Paper") or \
         (player_choice == "Scissors" and computer_choice == "Rock") or \
         (player_choice == "Paper" and computer_choice == "Scissors"):
        return "You Lose"
    else:
        return "You Win"

def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        player_choice = input("Enter your choice (Rock, Paper, Scissors) or 'I quit' to end: ").capitalize()

        if player_choice == "I quit":
            print("Thank you for playing. Goodbye!")
            break

        if player_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice. Please enter Rock, Paper, Scissors, or 'I quit'.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        print(f"Computer chose {computer_choice}. {result}")

main()
