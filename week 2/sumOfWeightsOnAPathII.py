def sum_path(M, vs):
    """
    This should take in a matrix (M) and a list of vertices (vs) and return the sum of the edges BUT if ANY of the values
    in the edges are None then you should IMMEDIATELY return None.
    :param M: A matrix.
    :param vs: A list of vertices.
    :return: The sum of edges OR None.
    """
    tempTotal = 0

    for i in range(1, len(vs)):
        if M[vs[i - 1]][vs[i]] == None:
            tempTotal = None
            break
        tempSummed = M[vs[i - 1]][vs[i]]
        tempTotal = tempTotal + tempSummed

    return tempTotal

# test code below
M = [[1, 2, 3], [4, None, 6], [7, 8, 9]]

vs = [0, 1]
print(sum_path(M, vs), "should be", 2)

vs = [1, 2]
print(sum_path(M, vs), "should be", 6)

vs = [2, 0]
print(sum_path(M, vs), "should be", 7)

vs = [0, 1, 2]
print(sum_path(M, vs), "should be", 2 + 6)

vs = [0, 1, 2, 0]
print(sum_path(M, vs), "should be", 2 + 6 + 7)

vs = [2, 2, 2, 2]
print(sum_path(M, vs), "should be", 9 + 9 + 9)

vs = [0, 0, 1, 2, 2]
print(sum_path(M, vs), "should be", 1 + 6 + 9)

vs = [1, 1]
print(sum_path(M, vs), "should be", None)

vs = [0, 0, 1, 1, 2, 2]
print(sum_path(M, vs), "should be", None)