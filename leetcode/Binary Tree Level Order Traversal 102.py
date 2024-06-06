

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        results = []
        stack = deque()
        stack.append(root)

        while stack:
            traversal = []

            for _ in range(len(stack)):
                curr = stack.popleft()
                traversal.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
            results.append(traversal)

        return results


"""
102. Binary Tree Level Order Traversal
Medium
Topics
Companies
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

