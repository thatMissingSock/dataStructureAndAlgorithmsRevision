def inc_all(x):
    for i in range(len(x)):
        x[i] += 1

"""Paste test code here"""
x = [1, 1, 1]
inc_all(x)
print(x, "should be [2, 2, 2]")

x = [1, 2, -1]
inc_all(x)
print(x, "should be [2, 3, 0]")

x = [6]
inc_all(x)
print(x, "should be [7]")

x = []
inc_all(x)
print(x, "should be []")