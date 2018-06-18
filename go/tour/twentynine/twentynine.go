package main

import "fmt"

func main() {
	fmt.Println("Couter")
	// notes https://blog.golang.org/defer-panic-and-recover
	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}
	fmt.Println("done")
}
