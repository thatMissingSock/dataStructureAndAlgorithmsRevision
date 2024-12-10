def find_all(M, v):
    """So this code should take in a matrix(M) and an integer(v), then find all instances of that integer in the
    matrix outputting just the coordinates of the found integers."""
    tempRow = len(M)
    tempColumn = len(M[0])
    tempList = []
    tempMatrix = []
    rowCount = 0
    columnCount = 0

    for row in range(tempRow):
        for column in range(tempColumn):
            if (M[rowCount][columnCount] == v):
                tempList.append([rowCount, columnCount])
                tempMatrix.append(tempList)
            tempList = []
            columnCount += 1
        rowCount += 1
        columnCount = 0
    return tempMatrix

test1 = [[1,2], [2,2]]
test2 = [[5,6], [7,8]]
test3 = [[1,2,1],[1,2,1],[1,2,1],[0,0,0]]
print(find_all(test1, 2))
print(find_all(test2, 2))
print(find_all(test3, 1))