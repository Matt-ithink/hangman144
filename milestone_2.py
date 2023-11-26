import random 

word_list = ["Orange", "Apple", "Banana", "Pear", "Raspberry"]

word = random.choice(word_list)

guess = input(f'Please enter a single letter ...')
if len(guess) == 1 and  guess.isalpha() == True:
    pass
else:
    input(f'Try again please enter a single letter ...')

print(word_list)
print(word)
print(guess)