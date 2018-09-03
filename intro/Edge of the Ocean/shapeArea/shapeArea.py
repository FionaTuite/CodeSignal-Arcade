def shapeArea(n):
    area = 1
    i = 1 #the starting middle block
    while i < n:
        area += 4 * i #4 times the previous i eg n=2, i is starting block 1, 4 * 1 = 4 therefore                          #there should be 4 blocks added onto the starting middle block
        i+=1
        
    return area
