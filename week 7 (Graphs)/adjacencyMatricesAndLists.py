def adj_mat2list(M):
    """
    This function should take in an adjacency matrix(M) of an UNWEIGHTED graph (meaning only 1's and 0's) and it should
    return a corresponding adjacency list.
    :param M: An adjacency matrix.
    :return: An adjacency list.
    """
    tempAdjacencyList = []
    for i in range(len(M)):
        tempAdjacencyList.append([])

    for row in range(len(M)):
        for column in range(len(M[0])):
            if M[row][column] == 1:
                tempAdjacencyList[row].append(column)

    return tempAdjacencyList

def adj_list2mat(L):
    """
    This function does the reverse of the function above. It takes in an adjacency list and then returns an unweighted
    adjacency matrix.
    :param L: An adjacency list.
    :return: An adjacency matrix.
    """
    tempMatrix = [None] * len(L)
    for i in range(len(L)):
        tempMatrix[i] = ([0] * len(L))

    for row in range(len(L)):
        if L[row] != []:
            for column in range(len(L[row])):
                tempMatrix[row][L[row][column]] = 1
        temp = L[row]

    return tempMatrix


# test code provided by Faris but slightly adjusted by me :)
M1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
L1 = [[0], [1], [2]]
print(f"{adj_mat2list(M1)}\nshould be:\n{L1}")

M2 = [[1, 1, 0], [1, 1, 1], [0, 0, 0]]
L2 = [[0, 1], [0, 1, 2], []]
print(f"\n{adj_mat2list(M2)}\nshould be:\n{L2}")

M3 = [[0, 0, 1], [1, 1, 0], [0, 1, 0]]
L3 = [[2], [0, 1], [1]]
print(f"\n{adj_mat2list(M3)}\nshould be:\n{L3}")

print(f"\n{adj_list2mat(L1)}\nshould be:\n{M1}")
print(f"\n{adj_list2mat(L2)}\nshould be:\n{M2}")
print(f"\n{adj_list2mat(L3)}\nshould be:\n{M3}")