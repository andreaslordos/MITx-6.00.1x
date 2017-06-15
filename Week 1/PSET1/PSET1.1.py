s=input("Input s: ")
print("S is: " + s)
alphastring=""
lcounter=0

for x in range(len(s)-1):
    print("x is: "+str(x))
    print("s[x] is: "+s[x])
    print("s[x+1] is: "+s[x+1])
    if ord(s[x])>ord(s[x+1]):
        alphastring=alphastring+s[x]
        if lcounter>len(alphastring):
            alphastring=""
            alphastring=s[x-lcounter:lcounter]
        else:
            lcounter=0

    else:
        alphastring=alphastring+s[x]
        print("alphastring is: "+alphastring)
        lcounter+=1
        
alphastring=alphastring+s[x+1]
print(alphastring)
