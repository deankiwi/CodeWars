// Asteroid Collision — LeetCode #735 (Medium)
// URL: https://leetcode.com/problems/asteroid-collision/
// Slug: asteroid-collision
// Difficulty: Medium
// Paid only: False
// Fetched: 2025-10-19
package main

import "fmt"

func asteroidCollision(asteroids []int) []int {

	stack := []int{}
	for _, rock := range asteroids {
		smashed := false
		for len(stack) != 0 && rock < 0 && stack[len(stack)-1] > 0 && !smashed {
			// crash is going to happen

			if stack[len(stack)-1] < rock*-1 {
				stack = stack[:len(stack)-1]
			} else if stack[len(stack)-1] == rock*-1 {
				smashed = true
				stack = stack[:len(stack)-1]
			} else {
				smashed = true
			}
		}
		if !smashed {
			stack = append(stack, rock)
		}

	}
	return stack
}

func main() {
	result := asteroidCollision([]int{5, 10, -5})
	fmt.Println(result)
	fmt.Println(asteroidCollision([]int{8, -8}))
	fmt.Println(asteroidCollision([]int{10, 2}))
	fmt.Println(asteroidCollision([]int{10, 2, -5}))
}

// Sample Test Case (from LeetCode)
// [5,10,-5]
