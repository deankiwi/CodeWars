

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:

        stack = deque()
        stack.append((root , ""))
        startFound = False
        destFound = False
        while len(stack) > 0:
            size = len(stack)

            for i in range(size):
                curr , path = stack.popleft()
                if curr.val == startValue:
                    startFound = True
                    startPath: str = path
                if curr.val == destValue:
                    destFound = True
                    destPath : str = path
                if startFound and destFound:
                    break

                if curr.left:
                    stack.append((curr.left , path + "L"))
                if curr.right:
                    stack.append((curr.right , path + "R"))
                
            if startFound and destFound:
                break
        min_size = min(len(startPath), len(destPath))
        if min_size == 0:
            return startPath + destPath # type: ignore
        i = 0
        while i < min_size and startPath[i] == destPath[i]:
            i+=1
        
        result = "U" * len(startPath[i:]) + destPath[i:]

                


