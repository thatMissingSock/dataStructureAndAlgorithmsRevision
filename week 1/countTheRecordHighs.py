def records(x):
    """
    This should iterate through a NON-EMPTY list and tell you how many elements were bigger than ALL previous
    :param x: A list
    :return: A value representing the number of times it was bigger than previous
    """
    tempOutput = 0
    tempHighest = x[0]
    count = 0
    for i in range(len(x)):
        if x[i] > tempHighest:
            count = 1
            tempHighest = x[i]
        elif x[i] < tempHighest:
            count += 1


# test code below
x = [4, 3, 2, 1]
print(records(x), "should be 1")

x = [2, 4, 3, 2, 1]
print(records(x), "should be 2")

x = [2, 3, 4, 3, 2, 1]
print(records(x), "should be 3")

x = [1, 2, 3, 4]
print(records(x), "should be 4")

x = [5]
print(records(x), "should be 1")