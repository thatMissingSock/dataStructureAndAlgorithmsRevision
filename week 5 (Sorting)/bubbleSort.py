
# THIS IS NOT THE QUESTION, these are used to answer the quiz inside bubbleSort

# this is boilerplate bubbleSort, nothing special just to be adapted based on the quiz
def bsort(x):
    """
    This is just used to bubble sort, which means to sort in ascending order by ONLY checking n and n-1 and then swapping.
    :param x: A list of numbers.
    :return: A sorted list of numbers.
    """
    for j in range(len(x)):
        didASwap = False
        for i in range(1, len(x)):
            if x[i] < x[i-1]:
                x[i-1], x[i] = x[i], x[i-1]
                didASwap = True
        if didASwap is not True:
            break
    return x

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def bsortStepCount(x):
    """
    This is just used to bubbleSort and tell you how many steps it took through the list.
    :param x: A list of numbers.
    :return: A sorted list of numbers.
    """
    count = 0
    for j in range(len(x)):
        didASwap = False
        for i in range(1, len(x)):
            if x[i] < x[i-1]:
                x[i-1], x[i] = x[i], x[i-1]
                didASwap = True
        if didASwap is not True:
            break
        count += 1
    return count

# test code based on the questions :)
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(bsortStepCount([1, 2, 3, 4, 5, 6, 8, 7]))
print(bsortStepCount([1, 2, 3, 4, 6, 7, 5, 8]))
print(bsortStepCount([2, 3, 4, 5, 1, 6, 7, 8]))
print(bsortStepCount([2, 3, 1, 5, 6, 7, 4, 8]))
print(bsortStepCount([2, 3, 4, 5, 6, 7, 8, 1]))
print(bsortStepCount([8, 7, 6, 5, 4, 3, 2, 1]))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bsortSwapCount(x):
    """
    This is just used to count the number of swaps that occur.
    :param x: A list of numbers.
    :return: A sorted list of numbers.
    """
    count = 0
    for j in range(len(x)):
        didASwap = False
        for i in range(1, len(x)):
            if x[i] < x[i-1]:
                x[i-1], x[i] = x[i], x[i-1]
                didASwap = True
                count += 1
        if didASwap is not True:
            break
    return count

# test code based on the question :0
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(bsortSwapCount([5, 4, 3, 2, 1]))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def bsortShowSteps(x):
    """
    This is just used to show each step in the bubbleSort.
    :param x: A list of numbers.
    :return: A sorted list of numbers.
    """
    for j in range(len(x)):
        didASwap = False
        for i in range(1, len(x)):
            if x[i] < x[i-1]:
                x[i-1], x[i] = x[i], x[i-1]
                didASwap = True
                print(x)
        if didASwap is not True:
            break
    print("This just shows a repeat since its printed the last step but then we ask it to print again once more.")
    return x

# test code based on the questions ;-;
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(bsortShowSteps([2, 6, 3, 5, 1, 4]))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# THIS IS JUST ASKING US TO CREATE A FUNCTION CALLED 'bsort' WHICH I'VE ALREADY DONE :P

# def bsort(x):
#     """
#     This is just used to bubble sort, which means to sort in ascending order by ONLY checking n and n-1 and then swapping.
#     :param x: A list of numbers.
#     :return: A sorted list of numbers.
#     """
#     for j in range(len(x)):
#         didASwap = False
#         for i in range(1, len(x)):
#             if x[i] < x[i-1]:
#                 x[i-1], x[i] = x[i], x[i-1]
#                 didASwap = True
#         if didASwap is not True:
#             break
#     return x

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# YES IT DOES, my code has a break statement that checks to see if the list is already sorted or not so the more sorted
# something is then the quicker the code can and will run. In addition to this, the best time complexity is O(n) because
# we have to iterate through each variable BUT if we have nested lists then the time complexity jumps to O(n^2),

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# THIS IS JUST ASKING US TO CREATE AN EFFICIENT FUNCTION CALLED 'bsort' WHICH I'VE ALREADY DONE :P

# def bsort(x):
#     """
#     This is just used to bubble sort, which means to sort in ascending order by ONLY checking n and n-1 and then swapping.
#     :param x: A list of numbers.
#     :return: A sorted list of numbers.
#     """
#     for j in range(len(x)):
#         didASwap = False
#         for i in range(1, len(x)):
#             if x[i] < x[i-1]:
#                 x[i-1], x[i] = x[i], x[i-1]
#                 didASwap = True
#         if didASwap is not True:
#             break

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# THIS IS ASKING TO ORDER THE LISTS IN THE FEWEST AMOUNT OF STEPS SO WE JUST CALL ON 'bsortStepCount' and rank it. I added
# a lil more code cuz I'm extra and lazy
def bsortStepCountNOALIASING(x):
    """
    This is just used to bubbleSort and tell you how many steps it took through the list. WITHOUT ALIASING.
    :param x: A list of numbers.
    :return: A sorted list of numbers.
    """
    xCopy = x[:]
    count = 0
    for j in range(len(xCopy)):
        didASwap = False
        for i in range(1, len(xCopy)):
            if x[i] < x[i-1]:
                xCopy[i-1], xCopy[i] = xCopy[i], xCopy[i-1]
                didASwap = True
        if didASwap is not True:
            break
        count += 1
    return count
bigList = [[1, 2, 3, 4, 6, 7, 5, 8], [2, 3, 4, 5, 6, 7, 8, 1], [2, 3, 4, 5, 1, 6, 7, 8], [1, 2, 3, 4, 5, 6, 8, 7], [2, 3, 1, 5, 6, 7, 4, 8], [1, 2, 3, 4, 5, 6, 7, 8]]
sortedBigList = sorted(bigList, key=bsortStepCountNOALIASING)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(sortedBigList)
