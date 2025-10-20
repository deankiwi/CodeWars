// Delete the Middle Node of a Linked List — LeetCode #2216 (Medium)
// URL: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
// Slug: delete-the-middle-node-of-a-linked-list
// Difficulty: Medium
// Paid only: False
// Fetched: 2025-10-20
package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteMiddle(head *ListNode) *ListNode {

	if head.Next == nil {
		return nil
	}
	middle := head
	tail := head

	for tail.Next != nil {
		tail = tail.Next
		if tail.Next == nil {
			// remove middle
			remove := middle.Next.Next
			middle.Next = remove
			return head
		}
		tail = tail.Next
		if tail.Next == nil {
			// remove middle
			remove := middle.Next.Next
			middle.Next = remove
			return head
		}

		middle = middle.Next

	}
	return head
}

func main() {
	// Example usage:
	// Creating a linked list: 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
	head := &ListNode{1, &ListNode{3, &ListNode{4, &ListNode{7, &ListNode{1, &ListNode{2, &ListNode{6, nil}}}}}}}

	// Deleting the middle node
	newHead := deleteMiddle(head)

	// Printing the modified linked list
	for node := newHead; node != nil; node = node.Next {
		print(node.Val, " ")
	}
}

// Sample Test Case (from LeetCode)
// [1,3,4,7,1,2,6]
