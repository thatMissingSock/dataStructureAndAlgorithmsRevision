from trees import *

def putInList(root):
    """
    Converts all values of the root and its descendants into a single list.
    I created a new function just because it seemed easier than to cram it all into one function.
    :param root: A tree.
    :return: A flat list containing all the values of the root and its descendants.
    """
    if root is None:
        return []

    tempList = [root.value]  # Start with the current node's value

    # Add all values from the children recursively
    for child in root.children:
        tempList.extend(putInList(child))  # Extend instead of append as we are adding 2 lists together

    return tempList
def max_T(root):
    """
    This function should take in a tree(root) and search through ALL of its children (if there are any) and return the
    LARGEST VALUE.
    I think recursion is the best choice.
    :param root: A tree.
    :return: The max value in root.
    """
    return max(putInList(root))


# Test code provided by Faris
def test_max_T():
  print("\n\033[1m############# max_T #############\033[0m\n")
  B = Tree(5)
  print(max_T(B), "should be", 5)
  C = Tree(3)
  D = Tree(6)
  E = join_T([C, D], 1)
  print(max_T(E), "should be", 6)
  A = join_T([B, E], 2)
  print(max_T(A), "should be", 6)

def most_kids_T(root):
    """
    This function should take in a tree(root) and return the max number of children that any node has.
    :param root: A tree.
    :return: The max number of children any node in that tree has.
    """


# Test code provided by Faris
def test_most_kids_T():
  print("\n\033[1m############# most_kids_T #############\033[0m\n")
  B = Tree(1)
  print(most_kids_T(B), "should be", 0)
  C = Tree(2)
  D = Tree(3)
  E0 = Tree(4)
  E0.children = [C, D]
  print(most_kids_T(E0), "should be", 2)
  E = Tree(4)
  F = Tree(5)
  G = Tree(6)
  H = Tree(7)
  I = join_T([E, F, G, H], 8)
  print(most_kids_T(I), "should be", 4)
  D.children = [I]
  A = join_T([B, C, D], 2)
  print(most_kids_T(A), "should be", 4)

def height_T(root):
  "to do"



# Test code provided by Faris
def test_height_T():
  print("\n\033[1m############# height_T #############\033[0m\n")
  B = Tree(1)
  print(height_T(B), "should be", 0)
  C = Tree(2)
  D = Tree(3)
  E = Tree(4)
  E.children = [C, D]
  print(height_T(E), "should be", 1)
  F = Tree(5)
  G = Tree(6)
  H = Tree(7)
  I = join_T([E, F, G, H], 8)
  print(height_T(I), "should be", 2)
  J = Tree(9)
  J.children = [I]
  print(height_T(J), "should be", 3)
  A = join_T([B, J], 2)
  print(height_T(A), "should be", 4)

test_max_T()
test_most_kids_T()
# test_height_T()