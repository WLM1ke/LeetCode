import random


def quick_sort(seq: list[int]) -> None:
    _helper(seq, 0, len(seq) - 1)


def _helper(seq: list[int], left: int, right: int) -> None:
    if left >= right:
        return

    pivot = seq[right]
    pointer = left

    for i in range(left, right + 1):
        if seq[i] <= pivot:
            seq[pointer], seq[i] = seq[i], seq[pointer]
            pointer += 1

    _helper(seq, left, pointer - 2)
    _helper(seq, pointer, right)


if __name__ == '__main__':
    seq = list(range(9, -1, -1))
    random.shuffle(seq)
    print(seq)
    quick_sort(seq)
    print(seq)

    assert seq == list(range(10))
