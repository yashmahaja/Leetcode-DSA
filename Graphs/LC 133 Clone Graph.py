class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    if not node:
        return None

    old_new = {}
    stack = [node]
    old_new[node] = Node(node.val)

    while stack:
        current = stack.pop()

        for neighbor in current.neighbors:
            if neighbor not in old_new:
                old_new[neighbor] = Node(neighbor.val)
                stack.append(neighbor)
            old_new[current].neighbors.append(old_new[neighbor])

    return old_new[node]


# Helper function to build a graph from adjacency list
def buildGraph(adj_list):
    if not adj_list:
        return None

    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}

    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]

    return nodes[1]


# Helper function to print graph
def printGraph(node):
    visited = set()
    queue = [node]
    result = {}

    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        result[current.val] = [n.val for n in current.neighbors]
        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

    return result


# Test the function
adj_List = [[2, 4], [1, 3], [2, 4], [1, 3]]
original_graph = buildGraph(adj_List)
cloned_graph = cloneGraph(original_graph)

print("Original Graph:", printGraph(original_graph))
print("Cloned Graph:", printGraph(cloned_graph))
