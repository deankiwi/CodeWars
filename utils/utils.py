from collections import deque
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        return str(self.val)

    def display(self):
        print(f"{self.val}, ", end="")
        if self.next:
            self.next.display()
        else:
            print(":end")


def create_linked_list(head: List[int], pos=-1):
    output = []
    for num in head:
        output.append(ListNode(num))
    for i in range(len(head) - 1):
        output[i].next = output[i + 1]
    if pos != -1:
        output[-1].next = output[pos]
    return output[0]


from typing import Optional, Tuple, List


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


def print_tree(root: Optional[TreeNode]) -> None:
    if not root:
        print("Empty tree")
        return

    # A queue to perform level-order traversal
    queue: List[Tuple[Optional[TreeNode], int]] = [(root, 0)]
    current_level = 0
    current_level_nodes: List[str] = []

    while queue:
        node, level = queue.pop(0)

        if level > current_level:
            print(" ".join(current_level_nodes))
            current_level_nodes = []
            current_level = level

        current_level_nodes.append(str(node.val) if node else "null")

        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

    # Print the last level
    if current_level_nodes:
        print(" ".join(current_level_nodes))


def array_to_binary_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        current = queue.popleft()
        
        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    
    return root

# Example usage:
if __name__ == "__main__":
    # Construct a sample binary tree
    #       1
    #      / \
    #     2   3
    #    /|   |\
    #   4 5   6 7
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    print_tree(tree)
