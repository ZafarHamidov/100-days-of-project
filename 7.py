import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Угадай слово: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"Вы уже догадались {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"Вы неугадали,буквы {guess} нету в загадонном слове. Вы теряете жизнь.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("Ты проиграл.")
    
    if not "_" in display:
        game_is_finished = True
        print("Ты победил.")

    print(stages[lives])
