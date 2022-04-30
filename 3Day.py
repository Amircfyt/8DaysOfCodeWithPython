import random

# List of possible choices
choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# What you choose?
input_choice = int(input("Write 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock:"))
your_choice = choices[input_choice]

# What machine choose?
machine_choice = random.choice(choices)
print(f"\nYour choice: {your_choice}\nComputer choice: {machine_choice}")

if your_choice == machine_choice:
    print("It's a draw")

elif your_choice == "Scissors" and machine_choice == "Paper":
    # Scissors cuts Paper
    print("You won!")

elif your_choice == "Paper" and machine_choice == "Rock":
    # Paper covers Rock
    print("You won!")

elif your_choice == "Rock" and machine_choice == "Lizard":
    # Rock crushes Lizard
    print("You won!")

elif your_choice == "Lizard" and machine_choice == "Spock":
    # Lizard poisons Spock
    print("You won!")

elif your_choice == "Spock" and machine_choice == "Scissors":
    # Spock smashes Scissors
    print("You won!")

elif your_choice == "Scissors" and machine_choice == "Lizard":
    # Scissors decapitates Lizard
    print("You won!")

elif your_choice == "Lizard" and machine_choice == "Paper":
    # Lizard eats Paper
    print("You won!")

elif your_choice == "Paper" and machine_choice == "Spock":
    # Paper disproves Spock
    print("You won!")

elif your_choice == "Spock" and machine_choice == "Rock":
    # Spock vaporizes Rock
    print("You won!")

elif your_choice == "Rock" and machine_choice == "Scissors":
    # Rock crushes Scissors
    print("You won!")
else:
    print("You lost!")

