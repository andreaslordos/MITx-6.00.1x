s=input("Type in S: ")
x=0
counter=0


for x in range(len(s)):
    if s[x:x+3]=='bob':
        counter+=1

print("Number of times bob occurs is: "+str(counter))
