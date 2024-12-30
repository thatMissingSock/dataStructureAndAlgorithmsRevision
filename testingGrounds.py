class BinaryTree:
    def __init__(new_tree, v):
        new_tree.value = v
        new_tree.left_child = None
        new_tree.right_child = None

    def __str__(root):
        s = str(root.value)
        s += " <"
        child_strings = []
        left = root.left_child
        right = root.right_child
        if left != None or right != None:
            child_strings.append(str(left))
            child_strings.append(str(right))
        s += ", ".join(child_strings)
        s += ">"
        return s

    def __repr__(root):
        return str(root)


class Tree:
    def __init__(new_tree, v):
        new_tree.value = v
        new_tree.children = []

    def __str__(root):
        s = str(root.value)
        s += " <"
        child_strings = []
        for child in root.children:
            child_strings.append(str(child))
        s += ", ".join(child_strings)
        s += ">"
        return s

    def __repr__(root):
        return str(root)


def join_T(trees, v):
    root = Tree(v)
    root.children = trees
    return root


def join_BT(left, right, v):
    root = BinaryTree(v)
    root.left_child = left
    root.right_child = right
    return root

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
            tempList.append(putInList(child))

        return tempList


def test_max_T():
  B = Tree(5)
  C = Tree(3)
  D = Tree(6)
  E = join_T([C, D], 1)
  A = join_T([B, E], 2)
  print(A)
  print(putInList(A))

test_max_T()