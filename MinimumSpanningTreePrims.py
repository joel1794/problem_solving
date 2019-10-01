def prims_algo(matrix, starting_node=0):
    elements = len(matrix)
    node_visited = [False] * elements
    parent = [None] * elements
    maximum_edge = [0] * elements

    maximum_edge[starting_node] = 999
    parent[starting_node] = -1
    number_of_nodes = elements
    # print(minimum_edge)

    for node in range(number_of_nodes):
        max_val = -999
        for i in range(len(maximum_edge)):
            if maximum_edge[i] > max_val and node_visited[i] is not True:
                max_val = maximum_edge[i]
                max_element = i
                # print(max_val, max_element)

        node_visited[max_element] = True
        new_node = max_element
        # print(new_node)
        # print(node_visited)
        for j in range(number_of_nodes):
            if node_visited[j] is False and matrix[new_node][j] > 0 and matrix[new_node][j] > maximum_edge[j]:
                maximum_edge[j] = matrix[new_node][j]
                parent[j] = new_node

        # print(node_visited)
        # print(maximum_edge)
    print("for start node ", starting_node + 1, "the minimum spanning tree is as follows:")
    nodes_visited_for_printing = [False] * number_of_nodes
    for i in range(number_of_nodes):
        i_inc = -1
        for j in range(number_of_nodes):
            if parent[j] == starting_node:
                print(parent[j] + 1, "-->", j + 1, "weight = ", matrix[parent[j]][j])
                i_inc += 1
        nodes_visited_for_printing[starting_node] = True

        for k in range(number_of_nodes):
            if nodes_visited_for_printing[k] is False:
                starting_node = k

max_pairwise_alignment_scores = [[0,85,0,0,0,84,0,0,0,0],
[85,0,79,0,0,0,94,0,0,0],
[0,79,0,0,0,0,0,85,0,0],
[0,0,0,0,105,0,0,0,0,0],
[0,0,0,105,0,0,0,79,0,0],
[84,0,0,0,0,0,0,0,0,78],
[0,94,0,0,0,0,0,0,0,0],
[0,0,85,0,79,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,81],
[0,0,0,0,0,78,0,0,81,0]]

for i in range(len(max_pairwise_alignment_scores)):
    prims_algo(max_pairwise_alignment_scores, i)
# print(max_pairwise_alignment_scores)