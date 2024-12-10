def immed_reps(x):
    """
    Checks if the current element matches the one previous and returns how many times this actually occurs.
    :param x: A list
    :return: A value of how many times it matches the value straight after
    """
    tempOutput = 0
    for i in range(1, len(x)):
        if x[i] == x[i - 1]:
            tempOutput += 1
    return tempOutput


# test code below
x = [3, 3, 3]
print(immed_reps(x), "should be 2")

x = [1, 3, 3, 3, 3, 3]
print(immed_reps(x), "should be 4")

x = [3, 3, 1, 4, 4, 1, 5, 5]
print(immed_reps(x), "should be 3")

x = [1, 2, 1, 3, 1, 4]
print(immed_reps(x), "should be 0")

x = [5]
print(immed_reps(x), "should be 0")

x = []
print(immed_reps(x), "should be 0")