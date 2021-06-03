# This program finds the possible paths starting at C and ending at C with a maximum of 3 stops.

# Graph distance in list
edges = [['A', 'B', 5], ['B', 'C', 4], ['C', 'D', 8], ['D', 'C', 8],
         ['D', 'E', 6], ['A', 'D', 5], ['C', 'E', 2], ['E', 'B', 3], ['A', 'E', 7]]


# Array to store the paths
array = []


def find_nextNode(next_node):  # find the next node
    for x in edges:
        if x[0] == next_node:
            next_node = x[1]
            array.append(x)
            break
    return next_node  # returns the next node found, to begin next search from that node


def find_paths():
    node = 'C'  # Beginning and ending node
    i = 0
    for edge in edges:  # Traverse through all the edges to find the node that begins with C
        if edge[0] == node:
            next_node = edge[1]
            array.append(edge)
            while (next_node != node) and (i <= 9):  # loop till the end node found or limit reached
                next_node = find_nextNode(next_node)
                i = i + 1
                if (next_node == node) and (len(array) < 4):  # If node found, then print the path
                    final_path = ""
                    for nodes in array:
                        final_path = final_path + nodes[0] + nodes[1]
                    print("The path from C to C is ", final_path)  # print the path
                    array.clear()


find_paths()  # Find the path
