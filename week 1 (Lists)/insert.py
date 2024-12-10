# YOU CANNOT USE APPEND/INSERT/REMOVE
def my_insert(a, x, n, i):
    """
    This modifies list 'a' by adding value 'x' at index 'i'.
    :param a: A list
    :param x: A value
    :param n: The number of elements in 'a' that are NON-ZERO
    :param i: An index
    :return:
    """
    tempList = [0] * len(a)

    for index in range(n):
        if (index - 1) != i:
            tempList[index] = a[index]
        else:
            tempList[index] = x

    return tempList

# test code below
a = [10, 20, 40, 50, 60, 0, 0, 0]
n = 5
x = 30
i = 2
my_insert(a, x, n, i)
print("Should move values 60, 50, 40 (in that order) into the next slot, and then put 30 at index 2")
print(a, "should now be [10, 20, 30, 40, 50, 60, 0, 0]")
print(len(a), "should still be 8")

a = [2, 3, 4, 5, 6, 7, 0]
n = 6
x = 1
i = 0
my_insert(a, x, n, i)
print("Should move values 7 down to 2 into the next slot, and then put 1 at index 2")
print(a, "should now be [1, 2, 3, 4, 5, 6, 7]")
print(len(a), "should still be 7")

a = [0, 0, 0, 0, 0]
n = 0
x = 1
i = 0
my_insert(a, x, n, i)
print("Should put 1 at index 0")
print(a, "should now be [1, 0, 0, 0, 0]")
print(len(a), "should still be 5")