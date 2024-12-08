def add_prev(x, n):
    """
    So this takes in a NON-EMPTY list and adds n to the first value then adds the value of x[i] to its successor.
    KEEP IN MIND, according to the example it only adds it AFTER n has been added!
    :param x: Non-empty list
    :param n: A value
    :return: An updated list
    """
    for i in range(len(x)):
        if i == 0:
            x[i] += n
        else:
            x[i] += x[i - 1]


# test code below
x = [1]
add_prev(x, 6)
print(x, "should be [7]")

x = [2, 1, 1, 2]
add_prev(x, 0)
print(x, "should be [2, 3, 4, 6]")

x = [2, 1, 1, 2]
add_prev(x, 10)
print(x, "should be [12, 13, 14, 16]")

x = [1, 2, 3, 4]
add_prev(x, 5)
print(x, "should be [6, 8, 11, 15]")

x = [2, 0, 0, 0]
add_prev(x, 3)
print(x, "should be [5, 5, 5, 5]")

x = [4, -1, 2, -2, 3]
add_prev(x, -3)
print(x, "should be [1, 0, 2, 0, 3]")