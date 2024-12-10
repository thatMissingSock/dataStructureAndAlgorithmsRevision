def my_max(x):
    """
    This should return the maximum number in a NON-EMPTY list. YOU CANNOT USE THE MAX FUNCTION
    :param x: A list
    :return: The maximum number
    """
    tempLargest = x[0]
    for i in range(len(x)):
        if x[i] > tempLargest:
            tempLargest = x[i]
    return tempLargest

# test cases
x = [1, 2, 3]
print(my_max(x), "should be 3")

x = [1, 2, -3]
print(my_max(x), "should be 2")

x = [3, 2, 1]
print(my_max(x), "should be 3")

x = [5]
print(my_max(x), "should be 5")