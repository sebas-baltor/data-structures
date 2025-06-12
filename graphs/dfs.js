const graph = {
  0: [1, 2],
  1: [0, 2],
  2: [0, 1, 3, 4],
  3: [2],
  4: [2],
};

// const graph = {
//   1: [2, 3],
//   2: [4],
//   3: [5],
//   4: [],
//   5: []
// };

function RecursiveDFS(node, visited = new Set()) {
  if (visited.has(node)) return;

  visited.add(node);
  console.log(node);

  for (const neigh of graph[node] || []) {
    // console.log("neigh: ",neigh)
    RecursiveDFS(neigh, visited);
  }
}

RecursiveDFS(0);
