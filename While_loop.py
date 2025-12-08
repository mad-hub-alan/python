
# FIND SECRET NUMBER GAME!

secret_number = 9
guess = -1
no_of_attempts = 0
attempts_limit = 5

while secret_number != guess and no_of_attempts < attempts_limit :
    guess = int(input("Enter your guess(1-10) : "))
    no_of_attempts += 1

if no_of_attempts == attempts_limit :
    print("You Lose! You reached attempts limit!")
else:
    print("You Won!, The secret number is "+str(secret_number))
