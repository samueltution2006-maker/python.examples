def calculateSquare(n, f):
    return n*f


numbers = (7, 2, 6, 4)
numbers1 = (1, 2, 3, 4)
result = map(calculateSquare, numbers, numbers1)
print(result)


# converting map object to set
numbersSquare = list(result)  #{ sorted(numbersSquare)
print(numbersSquare)