# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question N/A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def insertionSort(x):
    """
    This is the base template to see how insertionSort works. It can be adapted for the later questions.
    :param x: An unsorted list.
    :return: A sorted list.
    """
    xCopy = x[:]
    for i in range(1, len(x)):
        key = xCopy[i]
        j = i - 1
        while j >= 0 and xCopy[j] > key:
            xCopy[j + 1] = xCopy[j]
            j -= 1
        xCopy[j + 1] = key
    return xCopy
# test code provided by me :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question N/A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"{insertionSort([4, 2, 6, 1, 5, 3])} should be\n[1, 2, 3, 4, 5, 6]")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def insertionSortShowSteps(x):
    """
    This is the base template to see each step in the insertion sort.
    :param x: An unsorted list.
    :return: A sorted list.
    """
    xCopy = x[:]
    for i in range(1, len(x)):
        key = xCopy[i]
        j = i - 1
        while j >= 0 and xCopy[j] > key:
            print(xCopy)
            xCopy[j + 1] = xCopy[j]
            j -= 1
        xCopy[j + 1] = key


    return xCopy

# test code provided by me :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"{insertionSortShowSteps([4, 2, 6, 1, 5, 3])}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def insertionSortStepCount(x):
    """
    This is the base template to see how many steps there are when doing insertionSort on a list. We can then  use it to
    see which list would fix the quickest!
    :param x: An unsorted list.
    :return: A sorted list.
    """
    xCopy = x[:]
    count = 0
    for i in range(1, len(x)):
        key = xCopy[i]
        j = i - 1
        while j >= 0 and xCopy[j] > key:
            count += 1
            xCopy[j + 1] = xCopy[j]
            j -= 1
        xCopy[j + 1] = key
    return count

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
questions = [
    [21, 1, 33, 45, 5],
    ["e", "a", "c", "b", "d"],
    ["e", "d", "a", "b", "c"],
    ["e", "d", "c", "b", "a"],
    ["e", "a", "b", "c", "d"],
    ["d", "a", "b", "c", "e"],
    ["d", "c", "b", "a", "e"],
    ["c", "a", "b", "d", "e"],
    [2, 1, 3, 97, 79]]

# SO THERE IS AN ISSUE, I THINK HIS ORDER IS WRONG AS IT JUST DOESN'T MAKE SENSE. BOTH GPT AND A MATE I KNOW WHO WORKS
# IN THE INDUSTRY SAID THAT I WAS RIGHT IN THIS ORDER
sortedQuestions = (sorted(questions, key=insertionSortStepCount))

for i in range(len(sortedQuestions)):
    print(f"{sortedQuestions[i]}\n")