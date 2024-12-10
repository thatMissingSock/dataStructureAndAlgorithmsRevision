def adj(n, edges):
    """So the aim of this function is to take in two arguments n(a positive integer) and edges(a list). This is to do
    with graphs, and it is an unweighted graph that you input, but you then output a directed graph, but I SERIOUSLY
    don't understand it whatsoever. Regardless, I noticed that the values in list 'edges' are coordinates for where
    there should be a 1. EVERYWHERE ELSE should be a 0. The matrix I assume should use n as the values for width *
    height."""

    tempList = []
    tempMatrix = []

    for row in range(n):
        for column in range(n):
            tempList.append(0)
        tempMatrix.append(tempList)
        tempList = []

    for i in range(len(edges)):
        tempCoordinates = []
        for j in range(len(edges[0])):
            tempCoordinates.append(edges[i][j])
        count = 0
        tempMatrix[tempCoordinates[0]][tempCoordinates[1]] = 1
    return tempMatrix

# test cases
n = 5
e = [[1, 2]]
print(adj(n, e))

e = []
print(adj(n, e))

e = [[0, 1], [1, 2]]
print(adj(n, e))

e = [[0, 0], [1, 1], [2, 2]]
print(adj(n, e))

e = [[0, 1], [1, 2], [2, 1]]
print(adj(n, e))

e = [[0, 1], [1, 1], [1, 2], [2, 2]]
print(adj(n, e))