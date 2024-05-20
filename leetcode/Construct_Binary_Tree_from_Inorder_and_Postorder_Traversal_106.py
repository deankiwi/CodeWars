
from typing import List, Optional

from utils.utils import print_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        val = postorder[-1]
        head = TreeNode(val)

        index = inorder.index(val)

        head.left = self.buildTree(inorder[:index], postorder[:index])
        head.right = self.buildTree(inorder[index + 1 :], postorder[index:-1])

        return head


print_tree(Solution().buildTree([2, 1], [2, 1]))

"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium
Topics
Companies
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""


'''
improve solution

rather than using find on each recursion you can do it once then pass it down

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inMap={}
        for i in range(len(inorder)):
            inMap[inorder[i]]=i
        
        root=self.treeBuild(postorder,0,len(postorder)-1,inorder,0,len(inorder)-1,inMap)
        
        return root
    
    def treeBuild(self,postorder,postStart,postEnd,inorder,inStart,inEnd,inMap):
        
        if postStart>postEnd or inStart>inEnd:
            return None
        
        root=TreeNode(postorder[postEnd])
        
        index=inMap[root.val]
        
        leftNums=index-inStart
        
        root.left=self.treeBuild(postorder,postStart,postStart+leftNums-1,inorder,inStart,index-1,inMap)
        
        root.right=self.treeBuild(postorder,postStart+leftNums,postEnd-1,inorder,index+1,inEnd,inMap)
        
        return root
'''

