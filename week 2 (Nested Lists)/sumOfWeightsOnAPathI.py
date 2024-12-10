def sum_path(M, vs):
    """
    This assumes that you are given an n x n adjacency matrix (M) and a list of vertices (vs) and that you are able to give
    the sum of the weighted edges as a value. So if vs was [0, 1, 2, 0] then you give the sum of edges: 0-1, 1-2, 2-0.
    :param M: An adjacency matrix OF N X N SIZE. I THINK that if any edge is None than the sum should just be None (?).
    :param vs: A list of vertices.
    :return: A summed value of those edges.
    """

    tempTotal = 0

    for i in range(1, len(vs)):
        tempRow = vs[i - 1]
        tempColumn = vs[i]
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
print(sum_path(M, vs), "should be", 1 + 2 + 6 + 9)

vs = [1, 1]
print(sum_path(M, vs), "should be", None)

vs = [0, 0, 1, 1, 2, 2]
print(sum_path(M, vs), "should be", None)
