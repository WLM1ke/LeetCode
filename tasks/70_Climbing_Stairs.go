package main

func climbStairs(n int) int {
	s_2 := 1
	s_1 := 1

	for ; n > 1; n-- {
		s_2, s_1 = s_1, s_1+s_2
	}

	return s_1
}
