
graph = {
    0:[1,2],
    1:[0,2],
    2:[0,1,3,4],
    3:[2],
    4:[2]
}

def BFS(root):
    visited = {root}
    neighbors = [root]

    while neighbors :
        node = neighbors.pop(0)
        print(node)

        for neigh in graph.get(node,[]):
            if neigh not in visited: 
                neighbors.append(neigh)
                visited.add(neigh)

if __name__ == "__main__":
    BFS(0)

