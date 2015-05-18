package euler

// Max computes the maximum of the input slice
func Max(slice []uint64) uint64 {
	max := slice[0]
	var ix uint64 = 1
	for ix < uint64(len(slice)) {
		if slice[ix] > max {
			max = slice[ix]
		}
		ix++
	}
	return max
}
