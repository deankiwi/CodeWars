// Merge Strings Alternately — LeetCode #1894 (Easy)
// URL: https://leetcode.com/problems/merge-strings-alternately/
// Slug: merge-strings-alternately
// Difficulty: Easy
// Paid only: False
// Fetched: 2025-09-07
package main

func mergeAlternately(word1 string, word2 string) string {
	result := make([]byte,0)
	min := len(word1)
	maxWord := word1
	if len(word2) < min {
		min = len(word2)
		maxWord = word2
	}
	for i := 0; i < min; i++ {
		result = append(result, word1[i])
		result = append(result, word2[i])
	}
	for i := min; i < len(maxWord); i++ {
		result = append(result, maxWord[i])
	}

	
    return string(result)
}
// Sample Test Case (from LeetCode)
// "abc"


func main()  {

	println(mergeAlternately("abc", "pqr"))
	println(mergeAlternately("ab", "pqrs"))
	println(mergeAlternately("abcd", "pq"))
}