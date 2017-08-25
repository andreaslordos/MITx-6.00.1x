def getAvailableLetters(lettersGuessed):
    alphabet=list("abcdefghijklmnopqrstuvwxyz")
    for y in range(len(lettersGuessed)):
        if lettersGuessed[y] in alphabet:
            alphabet.remove(lettersGuessed[y])
                   
    alphabet=''.join(alphabet)
    return(alphabet)
