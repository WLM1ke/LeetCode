package main

func searchInsert(nums []int, target int) int {
	start := 0
	end := len(nums)

	for start < end {
		mid := (start + end) / 2
		cur := nums[mid]

		if cur == target {
			return mid
		} else if target > cur {
			start = mid + 1
		} else {
			end = mid
		}

	}

	return start
}
