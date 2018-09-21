def arrayMaximalAdjacentDifference(s):
    max = 0
    for i in range(len(s)-1):
        difference = abs(s[i] - s[i+1])
        print(difference)
        if difference > max:
            max = difference
            
    return max
