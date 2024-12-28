def show(M):
    print("\n".join(map(str, M)))

def fw(M):
    """
    This function should take in an adjacency matrix for an UNWEIGHTED graph(M) and should return a new adjacency matrix
    showing all the possibilities of movement using the "FLOYD-WARSHALL ALGORITHM". Technically, because it is unweighted,
    the new matrix should just be n*n with the values full of 1 but the aim of this is to do it using the person's algorithm.
    :param M: An adjacency matrix.
    :return: A new updated matrix.

    The following is the pseudocode to the algorithm:

    n = no of vertices
    A = matrix of dimension n*n
    for k = 1 to n
        for i = 1 to n
            for j = 1 to n
                Ak[i, j] = min (Ak-1[i, j], Ak-1[i, k] + Ak-1[k, j])
    return A
    """
    n = len(M) # this is the number of vertices
    tempMatrix = [[None] * n] * n
    for k in range(n):
        for i in range(n):
            for j in range(n):
                tempMatrix[i,j] = min(j)


# the following is test code provided by Faris
M = [
  [0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0],
]

print("After fw(M), M should all be 1s:")
fw(M)
show(M)
