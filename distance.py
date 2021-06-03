# This program finds the distance between A to B and B to C.

# Graph distance in list
edges = [['A', 'B', 5], ['B', 'C', 4], ['C', 'D', 8], ['D', 'C', 8],
         ['D', 'E', 6], ['A', 'D', 5], ['C', 'E', 2], ['E', 'B', 3], ['A', 'E', 7]]


# route
route = ['A', 'B', 'C']


def find_route():  # find route A->B->C
    distance = 0
    route_found = False  # route found flag
    for edge in edges:
        if edge[0] == route[0] and edge[1] == route[1]:  # If first node is 'A' and second node is 'B'
            distance += edge[2]
            for x in edges:
                if x[0] == route[1] and x[1] == route[2]:  # If first node is 'B' and last node is 'C'
                    distance += x[2]
                    route_found = True  # Set route found
                    break
            if route_found:
                print("The distance of A to B and B to C is ", distance)  # Print the distance
            else:
                print("No such route exists.")  # Print no route exists
            break
    return route_found


route_fetched = find_route()
if not route_fetched:
    print("No such route exists.")
