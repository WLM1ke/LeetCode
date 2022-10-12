package main

func maxArea(height []int) int {
	l, r := 0, len(height)-1

	area := 0

	for l < r {
		area = max11(area, (r-l)*min(height[r], height[l]))

		if height[l] < height[r] {
			l++
		} else {
			r--
		}
	}

	return area
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}

func max11(a, b int) int {
	if a > b {
		return a
	}

	return b
}
