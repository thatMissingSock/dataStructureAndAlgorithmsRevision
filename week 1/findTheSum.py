def my_sum(x):
    """
    Just gives the sum of the elements, if it is empty then it returns 0
    :param x: A list
    :return: The sum of the elements or 0
    """
    tempOutput = 0
    if len(x) == 0:
        return 0
    else:
        for i in range(len(x)):
            tempOutput += x[i]
        return tempOutput

# test code below
x = [1, 2, 3]
print(my_sum(x), "should be 6")

x = [1, 2, -3]
print(my_sum(x), "should be 0")

x = [5]
print(my_sum(x), "should be 5")

x = []
print(my_sum(x), "should be 0")