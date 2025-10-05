// Find the Highest Altitude — LeetCode #1833 (Easy)
// URL: https://leetcode.com/problems/find-the-highest-altitude/
// Slug: find-the-highest-altitude
// Difficulty: Easy
// Paid only: False
// Fetched: 2025-10-05
package main

import "fmt"

func largestAltitude(gain []int) int {
    max := 0
	curr := 0
	for _, v := range gain {
		curr += v
		if curr > max {
			max = curr
		}
	}
	return max
}

func main()  {
	fmt.Println(largestAltitude([]int{-5,1,5,0,-7}))
}
// Sample Test Case (from LeetCode)
// [-5,1,5,0,-7]

