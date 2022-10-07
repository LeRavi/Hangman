from hangman_art import logo, stages
from hangman_wordlist import word_list
import random
import os

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Testing code
print(f'The solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("cls")
    # let the user know the already guessed the letter
    if guess in display:
        print(f"You already guessed {guess} the letter")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guesses {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # print stages of lives
    print(stages[lives])
