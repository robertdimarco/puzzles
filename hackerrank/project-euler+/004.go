// https://www.hackerrank.com/contests/projecteuler/challenges/euler004
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

	for i := 0; i < T; i++ {
		scanner.Scan()
		N, _ := strconv.ParseUint(scanner.Text(), 10, 64)
		var max uint64
		for ix := 111; ix < 999; ix++ {
			for jx := ix; jx < 999; jx++ {
				x := uint64(ix * jx)
				if x < N && x > max {
					s := strconv.FormatUint(x, 10)
					if s == euler.StringReverse(s) {
						max = x
					}
				}
			}
		}
		fmt.Println(max)
	}
}
