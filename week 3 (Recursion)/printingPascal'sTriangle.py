def pascal(n):
    """
    This one is interesting too! The aim is to recursively make a pascal triangle (please wikepedia this, it's too long
    to explain simply without a diagram).
    WE ONLY RETURN THE CURRENT REQUESTED ROW!
    KEEP IN MIND that the outside most numbers on the left and right of the traingle are ALWAYS 1's irregardless of what
    row you are looking at.
    FOR N = 0 WE RETURN [1] AND FOR N = 1 WE RETURN [1, 1]
    :param n: The total number of rows (remember, we do zero-point indexing).
    :return: A pascal triangle.
    """

    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    forcedRecursion = pascal(n - 1)

    currentRow = [None] * (n + 1)

    for i in range(len(currentRow)):
        if i == 0:
            currentRow[i] = 1
        elif i == n:
            currentRow[i] = 1
        else:
            currentRow[i] = (forcedRecursion[i] + forcedRecursion[i - 1])
    return currentRow

# test code provided by me :)
# Test cases for pascal(n)

n = 0
print(f"{pascal(n)} should be [1]")

n = 1
print(f"{pascal(n)} should be [1, 1]")

n = 2
print(f"{pascal(n)} should be [1, 2, 1]")

n = 3
print(f"{pascal(n)} should be [1, 3, 3, 1]")

n = 4
print(f"{pascal(n)} should be [1, 4, 6, 4, 1]")

n = 5
print(f"{pascal(n)} should be [1, 5, 10, 10, 5, 1]")

n = 6
print(f"{pascal(n)} should be [1, 6, 15, 20, 15, 6, 1]")

n = 10
print(f"{pascal(n)} should be [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]")
