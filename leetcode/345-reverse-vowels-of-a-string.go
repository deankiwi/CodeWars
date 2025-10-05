// Reverse Vowels of a String — LeetCode #345 (Easy)
// URL: https://leetcode.com/problems/reverse-vowels-of-a-string/
// Slug: reverse-vowels-of-a-string
// Difficulty: Easy
// Paid only: False
// Fetched: 2025-09-08
package main

import (
	"fmt"
	"strings"
)

func reverseVowels(s string) string {
	runes := []rune(s)
	right := len(runes) - 1
	stack := []rune{}
	var result strings.Builder

	for left, v := range runes {
		if isVowel(v) {
			if left < right {
				for left <= right {

					if isVowel(runes[right]) {
						result.WriteRune(runes[right])
						stack = append(stack, v)
						right--
						break
					}
					right--
				}
			} else {
				result.WriteRune(stack[len(stack)-1])
				stack = stack[:len(stack)-1]
			}
		} else {
			result.WriteRune(v)
		}
	}

	return result.String()
}
func isVowel(c rune) bool {
	return strings.ContainsRune("aeiouAEIOU", c)
}

func main() {
	fmt.Println(reverseVowels("aeiou"))
}
