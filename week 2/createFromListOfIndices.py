def listind_to_mat(l, m, n):
  """Your code here"""

# ~~~~~~~~HIS TEST CODE DOESN'T WORK AND THE QUESTION MAKES NO SENSE~~~~~~~~
  return M

# test code below

M = listind_to_mat([[0], [1], [1], [0, 1], [0]], 5, 2)
print(M, "should be", [[1, 0],
                       [0, 1],
                       [0, 1],
                       [1, 1],
                       [1, 0]])

M = listind_to_mat([[0], [1, 2], [0, 1, 2]], 3, 3)
print(M, "should be", [[1, 0, 0],
                       [0, 1, 1],
                       [1, 1, 1]])

M = listind_to_mat([[0, 2], [2, 3], [0, 3]], 4, 3)
print(M, "should be", [[0, 0, 1, 0],
                       [0, 0, 1, 1],
                       [1, 0, 0, 1]])