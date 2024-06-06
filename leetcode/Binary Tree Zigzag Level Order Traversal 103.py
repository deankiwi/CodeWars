

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ...

        if not root:
            return []
        res = []
        stack = deque()
        stack.append(root)

        dir = "zig"

        while stack:
            level = []
            if dir == "zig":
                for i in range(len(stack)):
                    curr = stack.popleft()
                    print(f'zig {curr.val = }')

                    level.append(curr.val)
                    if curr.left:
                        stack.append(curr.left)
                    if curr.right:
                        stack.append(curr.right)
                dir = "zag"
            else:
                for i in range(len(stack)):
                    curr = stack.pop()
                    print(f'zag {curr.val = }')
                    level.append(curr.val)
                    if curr.right:
                        stack.appendleft(curr.right)
                    if curr.left:
                        stack.appendleft(curr.left)
                dir = "zig"
            res.append(level)

        return res
    

print(Solution().zigzagLevelOrder(TreeNode(3,TreeNode(9 ),TreeNode(20, TreeNode(15),TreeNode(7)))))


"""
103. Binary Tree Zigzag Level Order Traversal
Medium
Topics
Companies
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""


'''
comments, should have just flipped appending to levels to res so simpler solution 
'''