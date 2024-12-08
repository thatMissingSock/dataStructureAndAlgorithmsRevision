def list_to_mat(x, m, n):
    """
    So this takes in an existing list (x) and two integers (m and n). It uses these to give back a matrix of m x n length
    using the values within x to populate the new matrix.
    :param x: A list.
    :param m: An integer.
    :param n: An integer.
    :return: A matrix.
    """

    # note that I did it this way due to time complexity, there is a much easier way using append but because we have the
    # values given to us of the length and height of the matrix we can just create a template and swap out the values which
    # is much quicker!

    tempMatrix = [None] * m
    count = 0

    for i in range(m):
        tempMatrix[i] = [None] * n

    for row in range(m):
        for column in range(n):
            tempMatrix[row][column] = x[count]
            count += 1

    return tempMatrix



# test code below
M = list_to_mat([1, 2, 3, 4], 2, 2)
print(M, "should be", [[1, 2], [3, 4]])

M = list_to_mat([1, 2, 3, 4, 5, 6], 2, 3)
print(M, "should be", [[1, 2, 3], [4, 5, 6]])

M = list_to_mat([1, 2, 3, 4, 5, 6], 3, 2)
print(M, "should be", [[1, 2], [3, 4], [5, 6]])

M = list_to_mat([1, 2, 3, 4, 5, 6], 6, 1)
print(M, "should be", [[1], [2], [3], [4], [5], [6]])

M = list_to_mat([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
print(M, "should be", [[1, 2, 3], [4, 5, 6], [7, 8, 9]])