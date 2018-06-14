package main

import "fmt

func main() {
	v := 42
	// Won't compile
	// v := 3.142
	// v = 3.142
	// v := 3
	v = 3
	fmt.Printf("v is of type %T\n", v)
}