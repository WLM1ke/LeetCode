// https://leetcode.com/problems/toeplitz-matrix/
package main

func isToeplitzMatrix(matrix [][]int) bool {
	for x := 1; x < len(matrix); x++ {
		for y := 1; y < len(matrix[0]); y++ {
			if matrix[x][y] != matrix[x-1][y-1] {
				return false
			}
		}
	}

	return true
}
