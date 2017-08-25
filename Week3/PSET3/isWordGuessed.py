def isWordGuessed(secretWord, lettersGuessed):
    isWordGuessed=True
    for f in range(len(secretWord)):
        if secretWord[f] not in lettersGuessed:
            isWordGuessed=False
    return(isWordGuessed)
