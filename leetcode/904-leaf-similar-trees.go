// Leaf-Similar Trees — LeetCode #904 (Easy)
// URL: https://leetcode.com/problems/leaf-similar-trees/
// Slug: leaf-similar-trees
// Difficulty: Easy
// Paid only: False
// Fetched: 2025-10-27
package main

import "fmt"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	leafs1 := bfs(root1)
	leafs2 := bfs(root2)

	
	fmt.Println(leafs1)
	fmt.Println(leafs2)
	if len(leafs1) != len(leafs2) {
		return  false
	}
	for i := range leafs1 {
		if leafs1[i] != leafs2[i]{
			return  false
		}
	}

	return true
}


func bfs(node *TreeNode) []int{
 	result:= []int{}
	
	if node.Left != nil {
		result = append(result, bfs(node.Left)...)
	}
	if node.Right != nil {
		result = append(result, bfs(node.Right)...)
	}
	if node.Left == nil && node.Right == nil {
		result = append(result, node.Val)
	}
	return result
}

func main() {
	// Example usage:
	// Creating two binary trees
	root1 := &TreeNode{3, &TreeNode{5, &TreeNode{6, nil, nil}, &TreeNode{2, &TreeNode{7, nil, nil}, &TreeNode{4, nil, nil}}}, &TreeNode{1, &TreeNode{9, nil, nil}, &TreeNode{8, nil, nil}}}
	root2 := &TreeNode{3, &TreeNode{5, &TreeNode{6, nil, nil}, &TreeNode{7, nil, nil}}, &TreeNode{1, &TreeNode{4, nil, nil}, &TreeNode{2, nil, nil}}}

	// Checking if the two trees are leaf-similar
	result := leafSimilar(root1, root2)
	println(result) // Output: true
}

// Sample Test Case (from LeetCode)
// [3,5,1,6,2,9,8,null,null,7,4]
// [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
