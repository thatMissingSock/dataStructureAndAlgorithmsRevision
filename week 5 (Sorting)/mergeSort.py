# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question N/A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# the following is the base template to be changed for later questions

def recursiveMergeSort (x):
    """
    The aim of this function is to sort the list using merge sort BUT RECURSIVELY. The best way to do this is to have
    a base case of the length is 1 or less and return that value. If not, we then keep splitting it in half until it
    reaches the sorted part.
    :param x: An unsorted list.
    :return: A sorted list.
    """
    if len(x) <= 1:
        return x

    middleOfList = len(x) // 2 # we floor to round down so we don't get a float
    firstHalf = x[:middleOfList] # we slice to create a new list for the first half
    secondHalf = x[middleOfList:] # we slice to create a new list for the second half
    mergedFirstHalf = recursiveMergeSort(firstHalf) # we then recursively call the function to repeat for the first half
    mergedSecondHalf = recursiveMergeSort(secondHalf) # we then recursively call the function to repeat for the second half
    return mergeHalves(mergedFirstHalf, mergedSecondHalf, x)



def mergeHalves(firstPart, secondPart, x):
    """
    We need another function so we can do a few things:
    - check if the values in the halves are bigger than the other and "swap" places if need be
    - merge the sorted halves into a bigger half
    - placec the merged halves into a bigger list called 'x'
    :param firstPart: First half of a list we are checking.
    :param secondPart: The second half of a list we are checking.
    :param x: The current list that holds both parts of which we are sorting in order.
    :return:
    """
    initialIndex1 = 0
    initialIndex2 = 0
    indexOfX = 0
    lengthOfFirstHalf = len(firstPart)
    lengthOfSecondHalf = len(secondPart)

    while initialIndex1 < lengthOfFirstHalf and initialIndex2 < lengthOfSecondHalf:
      if firstPart[initialIndex1] <= secondPart[initialIndex2]:
        smaller_value = firstPart[initialIndex1]
        initialIndex1 += 1

      else:
        smaller_value = secondPart[initialIndex2]
        initialIndex2 += 1

      x[indexOfX] = smaller_value
      indexOfX += 1

    while initialIndex1 < lengthOfFirstHalf:
      x[indexOfX] = firstPart[initialIndex1]
      indexOfX += 1
      initialIndex1 += 1

    while initialIndex2 < lengthOfSecondHalf:
      x[indexOfX] = secondPart[initialIndex2]
      indexOfX += 1
      initialIndex2 += 1

    return x

# test code below
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question N/A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"{recursiveMergeSort([21, 1, 26, 45, 29, 28, 2, 9])} should be\n[1, 2, 9, 21, 26, 28, 29, 45]")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# the following function is the same as above, but they just print out what is currently going through the first
# function so we can see how the recursion occurs!

def recursiveMergeSortShowSteps (x):
    """
    The aim of this function is to sort the list using merge sort BUT RECURSIVELY. The best way to do this is to have
    a base case of the length is 1 or less and return that value. If not, we then keep splitting it in half until it
    reaches the sorted part.
    :param x: An unsorted list.
    :return: A sorted list.
    """
    if len(x) <= 1:
        print(x)
        return x
    else:
        print(x)


    middleOfList = len(x) // 2 # we floor to round down so we don't get a float
    firstHalf = x[:middleOfList] # we slice to create a new list for the first half
    secondHalf = x[middleOfList:] # we slice to create a new list for the second half
    # print(x)
    mergedFirstHalf = recursiveMergeSortShowSteps(firstHalf) # we then recursively call the function to repeat for the first half
    mergedSecondHalf = recursiveMergeSortShowSteps(secondHalf) # we then recursively call the function to repeat for the second half
    # print(x)
    # print(mergedFirstHalf)
    # print(mergedSecondHalf)
    return mergeHalves(mergedFirstHalf, mergedSecondHalf, x)


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
tempPlaceHolder = recursiveMergeSortShowSteps([21, 1, 26, 45, 29, 28, 2, 9])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# the following two functions are the same as the base template, but they print out what is returned in what order after
# calling on the merged function!

def recursiveMergeSortShowMergeSteps (x):
    """
    The aim of this function is to sort the list using merge sort BUT RECURSIVELY. The best way to do this is to have
    a base case of the length is 1 or less and return that value. If not, we then keep splitting it in half until it
    reaches the sorted part.
    :param x: An unsorted list.
    :return: A sorted list.
    """
    if len(x) <= 1:
        return x

    middleOfList = len(x) // 2 # we floor to round down so we don't get a float
    firstHalf = x[:middleOfList] # we slice to create a new list for the first half
    secondHalf = x[middleOfList:] # we slice to create a new list for the second half
    mergedFirstHalf = recursiveMergeSortShowMergeSteps(firstHalf) # we then recursively call the function to repeat for the first half
    print(mergedFirstHalf)
    mergedSecondHalf = recursiveMergeSortShowMergeSteps(secondHalf) # we then recursively call the function to repeat for the second half
    print(mergedSecondHalf)
    return mergeHalvesShowSteps(mergedFirstHalf, mergedSecondHalf, x)



def mergeHalvesShowSteps(firstPart, secondPart, x):
    """
    We need another function so we can do a few things:
    - check if the values in the halves are bigger than the other and "swap" places if need be
    - merge the sorted halves into a bigger half
    - placec the merged halves into a bigger list called 'x'
    :param firstPart: First half of a list we are checking.
    :param secondPart: The second half of a list we are checking.
    :param x: The current list that holds both parts of which we are sorting in order.
    :return:
    """
    initialIndex1 = 0
    initialIndex2 = 0
    indexOfX = 0
    lengthOfFirstHalf = len(firstPart)
    lengthOfSecondHalf = len(secondPart)

    while initialIndex1 < lengthOfFirstHalf and initialIndex2 < lengthOfSecondHalf:
      if firstPart[initialIndex1] <= secondPart[initialIndex2]:
        smaller_value = firstPart[initialIndex1]
        initialIndex1 += 1

      else:
        smaller_value = secondPart[initialIndex2]
        initialIndex2 += 1

      x[indexOfX] = smaller_value
      indexOfX += 1

    while initialIndex1 < lengthOfFirstHalf:
      x[indexOfX] = firstPart[initialIndex1]
      indexOfX += 1
      initialIndex1 += 1

    while initialIndex2 < lengthOfSecondHalf:
      x[indexOfX] = secondPart[initialIndex2]
      indexOfX += 1
      initialIndex2 += 1

    # print(x)
    return x
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
tempPlaceHolder = recursiveMergeSortShowMergeSteps([21, 1, 26, 45, 29, 28, 2, 9])
print(tempPlaceHolder)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# the aim of this is to see how many lists we make when doing a recursive merge sort and the sum of the number of elements

count = 0
elementCount = 0

def recursiveMergeSortCount (x):
    """
    The aim of this function is to sort the list using merge sort BUT RECURSIVELY. The best way to do this is to have
    a base case of the length is 1 or less and return that value. If not, we then keep splitting it in half until it
    reaches the sorted part.
    :param x: An unsorted list.
    :return: A sorted list.
    """
    global count
    global elementCount

    if len(x) <= 1:
        return x
    middleOfList = len(x) // 2 # we floor to round down so we don't get a float
    firstHalf = x[:middleOfList] # we slice to create a new list for the first half
    elementCount += len(firstHalf)
    count += 1
    secondHalf = x[middleOfList:] # we slice to create a new list for the second half
    count += 1
    elementCount += len(secondHalf)
    mergedFirstHalf = recursiveMergeSortCount(firstHalf) # we then recursively call the function to repeat for the first half
    mergedSecondHalf = recursiveMergeSortCount(secondHalf) # we then recursively call the function to repeat for the second half
    return mergeHalves(mergedFirstHalf, mergedSecondHalf, x)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
tempPlaceHolder = recursiveMergeSortCount([21, 1, 26, 45, 29, 28, 2, 9])
print(count)
print(elementCount)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# the aim of this question is to give us a mergedSorted list without actually modifying the original list

def recursiveMergeSortWithoutModifying (x):
    """
    The aim of this function is to sort the list using merge sort BUT RECURSIVELY. The best way to do this is to have
    a base case of the length is 1 or less and return that value. If not, we then keep splitting it in half until it
    reaches the sorted part.
    :param x: An unsorted list.
    :return: A sorted list COPY.
    """
    xCopy = x[:]
    if len(xCopy) <= 1:
        return xCopy

    middleOfList = len(xCopy) // 2 # we floor to round down so we don't get a float
    firstHalf = xCopy[:middleOfList] # we slice to create a new list for the first half
    secondHalf = xCopy[middleOfList:] # we slice to create a new list for the second half
    mergedFirstHalf = recursiveMergeSort(firstHalf) # we then recursively call the function to repeat for the first half
    mergedSecondHalf = recursiveMergeSort(secondHalf) # we then recursively call the function to repeat for the second half
    return mergeHalves(mergedFirstHalf, mergedSecondHalf, xCopy)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# test code to see if the orignal list has been changed or not provided by me :)
tempList = [21, 1, 26, 45, 29, 28, 2, 9]
print(f"{recursiveMergeSortWithoutModifying(tempList)} which should be\n[1, 2, 9, 21, 26, 28, 29, 45]\nThe original list is \n{tempList} which should be\n[21, 1, 26, 45, 29, 28, 2, 9]\nIf not then it has been altered and your code is wrong.")

