def find_first(M, v):
    """
    This should take in a matrix (M) and a number (v) and return a list containing the coordinates of the first occurance
    of said number. If no number is found then it should just return 'None'.
    :param M: A matrix.
    :param v: A number.
    :return: A list coordinates.
    """
    coordinates = []
    coordinatesFilled = False

    for row in range(len(M)):
        if coordinatesFilled == True:
            break
        for column in range(len([0])):
            if coordinatesFilled == True:
                break
            if M[row][column] == v:
                coordinates.append(row)
                coordinates.append(column)
                coordinatesFilled = True
                break

    if len(coordinates) == 0:
        return None

    return coordinates

# test code below
M = [[1, 1], [1, 1]]
print(find_first(M, 1), "should be", [0, 0])

M = [[1, 2], [2, 1]]
print(find_first(M, 2), "should be", [0, 1])

M = [[1, 2], [3, 4], [5, 6]]
print(find_first(M, 5), "should be", [2, 0])

M = [[1, 2, 3], [4, 5, 6]]
print(find_first(M, 7), "should be", None)

M = [[1]]
print(find_first(M, 2), "should be", None)
