s='xoumokpupgtwpgnox'
winner=s[0]
s=s[1:]
realwinner=""
x=0
while x<=(len(s)-1):
    print("x is: "+str(x))
    print("s is: "+str(s))
    print("s[x] is: "+s[x])
    if winner[-1]<=s[x]:
        winner=winner+s[x]
    else:
        if len(winner)>len(realwinner):
            realwinner=winner
        winner=""
        s=s[x:]
        x=0
        winner=s[0]
    print("Winner: "+winner)
    print("Real winner: "+realwinner)
    x+=1
    print("---------------------")

if realwinner=="":
    realwinner=winner

if len(winner)>len(realwinner):
    realwinner=winner

print("Winner is: "+winner)
print("Real winner is: "+realwinner)
