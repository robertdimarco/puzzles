// https://www.hackerrank.com/contests/projecteuler/challenges/euler002
package main

import (
	"./euler"
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	T, _ := strconv.Atoi(scanner.Text())
	var N []uint64
	N = make([]uint64, T, T)

	for i := 0; i < T; i++ {
		scanner.Scan()
		n, _ := strconv.ParseUint(scanner.Text(), 10, 64)
		N[i] = n
	}

	// List of even Fibonacci numbers less than Max(N):
	var fibs []uint64
	max := euler.Max(N)

	var x, y uint64 = 0, 1
	for x < max {
		z := x + y
		x = y
		y = z
		if z%2 == 0 {
			fibs = append(fibs, z)
		}
	}

	// Cumulative sum by index
	fibSum := []uint64{0}
	for ix := 0; ix < len(fibs); ix++ {
		fibSum = append(fibSum, fibs[ix]+fibSum[ix])
	}

	for ix := 0; ix < T; ix++ {
		n := uint64(N[ix])
		k := 0
		if len(fibs) < 1 {
			fmt.Println(0)
		} else {
			for len(fibs) > k && n >= fibs[k] {
				k++
			}
			fmt.Println(fibSum[k])
		}
	}
}
