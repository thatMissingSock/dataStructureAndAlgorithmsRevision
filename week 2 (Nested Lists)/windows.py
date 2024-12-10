def window(M, r1, c1, w, h):
    """The aim of this is to take in a matrix(M) and 4 integers(r1, c1, w and h) and output a new matrix. r1 and c1
        are the coordinates that we use as the satrting point for the new matrix (0,0 would bee the top right). We then
        use w(width) and h(height) as the parameters for how long and tall the new matrix needs to be.
        [[1], [2], [3]
         [4], [5], [6]
         [7], [8], [9]] is a matrix and asking for [0][0] 2,2 should output [[1],[2],[4],[5]]"""
    rowCount = 0
    columnCount = 0
    startingR1 = r1
    startingC1 = c1
    tempList = []
    tempMatrix = []
    while (rowCount < h):
        while (columnCount < w):
            tempList.append(M[startingR1][startingC1])
            columnCount += 1
            startingC1 += 1
        tempMatrix.append(tempList)
        tempList = []
        rowCount += 1
        startingR1 += 1
        startingC1 = c1
        columnCount = 0
    return tempMatrix

# test cases

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = window(M, 0, 0, 2, 2)
print(N)

N = window(M, 1, 1, 2, 2)
print(N)

N = window(M, 2, 1, 2, 1)
print(N)

N = window(M, 0, 1, 1, 3)
print(N)

N = window(M, 2, 0, 3, 1)
print(N)

#A very small window
N = window(M, 2, 2, 1, 1)
print(N)
