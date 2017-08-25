def print_without_vowels(s):
    vowels="aeiouAEIOU"
    x=0
    while x<len(s):
        if s[x] in vowels:
            s=s[:x]+s[x+1:]
            x-=1
        x+=1
    print(s)
