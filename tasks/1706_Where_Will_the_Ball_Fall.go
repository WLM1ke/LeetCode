// https://leetcode.com/problems/where-will-the-ball-fall/
package main

func findBall(grid [][]int) []int {
	rez := make([]int, len(grid[0]))

	for i := 0; i < len(grid[0]); i++ {
		rez[i] = traverse(i, grid)
	}

	return rez
}

func traverse(y int, grid [][]int) int {
	for x := 0; x < len(grid); x++ {
		switch dir := grid[x][y]; {
		default:
			y += dir
		case (dir == -1 && y == 0) || (dir == 1 && y == len(grid[0])-1):
			return -1
		case dir == -grid[x][y+dir]:
			return -1
		}
	}

	return y
}
