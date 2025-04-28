import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    your_score = 0

    for i in range(NUM_ROUNDS):
        print(f"Round {i + 1}")

        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)

        print("Your number is", your_num)

        # Get user input and validate it
        choice = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        while choice != "higher" and choice != "lower":
            choice = input("Please enter either 'higher' or 'lower': ").strip().lower()

        # Determine if the guess is correct
        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_num}")
            your_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")

        print("Your score is now", your_score)
        print()  # Blank line for better readability between rounds

    # End of game - print final message based on performance
    print("Thanks for playing!")

    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
