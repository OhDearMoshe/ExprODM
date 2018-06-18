package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("When is Sat?")
	today := time.Now().Weekday()
	switch time.Saturday {
	case today + 0:
		fmt.Println("It's today")
	case today + 1:
		fmt.Println("Tmoz")
	case today + 2:
		fmt.Println("Two days")
	default:
		fmt.Println("Quite a bit far away")
	}
}
