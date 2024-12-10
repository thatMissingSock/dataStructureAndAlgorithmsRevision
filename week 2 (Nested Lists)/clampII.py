def clamp(M, min, max):
    """
    This takes in a matrix (M) and two integers (min and max). This checks to see if every element within the matrix is
    greater than or equal to min, if not then it replaces that value with min. It also checks if every element is
    smaller than or equal to max, if not then it replaces that value with max. IT DOES NOT DEAL WITH ABSOLUTE VALUES!
    NOTE: if either min or max are None than we ignore that parameter and just deal with the other.
    :param M:
    :param min:
    :param max:
    :return:
    """

    for row in range(len(M)):
        for column in range(len(M[0])):
            if min is not None and max is not None:
                if M[row][column] < min:
                    M[row][column] = min
                if M[row][column] > max:
                    M[row][column] = max
            elif min is not None and max is None:
                if M[row][column] < min:
                    M[row][column] = min
            elif min is None and max is not None:
                if M[row][column] > max:
                    M[row][column] = max
            else:
                break
    return M

# test code below
M = [[1, 2, 3, 4, 5, 6, 7, 8]]
clamp(M, 3, 6)
print(M, "should now be", [[3, 3, 3, 4, 5, 6, 6, 6]])

M = [[1, 2, 3, 4, 5, 6, 7, 8]]
clamp(M, None, 6)
print(M, "should now be", [[1, 2, 3, 4, 5, 6, 6, 6]])

M = [[-4, 4], [6, 1]]
clamp(M, 3, None)
print(M, "should now be", [[3, 4], [6, 3]])

M = [[-5, 4, -3], [-4, 3, -2]]
clamp(M, -3, 3)
print(M, "should now be", [[-3, 3, -3], [-3, 3, -2]])

M = [[2]]
clamp(M, 3, 7)
print(M, "should now be", [[3]])