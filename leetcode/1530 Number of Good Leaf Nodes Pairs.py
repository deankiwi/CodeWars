
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0

        def find_leafs(curr):
            nonlocal count
            left = right = None


            if not curr.left and not curr.right:
                return deque([1]+ [0]* (distance -1))
            
            if curr.left:
                left = find_leafs(curr.left)
            if curr.right:
                right = find_leafs(curr.right)
            
            if left and right:
                sums = 0
                for i in range(distance-1):
                    sums += left[i]
                    count += sums*right[distance-2-i]
                for i in range(distance):
                    left[i] += right[i]

                left.pop()
                left.appendleft(0)
                return left
            if right:
                right.pop()
                right.appendleft(0)
                return right
            left.pop()
            left.appendleft(0)

            return left
        
        find_leafs(root)
        return count
        

            


