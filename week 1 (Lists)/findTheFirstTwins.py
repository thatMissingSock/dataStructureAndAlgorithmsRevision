def find_first_twins(x):
    """
    This code should return the index of the FIRST number which matches the value of the number after it.
    :param x: A list
    :return: An index
    """
    for i in range(len(x) - 1):
        if x[i] == x[i + 1]:
            return i
    return -1
# test code below

x = [5, 6, 7, 7, 8, 8]
n = find_first_twins(x)
print(n, "should be 2")
print(x[n], "should be 7")
print(x[n + 1], "should also be 7")

x = [4, 4, 3, 3, 2]
n = find_first_twins(x)
print(n, "should be 0")
print(x[n], "should be 4")
print(x[n + 1], "should also be 4")

x = [6, 8, 6, 8, 6]
n = find_first_twins(x)
print(n, "should be -1")

x = [7]
n = find_first_twins(x)
print(n, "should be -1")

x = []
n = find_first_twins(x)
print(n, "should be -1")