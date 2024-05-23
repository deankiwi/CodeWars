

from typing import Optional

from utils.utils import array_to_binary_tree, print_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def dfs(node, up):
            nonlocal maxPathAns

            maxPathAns = max(maxPathAns, node.val)
            print(f'{maxPathAns = }')

            up += node.val
            if not node.left and not node.right:
                # at leaf

                return max(up, node.val, 0)
            elif node.left and node.right:
                # check if on max path and if so update
                # return max length going through path
                left = dfs(node.left, up)
                right = dfs(node.right, up)
                print(f'{node.val = }')

                
                print(f'{ left , right, up = }')

                maxPathAns = max(
                    maxPathAns, left, right, left + right - node.val 
                )
                print(f'{maxPathAns = }')

                return max(max(left, right) + node.val, node.val, 0)
            elif node.left:
                return max(dfs(node.left, up) + node.val, node.val)

            return max(dfs(node.right, up) + node.val, node.val)

        maxPathAns = root.val
        # create a dummy node as be need to have minimum 1 node with both .left and .right node for dfs to work
        dfs(root, 0)
        return maxPathAns
    

# print(Solution().maxPathSum(TreeNode(1,TreeNode(2),TreeNode(3))))

tree = [-10,9,20,None,None,15,7]

tree_node = array_to_binary_tree(tree)
print_tree(tree_node)
print()
print(Solution().maxPathSum(tree_node), ' == 42') # type: ignore


"""
124. Binary Tree Maximum Path Sum
Hard
Topics
Companies
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""

