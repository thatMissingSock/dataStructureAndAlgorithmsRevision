def min_edge_weight_ind(M, i):
    """
    This needs to take in a weighted matrix (M) and a value for an vertex that your checking (i) and return another vertex
    that is connected to the one you are checking but with the SMALLEST VALUE!
    :param M: A weighted matrix.
    :param i: A vertex to check.
    :return: The connected vertex with the SMALLEST EDGE.
    """
    tempOutput = None
    tempWeightedValue = None
    for column in range(len(M[0])):
        if tempOutput is None and M[i][column] is not None:
            tempOutput = column
            tempWeightedValue = M[i][column]
        elif M[i][column] is not None:
            if tempWeightedValue > M[i][column]:
                tempOutput = column
                tempWeightedValue = M[i][column]

    return tempOutput


# test code below (provided by GPT)
# Test cases for min_edge_weight_ind(M, i)

# Example adjacency matrix with weights and some None values
M1 = [
    [None, 3, None, 8],
    [6, None, 5, None],
    [None, None, None, 6],
    [4, None, 2, 0]
]

print(f"{min_edge_weight_ind(M1, 0)} should be 1")  # Edge from 0->1 has min weight 3
print(f"{min_edge_weight_ind(M1, 1)} should be 2")  # Edge from 1->2 has min weight 5
print(f"{min_edge_weight_ind(M1, 2)} should be 3")  # Edge from 2->3 has min weight 6
print(f"{min_edge_weight_ind(M1, 3)} should be 3")  # Edge from 3->3 has min weight 0

# Test case with ties for minimum weight
M2 = [
    [1, 1, None],
    [2, None, 1],
    [None, 1, None]
]
print(f"{min_edge_weight_ind(M2, 0)} should be 0 or 1")  # Both 0->0 and 0->1 have weight 1
print(f"{min_edge_weight_ind(M2, 1)} should be 2")  # Edge from 1->2 has min weight 1
print(f"{min_edge_weight_ind(M2, 2)} should be 1")  # Edge from 2->1 has min weight 1

# Test case with all None values
M3 = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
print(f"{min_edge_weight_ind(M3, 0)} should be None")  # No edges present
print(f"{min_edge_weight_ind(M3, 1)} should be None")  # No edges present
print(f"{min_edge_weight_ind(M3, 2)} should be None")  # No edges present

# Test case with a mix of values
M4 = [
    [None, 10, 15],
    [None, None, 5],
    [None, 1, None]
]
print(f"{min_edge_weight_ind(M4, 0)} should be 1")  # Edge from 0->1 has min weight 10
print(f"{min_edge_weight_ind(M4, 1)} should be 2")  # Edge from 1->2 has min weight 5
print(f"{min_edge_weight_ind(M4, 2)} should be 1")  # Edge from 2->1 has min weight 1

