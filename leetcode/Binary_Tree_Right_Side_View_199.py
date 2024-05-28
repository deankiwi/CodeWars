
# Definition for a binary tree node.
from typing import List, Optional

from utils.utils import array_to_binary_tree, print_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        views = []
        stack = []
        depth = 0

        curr = root

        while curr:
            depth += 1
            stack.append([curr, depth])
            views.append(curr.val)
            curr = curr.right

        max_depth = depth

        while stack:
            curr, depth = stack.pop()

            curr = curr.left
            while curr:
                depth += 1
                stack.append([curr, depth])
                if depth > max_depth:
                    views.append(curr.val)
                    max_depth = depth
                curr = curr.right

        return views


print(Solution().rightSideView(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))))


tree = array_to_binary_tree([1, 2, 3, None, 5, 6])
# print_tree(tree)
print(Solution().rightSideView(tree))


"""
199. Binary Tree Right Side View
Medium
Topics
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


'''
other solution

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def solve(root, lvl):
        	if root:
        		if len(res)==lvl:
        			res.append(root.val)
        		solve(root.right, lvl + 1)
        		solve(root.left, lvl + 1)
        	return 

        res = []
        solve(root,0)
        return res
'''

