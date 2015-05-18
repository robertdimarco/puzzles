package euler

// A000217 : Triangular numbers: a(n) = C(n+1,2) = n(n+1)/2 = 0+1+2+...+n.
// 0, 1, 3, 6, 10, 15, 21, 28, 36, 45 ...
func A000217(n uint64) uint64 {
	return (n*n + n) >> 1
}

// A126592 : Sum of numbers <=n which are multiples of 3 or 5.
// 0, 0, 3, 3, 8, 14, 14, 14, 23, 33 ...
func A126592(n uint64) uint64 {
	return 3*A000217(n/3) + 5*A000217(n/5) - 15*A000217(n/15)
}
