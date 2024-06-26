
# Definition for a binary tree node.

from typing import List, Optional

from utils.utils import print_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dummy = TreeNode()

        order_index = {}  # value : index
        for i in range(len(inorder)):
            order_index[inorder[i]] = i

        tree = [[dummy, float("inf")]]  # node : index

        for val in preorder:

            new_node = TreeNode(val)
            index = order_index[val] 
            if index < tree[-1][1]:

                tree[-1][0].left = new_node
                tree.append([new_node, index])
            else:

                while index > tree[-2][1]:

                    tree.pop()
                tree[-1][0].right = new_node
                tree.append([new_node, index])
  
        return dummy.left


print_tree(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))


# preorder [Root, L, R]
# inorder [L, Root, R]


"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
Topics
Companies
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""

