def gate(M, min, max):
    """So the aim of this function is to take in a matrix(M) and two POSITIVE INTEGERS(min and max). It should then
    check if the elements(THEIR ABSOLUTE VAUES) inside the matrix are inside the said range, if so they are left
    alone and ANY THAT ARE NOT are changed to 0. If either min or max have the value of 'None' then this condition is
    ignored, and we just change the value that is too small or too big. MAJOR CORRECTION, so it changes the value to
    0 even if there isn't both an upper and lower limit BUT the condition of the absolute value ONLY affects the
    function when there is BOTH limits applied :)"""

    tempList = []
    tempMatrix = []
    upperLimit = True
    lowerLimit = True

    if (min == None):
        lowerLimit = False
    if (max == None):
        upperLimit = False

    # this is to check in case there are no limits to both the min and max
    if (lowerLimit == False and upperLimit == False):
        for row in range(len(M)):
            for column in range(len(M[0])):
                tempList.append(M[row][column])
            tempMatrix.append(tempList)
            tempList = []
    else:
        # this statement is only doing it if there is an UPPER LIMIT
        if (lowerLimit == False):
            for row in range(len(M)):
                for column in range(len(M[0])):
                    if (M[row][column] > max):
                        M[row][column] = 0
                    tempList.append(M[row][column])
                tempMatrix.append(tempList)
                tempList = []
        # the following is only doing if it there is a LOWER LIMIT
        elif (upperLimit == False):
            for row in range(len(M)):
                for column in range(len(M[0])):
                    if (M[row][column] < min):
                        M[row][column] = 0
                    tempList.append(M[row][column])
                tempMatrix.append(tempList)
                tempList = []
        # the following is if there is BOTH AN UPPER AND LOWER LIMIT.
        # THE RULES ARE if the number is within the range it is left alone else it is changed to 0
        else:
            for row in range(len(M)):
                for column in range(len(M[0])):
                    if (abs(M[row][column]) > max or abs(M[row][column]) < min):
                        M[row][column] = 0
                    tempList.append(M[row][column])
                tempMatrix.append(tempList)
                tempList = []
    return tempMatrix

# test code below
M = [[1, -2, 3, -4, 5, -6, 7, -8]]
gate(M, 4, 5)
print(M, "should now be", [[0, 0, 0, -4, 5, 0, 0, 0]])

M = [[1, -2, 3, -4, 5, -6, 7, -8]]
gate(M, 2, 5)
print(M, "should now be", [[0, -2, 3, -4, 5, 0, 0, 0]])

M = [[-4, -2], [4, 6]]
gate(M, 3, 5)
print(M, "should now be", [[-4, 0], [4, 0]])

M = [[-5, 4, -3], [-4, 3, -2]]
gate(M, 2, 3)
print(M, "should now be", [[0, 0, -3], [0, 3, -2]])