from collections import Counter

def palindromeRearranging(s):
    return sum(c % 2 for c in Counter(s).values()) <= 1  
