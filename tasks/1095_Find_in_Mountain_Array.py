# https://leetcode.com/problems/find-in-mountain-array/
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        peak = self.find_peak(mountain_arr)

        if (rez := self.search_l(mountain_arr, peak, target)) != -1:
            return rez

        return self.search_r(mountain_arr, peak, target)

    def find_peak(self, mountain_arr: "MountainArray") -> int:
        l, r = 0, mountain_arr.length() - 1

        while l + 2 < r:
            mid = (l + r) // 2

            if (prev := mountain_arr.get(mid - 1)) < (cur := mountain_arr.get(mid)) and cur > mountain_arr.get(mid + 1):
                return mid
            elif prev < cur:
                l = mid
            else:
                r = mid

        return l + 1

    def search_l(self, mountain_arr: "MountainArray", peak: int, target: int):
        l, r = -1, peak

        while l + 1 < r:
            mid = (l + r) // 2

            if mountain_arr.get(mid) < target:
                l = mid
            else:
                r = mid

        if mountain_arr.get(r) != target:
            return -1

        return r

    def search_r(self, mountain_arr: "MountainArray", peak: int, target: int):
        l, r = peak, mountain_arr.length()

        while l + 1 < r:
            mid = (l + r) // 2

            if target > mountain_arr.get(mid):
                r = mid
            else:
                l = mid

        if mountain_arr.get(l) != target:
            return -1

        return l
