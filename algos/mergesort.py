import random


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    half = len(nums) >> 1

    return merge(merge_sort(nums[:half]), merge_sort(nums[half:]))


def merge(nums1: list[int], nums2: list[int]) -> list[int]:
    if not nums1:
        return nums2

    if not nums2:
        return nums1

    rez = []
    p1 = 0
    p2 = 0

    while True:
        if nums1[p1] < nums2[p2]:
            rez.append(nums1[p1])
            p1 += 1
        else:
            rez.append(nums2[p2])
            p2 += 1

        if p1 == len(nums1):
            rez += nums2[p2:]

            return rez

        if p2 == len(nums2):
            rez += nums1[p1:]

            return rez


if __name__ == '__main__':
    seq = list(range(9, -1, -1))
    random.shuffle(seq)
    print(seq)
    seq = merge_sort(seq)
    print(seq)

    assert seq == list(range(10))
