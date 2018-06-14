package main

import "fmt"

// More pythong vibes
func swap(x, y string) (string, string) {
	return y, x
}

func main() {
	func a, b := swap("hello", "world")
	fmt.Println(a, b)
}