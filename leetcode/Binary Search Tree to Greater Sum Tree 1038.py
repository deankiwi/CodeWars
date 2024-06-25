

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        stack = []
        bigger = 0

        curr = root
        while curr:
            stack.append(curr)
            curr = curr.right

        while stack:
            curr = stack.pop()
            curr.val += bigger
            bigger = curr.val
            if curr.left:
                curr = curr.left
                while curr:
                    stack.append(curr)
                    curr = curr.right

        return root



"""
1038. Binary Search Tree to Greater Sum Tree
Medium
Topics
Companies
Hint
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:

Input: root = [0,null,1]
Output: [1,null,1]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val <= 100
All the values in the tree are unique.
"""


'''
another solution,
- used self.val to store value in class
- dfs rather than stack


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            self.val += node.val
            node.val = self.val
            dfs(node.left)
        
        dfs(root)
        return root
'''

