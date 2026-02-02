import random

choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors!")
print("Type rock, paper, or scissors")
print("Type 'quit' to stop the game")

while True:
    user = input("\nYour choice: ").lower()

    if user == "quit":
        print("👋 Thanks for playing!")
        break

    if user not in choices:
        print("❌ Invalid choice. Try again.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("🤝 It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")
