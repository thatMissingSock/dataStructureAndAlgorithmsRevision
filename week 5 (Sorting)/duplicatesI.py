"""
FORENOTE: these are all the doing the same thing but in different methods with different time complexities. The main
'basic' function of these is to see if there are ANY duplicates and return a BOOLEAN as the answer.
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question N/A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# the following is for testing
duplicatesList = [1, 2, 1, 3, 2, 6, 2, 1, 4, 2, 1, 4, 22, 44, 1, 34, 6, 3, 2, 34, 7, 3, 5, 67, 2]
uniqueList = [47, 3, 88, 12, 65, 29, 71, 34, 55, 19, 62, 78, 90, 24, 5, 16, 81, 42, 53, 7, 93, 21, 39, 68, 10]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dup_v1(x):
    """
    This method we are checking every element against the other.
    :param x: A list.
    :return: Boolean false IF THERE ARE DUPES.
    """
    noDupes = True
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                if x[i] == x[j]:
                    noDupes = False
                    break

    return noDupes

# test code below provided by me :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"{dup_v1(uniqueList)} should be {True}")
print(f"{dup_v1(duplicatesList)} should be {False}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dup_v2(x):
    """
    This should check for dupes in an ALREADY SORTED LIST (you should use the inbuilt sorted function). Because of this
    we only need to check for n and n-1
    :param x: A list.
    :return: Boolean false IF THERE ARE DUPES.
    """
    noDupes = True
    sortedX = sorted(x)
    for i in range(1, len(sortedX)):
        if sortedX[i] == sortedX[i - 1]:
            noDupes = False
            break
    return noDupes


# test code below provided by me :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"{dup_v2(uniqueList)} should be {True}")
print(f"{dup_v2(duplicatesList)} should be {False}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dup_v3(x):
    """
    This one he mentions a second parameter but doesn't provide it...so instead I will use the max function to provide this.
    WE ASSUME that list(x) is all numbers.
    WE ASSUME that it is only numbers from 1 to max(x).
    This function should keep a list called 'seen' to keep track of what you have and haven't viewed already.
    :param x: A list of numbers.
    :return: Boolean false IF THERE ARE DUPES.
    """

    seenList = [None] * len(x)
    maxValue = max(x)
    noDupes = True
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j and seenList[i] == None and seenList[j] == None:
                if x[i] == x[j]:
                    noDupes = False
        seenList[i] = x[i]

    return noDupes



# test code below provided by me :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"{dup_v3(uniqueList)} should be {True}")
print(f"{dup_v3(duplicatesList)} should be {False}")
