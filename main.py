import random
import os
from operator import truediv

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboom", "camel"]

chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

frame_word = []
word_len = len(chosen_word)

for _ in range(word_len):
    frame_word += "_"
def fill_letter(len, frame, word):
    for position in range(len):
        letter = word[position]
        if letter == guess:
            frame[position] = letter

lives = 6

isEnded = False
while not isEnded:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    fill_letter(word_len, frame_word, chosen_word)

    if guess not in chosen_word:
        lives -= 1
            
    if frame_word.count("_") == 0:
        print("You win!")
        isEnded = True
    elif lives == 0 :
        print("You lose.")
        isEnded = True
    else:
        print(f"{' '.join(frame_word)}")
    print(stages[lives])

    
