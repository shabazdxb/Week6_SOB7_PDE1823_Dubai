import random

def compare_numbers(number, user_guess):
    cows = 0
    bulls = 0
    
    # Loop through all 4 digits to check for matches
    for i in range(len(number)):
        if user_guess[i] == number[i]:
            bulls += 1
        elif user_guess[i] in number:
            cows += 1
            
    return [cows, bulls]

playing = True 

# CHANGED: Removed .zfill() as requested, and updated the randint range to 1000-9999 to guarantee a 4-digit number is generated instead.
number = str(random.randint(1000, 9999)) 
guesses = 0

print("Let's play a game of Cowbull!")
print("I will generate a 4-digit number, and you have to guess the numbers.")
print("For every number that exists in the sequence but is in the wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type 'exit' at any prompt to exit.\n")

while playing:
    user_guess = input("Give me your best 4-digit guess! ")#changed raw input as it was removed in python 3. no longer needed for this code.
    
    # CHANGED: Added .lower() so it safely catches if the user types "Exit" or "EXIT"
    if user_guess.lower() == "exit":
        break
        
    # CHANGED: Added a safety check to ensure the guess is exactly 4 characters to prevent the script from crashing with an IndexError
    if len(user_guess) != 4:
        print("Oops! You must enter exactly 4 digits. Try again.")
        continue

    cowbullcount = compare_numbers(number, user_guess)
    guesses += 1
    
    print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1] == 4:
        playing = False
        print("You win the game after " + str(guesses) + " guesses! The number was " + str(number))
    else:
        print("Your guess isn't quite right, try again.\n")
