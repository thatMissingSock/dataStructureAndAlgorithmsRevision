def flatten(M):
    """So the aim of this function is to take in a matrix(M) and flatten it into one singular list. The only
    conditions are that it should post it all reading each row from left to right and reading the entire matrix from
    top to bottom."""

    tempList =[]

    for row in range(len(M)):
        for column in range(len(M[0])):
            tempList.append(M[row][column])

    return tempList

M = [[1, 1], [2, 2], [3, 3]]
print(flatten(M))

M = [[1, 2, 3], [1, 2, 3]]
print(flatten(M))

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten(M))

M = [[1, 2, 3, 4]]
print(flatten(M))

M = [[1], [2], [3], [4]]
print(flatten(M))

M = [[5]]
print(flatten(M))