def sortByHeight(a):
    l = sorted([i for i in a if i != -1])

    for c ,i in enumerate(a):
        if i == -1:
            l.insert(c,i) # c is the position where the element i is going to be inserted.
    return(l)
