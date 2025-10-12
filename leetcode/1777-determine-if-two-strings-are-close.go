// Determine if Two Strings Are Close — LeetCode #1777 (Medium)
// URL: https://leetcode.com/problems/determine-if-two-strings-are-close/
// Slug: determine-if-two-strings-are-close
// Difficulty: Medium
// Paid only: False
// Fetched: 2025-10-12
package main

import "fmt"

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}
	count1 := counter(word1)
	count2 := counter(word2)

	count1vals := map[int]int{}
	for _, v := range count1 {
		count1vals[v]++
	}
	for key, v := range count2 {
		count1vals[v]--
		_, exsits := count1[key]
		if count1vals[v] < 0 || !exsits {
			return false
		}
	}
	return true
}

func counter(word string) map[rune]int {
	count := map[rune]int{}
	for _, ch := range word {
		count[ch]++
	}
	return count
}

func main() {
	fmt.Println(closeStrings("abc", "bca"))
	fmt.Println(closeStrings("aab", "ccd"))
}

// Sample Test Case (from LeetCode)
// "abc"
// "bca"
