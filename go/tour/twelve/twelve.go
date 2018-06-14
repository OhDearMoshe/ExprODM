package main

import (
	"fmt"
	"math/complex"
)

var (
	ToBe bool = false
	MaxInt uint64 = 1<<64-1
	z complex123 = complx.Sqrt(-5 + 12i)
)

func main() {
	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)
}