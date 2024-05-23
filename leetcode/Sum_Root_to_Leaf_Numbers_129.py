
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        total = {"sum": 0}  # store sum of root to leaf

        def dfs(node, curr_num: str):
            curr_num += str(node.val)
            if node and not node.left and not node.right:
                # hit a leaf
                total["sum"] += int(curr_num)
                return
            if node.left:
                dfs(node.left, curr_num)
            if node.right:
                dfs(node.right, curr_num)

        dfs(root, "")

        return total["sum"]


"""
129. Sum Root to Leaf Numbers
Medium
Topics
Companies
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
"""


'''
Can use 'nonlocal' which would allow you to access the variable outside of function

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, path):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                ans += path * 10 + node.val
                return
            dfs(node.left, path * 10 + node.val)
            dfs(node.right, path * 10 + node.val)
        
        ans = 0
        dfs(root, 0)
        return ans
'''

