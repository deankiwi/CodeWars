// Minimum Time to Make Rope Colorful — LeetCode #1700 (Medium)
// URL: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
// Slug: minimum-time-to-make-rope-colorful
// Difficulty: Medium
// Paid only: False
// Fetched: 2025-11-03
package main

func minCost(colors string, neededTime []int) int {
	if len(colors) == 0 {
		return 0
	}
    curr := colors[0]
	currWait := neededTime[0]
	awaited := 0

	for i := 1; i < len(colors); i++ {
		letter := colors[i]
		if letter == curr {
			if neededTime[i] > currWait {
				awaited += currWait
				currWait = neededTime[i]
			} else {
				awaited += neededTime[i]
			}
		} else {
			curr = colors[i]
			currWait = neededTime[i]
		}
	}
	return awaited
}

func main() {
	// You can use this main function to test your implementation.
	// Sample Test Case
	colors := "abaac"
	neededTime := []int{1, 2, 3, 4, 5}
	result := minCost(colors, neededTime)
	println(result) // Expected output: 3
}
// Sample Test Case (from LeetCode)
// "abaac"
// [1,2,3,4,5]

