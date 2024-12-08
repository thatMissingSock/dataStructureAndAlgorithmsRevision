def gate(M, min, max):
    """
    This basically alters the values of anything that isn't inside the range to 0. If either min or max are None then we
    ignore that parameter and just deal with the other. The range should INCLUDE THE VALUES OF MIN AND MAX ALSO.
    WE DEAL WITH ABSOLUTE VALUES WHEN CHECKING!
    :param M: A matrix.
    :param min: An integer or None.
    :param max: An integer or None.
    :return: A matrix that adheres to the new range.
    """

    for row in range(len(M)):
        for column in range(len(M[0])):
            if min is not None and max is not None:
                if abs(M[row][column]) < min or abs(M[row][column]) > max:
                    M[row][column] = 0
            elif min is not None and max is None:
                if abs(M[row][column]) < min:
                    M[row][column] = 0
            elif min is None and max is not None:
                if abs(M[row][column]) > max:
                    M[row][column] = 0
            else:
                break
    return M

# test code below
M = [[1, -2, 3, -4, 5, -6, 7, -8]]
gate(M, 4, 5)
print(M, "should now be", [[0, 0, 0, -4, 5, 0, 0, 0]])

M = [[1, -2, 3, -4, 5, -6, 7, -8]]
gate(M, None, 5)
print(M, "should now be", [[1, -2, 3, -4, 5, 0, 0, 0]])

M = [[-4, 4], [6, 1]]
gate(M, 3, None)
print(M, "should now be", [[0, 4], [6, 0]])

M = [[-5, 4, -3], [-4, 3, -2]]
gate(M, 2, 3)
print(M, "should now be", [[0, 0, -3], [0, 3, -2]])