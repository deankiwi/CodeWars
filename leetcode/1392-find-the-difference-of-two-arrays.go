// Find the Difference of Two Arrays — LeetCode #1392 (Easy)
// URL: https://leetcode.com/problems/find-the-difference-of-two-arrays/
// Slug: find-the-difference-of-two-arrays
// Difficulty: Easy
// Paid only: False
// Fetched: 2025-10-11
package main

import "fmt"

func findDifference(nums1 []int, nums2 []int) [][]int {
	set1 := make(map[int]bool)
	set2 := make(map[int]bool)
	for _, v := range nums1 {
		set1[v] = true
	}
	for _, v := range nums2 {
		set2[v] = true
	}
	unique1 := make([]int, 0)
	unique2 := make([]int, 0)
	for k := range set1 {

		if set2[k] != true {
			unique1 = append(unique1, k)
		}
	}
	for k := range set2 {

		if set1[k] != true {
			unique2 = append(unique2, k)
		}
	}

	return [][]int{unique1, unique2}

}

func main() {
	fmt.Println(findDifference([]int{1, 2, 3}, []int{2, 4, 6}))
}

// Sample Test Case (from LeetCode)
// [1,2,3]
// [2,4,6]
