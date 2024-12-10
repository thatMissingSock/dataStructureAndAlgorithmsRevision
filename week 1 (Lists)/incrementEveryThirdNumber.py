def inc_every_third(x):
    for i in range(len(x)):
        if (x[i] % 3 == 0):
            x[i] += 1

"""Test code here"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
inc_every_third(x)
print(x, "should be [1, 1, 2, 4, 4, 5, 7, 7, 8]")

x = []
inc_every_third(x)
print(x, "should be []")