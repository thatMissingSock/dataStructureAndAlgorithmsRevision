def alt_sums(x):
    """
    The aim of this is to check a list and return the sum of all the even-indexed numbers as e and odd-indexed numbers as o.
    :param x: A list
    :return: A list in this format [e, o]
    """
    even = 0
    odd = 0
    for i in range(len(x)):
        if i % 2 == 0:
            even += x[i]
        else:
            odd += x[i]
    return [even, odd]

# test code below
x = [1, 5, 1, 5, 1]
y = alt_sums(x)
print(y, "should be [3, 10]")

x = [0, 1, 2, 3]
y = alt_sums(x)
print(y, "should be [2, 4]")

x = [1, -1, 1, -1, 1, -1]
y = alt_sums(x)
print(y, "should be [3, -3]")

x = [1, 2]
y = alt_sums(x)
print(y, "should be [1, 2]")

x = [5]
y = alt_sums(x)
print(y, "should be [5, 0]")

x = []
y = alt_sums(x)
print(y, "should be [0, 0]")