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
    Finds the maximum number of children that any node has in the tree starting at root.
    :param root: The root of the tree.
    :return: The maximum number of children of any node.
    """
    if root is None:
      return 0  # Base case: no tree means no children

    # Count the children of the current node
    currentChildrenCount = len(root.children)

    # Recursively calculate the maximum for all children
    maxChildrenInSubtree= max((most_kids_T(child) for child in root.children), default=0)

    # Return the maximum of the current node's children count and the maximum from subtrees
    return max(currentChildrenCount, maxChildrenInSubtree)


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
    """
    So this function needs to take in a tree(root) and output the height of the root of the tree to the 'lowest' leaf.
    It should do this recursively but also iteratively.
    :param root: A tree.
    :return: The longest route(??).
    """
    if root is None:
      return -1 # this base case is incase there is NO tree

    if not root.children:
      return 0 # this base case is in case we reach the last leaf node

    childHeights = [height_T(child) for child in root.children]
    return 1 + max(childHeights)

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
test_height_T()