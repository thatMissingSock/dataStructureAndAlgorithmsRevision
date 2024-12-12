# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question N/A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
THIS ONE IS A FUCKING MESS. I don't fully understand how quick sort works and his code does not help at all.
After watching a video (https://www.youtube.com/watch?v=Hoixgm4-P4M) and thanks to a friend (thanks Dami!),
I can explain and my code seems to be more optimised.

SKIP THIS IF YOU DON'T NEED TO UNDERSTAND!

What quick sort does can be explained in steps:

1. First, we choose a pivot point. This can be any number in the list, BUT it would be more optimised if you chose the median
index (middle index between start and finish). Why? Well, we ASSUME that it would bring us closer to the actual median of
the values inside the list. IF IT ISN'T. THEN WORST CASE SCENARIO, WE JUST ITERATE THROUGH THEM ALL SO THERE IS NO RISK.

2. We then create 2 new lists, a left list and a right list. The rules for each list are that the left list ONLY contains
values of those smaller than the pivot value, and the right list contains the opposite.

3. We then recursively do the same for the left list and the right list until they reach the base case (which in this case
is just if the length is 1). Because of the parameters we stated in step 2 it should return a sorted list.

4. We then just add the values into a sorted list by doing "return quickSort(leftList) + [middle] + quickSort(rightList).
Here you can see that in the same line of the return we call upon the same function twice, once for the left and once for
the right, which is where the recursion occurs. We ALSO put the value of middle inside a list...why?
BECAUSE YOU CANNOT MIX DATATYPES!
You cannot concatenate a list (which is what the leftList and rightList are) with an int (middle).
After ALL of the recursions, we finally get our sorted list.

THIS IS QUICKER THAN MERGE SORT. Why?
Well we do a few things different:
- we use a pivot point which gives us a *chance* to have a value that is close to the actual middle value of the list
- we also SHOULD be swapping in place which is just inherently quicker, my first function DOES NOT DO THIS. It is just
used to show how quickSort works, and my optimised version is the more complex version.
- because of how everything is, we don't really use that much RAM which is good for LONG-ASS LISTS!

Honestly, put this into pythonTutor.com and see if it helps. If not then call me and I'll try and show you on a whiteboard :).
"""
from pickle import PROTO


# WHILE THIS IS TECHNICALLY 'QUICKSORT' ITS INEFFIECIENT SINCE IT CREATES A MULTITUDE OF LISTS. FARIS' CODE IS BETTER AND
# AFTER ANALYSING MY FUNCTION HIS ONE SHOULD MAKE SENSE
def quickSort(y):
    """
    This is a template, it's the base example to do a quickSort and should be adapted based on the question
    :param y: An unsorted list.
    :return: A sorted list.
    """
    if len(y) <= 1:  # Base case
        return y

    pivotIndex = len(y) // 2 # we floor to not get a floating number
    middle = [y[pivotIndex]]
    leftList = []
    for i in range(len(y)):
        if y[i] < y[pivotIndex]:
            leftList.append(y[i])
    rightList = []
    for i in range(len(y)):
        if y[i] > y[pivotIndex]:
            rightList.append(y[i])

    return quickSort(leftList) + middle + quickSort(rightList)  # Recursively sort

# test code just to see if my base template works :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question N/A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
tempList = [8, 3, 1, 7, 0, 10, 2]
print(f"{quickSort(tempList)} should be\n[0, 1, 2, 3, 7, 8, 10]")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FARIS' CODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def choose_pivot_v1(x, begin, end):
    return begin


def choose_pivot_v2(x, begin, end):
    """YCH: Choose the last element of the range begin-end as the pivot"""


def choose_pivot_v3(x, begin, end):
    """YCH: Choose the median of the first, middle, and last element of the list as the pivot"""


# Change "v1" into "v2" or "v3" to test those versions, above:
choose_pivot = choose_pivot_v1


def swap(x, i, j):
    temp = x[i]
    x[i] = x[j]
    x[j] = temp


def divide(x, begin, end):
    chosen_index = choose_pivot(x, begin, end)
    swap(x, begin, chosen_index)  # Step 1​
    pivot = x[begin]

    left = begin + 1
    right = end

    done = False
    while not done:
        while left <= right and x[left] <= pivot:
            left += 1
        while x[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            swap(x, left, right)  # Step 4​

    swap(x, begin, right)  # Step 5​
    return right


def qsort_view(x, begin, end):
    if begin < end:
        split_point = divide(x, begin, end)
        qsort_view(x, begin, split_point - 1)
        qsort_view(x, split_point + 1, end)


def qsort(x):
    qsort_view(x, 0, len(x) - 1)


# test code to see if his method makes sense
x = [5, 9, 7, 8, 10, 2, 6, 1, 4, 3]
qsort(x)

print(f"\n{x} should be\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Whilst yes, I can alter mine or Faris' code to make this count the number of elements in the left list and/or right list
# its just easier to create a new function.
# KEEP IN MIND: this function is basically just doing step 1 of quick sort!
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def countElements(x, pivotIndex):
    pivotValue = x[pivotIndex]
    leftList = []
    rightList = []
    for i in range(len(x)):
        if x[i] < pivotValue:
            leftList.append(x[i])
        elif x[i] > pivotValue:
            rightList.append(x[i])
    lengthOfLeftList = len(leftList)
    lengthOfRightList = len(rightList)
    print(f"The original list was {x}.\nThe left list contains {leftList}\nwhich has a length of {lengthOfLeftList}.\nThe right list contains {rightList}\nwhich has a length of {lengthOfRightList}.\nThe middle value is {[pivotValue]}.")

tempPlaceholder = countElements([4, 3, 7, 2, 6, 5, 1, 8], 0)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# I have to adapt Faris' code so it shows each step :))))))))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FARIS' CODE (ADAPTED)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def choosePivotShowSteps_v1(x, begin, end):
    return begin

choosePivotShowSteps = choosePivotShowSteps_v1


def swapShowSteps(x, i, j):
    temp = x[i]
    x[i] = x[j]
    x[j] = temp


def divideShowSteps(x, begin, end):
    chosen_index = choosePivotShowSteps_v1(x, begin, end)
    swapShowSteps(x, begin, chosen_index)  # Step 1​
    pivot = x[begin]

    left = begin + 1
    right = end

    done = False
    while not done:
        while left <= right and x[left] <= pivot:
            left += 1
        while x[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            swapShowSteps(x, left, right)  # Step 4​
            print(x)

    swapShowSteps(x, begin, right)  # Step 5​
    return right


def qSortViewShowSteps(x, begin, end):
    if begin < end:
        split_point = divideShowSteps(x, begin, end)
        qSortViewShowSteps(x, begin, split_point - 1)
        qSortViewShowSteps(x, split_point + 1, end)


def qSortShowSteps(x):
    qSortViewShowSteps(x, 0, len(x) - 1)


# test code to see the answer
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
x = [5, 9, 7, 8, 10, 2, 6, 1, 4, 3]
print(x)
qSortShowSteps(x)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2.2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# We call on the function from question 1 but with a new list

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2.2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
tempPlaceholder = countElements([5, 9, 7, 8, 10, 2, 6, 1, 4, 3], 0)
# PLEASE NOTE, his question states to enter the parts that are in the leftList and rightList which is fine but its hard
# to get the right answer as you don't know how he wants it formatted (with spaces, commas and/or in a list)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# I have to adapt Faris' code so it shows the pivot for each recursive call

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FARIS' CODE (adapted)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def choosePivotShowPivots_v1(x, begin, end):
    return begin

choosePivotShowPivots = choosePivotShowPivots_v1

def swapShowPivots(x, i, j):
    temp = x[i]
    x[i] = x[j]
    x[j] = temp


def divideShowPivots(x, begin, end):
    chosen_index = choosePivotShowPivots(x, begin, end)
    swapShowPivots(x, begin, chosen_index)  # Step 1​
    pivot = x[begin]
    print(pivot)

    left = begin + 1
    right = end

    done = False
    while not done:
        while left <= right and x[left] <= pivot:
            left += 1
        while x[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            swapShowPivots(x, left, right)  # Step 4​

    swapShowPivots(x, begin, right)  # Step 5​
    return right


def qSortShowPivotsViewShowPivots(x, begin, end):
    if begin < end:
        split_point = divideShowPivots(x, begin, end)
        qSortShowPivotsViewShowPivots(x, begin, split_point - 1)
        qSortShowPivotsViewShowPivots(x, split_point + 1, end)


def qSortShowPivots(x):
    qSortShowPivotsViewShowPivots(x, 0, len(x) - 1)


# test code to see if his method makes sense
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
x = [5, 9, 7, 8, 10, 2, 6, 1, 4, 3]
qSortShowPivots(x)
print("PLEASE NOTE: 2 and 4 are the left side pivots whilst 9, 7 and 10 are the right side pivots.\nI just couldn't get the answer in codio because again we don't know how he wants it.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3.2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# I DID NOT DO THIS....cba

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The following are how each should be written based on if you want the start, end or middle :)

def choosePivotBeginning(x, begin, end):
    return begin

def choosePivotEnding(x, begin, end):
    return end

def choosePivotMedian(x, begin, end):
        return end // 2
# test code to make sure I'm not smoking crack
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"The list currently contains {tempList}.\n"
      f"Therefore, the function to find the beginning index returns {choosePivotBeginning(tempList, 0, (len(tempList) - 1))} and it should return 0.\n"
      f"The function to find the end index returns {choosePivotEnding(tempList, 0, (len(tempList) - 1))} and it should return 6\n"
      f"The function to find the median returns {choosePivotMedian(tempList, 0, (len(tempList) - 1))} and it should return 3.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# I DID NOT DO THIS....cba