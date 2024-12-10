def tilings(x, n):
    """
    THIS ONE IS BLOODY HARD, I THINK.
    The aim of this function is that when given a list of DISTINCT integers (x) and a positive integer (n) can you return
    a list of ways the numbers inside x can sum to equate n. If not, then you just return and empty list like this [[]].
    If x = [1,2] and n = 3, then you'd get:
    [[1, 1, 1], [1, 2]].
    THIS MUST BE DONE RECURSIVELY KEEP IN MIND.
    :param x: A list of distinct integers.
    :param n: A positive integer.
    :return: A list containing all possibilities to sum each distinct integer to make n.
    """

# ~~~~~~~~~~~~~~~~~~~~~~I COULDN'T FIGURE THIS ONE OUT, HIS SOLUTION DOESN'T WORK EITHER~~~~~~~~~~~~~~~~~~~~~~


    # tempSolutions = []
    #
    # for firstTile in x:
    #     restOfTiles = tilings(x, n - firstTile)
    #     for leftoverTiles in restOfTiles:
    #         tempSolutions.append([firstTile] + leftoverTiles)
    # return tempSolutions



# test code provided by GPT
# Test cases for tilings(x, n)

# Base case: x = [1] and n = 0
x, n = [1], 0
print(f"{tilings(x, n)} should be [[]]")  # Expected output: [[]]

# Case: x = [1] and n = 1
x, n = [1], 1
print(f"{tilings(x, n)} should be [[1]]")  # Expected output: [[1]]

# Case: x = [1] and n = 3
x, n = [1], 3
print(f"{tilings(x, n)} should be [[1, 1, 1]]")  # Expected output: [[1, 1, 1]]

# Case: x = [1, 2] and n = 4
x, n = [1, 2], 4
expected = [
    [1, 1, 1, 1],
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 1],
    [2, 2],
]
print(f"{tilings(x, n)} should be {expected}")

# Case: x = [1, 2] and n = 5
x, n = [1, 2], 5
expected = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 1, 2, 1],
    [1, 2, 1, 1],
    [1, 2, 2],
    [2, 1, 1, 1],
    [2, 1, 2],
    [2, 2, 1],
]
print(f"{tilings(x, n)} should be {expected}")

# Case: x = [2, 5] and n = 13
x, n = [2, 5], 13
print(f"{tilings(x, n)} should be []")  # Expected output: []

# Case: x = [2, 3] and n = 7
x, n = [2, 3], 7
expected = [
    [2, 2, 3],
    [2, 3, 2],
    [3, 2, 2],
]
print(f"{tilings(x, n)} should be {expected}")

# Case: x = [1, 3, 4] and n = 6
x, n = [1, 3, 4], 6
expected = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 3],
    [1, 1, 3, 1],
    [1, 3, 1, 1],
    [3, 1, 1, 1],
    [1, 1, 4],
    [1, 4, 1],
    [4, 1, 1],
    [3, 3],
]
print(f"{tilings(x, n)} should be {expected}")

# Case: x = [1, 2, 3] and n = 4
x, n = [1, 2, 3], 4
expected = [
    [1, 1, 1, 1],
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 1],
    [2, 2],
    [1, 3],
    [3, 1],
]
print(f"{tilings(x, n)} should be {expected}")
