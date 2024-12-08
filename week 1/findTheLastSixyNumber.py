def find_last_sixy(x):
    """
    The aim is to return the index of the LAST number that CONTAINS a 6 NOT A FACTOR OF 6.
    :param x: A list
    :return: An index
    """
    for i in reversed(range(len(x))):
        tempString = str(x[i])
        for j in range(len(tempString)):
            if tempString[j] == "6":
                return i
    return -1

# test code
x = [6, 8, 16, 18, 24]
n = find_last_sixy(x)
print(n, "should be 2")
print(x[n], "should be 16")
print(x, "should still be [6, 8, 16, 18, 24]")

x = [666, 69, 55]
n = find_last_sixy(x)
print(n, "should be 1")
print(x[n], "should be 69")

x = [555, 444, 333]
n = find_last_sixy(x)
print(n, "should be -1")

x = []
n = find_last_sixy(x)
print(n, "should be -1")
