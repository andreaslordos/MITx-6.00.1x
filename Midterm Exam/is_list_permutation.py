'''
Write a Python function that takes in two lists and calculates whether they are permutations of each other. The lists can contain both integers and strings. We define a permutation as follows:

the lists have the same number of elements
list elements appear the same number of times in both lists
If the lists are not permutations of each other, the function returns False. 
If they are permutations of each other, the function returns a tuple consisting of the following elements:

the element occuring the most times
how many times that element occurs
the type of the element that occurs the most times
If both lists are empty return the tuple (None, None, None). If more than one element occurs the most number of times, you can return any of them.

'''

def is_list_permutation(L1, L2):
    if len(L1) != len(L2):
        return False
    if len(L1) == 0:
        return (None, None, None)
    freq1 = {}  
    freq2 = {}  
    for i in range(len(L1)):
        freq1[L1[i]] = freq1.get(L1[i], 0) + 1
        freq2[L2[i]] = freq2.get(L2[i], 0) + 1
    if freq1 != freq2:
        return False
    for key in freq1.keys():
        max_freq = freq1[key]
        max_freq_item = key
        max_type = type(key)
        break
    for key in freq1.keys():
        if freq1[key] > max_freq:
            max_freq = freq1[key]
            max_freq_item = key
            max_type = type(key)
    return (max_freq_item, max_freq, max_type)
