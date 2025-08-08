import random
print("please enter only numbers in lowest and highest variables....")
print(".............................................................")
lowest = int(input("enter the lowest:"))
highest = int(input("enter the highest: "))
answer = random.randint(lowest, highest)

print("Python Number Guessing Game!")
print(".............................................................")
print()
print(f"Select a number between {lowest} and {highest}")
# print(answer)  # Uncomment for testing

guesses = 0
max_guesses = 10

while guesses < max_guesses:
    try:
        guess = int(input("Enter your guess: "))
        guesses += 1

        if guess == answer:
            print(f" You guessed it right in {guesses} attempt(s)! The number was {answer}.")
            break
        elif guess < answer:
            print("Too low.")
        else:
            print(" Too high.")
        
        print(f"Attempts left: {max_guesses - guesses}")
    except ValueError:
        print(" Invalid input. Please enter a number.")

else:
    print(f"You've used all {max_guesses} attempts. The number was {answer}.")
