def addBorder(p):
    l = []
    length = 0
    
    for c in p:
        s =  "*" + c + "*"
        l.append(s)
        
    for c in l:
        length = len(c)
        
    stars = "*" * length
    l.insert(0,stars)
    l.append(stars)
    return l
