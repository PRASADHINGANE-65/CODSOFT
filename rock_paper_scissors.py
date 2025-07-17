import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_result(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    print("--- ROCK PAPER SCISSORS GAME ---")

    while True:
        user = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user == "quit":
            break

        if user not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Try again.")
            continue

        computer = get_computer_choice()
        print(f"🧍 You chose: {user}")
        print(f"💻 Computer chose: {computer}")

        result = get_result(user, computer)
        print(f"🎯 Result: {result}")

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"📊 Score — You: {user_score} | Computer: {computer_score}\n")

    print("👋 Thanks for playing!")

# Run the game
main()
