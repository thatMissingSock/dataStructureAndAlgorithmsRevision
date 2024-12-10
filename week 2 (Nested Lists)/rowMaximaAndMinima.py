def row_min_max(M):
    """So the challenge for this one is that the function takes in an argument matrix(M) and outputs pairs in another
    matrix. The pairs are made up of the highest and lowest numbers in each of the rows of the inputted matrix"""
    tempMatrix = []
    tempList = []
    for row in range(len(M)):
        tempLowest = M[row][0]
        tempHighest = M[row][0]
        for column in range(len(M[0])):
            if (tempHighest < M[row][column]):
                tempHighest = M[row][column]
            if (tempLowest > M[row][column]):
                tempLowest = M[row][column]
        tempList.append(tempLowest)
        tempList.append(tempHighest)
        tempMatrix.append(tempList)

        tempList = []
    return (tempMatrix)



# this is just the testing grounds and should be ignored
test1 = [[1,7,4,1], [8,2,0,8], [3,6,2,5]]
print(row_min_max(test1))
# print(min(test1[0], test1[0]))
# this doesn't work so the only over way is to iterate using an if loop