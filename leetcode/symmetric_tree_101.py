
# Definition for a binary tree node.
from turtle import right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isEqual(left, right):
            if left == right == None:
                return True
            elif not (left and right):
                return False
            # now we know they are both Treenode
            elif left.val != right.val:
                return False
            else:
                return isEqual(left.left, right.right) and isEqual(
                    left.right, right.left
                )
        return isEqual(root.left, root.right)

 


"""
101. Symmetric Tree
Easy
Topics
Companies
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
"""

