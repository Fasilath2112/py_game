import random

def get_random_word():
    with open("hangman.txt", 'r') as file:
        wordlist = file.read().splitlines()
    return random.choice(wordlist).lower()

def is_valid_input(character):
    return len(character) == 1 and character.isalpha()

def is_already_guessed(character, guessed_chars):
    return character in guessed_chars

def handle_correct_guess(word, guessed_chars, temp, character):
    guessed_chars.append(character)
    print("\nBravo! You found a letter. You're one step closer to victory!")
    return update_display(word, guessed_chars)

def handle_wrong_guess(chances, word, guessed_chars):
    print("\nOops!! Wrong guess..")
    chances -= 1
    draw_hangman(chances)
    return chances

def update_display(word, guessed_chars):
    temp = ''
    for char in word:
        if char in guessed_chars:
            temp += char + ' '
        else:
            temp += '_ '
    return temp.rstrip()

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

def display_game_state(temp, chances, guessed_chars):
    print(temp)
    print(f"\nChances left: {chances}... the hangman's breath is on your neck.")
    print(f"Guessed letters: {', '.join(guessed_chars)}")

def play_game(word):
    temp = '_ ' * len(word)
    chances = 7
    guessed_chars = []

    while chances > 0 and '_ ' in temp:
        character = input("Enter a letter....if you dare: ").lower()

        if not is_valid_input(character):
            print("Invalid input. Please enter a single alphabetic character.")
            continue

        if is_already_guessed(character, guessed_chars):
            print(f"You've already guessed '{character}'. Try another letter.")
            continue

        if character in word:
            temp = handle_correct_guess(word, guessed_chars, temp, character)
        else:
            chances = handle_wrong_guess(chances, word, guessed_chars)

        display_game_state(temp, chances, guessed_chars)

    return temp, chances

def start_game():
    word = get_random_word()
    temp, chances = play_game(word)

    if '_ ' not in temp:
        win_game(word)
    else:
        lose_game(word)

if __name__ == "__main__":
    print("\n******* Welcome to Hangman, where every wrong guess tightens the noose.. *******")
    print("-----------------------------------------------------------------------------------")
    while True:
        choice = input("Can you solve the word before time runs and the darkness claims another soul? (yes/no): ").lower()
        if choice == 'yes':
            start_game()
        elif choice == 'no':
            print("Quitting the game...")
            break
        else:
            print("Please enter a valid choice")
        print("\n")
