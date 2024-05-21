
# Definition for a binary tree node.
from typing import Optional

from utils.utils import array_to_binary_tree, print_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root) -> None:

        if not root:
            return
        parent = root
        curr = root.left

        while parent and (parent.left or parent.right):
            # print(f"{parent.val = }")
            if parent.left and parent.right:
                while curr and (curr.left or curr.right):
                    if curr.right:
                        curr = curr.right
                    else:
                        curr = curr.left
                curr.right = parent.right
            if parent.left:
                parent.right = parent.left
                parent.left = None

            parent = parent.right
            curr = parent.left


tree = array_to_binary_tree([1, 2, 5, 3, 4, None, 6])

print_tree(tree)
x = Solution()
x.flatten(tree)
print_tree(tree)


"""
114. Flatten Binary Tree to Linked List
Medium
Topics
Companies
Hint
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""

