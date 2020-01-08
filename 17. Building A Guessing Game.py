#guessing game with unlimited tries
secret_word = "giraffe"
guess = ""

while guess != secret_word:     #until guess is not equal to secret word keep asking the question
    guess = input("Enter guess: ")

print("You Win")

#guessing game with limited tries

secret_word_1 = "giraffe"
guess_1 = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess_1 != secret_word_1 and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_1 = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You LOSE!")
else:
    print("You win!")