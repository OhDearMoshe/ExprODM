package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("おはよう ございます")
	case t.Hour() < 17:
		fmt.Println("こんにちは")
	default:
		fmt.Println("こんばんは")
	}
}
