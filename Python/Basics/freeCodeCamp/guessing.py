
secret_number = 69
guess = 0
guess_count = 0;
guess_limit = 5
out_of_guesses = False

while guess != secret_number and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = int(input("Enter guess: "))
        if guess > secret_number:
            print("Guess was too high")
        elif guess < secret_number:
            print("Guess was too low")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses: 
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")
