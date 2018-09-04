def makeArrayConsecutive2(statues):
    n = []

    for i in range(min(statues), max(statues)+1):
        if i not in statues:
            n.append(i)
        
    return len(n)
