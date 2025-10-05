package main

import "fmt"
func sumZero(n int) []int {
	result :=  make([]int,0)
	for i := 1; i <= n/2; i++ {
		result = append(result, i)
		result = append(result, -i)
	}
	if n%2 == 1 {
		result = append(result, 0)
	}

    return result
}

func main()  {
	fmt.Println(sumZero(5))
	fmt.Println(sumZero(4))
}