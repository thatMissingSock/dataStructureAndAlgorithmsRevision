from asyncio import run_coroutine_threadsafe


def set_all(x, n):
    for i in range(len(x)):
        x[i] = n

"""Test code goes here"""
x = [1, 2, 3]
set_all(x, 'a')
print(x, "should be ['a', 'a', 'a']")

x = [2, 3]
set_all(x, 1)
print(x, "should be [1, 1]")

x = []
set_all(x, 5)
print(x, "should be []")

x = [1]
set_all(x, x)
print("This might make more sense next week:", x)
print(x is x[0], "should be True...")