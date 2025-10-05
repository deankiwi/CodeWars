// Convert Integer to the Sum of Two No-Zero Integers — LeetCode #1440 (Easy)
// URL: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
// Slug: convert-integer-to-the-sum-of-two-no-zero-integers
// Difficulty: Easy
// Paid only: False
// Fetched: 2025-09-08
package main

import "fmt"


func getNoZeroIntegers(n int) []int {
	result := []int{}
	result = append(result, n-1)
	result = append(result, n-result[0])
	for {
		if (!hasZero(result[0]) && !hasZero(result[1])) || result[0] < 1  {
			break
		}
		result[0]--
		result[1]++
	}

    return result
}

func hasZero(num int) bool {
	for num > 0 {
		if num%10==0 {
			return true
		}
		num /=10
	}
	return false
}

func main() {
	fmt.Println(getNoZeroIntegers(2))
	fmt.Println(getNoZeroIntegers(11))
	fmt.Println(getNoZeroIntegers(1010))
}