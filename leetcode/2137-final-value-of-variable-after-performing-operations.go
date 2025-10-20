// Final Value of Variable After Performing Operations — LeetCode #2137 (Easy)
// URL: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
// Slug: final-value-of-variable-after-performing-operations
// Difficulty: Easy
// Paid only: False
// Fetched: 2025-10-20
package main

func finalValueAfterOperations(operations []string) int {
	result := 0
	for _, v := range operations {
		switch v {
		case "++X", "X++":
			{
				result++
			}
		default:{
			result--
		}

		}

	}
	return result
}
func main() {
	// Example usage:
	result := finalValueAfterOperations([]string{"--X", "X++", "X++"})
	println(result) // Output: 1
}

// Sample Test Case (from LeetCode)
// ["--X","X++","X++"]
