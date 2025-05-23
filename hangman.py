import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'programming', 'computer','bighero']
    word = random.choice(words)
    guessed_letters = set()
    attempts_left = 6  # Number of allowed wrong guesses
    word_display = ['_'] * len(word)

    print("🎮 Welcome to Hangman!")
    print("Guess the word, by entering one letter at a time.")

    while attempts_left > 0 and '_' in word_display:
        print("\nWord:", ' '.join(word_display))
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        print("Attempts left:", attempts_left)

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("⛔ Given letter already entered try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ The guessed letter is there in the word,congrats!")
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
        else:
            print("❌ The guessed letter is not there in the word,better luck next time!")
            attempts_left -= 1

    # Final result
    if '_' not in word_display:
        print("\n🎉Good luck and Congratulations!/n")
        print("You guessed the word:", word)
    else:
        print("\n💀 Out of Attempts, Game over!/n The correct word was:", word)

# Run the game
hangman()
