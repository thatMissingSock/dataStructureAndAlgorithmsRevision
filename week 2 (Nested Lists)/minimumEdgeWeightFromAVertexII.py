def min_edge_weight(M, i):
    """
    This is the same thing, we check the edges of all those connected to the vertex (i) but instead we have to account for
    the possibility of None. If it is None then we ignore it and go to the next one UNLESS THE VERTEX HAS NO EDGES, in
    that case we return None.
    :param M: An adjacency matrix.
    :param i: A vertex.
    :return: The smallest edge OR None.
    """
    smallestWeight = None

    for column in range(len(M)):
        if smallestWeight == None:
            if M[i][column] != None:
                smallestWeight = M[i][column]
        else:
            if M[i][column] != None:
                if smallestWeight > M[i][column]:
                    smallestWeight = M[i][column]

    return smallestWeight

# test code below (given by gpt)
# Example adjacency matrix with None values
M = [
    [None, 3, None, 8],
    [6, None, 5, None],
    [None, None, None, 6],
    [4, None, 2, 0]
]

print(min_edge_weight(M, 0), "should be", 3)  # Minimum edge weight for row 0
print(min_edge_weight(M, 1), "should be", 5)  # Minimum edge weight for row 1
print(min_edge_weight(M, 2), "should be", 6)  # Minimum edge weight for row 2
print(min_edge_weight(M, 3), "should be", 0)  # Minimum edge weight for row 3

# Additional test cases
M2 = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
print(min_edge_weight(M2, 0), "should be", None)  # No edges present
print(min_edge_weight(M2, 1), "should be", None)  # No edges present
print(min_edge_weight(M2, 2), "should be", None)  # No edges present

M3 = [
    [None, 2, 3],
    [None, None, None],
    [4, None, 0]
]
print(min_edge_weight(M3, 0), "should be", 2)  # Minimum edge weight for row 0
print(min_edge_weight(M3, 1), "should be", None)  # No edges present
print(min_edge_weight(M3, 2), "should be", 0)  # Minimum edge weight for row 2
