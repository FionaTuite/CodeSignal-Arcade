def almostIncreasingSequence(s):
    x = 0
    y = 0
    for i in range(1, len(s)-1):
        if s[i] <= s[i-1]:            
            x += 1                               
        if s[i+1]<=s[i-1]:
            y+=1            
    if s[len(s)-1]<=s[len(s)-2]:
            x+=1
    
    if x <= 1 and y<=1:
        return True
    return False
