import random

def get_random_word():
    with open("hangman.txt", 'r') as file:
        wordlist = file.read().splitlines()
    return random.choice(wordlist).lower()

def validate_input(character):
    return len(character) == 1 and character.isalpha()

def already_guessed(character, guessed_chars):
    return character in guessed_chars

def handle_guess(word, guessed_chars, chances, character):
    if not validate_input(character):
        return guessed_chars, chances, False

    if already_guessed(character, guessed_chars):
        return guessed_chars, chances, False

    guessed_chars.append(character)

    if character in word:
        return guessed_chars, chances, True
    else:
        chances -= 1
        return guessed_chars, chances, False

def update_display(word, guessed_chars):
    temp = ''
    for char in word:
        if char in guessed_chars:
            temp += char + ' '
        else:
            temp += '_ '
    return temp.rstrip()  # Remove trailing spaces

def draw_hangman(chances):
    if chances == 7:
        print("_________     ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif chances == 6:
        print("_________     ")
        print("|       |     ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif chances == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif chances == 4:
        print("________  ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif chances == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif chances == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\    ")
        print("|             ")
        print("|             ")
    elif chances == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\    ")
        print("|     /       ")
        print("|             ")
    elif chances == 0:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\    ")
        print("|     / \\    ")
        print("|             ")

def win_game(word):
    print("\nYou did it! The hangman is spared...for now. You live to see another day!")
    print(f"\nThe word was: {word}")

def lose_game(word):
    print("\nNo! The word remains unsolved and the hangman claims another victim.")
    print(f"\nThe word was: {word}")

def run_game():
    word = get_random_word()
    temp = '_ ' * len(word)
    chances = 7
    guessed_chars = []

    while chances > 0 and '_ ' in temp:
        guessed_chars, chances, valid_guess = handle_guess(word, guessed_chars, chances, input("Enter a letter....if you dare: ").lower())
        if valid_guess:
            temp = update_display(word, guessed_chars)
        else:
            draw_hangman(chances)
            print(update_display(word, guessed_chars))  # Display updated word after drawing hangman

    if '_ ' not in temp:
        win_game(word)
    else:
        lose_game(word)

def play_hangman():
    print("\n******* Welcome to Hangman, where every wrong guess tightens the noose.. *******")
    print("-----------------------------------------------------------------------------------")

    while True:
        choice = input("Can you solve the word before time runs and the darkness claims another soul? (yes/no): ").lower()
        if choice == 'yes':
            run_game()
        elif choice == 'no':
            print("Quitting the game...")
            break
        else:
            print("Please enter a valid choice")
        print("\n")

if __name__ == "__main__":
    play_hangman()
