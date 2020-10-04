import random, string

print("H A N G M A N")
print()
word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(word_list)

num_guesses = 0
guesses = set()
menu = ""

while menu != "exit":
    menu = input('Type "play" to play the game, "exit" to quit:')

    if menu == "play":

        while num_guesses <= 7 and guesses != set(chosen_word) :
            reveal = chosen_word
            for char in chosen_word:
                if char not in guesses:
                    reveal = reveal.replace(char, '-')
            print()
            print(reveal)
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("You should input a single letter")
            elif guess not in string.ascii_lowercase:
                print("It is not an ASCII lowercase letter")
            elif guess in set(chosen_word) and guess not in guesses:
                 guesses.add(guess)
            elif guess in guesses:
                print("You already typed this letter")
            else:
                num_guesses += 1
                print("No such letter in the word")
                guesses.add(guess)
        if guesses == set(chosen_word):
            print("You guessed the word!")
            print("You survived!")
        else:
            print("You lost!")

    elif menu == "exit":
        break;
    else:
        continue
