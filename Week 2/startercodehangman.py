#gives us randoms
import random

potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)
#to test: print(word)

#converts the word to lowercase
word = word.lower()

#make it a list of letters for someone to guess
current_word = list(word) #the number of letters should match the word
#print(current_word)

#some useful variables
guesses = [] #holds all previously guessed letters
maxfails = 7
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ").lower()

    #if the guess is a single letter           if not guessed already
    if guess.isalpha() and len(guess) == 1 and guess not in guesses:
        guesses.append(guess)
        print(guesses)

        if guess in current_word:
            #guess is right
            print("You guessed a letter correctly!")

        else:
            #guess is wrong
            print("You guessed incorrectly.")
            fails += 1

    else:
        #not valid input
        print("Invalid guess. Try again!")

    #check if the guess is valid. is it one letter? have they already guessed it?

    #check if the guess is correct: is it in the word? if so, reveal the letters

    #print(current_word)

    print("You have " + str(maxfails - fails) + " tries left!")

    #display the status of the word
    display = ""
    winning = ""
    for i in current_word:
        if i in guesses:
            display += i + " "
            winning += i
            #print(i)
        else:
            display += "_ "
            #print("_ ")
    print(display)

    if winning == word:
        print("You won!")
        exit(0)

print(f"You have lost; the word was {word}.")
