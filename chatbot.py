# DEFINITIONS OF FUNCTIONS

#Greeting Function defintion
def greetingFunction():
    name = input("Welcome to the chat! What's your name? ")
    print(f"Hello, {name}!")

    #stateOfMind = input("How are you doing today?")

def goodFunction():
    print("Oh nice! That's great!")
    knocks = input("Do you want to hear a knock-knock joke? (yes or no) ")
    if knocks == "yes":
        print(f"Great! You start!")
        yesKnockKnock = input("(Start your knock-knock joke!) ")
        beginningKnockKnock = input("Who's there? ")
        continueKnockKnock = input(f"{beginningKnockKnock} who? ")
        print("Haha, that's funny!")
    if knocks == "no":
        print("Oh, okay then :(")
        storyAnswer = input("Would you like to hear a story? (yes or no)")
        if storyAnswer == "yes":
            storyType = input("Would you like to hear a story or a different story? (1 or 2)")
            if storyType == "1":
                story1()
            if storyType == "2":
                story2()
        else:
            print("Well, I'll tell you a story anyway.")
            story1()

def badFunction():
    print("Oh, I'm sorry.")
    cheerUp = input("Would something help you feel better? (yes or no)")
    if cheerUp == "yes":
        print("Okay, amazing. I'm going to tell you a story.")
        story2()
    else:
        print("Maybe a game of hangman will help.")
        hangman()

def story1():
    print("Once upon a time...")
    print("The end.")

def story2():
    print("I said: 'The city would've been better if the weather had been better.''")
    print("My mom replied:")
    print("'Just like the bones of a good house, you have to look past the decor.'")
    print("(I don't know what this means.)")

def hangman():
    import random
    potential_words = ["example", "words", "anagram", "jazz", "floccinaucinihilipilification", "campus", "overjoyed"]
    word = random.choice(potential_words)
    word = word.lower()
    current_word = list(word)
    guesses = []
    maxfails = 7
    fails = 0
    while fails < maxfails:
        guess = input("Guess a letter: ").lower()
        if guess.isalpha() and len(guess) == 1 and guess not in guesses:
            guesses.append(guess)
            print(guesses)
            if guess in current_word:
                print("You guessed a letter correctly!")
            else:
                print("You guessed incorrectly.")
                fails += 1
        else:
            print("Invalid guess. Try again!")
        print("You have " + str(maxfails - fails) + " tries left!")
        display = ""
        winning = ""
        for i in current_word:
            if i in guesses:
                display += i + " "
                winning += i
            else:
                display += "_ "
        print(display)
        if winning == word:
            print("Congrats! You won!")
            exit(0)
    print(f"You have lost; the word was {word}.")

def math(integer1, integer2):
    print(f"I will find what {input1} equals in mod{input2}.")




def main():
  while True:
    answer = input("(What will you say?) ")
    print("That's cool!")


#############################################################################

if __name__ == "__main__":
    #main()
    greetingFunction()
    stateOfMind = input("How are you doing today?")
    if stateOfMind == "good":
        goodFunction()
    elif stateOfMind == "bad":
        badFunction()
    else:
        input1 = int(input("Give me a number: "))
        input2 = int(input("Give me another number: "))
        math(input1, input2)
