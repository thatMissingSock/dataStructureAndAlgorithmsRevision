def min_edge_weight(M, i):
    """
    You need to find the SMALLEST weight from vertex 'i' to anything it is linked to and return that value. You do this
    by using the adjacency matrix give 'M'.
    :param M: An adjacency matrix.
    :param i: The vertex we are checking.
    :return: The SMALLEST weight
    """

    smallestWeight = None
    for column in range(len(M)):
        if smallestWeight == None:
            smallestWeight = M[i][column]
        else:
            if smallestWeight > M[i][column]:
                smallestWeight = M[i][column]

    return smallestWeight




# test code below (none was given)
# Example adjacency matrix (provided by chatGPT)
M = [
    [9, 3, 7, 8],
    [6, 4, 5, 2],
    [1, 8, 3, 6],
    [4, 7, 2, 0]
]

print(min_edge_weight(M, 0), "should be", 3)  # Minimum edge weight for row 0
print(min_edge_weight(M, 1), "should be", 2)  # Minimum edge weight for row 1
print(min_edge_weight(M, 2), "should be", 1)  # Minimum edge weight for row 2
print(min_edge_weight(M, 3), "should be", 0)  # Minimum edge weight for row 3
