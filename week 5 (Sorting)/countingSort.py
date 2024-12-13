# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question N/A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This is my attempt at writing code for any counting sort method(s).

From what I understand, there are a few steps to accomplish this:

1. The first step is to find the smallest VALUE in the list and the largest VALUE in the list and initialise them to a
variable for later use.

2. The second step is to create 2 lists. One is an empty list that consists of 0's the size of the length of the initial
unsorted list (outputList = [None] * len(inputList)).
The second list is a countingList that is the size of the range between the smallest and largest value in the list.

3. We then need to populate the list from step 2 (countList). We do this by using a for loop to iterate through each value
in the inputted list and adding 1 to that index in the countList (check the code below for further information).

4. We then need to make the countList into a cumulative count list which essentially means to do another for loop and increase
based on how big the valueRangeSize is.

5. Finally, we use the initialised lists from earlier (both the countList and outputList) to populate the output lists with
the values from the inputted array but in order. It does this by utilising the countList to see where each value should go.

Why does this work?
It's surprisingly simple.
Imagine you have 20 kids doing a quiz and the scores can range from 1-20 (you get a point for putting your name). This means
that EVERY kid will have a score ranging from 1-20 points. You now need to put them in order of highest to lowest, and the
best way to do that is to create a table/tally. After the first header is filled with 19 columns (1-20), underneath you
add 1 tally for each time a student has received that score.
Using that tally, you can then just put the scores in order, and it doesn't really matter if the same score comes before
or after because IT'S THE SAME SCORE.
If you still don't get it. Give 20 kids random scores between 1-20 and create a tally, then create an ordered list of the
scores based off of that tally.
In the question N/A part change the scores to match to the ones you gave and debug to run through the code step by step and
see how it does the same thing as you!

PLEASE NOTE: Faris' way is much simpler but both works! And my way kinda shows it a lil better when you debug :P
"""

def countingSort(x):
    """
    This function should sort a list using the count-sort method.
    :param x: An unsorted list.
    :return: A sorted list.
    """
    # step 1
    minimumValue = min(x) # this gives us the minimum value of the list
    maximumValue = max(x) # this gives us the maximum value of the list
    rangeSize = maximumValue - minimumValue + 1 # we need a +1 because of 0-point indexing

    # step 2
    outputList = [None] * len(x) # initialise the legnth of the final sorted list (we use None so if there are ANY values with None we know we done messed up)
    countList = [0] * rangeSize # initialise the countList, it's the size of the range of values found in the list

    # step 3
    for number in x: # this iterates through each element in list x
        countList[number - minimumValue] += 1 # for the index of number - minumumValue we increase it by 1 (because it means we can tally someone got this score)

    # step 4
    for i in range(1, rangeSize): # this iterates through the index of the countList (we start at 1 so the logic doesn't fail)
        countList[i] += countList[i - 1]

    # step 5
    for number in reversed(x):  # Traverse in reverse to maintain stability
        outputList[countList[number - minimumValue] - 1] = number # we add to the list 'outputList' the values inside 'x' based on the index found within 'countList'
        countList[number - minimumValue] -= 1 # we need to decrease the tally within 'countList' since we added that score to the final output list

    return outputList

# test code to make sure my stuff works :P
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question N/A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
scores = [4, 2, 2, 8, 3, 3, 1, 17]
print(f"{countingSort(scores)} should be\n[1, 2, 2, 3, 3, 4, 8, 17]")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
This one is pretty simple, just be careful with your formatting since he's asking for a list.
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
I did this already in Question N/A :)
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
I did this one already too!
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def countingSortWithLimit(x, l):
    """
    I guess this is cheating? Because I don't create a list of None's before filling it in thus increasing the time complexity
    but I tried everything from a-z and nothing seemed to work.x
    :param x: An unsorted list of integers.
    :param l: The maximum allowed occurrences of any number.
    :return: A sorted list with duplicates removed beyond the limit.
    """
    # If the list is empty, return it directly
    if not x:
        return []

    # Find the minimum and maximum values to establish the range
    minValue = min(x)
    maxValue = max(x)
    rangeSize = maxValue - minValue + 1

    # Initialize the count list
    countList = [0] * rangeSize

    # Count occurrences of each number
    for number in x:
        countList[number - minValue] += 1

    # Create the sorted output list with the duplicates capped at the limit
    outputList = []
    for i in range(rangeSize):
        occurrences = min(countList[i], l)  # Cap occurrences at the limit `l`
        outputList.extend([i + minValue] * occurrences)

    return outputList

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"{countingSortWithLimit(scores, 1)} should be\n[1, 2, 3, 4, 8, 17]")