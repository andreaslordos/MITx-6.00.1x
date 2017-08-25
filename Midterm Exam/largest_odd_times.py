def largest_odd_times(L):
    L.sort()
    x=1
    occurs=1
    oddFound=False
    iterationno=1
    
    while x+1<=len(L):
        if L[-(x)]==L[-(x+1)]:
            occurs+=1
        else:
            if occurs%2!=0:
                if x!=1 and occurs!=1:
                    return(L[-x+1])
                else:
                    return(L[-x])
            else:
                occurs=1
        x+=1
        iterationno+=1

    if oddFound==False:
        return None
        
    return(None)
