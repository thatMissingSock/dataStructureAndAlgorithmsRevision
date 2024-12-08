def inc_evens(x):
    for i in range(len(x)):
        if (x[i] % 2 == 0):
            x[i] += 1

"""Test code here"""
x = [2, 2, 9]
inc_evens(x)
print(x, "should be [3, 3, 9]")

x = [4, 11, 11, 50]
inc_evens(x)
print(x, "should be [5, 11, 11, 51]")

x = []
inc_evens(x)
print(x, "should be []")