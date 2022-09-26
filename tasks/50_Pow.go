package main

// https://leetcode.com/problems/powx-n
func myPow(x float64, n int) float64 {
	switch {
	case n == 0:
		return 1
	case n < 0:
		return 1 / myPow(x, -n)
	case n%2 == 0:
		half := myPow(x, n/2)
		return half * half
	default:
		return myPow(x, n-1) * x
	}
}
