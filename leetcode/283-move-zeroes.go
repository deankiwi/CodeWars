// Move Zeroes — LeetCode #283 (Easy)
// URL: https://leetcode.com/problems/move-zeroes/
// Slug: move-zeroes
// Difficulty: Easy
// Paid only: False
// Fetched: 2025-09-14
package main

import "fmt"

func moveZeroes(nums []int) {
	left := 0
	right := 0
	for right < len(nums) {
		if nums[right] == 0 {
			right ++
		} else {
			// todo do something
			right--
		}
}

// Sample Test Case (from LeetCode)
// [0,1,0,3,12]

func main() {
	myList := []int{0, 0, 1}
	// myList := []int{0, 1, 0, 3, 12}
	fmt.Println(myList)
	moveZeroes(myList)
	fmt.Println(myList)
}
