import random


# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
from hangman_words import word_list

chosen_word = random.choice(word_list)
length = len(chosen_word)
print(length)

lives = 6

display = []

for _ in chosen_word:
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Enter the letter you guess: ").lower()

    if guess in display:
        print(f"you have already guessed {guess}")

    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. you loose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    if "_" not in display:
        end_of_game = True
        print("You win")
    # print(stages[lives])
