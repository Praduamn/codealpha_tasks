import random

def hangman():
    words = ["hangman", "coding", "internship", "game", "python","fortnite"]
    word = random.choice(words)  
    guessed = ["_"] * len(word)
    attempts = 6  
    guessed_letters = [] 

    print("Hangman Game!!")
    print(" ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("Enter a letter: ").lower()
      
        if len(guess) != 1 or not guess.isalpha():
            print("Only 1 letter please.")
            continue

        if guess in guessed_letters:
            print("Letter already guessed!")
            continue
        guessed_letters.append(guess)

        if guess in word:
            print(f"Great guess!!! {guess} is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! lives left: {attempts}")

        print(" ".join(guessed))
      
    if "_" not in guessed:
        print("YOU WIN!!! You guessed the word! ", word)
    else:
        print("Game Over... The word was:", word)



hangman()
