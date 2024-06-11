
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = [root]
        count = 0

        curr = root
        while curr and curr.left:
            curr = curr.left
            stack.append(curr)
        
        while count != k:
            count += 1
            curr = stack.pop()
            if count == k:
                return curr.val
            if curr and curr.right:
                curr = curr.right
                stack.append(curr)
                while curr and curr.left:
                    curr = curr.left
                    stack.append(curr)
        
        return curr.val


'''
230. Kth Smallest Element in a BST
Medium
Topics
Companies
Hint
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
'''

'''
didn't need to traves left left side first

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root
        
        while True:
            while current is not None:
                stack.append(current)
                current = current.left
            
            if not stack:
                break
                
            node = stack.pop()
            k -= 1
            
            if k == 0:
                return node.val
            
            current = node.right
'''

