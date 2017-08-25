guess=50
print("Please think of a number between 0 and 100!")
userinput="l"
maxpossible=99.5
minpossible=0.5
count=0
while userinput!="c":
    count+=1
    print("Is your secret number "+str(guess)+"?")
    userinput=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess it too low. Enter 'c' to indicate I guessed correctly. ")
    if userinput=="l":
        maxpossible=guess+1
        guess=round((guess+maxpossible)/2)
        print(minpossible)
        print(maxpossible)
        print("-----------")
    elif userinput=="h":
        minpossible=guess-1
        guess=round((guess+minpossible)/2)
        print(minpossible)
        print(maxpossible)
        print("-----------")
    elif userinput!="c":
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: "+str(guess))
