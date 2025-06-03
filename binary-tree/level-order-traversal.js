// class TreeNode {
//     val: number
//      left: TreeNode | null
//      right: TreeNode | null
//      constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//          this.val = (val===undefined ? 0 : val)
//          this.left = (left===undefined ? null : left)
//          this.right = (right===undefined ? null : right)
//      }
//  }


function levelOrder(root) {
    if (!root) return [];

  let queue = [root];
  let result = [];

  while (queue.length > 0) {
    const levelSize = queue.length;
    const level = [];

    // Process exactly levelSize nodes from this level
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      level.push(node.val);

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(level);
  }

  return result;
};