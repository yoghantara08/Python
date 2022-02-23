secret_word = "Python"
user_guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("Guess a Programming Language")
print("You have 3 chances")
while user_guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        user_guess = input("Enter a programming language : ")
        guess_count += 1  
    else:
        out_of_guesses = True
    if guess_count == 1 and user_guess != secret_word:
        print("You have 2 more chances")
    if guess_count == 2 and user_guess != secret_word:
        print("You have 1 more chance")  

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("Correct, YOU WIN!")
    
    

