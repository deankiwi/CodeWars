// Maximum Average Subarray I — LeetCode #643 (Easy)
// URL: https://leetcode.com/problems/maximum-average-subarray-i/
// Slug: maximum-average-subarray-i
// Difficulty: Easy
// Paid only: False
// Fetched: 2025-10-01
package main

import "fmt"

func findMaxAverage(nums []int, k int) float64 {
	sum := 0
	for i := 0; i < k; i++ {
		sum += nums[i]
	}
	max := float64(sum)
	for i := k; i < len(nums); i++ {
		sum -= nums[i-k]
		sum += nums[i]
		if float64(sum) > max {
			max = float64(sum)
		}
	}

	return max / float64(k)
}

// Sample Test Case (from LeetCode)
// [1,12,-5,-6,50,3]

func main() {
	fmt.Println(findMaxAverage([]int{1, 12, -5, -6, 50, 3}, 4))
}
