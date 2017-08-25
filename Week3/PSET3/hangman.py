import random
WORDLIST_FILENAME = "words.txt"
playagain=True

def cls():
    print ("\n"*100)


def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")

    return wordlist


wordlist = loadWords()

def countPlusses(userinput):
    g=0
    modifier=len(userinput)+1
    return(modifier)

def chooseWord(wordlist):
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    isWordGuessed=True
    for f in range(len(secretWord)):
        if secretWord[f] not in lettersGuessed:
            isWordGuessed=False
    return(isWordGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    fullstring=""
    cursor=0
    while cursor<len(secretWord):
        letter=secretWord[cursor]
        underscore=True
        for x in range(len(lettersGuessed)):
            if letter==lettersGuessed[x]:
                fullstring=fullstring+letter
                underscore=False
        if underscore==True:
            fullstring=fullstring+' _ '
        cursor+=1
    return(fullstring)

       
def getAvailableLetters(lettersGuessed):
    alphabet=list("abcdefghijklmnopqrstuvwxyz")
    for y in range(len(lettersGuessed)):
        if lettersGuessed[y] in alphabet:
            alphabet.remove(lettersGuessed[y])
                   
    alphabet=''.join(alphabet)
    return(alphabet)
            

def hangman(secretWord):
    tempalphabet="abcdefghijklmnopqrstuvwxyz"
    guesses=13
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print("The word starts with "+secretWord[0]+" and ends with "+secretWord[-1])
    while isWordGuessed(secretWord,lettersGuessed)== False and guesses>0:
        print("-----------")
        if guesses>1:
            print("You have "+str(guesses)+" guesses left")
        elif guesses==1:
            print("You have 1 guess left")
        guesses-=1
        avletters=getAvailableLetters(lettersGuessed)
        print("Available Letters: "+avletters)
        userguess=input("Please guess a letter: ")
        if userguess[0]=="+":
            modifier=countPlusses(userguess)
            guesses+=modifier
        elif userguess not in lettersGuessed and len(userguess)==1:
            lettersGuessed.append(userguess)
        displayonscreen=getGuessedWord(secretWord,lettersGuessed)
        if userguess in secretWord and userguess!="":
            print("Good guess: "+displayonscreen)
        elif userguess!="" and len(userguess)==1 and userguess in tempalphabet:
            print("Oops! That letter is not in my word: "+displayonscreen)
        elif userguess[0]!="+":
            print("Invalid!")
            guesses+=1
    won=isWordGuessed(secretWord,lettersGuessed)
    return(won)


while playagain==True:
    difficulty=input("Select a difficulty, by typing in 'Easy', 'Medium' or 'Hard \n")
    if difficulty[0]=="H" or difficulty[0]=="h":
        minlength=9
    elif difficulty[0]=="M" or difficulty[0]=="m":
        minlength=7
    else:
        minlength=5

    lettersGuessed=[]
    secretWord="----------"
    while len(secretWord)!=minlength:
        secretWord = chooseWord(wordlist).lower()
    won=hangman(secretWord)
    print("-----------")
    if won==True:
        print("Great job! You won!")
    else:
        print("Close! The word was "+secretWord)
    playagainin=input("Would you like to play again? [Y/N] ")
    if playagainin=="":
        print("Okay, bye!")
    elif playagainin[0]=="Y" or playagainin[0]=="y":
        playagain=True
        cls()
    else:
        playagain=False
        print("Okay, bye!")
        

