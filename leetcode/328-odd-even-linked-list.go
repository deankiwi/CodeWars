// Odd Even Linked List — LeetCode #328 (Medium)
// URL: https://leetcode.com/problems/odd-even-linked-list/
// Slug: odd-even-linked-list
// Difficulty: Medium
// Paid only: False
// Fetched: 2025-10-26
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

func oddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	oddCurr := head
	curr := head.Next
	evenFirst := curr
	evenCurr := curr
	evenTurn := false

	for curr.Next != nil {
		curr = curr.Next
		if evenTurn {
			evenCurr.Next = curr
			evenCurr = evenCurr.Next
		} else {
			oddCurr.Next = curr
			oddCurr = oddCurr.Next
		}
		evenTurn = !evenTurn
	}
	evenCurr.Next = nil
	oddCurr.Next = evenFirst
	return head
}

func main() {
	// Example usage:
	// Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
	head := &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, nil}}}}}

	// Rearranging the linked list
	newHead := oddEvenList(head)

	// Printing the modified linked list
	for newHead != nil {
		print(newHead.Val, " ")
		newHead = newHead.Next
	}
}

// Sample Test Case (from LeetCode)
// [1,2,3,4,5]
