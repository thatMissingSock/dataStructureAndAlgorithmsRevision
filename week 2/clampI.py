def clamp(M, min, max):
    """So the aim of this function is take in a matrix(M) and two arguments (min and max). These arguments can EITHER
    be an integer or the value of 'None'. The function should check each element in the matrix and check to see if
    it's bigger than the max or the min and if so then to replace the element with that value. If the argument is none
    then we can assume there is no min or max value and only check for the other."""

    tempMatrix = []
    tempList = []
    lowerLimit = True
    upperLimit = True
    if (min == None):
        lowerLimit = False
    if (max == None):
        upperLimit = False

    # statement to copy the matrix and output it JUST IN CASE THERE ARE NO LIMITS
    if (upperLimit == False and lowerLimit == False):
        for row in range(len(M)):
            for column in range(len(M[0])):
                tempList.append(M[row][column])
            tempMatrix.append(tempList)
            tempList = []


    else:
        # statement to only do the check for the UPPER LIMIT
        if (lowerLimit == False):
            for row in range(len(M)):
                for column in range(len(M[0])):
                    if (M[row][column] > max):
                        M[row][column] = max
                    tempList.append(M[row][column])
                tempMatrix.append(tempList)
                tempList = []

        # statement to only do the check for the LOWER LIMIT
        elif (upperLimit == False):
            for row in range(len(M)):
                for column in range(len(M[0])):
                    if (M[row][column] < min):
                        M[row][column] = min
                    tempList.append(M[row][column])
                tempMatrix.append(tempList)
                tempList = []

        else:
            # statement in case there ARE BOTH LIMITS
            for row in range(len(M)):
                for column in range(len(M[0])):
                    if (M[row][column] > max):
                        M[row][column] = max
                    if (M[row][column] < min):
                        M[row][column] = min
                    tempList.append(M[row][column])
                tempMatrix.append(tempList)
                tempList = []
    return tempMatrix

M = [[1, 2, 3, 4, 5, 6, 7, 8]]
clamp(M, 3, 6)
print(M)

M = [[1, 2, 3, 4, 5, 6, 7, 8]]
clamp(M, None, 6)
print(M)

M = [[-4, 4], [6, 1]]
clamp(M, 3, None)
print(M)

M = [[-5, 4, -3], [-4, 3, -2]]
clamp(M, -3, 3)
print(M)

M = [[2]]
clamp(M, 3, 7)
print(M)