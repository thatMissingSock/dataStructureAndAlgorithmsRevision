def show(list):
  print("\n".join(map(str, list)))


x = [1, 5, 2, 4, 6, 3]


sorted(x, reverse=True)

def negate(n):
  return -n

sorted(x, key=negate)

show(sorted(x))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

y = ["zebra", "giraffe", "lion", "ant-eater", "dog"]
sorted(y)

def length(s):
  return len(s)

sorted(y, key=length, reverse=True)
sorted(y, key=len)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

u = ["ba", "ab", "ba", "bb"]
sorted(u)

u = [12, 1, 2, 11, 22, 3]
sorted(u)

u = ["12", "1", "2", "11", "22", "3"]
sorted(u)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

z = [12, 23, 2, 4, 45]
sorted(z)
sorted(z, key=str)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

t = [[12, "b"], [1, "a"], [21, "a"], [1, "b"]]
sorted(t)

u = [[1, 2], [1], [2], [1, 1], [2, 2], [3]]
sorted(u)

v = [[1, 4], [2, 5], [1, 3], [2, 4]]
sorted(v)

w = [[1, 1, 3], [1, 1], [2], [1, 2, 3], [1, 2, 1]]
sorted(w)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def show(list):
  print("\n".join(map(str, list)))

names = [
  [500, "John", "Smith"],
  [321, "Arnold", "Black"],
  [112, "Adam", "Smith"],
  [440, "Jack", "Black"]
]
show(sorted(names))

def key2(name):
  return name[1]
names2 = sorted(names, key=key2)
show(names2)

def key3(name):
  return name[2]
names3 = sorted(names2, key=key3)
show(names3)
