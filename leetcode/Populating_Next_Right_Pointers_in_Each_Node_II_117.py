

from utils.utils import array_to_binary_tree, print_tree


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":

        if not root:
            return root

        parent = root
        leftmost = None
        left = None

        while parent.left or parent.right or parent.next or leftmost:

            if parent.left:

                if left:
                    left.next = parent.left
                    left = left.next
                else:

                    left = parent.left
                    leftmost = parent.left
            if parent.right:

                if left:
                    left.next = parent.right
                    left = left.next
                else:

                    left = parent.right
                    leftmost = parent.right
            if parent.next:
                parent = parent.next

            elif leftmost:
                parent = leftmost
                leftmost = None
                left = None

        return root


# tree = Node(1, Node(2,Node(4),Node(5)), Node(3))
# print_tree(Solution().connect(tree))

# tree = Node(1)
# tree.right = Node(2)
# print_tree(Solution().connect(tree))

tree = array_to_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4])

print_tree(Solution().connect(tree))

"""
117. Populating Next Right Pointers in Each Node II
Medium
Topics
Companies
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""


"""
cleaner solution 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr=root
        dummy=Node(-999)        
        head=root        

		while head:
            curr=head # initialize current level's head
            prev=dummy # init prev for next level linked list traversal
			# iterate through the linked-list of the current level and connect all the siblings in the next level
            while curr:  
                if curr.left:
                    prev.next=curr.left
                    prev=prev.next
                if curr.right:
                    prev.next=curr.right
                    prev=prev.next                                                
                curr=curr.next
            head=dummy.next # update head to the linked list of next level
            dummy.next=None # reset dummy node
        return root
            
"""

