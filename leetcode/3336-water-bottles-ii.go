// Water Bottles II — LeetCode #3336 (Medium)
// URL: https://leetcode.com/problems/water-bottles-ii/
// Slug: water-bottles-ii
// Difficulty: Medium
// Paid only: False
// Fetched: 2025-10-06
package main

import (
	"fmt"
)

func maxBottlesDrunk(numBottles int, numExchange int) int {
	drank := numBottles
	empty := numBottles
	numBottles = 0
    for empty / numExchange >= 1 {
		numBottles = empty / numExchange
		empty -= (empty / numExchange) * numExchange
		drank += numBottles
		empty += numBottles + (empty % numExchange)
		numBottles = 0
		numExchange += 1
	}
	return drank 
}

func main()  {
	fmt.Println(maxBottlesDrunk(13,6))
	fmt.Println("13 == %s",maxBottlesDrunk(10,3))
}
// Sample Test Case (from LeetCode)
// 13
// 6

