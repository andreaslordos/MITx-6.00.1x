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
