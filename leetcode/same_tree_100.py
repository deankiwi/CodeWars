from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def array_tree(root):
            if not root:
                return
            return [root.val, array_tree(root.left), array_tree(root.right)]
        p_tree = array_tree(p)
        q_tree = array_tree(q)
        # print(p_tree)
        # print(q_tree)

        return p_tree == q_tree


print(
    Solution().isSameTree(
        TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))
    ),
    " = True",
)
print(
    Solution().isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))),
    " = False",
)


'''
other solutions

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if p or q:
                if not p or not q or p.val != q.val:
                    return False
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
        return True
'''

