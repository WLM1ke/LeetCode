package main

// https://leetcode.com/problems/find-k-closest-elements/
func findClosestElements(arr []int, k int, x int) []int {
	first := 0
	last := len(arr) - k
	for first < last {
		next := (first + last) / 2
		if x-arr[next] > arr[next+k]-x {
			first = next + 1
		} else {
			last = next
		}
	}

	return arr[first : first+k]
}
