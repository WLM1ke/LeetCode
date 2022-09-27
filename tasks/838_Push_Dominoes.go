package main

import "strings"

// https://leetcode.com/problems/push-dominoes/
func pushDominoes(dominoes string) string {
	falling := make([]int, 0)

	rez := make([]string, len(dominoes))

	for pos := range dominoes {
		dir := dominoes[pos : pos+1]
		rez[pos] = dir

		if dominoes[pos:pos+1] != "." {
			falling = append(falling, pos)
		}
	}

	for len(falling) > 0 {
		fallingNext := make([]int, 0)
		skip := false

		for _, pos := range falling {
			dir := rez[pos]

			if skip {
				skip = false

				continue
			} else if (pos == 0 && dir == "L") || (pos == len(rez)-1 && dir == "R") {
				continue
			} else if pos == 1 && rez[0] == "." && dir == "L" {
				rez[0] = "L"
			} else if pos == len(rez)-2 && rez[len(rez)-1] == "." && dir == "R" {
				rez[len(rez)-1] = "R"
			} else if dir == "L" && rez[pos-1] == "." {
				rez[pos-1] = "L"
				fallingNext = append(fallingNext, pos-1)
			} else if dir == "R" && rez[pos+1] == "." && rez[pos+2] == "L" {
				skip = true
			} else if dir == "R" && rez[pos+1] == "." && rez[pos+2] != "L" {
				rez[pos+1] = "R"
				fallingNext = append(fallingNext, pos+1)
			}
		}

		falling = fallingNext
	}

	return strings.Join(rez, "")
}
