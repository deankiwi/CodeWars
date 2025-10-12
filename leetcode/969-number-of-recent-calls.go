// Number of Recent Calls — LeetCode #969 (Easy)
// URL: https://leetcode.com/problems/number-of-recent-calls/
// Slug: number-of-recent-calls
// Difficulty: Easy
// Paid only: False
// Fetched: 2025-10-12
package main

import "fmt"

type RecentCounter struct {
    requests []int
	head int
}

func Constructor() RecentCounter {
    return RecentCounter{}
}

func (this *RecentCounter) Ping(t int) int {
    this.requests = append(this.requests, t)
    
    for this.requests[this.head] < t-3000 {
		this.head++

    }
    return len(this.requests)-this.head
}

func main() {
	// Example usage:
	obj := Constructor()
	param_1 := obj.Ping(1)
	fmt.Println(param_1) // Output: 1
	param_2 := obj.Ping(100)
	fmt.Println(param_2) // Output: 2
	param_3 := obj.Ping(3001)
	fmt.Println(param_3) // Output: 3
	param_4 := obj.Ping(3002)
	fmt.Println(param_4) // Output: 3
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
// Sample Test Case (from LeetCode)
// ["RecentCounter","ping","ping","ping","ping"]
// [[],[1],[100],[3001],[3002]]

