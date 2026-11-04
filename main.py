password = "python"
guess=5
print("Welcome to the password guessing game!")
print("you have 5 guesses to guess the password")
while guess>0:
    x=input("Enter your guess: ")
    if x==password:
        print("Congratulations! You guessed the password correctly.")
        break
    else:
        guess -= 1
        print(f"Incorrect guess. You have {guess} guesses left.")
        if guess == 0:
            print("Sorry, you've run out of guesses.")