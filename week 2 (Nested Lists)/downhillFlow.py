def flow_down(M, i):
    """
    So this is supposed to take in an adjacency matrix for a WEIGHTED graph (M) and a vertex index (i) where you start.
    From the starting point you need to check each value until you find the smallest, when the smallest is found you take
    that path to the next node and continue until the same node is hit twice (we stop here otherwise it'll be an endless
    loop).
    :param M: A weighted adjacency matrix.
    :param i: A vertex index.
    :return: A list of vertices that would take the smallest amount of edges.
    """

    outputVertices = []
    outputVertices.append(i)
    count = 0

    isItFin = False
    while isItFin is not True:
        smallestPath = None
        tempValue = None
        for column in range(len(M[0])):
            if smallestPath is None and M[outputVertices[count]][column] is not None:
                smallestPath = column
                tempValue = M[outputVertices[count]][column]
            elif M[outputVertices[count]][column] is not None:
                if tempValue > M[outputVertices[count]][column]:
                    smallestPath = column
                    tempValue = M[outputVertices[count]][column]
        outputVertices.append(smallestPath)
        count += 1
        if outputVertices[count] == outputVertices[count - 1]:
            isItFin = True

    return outputVertices


# test code below
M = [[None, 1, 2], [3, None, 2], [4, None, 3]]
print(flow_down(M, 0), "should be", [0, 1, 2, 2])

# # test code provided by GPT
# # Test cases for flow_down(M, i)
#
# # Example adjacency matrix
# M1 = [
#     [None, 1, None],
#     [None, None, 2],
#     [None, None, 3]
# ]
# # Expected path: [0, 1, 2, 2]
# print(f"{flow_down(M1, 0)} should be [0, 1, 2, 2]")
#
# # ~~~~~~~~~~~~~~THIS IS AN ENDLESS LOOP SO I TOOK IT AWAY~~~~~~~~~~~~~~
# # # Test case: Multiple outgoing edges with distinct weights
# # M2 = [
# #     [None, 3, 1],
# #     [4, None, 2],
# #     [None, 5, None]
# # ]
# # # Expected path: [0, 2, 1]
# #
# # print(f"{flow_down(M2, 0)} should be [0, 2, 1]")
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# # Test case: Vertex revisits itself
# M3 = [
#     [None, 2, None],
#     [None, None, None],
#     [None, None, 1]
# ]
# # Expected path: [2, 2]
# print(f"{flow_down(M3, 2)} should be [2, 2]")
#
# # Test case: No outgoing edges at starting vertex
# M4 = [
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
# ]
# # Expected path: [0] (no outgoing edges from 0)
# print(f"{flow_down(M4, 0)} should be [0]")
#
# # Test case: A larger graph with a mix of weights
# M5 = [
#     [None, 2, 3, None],
#     [None, None, 1, 5],
#     [None, None, None, 4],
#     [None, None, None, None]
# ]
# # Expected path: [0, 1, 2, 3]
# print(f"{flow_down(M5, 0)} should be [0, 1, 2, 3]")
#
# # Test case: Circular graph
# M6 = [
#     [None, 1, None],
#     [None, None, 2],
#     [3, None, None]
# ]
# # Expected path: [0, 1, 2, 0]
# print(f"{flow_down(M6, 0)} should be [0, 1, 2, 0]")
#
# # Test case: Ties in minimum weights
# M7 = [
#     [None, 1, 1],
#     [None, None, 2],
#     [None, None, None]
# ]
# # Expected path: [0, 1, 2]
# print(f"{flow_down(M7, 0)} should be [0, 1, 2] or [0, 2]")  # Either option is valid
