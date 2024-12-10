def is_symm(M):
    """So the aim of this function is to check if the SQUARE MATRIX(M) is symmetrical but going from vertices 2 to 3
    (slicing as if using a fowardslash  ). It's an odd one because I don't know how one would check it as you CANNOT
    just check if there is an equal distribution of numbers as an example states that it does not work."""
    tempRowNum = 0
    tempColumnNum = 0
    elementAmount = (len(M) * len(M))
    isSymmetrical = True

    for row in range(len(M)):
        if (isSymmetrical == False):
            return isSymmetrical
        else:
            for column in range(len(M[0])):
                firstCheck = M[row][column]
                secondCheck = M[column][row]
                if (firstCheck != secondCheck):
                    isSymmetrical = False

    return isSymmetrical

M = [[1, 2], [2, 1]]
print(is_symm(M))

M = [[1, 1], [1, 1]]
print(is_symm(M))

M = [[1, 0], [1, 0]]
print(is_symm(M))

M = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print(is_symm(M))

M = [[1, 2, 3], [2, 4, 5], [3, -5, 6]]
print(is_symm(M))

M = [[1]]
print(is_symm(M))