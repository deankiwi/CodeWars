// Unique Number of Occurrences — LeetCode #1319 (Easy)
// URL: https://leetcode.com/problems/unique-number-of-occurrences/
// Slug: unique-number-of-occurrences
// Difficulty: Easy
// Paid only: False
// Fetched: 2025-10-11
package main

import "fmt"

func uniqueOccurrences(arr []int) bool {
	count := map[int]int{}
	for _, v := range arr {
		_, exsits := count[v]
		if !exsits {
			count[v] = 0
		}
		count[v] = count[v] + 1
	}
	uniques := map[int]bool{}
	for _, v := range count {
		// v := count[key]
		if uniques[v] {
			return false
		}
		uniques[v] = true
	}
	return true
}

func main() {
	// fmt.Println(uniqueOccurrences([]int{1, 2, 2, 1, 1, 3}))
	fmt.Println(uniqueOccurrences([]int{-3,0,1,-3,1,1,1,-3,10,0}))
}

// Sample Test Case (from LeetCode)
// [1,2,2,1,1,3]
