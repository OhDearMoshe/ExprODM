package main

import (
	"fmt"
)

func Sqrt(x float64) float64 {
	z := 1.0
	previous := 4.0 // Arbitary bigger number
	for y := 1; y < 10; y++ {
		z -= (z*z - x) / (2 * z)
		if z == previous {
			return z
		}
		fmt.Println(z)
		previous = z
	}
	return z
}

func main() {
	fmt.Println(Sqrt(4))
	fmt.Println("Done ^")
}
