def adjacentElementsProduct(inputArray):
    result = []
    for c in range(len(inputArray) - 1):
        result.append(inputArray[c] * inputArray[c + 1])
    return max(result)
