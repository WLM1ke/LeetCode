package main

// https://leetcode.com/problems/two-sum/
func twoSum(nums []int, target int) []int {
	cache := make(map[int]int, len(nums))
	for pos, num := range nums {
		if pos2, ok := cache[target-num]; ok {
			return []int{pos, pos2}
		}

		cache[num] = pos
	}

	return nil
}
