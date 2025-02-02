import random
word_list = ["cat" ,"dog" ,"star" , " python"]
chosen_word = random.choice(word_list)

word_length = len(chosen_word)
end_of_game = False

lives = 6

print (" welcome to hangman game ")

stages= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input(" guess a letter :").lower()
    if guess in display :
        print(f" you have already guessed {guess}")
    for position in range (word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f" you guessed {guess} , thats not in the word , you lose atry")
        lives -=1
        if lives == 0:
            end_of_game = True
            print(" you lose")
    print(f" {' '.join(display)}")
    if "_" not in display :
        end_of_game =True
        print(" you win")
    print(stages[6-lives])
