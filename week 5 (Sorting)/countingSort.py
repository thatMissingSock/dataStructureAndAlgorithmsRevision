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
that EVERY kid will have a score ranging from 1-20 points. You now need to put them in order of highest to lowest and the
best way to do that is to create a table/tally. After the first header is filled with 19 columns (1-20), underneath you
add 1 tally for each time a student has received that score.
Using that tally, you can then just put the scores in order and it doesn't really matter if the same score comes before
or after because IT'S THE SAME SCORE.
You want an example, fine. I'll create a lil part at the end to show how it can be used to put scores in order :).
"""

def countingSort(x):
    """
    This function should sort a list using the count-sort method.
    :param x: An unsorted list.
    :return: A sorted list.
    """
    # step 1
    minimumValue = min(x)
    maximumValue = max(x)
    rangeSize = maximumValue - minimumValue + 1 # not sure why we need +1, but it doesn't work without it

    # step 2
    outputList = [None] * len(x)
    countList = [0] * rangeSize

    # step 3
    for number in x: # this iterates through each element in list x
        countList[number - minimumValue] += 1 # for the index of number - minumumValue we increase it by 1 (because it means we can tally someone got this score)

    # step 4
    for i in range(1, rangeSize):
        countList[i] += countList[i - 1]

    # step 5
    for number in reversed(x):  # Traverse in reverse to maintain stability
        outputList[countList[number - minimumValue] - 1] = number # we add to the list 'outputList' the values inside 'x' based on the index found within 'countList'
        countList[number - minimumValue] -= 1 # we need to decrease the tally within 'countList' since we added that score to the final output list

    return outputList

# test code to make sure my stuff works :P
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question N/A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
scores = [4, 2, 2, 8, 3, 3, 1]
print(countingSort(scores))