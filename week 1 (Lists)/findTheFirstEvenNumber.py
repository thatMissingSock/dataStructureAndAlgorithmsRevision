
def find_first_even(x):
    """
    It should return the INDEX of the first EVEN number in the list or return -1 to signify none was found
    :param x: A list
    :return: The index of the even number (or -1)
    """

    for i in range(len(x)):
        if (x[i] % 2 == 0):
            return i
    return -1


"""Test code here. Last time :-)"""
x = [1, 1, 1, 1, 2, 3, 4, 5]
n = find_first_even(x)
print(n, "should be 4")
print(x[n], "should be 2")
print(x, "should still be [1, 1, 1, 1, 2, 3, 4, 5]")

x = [4, 3, 2, 1, 0]
n = find_first_even(x)
print(n, "should be 0")
print(x[n], "should be 4")

x = [1, 3, 5, 3, 1]
n = find_first_even(x)
print(n, "should be -1")

x = []
n = find_first_even(x)
print(n, "should be -1")