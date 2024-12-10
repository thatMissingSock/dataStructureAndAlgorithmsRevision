def print_peaks(x):
    """
     It should PRINT the index of any values who is greater than BOTH of its neighbours.
    :param x: A list of at least 3 numbers
    :return: A string holding the values(?)
    """
    for i in range(1, (len(x) - 1)):
        if (x[i] > x[i - 1]) and (x[i] > x[i + 1]):
            print(i)


# test code below
x = [6, 7, 8, 7, 6, 5, 4]
print_peaks(x)
print("Should print 2 only")

x = [1, 2, 1, 2, 1, 2, 1]
print_peaks(x)
print("Should print 1, 3, and 5")

x = [1, 2, 1]
print_peaks(x)
print("Should print 1 only")

x = [5, 10, 5, 20, 5, 30]
print_peaks(x)
print("Should print 1 and 3")

x = [5, 5, 5, 6, 6, 6]
print_peaks(x)
print("Should print nothing")

x = [4, 5, 6, 7, 8]
print_peaks(x)
print("Should print nothing")

x = [3, 2, 1, 2, 3]
print_peaks(x)
print("Should print nothing")