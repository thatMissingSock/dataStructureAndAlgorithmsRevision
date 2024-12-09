def rec_ruler(n):
    """
    WE ASSUME N >= 1. This function should return a list based on the value of n.
    n = 1: [1]
    n = 2: [1, 2, 1]
    n = 3: [1, 2, 1, 3, 1, 2, 1]
    n = 4: [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]
    The value of n is in the middle whilst adding the values from n - 1 to its left and right in the list.
    (I'M SORRY I CANNOT EXPLAIN THIS ANY BETTER).
    :param n:
    :return:
    """
    # look I know we said we assume n >= 1, but I was being extra, the base case can indeed be 1 :)

    if n == 0:
        return []

    forcedRecursion = rec_ruler(n - 1)

    return forcedRecursion +  [n] + forcedRecursion

# test code below provided by me :)

n = 1
print(f"{rec_ruler(n)} should be \n[1]")

n = 2
print(f"{rec_ruler(n)} should be \n[1, 2, 1]")

n = 3
print(f"{rec_ruler(n)} should be \n[1, 2, 1, 3, 1, 2, 1]")

n = 4
print(f"{rec_ruler(n)} should be \n[1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]")
# Expected output: [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]

n = 5
expected = [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]
print(f"{rec_ruler(n)} should be \n{expected}")



