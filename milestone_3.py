import random 


word_list = ["Orange", "Apple", "Banana", "Pear", "Raspberry"]
word = random.choice(word_list)

def ask_for_input():
    while True:
        guess = input(f'Hangman letter guess, please enter a single letter ...')
        if len(guess) == 1 and  guess.isalpha() == True:
            break
        else:
            input(f"Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

def check_guess(guess):
    guess = guess.lower()
    if guess in word.lower():
        print(f"Good guess!",guess,"is in the word.")
    else:
        print(f"Sorry,",guess,"is not in the word. Try again.")

ask_for_input()
print(word)

