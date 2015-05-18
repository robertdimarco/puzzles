package euler

// PrimeFactors returns an array of the prime factors of the input int
func PrimeFactors(n uint64) []uint64 {
	var i uint64 = 2
	for i*i <= n {
		if n%i == 0 {
			return append(PrimeFactors(n/i), i)
		}
		i++
	}
	return []uint64{n}
}
