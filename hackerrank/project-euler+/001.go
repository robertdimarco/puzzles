// https://www.hackerrank.com/contests/projecteuler/challenges/euler001
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
		fmt.Println(euler.A126592(N - 1))
	}
}
