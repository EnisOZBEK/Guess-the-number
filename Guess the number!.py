import random

difficulty = int(input("\nChoose a difficulty level\n\nPress 1 for HARD(1-1000)--mode!\nPress 2 for NORMAL(1-100)-mode!\nPress 3 for EASY(1-10)----mode!\nPress 4 for play with your own limits!\nDiff: "))

again = "y"

while again == "y" and difficulty == 1:
    number = random.randrange(1, 1001)

    guess = int(input("\nGuess a number between 1 and 1000: "))

    guesses_taken = 0

    while guess != number:
        if guess < number:
            print("\nYour guess is lower than the actual number!")
            guess = int(input("Guess higher: "))

            guesses_taken = guesses_taken + 1

        elif guess > number:
            print("\nYour guess is higher than the actual number!")
            guess = int(input("Guess lower: "))

            guesses_taken = guesses_taken + 1

    guesses_taken = guesses_taken + 1

    print(f"\nCongratz! You guessed the number correctly! and it took you {guesses_taken} guesses!")
    
    again = input("Play again ? (y, n): ")

    if again == "n":
        print("\nThanks for playing!")

# ---------------------------------------------------------------------------------------------------------

while again == "y" and difficulty == 2:
    number = random.randrange(1, 101)

    guess = int(input("\nGuess a number between 1 and 100: "))

    guesses_taken = 0

    while guess != number:
        if guess < number:
            print("\nYour guess is lower than the actual number!")
            guess = int(input("Guess higher: "))

            guesses_taken = guesses_taken + 1

        elif guess > number:
            print("\nYour guess is higher than the actual number!")
            guess = int(input("Guess lower: "))

            guesses_taken = guesses_taken + 1

    guesses_taken = guesses_taken + 1

    print(f"\nCongratz! You guessed the number correctly! and it took you {guesses_taken} guesses!")
    
    again = input("Play again ? (y, n): ")

    if again == "n":
        print("\nThanks for playing!")

# ---------------------------------------------------------------------------------------------------------

while again == "y" and difficulty == 3:
    number = random.randrange(1, 11)

    guess = int(input("\nGuess a number between 1 and 10: "))

    guesses_taken = 0

    while guess != number:
        if guess < number:
            print("\nYour guess is lower than the actual number!")
            guess = int(input("Guess higher: "))

            guesses_taken = guesses_taken + 1

        elif guess > number:
            print("\nYour guess is higher than the actual number!")
            guess = int(input("Guess lower: "))

            guesses_taken = guesses_taken + 1

    guesses_taken = guesses_taken + 1

    print(f"\nCongratz! You guessed the number correctly! and it took you {guesses_taken} guesses!")
    
    again = input("Play again ? (y, n): ")

    if again == "n":
        print("\nThanks for playing!")

# ---------------------------------------------------------------------------------------------------------

while again == "y" and difficulty == 4:
    lowest_limit = int(input("Type your lowest limit!: "))
    highest_limit = int(input("Type your highest limit!: "))

    number = random.randrange(lowest_limit, highest_limit)

    guess = int(input(f"Guess a number between {lowest_limit} and {highest_limit}: "))

    guesses_taken = 0

    while guess != number:
        if guess < number:
            print("\nYour guess is lower than the actual number!")
            guess = int(input("Guess higher: "))
            guesses_taken = guesses_taken + 1

        elif guess > number:
            print("\nYour guess is higher than the actual number!")
            guess = int(input("Guess lower: "))
            guesses_taken = guesses_taken + 1

    guesses_taken = guesses_taken + 1

    print(f"\nCongratz! You guessed the number correctly! and it took you {guesses_taken} guesses!")
    again = input("Play again ? (y, n): ")

    if again == "n":
        print("\nThanks for playing!")