import random


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    half = len(nums) >> 1

    return _merge(merge_sort(nums[:half]), merge_sort(nums[half:]))


def _merge(nums1, nums2):
    if not nums1:
        return nums2

    if not nums2:
        return nums1

    rez = []
    counter1 = -len(nums1)
    counter2 = -len(nums2)

    while counter1 and counter2:
        if nums1[counter1] < nums2[counter2]:
            rez.append(nums1[counter1])
            counter1 += 1
        else:
            rez.append(nums2[counter2])
            counter2 += 1

    if counter1:
        rez.extend(nums1[counter1:])
    else:
        rez.extend(nums2[counter2:])

    return rez


if __name__ == '__main__':
    seq = list(range(9, -1, -1))
    random.shuffle(seq)
    print(seq)
    seq = merge_sort(seq)
    print(seq)

    assert seq == list(range(10))
