import bisect
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        best_sum = sum(nums[0:3])
        if best_sum > target:
            return best_sum

        best_sum = sum(nums[-3:])
        if best_sum < target:
            return best_sum

        size = len(nums)
        min_dist = 10 ** 10
        best_sum = 10 ** 10

        for n in range(size - 2):
            if not min_dist:
                return target

            for k in range(n + 1, size - 1):
                if (cur_sum := (nums[n] + nums[k] + nums[k + 1])) > target or k + 1 == size - 1:
                    if min_dist > (new_dist := abs(cur_sum - target)):
                        min_dist = new_dist
                        best_sum = cur_sum

                    if k == n + 1:
                        return best_sum

                    break

                last = target - (nums[n] + nums[k])
                pos = bisect.bisect_left(nums, last, k + 2)
                if pos == size:
                    if min_dist > (new_dist := last - nums[size - 1]):
                        min_dist = new_dist
                        best_sum = nums[n] + nums[k] + nums[size - 1]

                    continue

                if delta := (nums[pos] - last):
                    return target

                min_dist = min(min_dist, delta)

                if pos != k + 2:
                    if min_dist > (new_dist := last - nums[pos - 1]):
                        min_dist = new_dist
                        best_sum = nums[n] + nums[k] + nums[pos - 1]

                    min_dist = min(min_dist, last - nums[pos - 1])

        return best_sum
