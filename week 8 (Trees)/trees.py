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