#I am wrting a program of a guesing game
#The program will generate a random number between 1 and 100
#The user will have to guess the number
#The program will tell the user if the number is higher or lower than the guess
#The user will have 10 attempts to guess the number
#If the user fails to guess the number, the program will tell the user the number
#The program will also tell the user how many attempts he needed to guess the number
#The program will also tell the user if he guessed the number correctly

def guessing_game():
    import random
    number = random.randint(1, 100)
    attempts = 0
    print("I have generated a random number between 1 and 100. You have 10 attempts to guess it.")
    while attempts < 10:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("The number is higher than your guess.")
        elif guess > number:
            print("The number is lower than your guess.")
        else:
            print("Congratulations! You have guessed the number in", attempts, "attempts.")
            return
    print("You have failed to guess the number. The number was", number)
    return

guessing_game()