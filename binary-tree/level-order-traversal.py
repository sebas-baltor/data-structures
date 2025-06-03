from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]  # use a simple list as our queue

        while queue:
            level_size = len(queue)
            current_level = []

            # Process exactly level_size nodes for this level
            for _ in range(level_size):
                # Pop from front (inefficient for large lists, but works)
                node = queue.pop(0)
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result



if __name__ == "__main__":
    # Constructing a binary tree
    #       1
    #      / \
    #     2   3
    #    / \                
    #   4   5
    #   / \
    #  6   7
#     8
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)


    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.left.left.left = TreeNode(8)    
    solution = Solution()
#     print(solution.levelOrder(root))  # Output: [[1], [2, 3], [4, 5], [6, 7], [8]]
#     print(solution.levelOrder(None))  # Output: []
#     print(solution.levelOrder(TreeNode(1)))  # Output: [[1]]
#     print(solution.levelOrder(TreeNode(1, TreeNode(2))))  # Output: [[1], [2]]
#     print(solution.levelOrder(TreeNode(1, None, TreeNode(3))))  # Output: [[1], [3]]
#     print(solution.levelOrder(TreeNode(1, TreeNode(2), TreeNode(3))))  # Output: [[1], [2, 3]]
#     print(solution.levelOrder(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))))  # Output: [[1], [2, 3], [4]]
#     print(solution.levelOrder(TreeNode(1, None, TreeNode(2, None, TreeNode(3)))))  # Output: [[1], [2], [3]]          
#     print(solution.levelOrder(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))))  # Output: [[1], [2, 4], [3]]
#     print(solution.levelOrder(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5))))  # Output: [[1], [2, 5], [3], [4]]
#     print(solution.levelOrder(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4))))  # Output: [[1], [2, 4], [3]]
#     print(solution.levelOrder(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))))  # Output: [[1], [2, 4], [3, 5]]

    print(solution.levelOrder(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5, TreeNode(6)))))  # Output: [[1], [2, 5], [3, 6], [4]]
        