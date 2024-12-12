# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question N/A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from itertools import count


def selectionSort(x):
    """
    The following is my code at doing selectionSorting. It is a standard boilerplate to be adapted for the later questions.
    :param x: A list.
    :return: A sorted list.
    """
    xCopy = x[:]
    for i in range(len(x)):
        tempCopy = xCopy[i:]
        minimumValue = tempCopy[0]
        indexValue = 0
        for j in range(len(tempCopy)):
            if tempCopy[j] < minimumValue:
                minimumValue = tempCopy[j]
                indexValue = j
        xCopy[indexValue + i], xCopy[i] = xCopy[i], xCopy[indexValue + i]
    return xCopy


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
FORENOTE: for some reason his order that he has in codio is in reverse order. By that I mean he does selection sort in 
reverse staring at x[-1] instead of x[0]. 
From multiple sources (GPT, stackOverflow and freeCodeCamp) they state that selection swap USUALLY starts from left to
right (x[0]) instead of right to left (x[-1]).
So urhh my code works just reverse the order :P
"""
def selectionSortShowSteps(x):
    """
    The following is my code at doing selectionSorting but by also showing the steps after each sort.
    :param x: A list.
    :return: A sorted list.
    """
    xCopy = x[:]
    print(xCopy)
    for i in range(len(x)):
        tempCopy = xCopy[i:]
        minimumValue = tempCopy[0]
        indexValue = 0
        for j in range(len(tempCopy)):
            if tempCopy[j] < minimumValue:
                minimumValue = tempCopy[j]
                indexValue = j
        xCopy[indexValue + i], xCopy[i] = xCopy[i], xCopy[indexValue + i]
        print(xCopy)
    print("This will show a repeat, I apologise.")
    return xCopy
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(selectionSortShowSteps([2, 6, 3, 5, 1, 4]))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
I DID THIS ALREADY IN QUESTION N/A
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
NAH NOT REALLY! The time complexity of selectionSort is usually O(n^2) irregardless of if there are nested lists or if 
the list is nearly organised or not. This is because the code iterates through the number of elements (n) and then again
inside that iteration (which can be represented as n X n or n^2).
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
The answer to this one is ALMOST ALWAYS BE n - 1, because we iterate through each value and swap by the smallest value. 
Since the last value will ALWAYS be the biggest we don't need to swap it. In my code the only exception is if the number 
is already in the right place, since it won't need to swap it.
"""

def selectionSortSwapCount(x):
    """
    The following is my code at doing selectionSorting but we are counting the number of steps.
    :param x: A list.
    :return: A sorted list.
    """
    xCopy = x[:]
    count = 0
    for i in range(len(x)):
        tempCopy = xCopy[i:]
        minimumValue = tempCopy[0]
        indexValue = 0
        for j in range(len(tempCopy)):
            if tempCopy[j] < minimumValue:
                minimumValue = tempCopy[j]
                indexValue = j
                count += 1
        xCopy[indexValue + i], xCopy[i] = xCopy[i], xCopy[indexValue + i]
    return count

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(selectionSortSwapCount([2, 6, 3, 5, 1, 4]))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
In this one he wants us to create a function that does it the opposite which in my case is his original (??) since my 
selection swap finds the smallest and puts it in the front and his one finds the largest and puts it at the end (??).
I mean after doing it, kinda makes a lil more sense in regards to the time complexity but that's about it.
"""
def selectionSortOpposite(x):
    """
    The following is my code at doing selectionSorting but opposite to my original method which is the proffesor's
    normal method (??).
    :param x: A list.
    :return: A sorted list.
    """
    # xCopy = x[:]
    # for i in range(len(x)):
    #     tempCopy = xCopy[i:]
    #     minimumValue = tempCopy[0]
    #     indexValue = 0
    #     for j in range(len(tempCopy)):
    #         if tempCopy[j] < minimumValue:
    #             minimumValue = tempCopy[j]
    #             indexValue = j
    #     xCopy[indexValue + i], xCopy[i] = xCopy[i], xCopy[indexValue + i]
    # return xCopy

    xCopy = x[:]
    count = 0
    for i in range(len(x), -1, -1):
        # tempCopy = xCopy[start:stop:step]
        tempCopy = xCopy[:i]
        if len(tempCopy) == 1:
            break
        maximumValue = tempCopy[0]
        indexValue = 0
        for j in range((len(tempCopy) - 1), -1, -1):
            if tempCopy[j] > maximumValue:
                maximumValue = tempCopy[j]
                indexValue = j
        xCopy[indexValue], xCopy[i - 1] = xCopy[i - 1], xCopy[indexValue]
        count += 1
    return xCopy

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(selectionSortOpposite([2, 6, 3, 5, 1, 4]))



