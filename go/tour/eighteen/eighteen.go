package main

import "fmt"

func main() {
	sum := 0
	// Lack of () scares me
	for i := 0; i < 10; i++ {
		sum += 1
	}
	fmt.Println(sum)
}
