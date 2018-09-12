def isLucky(n):
    a = str(n)
    first_half = a[0:len(a)//2]
    second_half = a[len(a)//2:len(a)]
    count = 0
    count2 = 0
    for c in first_half:
        count += int(c)
    for c in second_half:
        count2 += int(c)
        
    return count == count2
