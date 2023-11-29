import random 

class hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(self.word)
        self.word_guessed = list('_' * len(self.word))
        self.list_of_guesses = []


    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter.lower() == guess.lower():
                    self.num_letters -= 1
                    self.word_guessed[i] = letter
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while True:
            guess = input(f'Hangman letter guess, please enter a single letter ...')
            if len(guess) != 1 or guess.isalpha() != True:
               print(f"Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f'You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_letters == 0:
            print(f'Congratulations. You won the game!')
            break
        else:
            print(f'There is an error!')
            break
    print(f'The word is {game.word}')

play_game(["Orange", "Apple", "Banana", "Pear", "Raspberry"])

