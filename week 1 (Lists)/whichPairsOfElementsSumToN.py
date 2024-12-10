def print_sum_pairs(x, n):
    """
    This should tell us the indices in this form (z,y) of any pair of numbers within the list that add up to the value of
    n. This does mean that it can be the same indices twice (if x[i] + x[i] == n). DO NOT DUPLICATE.
    :param x: A list
    :param n: A number
    :return: A list of indices that add up to n
    """
    output = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] + x[j] == n:
                if i <= j:
                    output.append((i, j))
    if output != []:
        print(output)


# test code below
x = [2, 3, 4]
print_sum_pairs(x, 7)
print("Should print (1, 2)")

x = [2, 3, 5]
print_sum_pairs(x, 6)
print("Should print (1, 1)")

x = [2, 3, 4]
print_sum_pairs(x, 6)
print("Should print (0, 2), (1, 1)")

x = [4, 5, 4, 5]
print_sum_pairs(x, 9)
print("Should print (0, 1), (0, 3), (1, 2), (2, 3)")

x = [3, 3, 3]
print_sum_pairs(x, 6)
print("Should print (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)")

x = [2, 4, 6]
print_sum_pairs(x, 7)
print("Should print nothing")

x = []
print_sum_pairs(x, 6)
print("Should print nothing")