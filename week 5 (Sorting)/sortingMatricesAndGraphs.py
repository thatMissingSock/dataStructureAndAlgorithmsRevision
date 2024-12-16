# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sort_fnonzero(M):
    """
    This should take in a matrix and sort out each row based on the first NON-ZERO value found in the columns (reading
    left to right) and organsise it based on this.
    :param M: An unsorted matrix.
    :return: A sorted matrix.
    """
    def whatIsNonZero(x):
        """
        We just need to create this temp function as a key for the sorted function. All it does is iterate through each
        element in each column and returns the value of the FIRST NON-ZERO VALUE
        :param x:
        :return:
        """
        for column in range(len(x)):
            if x[column] != 0:
                return x[column]


    sortedList = sorted(M, key=whatIsNonZero)

    return sortedList


# test code provided by me :O

M = [
    [0, 0, 4, -2, 3],
    [0, 5, 4, -2, 3],
    [0, 0, 0, 1, 2],
    [0, 0, -3, 2, 5],
    ]

expected = [
    [0, 0, -3, 2, 5],
    [0, 0, 0, 1, 2],
    [0, 0, 4, -2, 3],
    [0, 5, 4, -2, 3],
    ]

print(f"The original list is: \n{M}\nSorting it using your function gives us: \n{sort_fnonzero(M)}\nand it should be: \n{expected}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def sort_echelon(M):
    """
    This is similar to above but instead of looking at the value of the first non-zero element, we look at what index it
    is found at.
    :param M: An unsorted matrix.
    :return: A sorted matrix based on the index of the first non-zero value.
    """

    def whatIsNonZeroIndex(x):
        """
        We just need to create this temp function as a key for the sorted function. All it does is iterate through each
        element in each column and returns the index of the FIRST NON-ZERO VALUE
        :param x:
        :return:
        """
        for column in range(len(x)):
            if x[column] != 0:
                return column

    sortedList = sorted(M, key=whatIsNonZeroIndex)
    return sortedList

# test code provided by me


M = [
    [0, 0, 4, -2, 3],  # First non-zero at index 2
    [0, 5, 4, -2, 3],  # First non-zero at index 1
    [0, 0, 0, 1, 2],   # First non-zero at index 3
    [0, 0, -3, 2, 5],  # First non-zero at index 2
    ]

# Sorted by index of first non-zero: 1, 2, 2, 3
expected = [
    [0, 5, 4, -2, 3],
    [0, 0, 4, -2, 3],
    [0, 0, -3, 2, 5],
    [0, 0, 0, 1, 2],
    ]

print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"The original list is: \n{M}\nSorting it using your function gives us:\n{sort_echelon(M)}\nand it should be:\n{expected}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sort_weights(M):
    """
    This function should take in the adjacency matrix of a WEIGHTED graph and return a sorted list of its edge weights.
    It does not state from lowest to highest...so we assume we go in ascending order.
    Based on the question too, we assume that all the graphs are undirected(??).
    :param M: An adjacency matrix.
    :return: A sorted list of edges based on that matrix.
    """
    tempList = []
    for row in range(len(M)):
        for column in range(len(M[0])):
            if M[row][column] != 0 and M[row][column] not in tempList:
                tempList.append(M[row][column])

    return sorted(tempList)



# test code below
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

M = [
    [0, 4, 0, 6],
    [4, 0, 5, 0],
    [0, 5, 0, 7],
    [6, 0, 7, 0],
    ]
# Edges: 4, 6, 5, 7 (undirected graph, so avoid duplicates)
expected = [4, 5, 6, 7]

print(f"The orignal UNDIRECTED and WEIGHTED adjancency matrix is: \n{M}\nThe list of the ONLY edges found on the graph based on your function is: \n{sort_weights(M)}\nand it should be: \n{expected}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sort_paths(M, p):
    """
    For this function, we are taking in an adjacency matrix(m) and a list of paths(p) that the 'walk' (walk is the list of
    vertices you can take where there is an edge) is taking. It should return a sorted list of paths based on the weight
    of the edges (ascending in value).
    NOTE: to make it harder, our code should put any edges that are invalid (not possible) first in no particular order.
    :param M: An adjacency matrix.
    :param p: An unsorted list of vertices that the walk took.
    :return: A sorted list of vertices that the walk took.
    """

    pathsTotal = [None] * len(p)
    for pathRow in range(len(p)):
        invalid = False
        tempSum = 0
        for pathColumn in range(1, len(p[pathRow])):
            tempSum += M[p[pathRow][pathColumn]][p[pathRow][pathColumn - 1]]
            if M[p[pathRow][pathColumn]][p[pathRow][pathColumn - 1]] == 0:
                invalid = True
                break
        if invalid is not True:
            pathsTotal[pathRow] = tempSum


    for i in range(len(pathsTotal)):
        if pathsTotal[i] == None:
            pathsTotal[i] = 0
            pathsTotal[i] = min(pathsTotal) - 1


    outputList = [None] * len(p)

    count = 0
    while None in outputList:
        for i in range(len(pathsTotal)):
            if pathsTotal[i] == min(pathsTotal):
                outputList[count] = p[i]
                pathsTotal[i] = (max(pathsTotal) + 1)
                count += 1
                break
    return outputList




# test code below

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
M = [
    [0, 1, 4, 0],
    [1, 0, 2, 6],
    [4, 2, 0, 3],
    [0, 6, 3, 0],
    ]
paths = [
    [0, 1, 2, 3],  # Total weight: 1 + 2 + 3 = 6
    [0, 2, 3],     # Total weight: 4 + 3 = 7
    [1, 2, 1],     # Total weight: 2 + 1 = 3
    [0, 3],        # Total weight: 0 (no edge directly)
    ]
# Sort by total weights: 3, 6, 7, 0 (invalid path)
expected = [
    [0, 3],        # Invalid path
    [1, 2, 1],     # Total weight: 3
    [0, 1, 2, 3],  # Total weight: 6
    [0, 2, 3],     # Total weight: 7
    ]

print(f"The original adjacency matrix is: \n{M}\nThe orginal path(s) is: \n{paths}\nThe sorted path(s) based on the matrix and your function is:\n{sort_paths(M, paths)}\nand it should be:\n{expected}")