def odd_sum(x):
    """
    It should return the sum of ONLY the ODD numbers, unless it is empty then return 0
    :param x: A list
    :return: Sum of odd numbers or 0
    """
    tempOutput = 0
    if len(x) == 0:
        return 0
    else:
        for i in range(len(x)):
            if x[i] % 2 != 0:
                tempOutput += x[i]
        return tempOutput

# test code below
x = [1, 3, 2]
print(odd_sum(x), "should be 4")

x = [5]
print(odd_sum(x), "should be 5")

x = [5, 2, -3, 0, 1]
print(odd_sum(x), "should be 3")

x = [2, 4, 6, 8]
print(odd_sum(x), "should be 0")

x = []
print(odd_sum(x), "should be 0")