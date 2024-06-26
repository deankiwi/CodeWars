
# Definition for a binary tree node.



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        # do an inorder traves through the tree to create a list
        stack = []

        def dfs(curr: TreeNode):
            if curr.left:
                dfs(curr.left)
            stack.append(curr)
            if curr.right:
                dfs(curr.right)

        dfs(root)
        for i in stack:
            print(i.val)

        def balance(i, j) -> TreeNode:
            mid = (j + i) // 2
            val = stack[mid].val
            # print(f'{mid = } {val = } {i = } {j = }')
            curr = TreeNode(val)
            if j >= i:
                # print('left')
                curr.left = balance(i, mid - 1)
                # print('right')
                curr.right = balance(mid + 1, j)
                return curr
            return None

        mid_node = balance(0, len(stack)-1)

        return mid_node


"""
1382. Balance a Binary Search Tree
Medium
Topics
Companies
Hint
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
"""

