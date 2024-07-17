
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        result = []
        set_del = set(to_delete)


        stack = deque([(root, True)])

        while len(stack) > 0:
            size = len(stack)
            for _ in range(size):
                curr, delete_node = stack.popleft()
                if curr.val in set_del:
                    delete_node = True
                elif delete_node:
                    result.append(curr)
                    delete_node = False
                else:
                    delete_node = False


                if curr.left:
                    stack.append((curr.left , delete_node))

                    if curr.left.val in set_del:
                        curr.left = None
                if curr.right:
                    stack.append((curr.right , delete_node))

                    if curr.right.val in set_del:
                        curr.right = None

        return result

