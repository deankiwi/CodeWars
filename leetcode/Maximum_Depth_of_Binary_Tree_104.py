

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def depth(self, root, d):
        if not root:
            return d-1

        return max(self.depth(root.left, d + 1), self.depth(root.right, d + 1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        print(self.depth(root, 1))
        return self.depth(root, 1)


bin_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(Solution().maxDepth(bin_tree), " = 3")
print(Solution().maxDepth(TreeNode(1, None, TreeNode(2))), " = 3")

