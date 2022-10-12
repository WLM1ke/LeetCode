package main

import "sort"

func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool { return intervals[i][0] < intervals[j][0] })

	rez := make([][]int, 0, len(intervals))

	start, end := intervals[0][0], intervals[0][1]

	for _, interval := range intervals {
		if interval[0] > end {
			rez = append(rez, []int{start, end})
			start, end = interval[0], interval[1]
		} else if interval[1] > end {
			end = interval[1]
		}
	}

	rez = append(rez, []int{start, end})

	return rez
}
