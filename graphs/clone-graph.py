# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    dictionary = {}
    nodes = [node]
    newNodes = []

    while len(nodes) >= 1 :
        actual_node = nodes.pop(0)
        actual_vals = []
        if actual_node.val not in dictionary:
            dictionary[actual_node.val] = 1
        for _,n in enumerate(actual_node.neighbors):
            if n.val not in dictionary and n.val -1 == actual_node.val:
                nodes.append(n)
            if n.val:
                actual_vals.append(n.val)
        newNodes.append(actual_vals)
    return newNodes


if __name__ == "__main__":
    # Example usage:
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    cloned_graph = cloneGraph(None, node1)
    print(cloned_graph)  # Output: [[2, 4], [1, 3], [2, 4], [1, 3]]