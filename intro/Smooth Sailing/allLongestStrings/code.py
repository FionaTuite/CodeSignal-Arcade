def allLongestStrings(inputArray):
    a = []
    b = []
    count = 0    #You set the count to 0
    for i in inputArray: # Go through the whole list
        if len(i) >= count : #Checking for the longest word(string)
            count = len(i)
            word = i
            a.append(word)
            
    for c in a:
        if len(c) >= count:
            count = len(c)
            word = c
            b.append(word)
    return(b)
