import random
#function for reading a text file and getting a random text
def get_random_word():
    with open("hangman.txt", 'r') as file:
#reads the entire content as a single string so it splits the string into a list of lines removing the newline 
        wordlist = file.read().splitlines()
#choose a random word and convert it to lowercase
    return random.choice(wordlist).lower()

#draws the hangman based on the number of chances
def draw_hangman(chances):
    if chances == 7:
        print("_________     ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    if chances == 6:
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

def start_game():
#get a random word and stores it to variable word
    word = get_random_word()
#according to the length of word '_' is created
    temp = '_ ' * len(word)
#no.of chances is set to 7
    chances = 7
#empty list for storing guessed chars
    guessed_chars = []
#loop until the player runs out of chances or guesses the word
    while chances > 0 and '_ ' in temp:
#display the current state of the word
        print(temp)
        print(f"\nChances left: {chances}... the hangman's breath is on your neck.")
        print(f"Guessed letters: {', '.join(guessed_chars)}")
        character = input("Enter a letter....if you dare: ").lower()
#validate the input to ensure it is a single alphabetic character
        if len(character) != 1 or not character.isalpha():
            print("\nPlease enter a single alphabet only")
            continue
#check if the character has already been guessed
        if character in guessed_chars:
            print("\nYou have already guessed that character. Try another one.")
            continue
#add the guessed character to the list
        guessed_chars.append(character)
#check if the guessed character is in the word
        if character in word:
            print("\nBravo! You found a letter. You're one step closer to victory!")
 #update the diaplay variable with the guessed letters
            temp = ''
            for char in word:
                if char in guessed_chars:
                    temp += char + ' '
                else:
                    temp += '_ '
        else:
            print("\nOops!! Wrong guess..")
#decrease the number of chances
            chances -= 1
            draw_hangman(chances)
#if the user guessed correctly
    if '_ ' not in temp:
        print(f"\nThe word was: {word}")
        print(f"\nYou did it! The hangman is spared...for now. You live to see another day!")
 #if the user fails to guess the word 
    else:
        print(f"\nNo! The word remains unsolved and the hangman claims another victim.")
        print(f"The word was {word} - the darkness has won this round")
#Welcome message and main game loop
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
