def longest_run(x):
    """
    Should give us the longest amount of times a number is instantly repeated (including the starting 1 according to the examples)
    :param x: A list
    :return: The longest run
    """
    longestRun = 0
    currentNum = x[0]
    tempRun = 0
    for i in range(len(x)):
        if x[i] == currentNum:
            tempRun += 1
        elif x[i] != currentNum:
            if tempRun > longestRun:
                longestRun = tempRun
            tempRun = 1
            currentNum = x[i]
    return longestRun
# test code below
x = [2, 2, 2, 1, 1, 0]
print(longest_run(x), "should be 3")

x = [2, 1, 1, 1, 1, 3, 3]
print(longest_run(x), "should be 4")

x = [3, 1, 4, 1, 5, 5]
print(longest_run(x), "should be 2")

x = [2, 3, 2, 3, 2]
print(longest_run(x), "should be 1")

x = [5]
print(longest_run(x), "should be 1")