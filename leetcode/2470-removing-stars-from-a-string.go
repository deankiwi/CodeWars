// Removing Stars From a String — LeetCode #2470 (Medium)
// URL: https://leetcode.com/problems/removing-stars-from-a-string/
// Slug: removing-stars-from-a-string
// Difficulty: Medium
// Paid only: False
// Fetched: 2025-10-13
package main

func removeStars(s string) string {
	stack := []byte{}
    for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch == '*' {
			stack = stack[:len(stack) - 1]
		} else {
			stack = append(stack, ch)
		}
	}
	return string(stack)
}
func main() {
	// Example usage:
	result := removeStars("leet**cod*e")
	println(result) // Output: "lecoe"
}
// Sample Test Case (from LeetCode)
// "leet**cod*e"

