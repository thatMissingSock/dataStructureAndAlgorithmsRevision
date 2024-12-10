def mat_from_row(r, m):
    """basically r is a list of numbers and m is the number of rows. The matrix should just repeat r but IT SHOULD NOT
  ALIAS"""

    tempMatrix = []
    columnCount = 0
    for row in range(m):
        tempMatrix.append([])
        for column in range(len(r)):
            tempMatrix[columnCount].append(r[column])
        columnCount += 1
    for i in range(len(tempMatrix)):
        print(tempMatrix[i])
    return (tempMatrix)

print(mat_from_row([1,2,3], 3))
