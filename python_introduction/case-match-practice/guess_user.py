import random

def play_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue  # Skip the rest of the loop and ask again

        attempts += 1  # Only increment if input was valid

        match guess:
            case x if x == secret_number:
                print(f"🎉 Congratulations, you guessed it in {attempts} attempt(s)!")
                break
            case x if x > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case x if x < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
            case _:
                print("Invalid input. Please enter a number between 1 and 10.")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
