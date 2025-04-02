import random

# Choices mapped to numbers
choices = {1: "rock", 2: "paper", 3: "scissors"}

# Function to determine winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Get number of rounds from the user
while True:
    try:
        total_rounds = int(input("How many rounds do you want to play? "))
        if total_rounds > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input! Enter a valid number.")

# Initialize scores
user_score = 0
computer_score = 0

# Main game loop
for round_num in range(1, total_rounds + 1):
    print(f"\nRound {round_num}/{total_rounds}")
    print("1. Rock\n2. Paper\n3. Scissors")

    try:
        user_choice_num = int(input("Enter your choice (1-3): ").strip())
        if user_choice_num not in choices:
            print("Invalid choice! Please choose 1, 2, or 3.")
            continue
    except ValueError:
        print("Invalid input! Enter a number between 1-3.")
        continue

    user_choice = choices[user_choice_num]
    computer_choice = random.choice(list(choices.values()))

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Update scores
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"Scores - You: {user_score} | Computer: {computer_score}")

# Display final result
print("\nGame Over!")
print(f"Final Scores - You: {user_score} | Computer: {computer_score}")
if user_score > computer_score:
    print("Congratulations! You won the game! 🎉")
elif user_score < computer_score:
    print("Computer wins the game! Better luck next time.")
else:
    print("It's a tie game!")

print("Thanks for playing!")