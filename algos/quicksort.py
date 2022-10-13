import random


def quick_sort(nums: list[int]) -> None:
    helper(nums, 0, len(nums) - 1)


def helper(nums: list[int], left: int, right: int) -> None:
    if left >= right:
        return

    pivot = nums[right]

    pointer = left

    for i in range(left, right):
        if nums[i] < pivot:
            nums[pointer], nums[i] = nums[i], nums[pointer]
            pointer += 1

    nums[pointer], nums[right] = nums[right], nums[pointer]

    helper(nums, left, pointer - 1)
    helper(nums, pointer + 1, right)


if __name__ == '__main__':
    seq = list(range(9, -1, -1))
    random.shuffle(seq)
    print(seq)
    quick_sort(seq)
    print(seq)

    assert seq == list(range(10))
