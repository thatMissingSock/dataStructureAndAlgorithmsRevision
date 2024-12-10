def get_from_rows(M, ids):
    """So the main purpose of this function is to take in a matrix(M) and another integer(ids) which acts as the
    indices that we will use to output a matrix for each number. So if the matrix is [[1,2,3],[4,5,6],[7,8,
    9]] and the indices were [0,1,2] then the output should be [1.5.9]. ALWAYS assume that the ids will be a list and
    that the output will always be a single list."""
    IDSCount = 0
    tempList = []
    for IDSRow in range(len(ids)):
        tempCheck = ids[IDSRow]
        tempList.append(M[IDSCount][tempCheck])
        IDSCount += 1
    return tempList


test1 = [[1,7,4,1], [8,2,0,8], [3,6,2,5]]
print(get_from_rows(test1, [0,3,1]))