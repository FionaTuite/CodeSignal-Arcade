def matrixElementsSum(matrix):

    count=0
    l = []
    for row in matrix:
        for j,r in enumerate(row):
            if j not in l:
                if r == 0:
                    l.append(j)
                else :
                    count+=r
    return count
