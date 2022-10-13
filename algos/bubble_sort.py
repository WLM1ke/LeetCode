import random


def bubble_sort(seq):
    for i in range(1, len(seq)):
        changed = False
        for j in range(len(seq) - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                changed = True

        if not changed:
            return


if __name__ == '__main__':
    seq = list(range(9, -1, -1))
    random.shuffle(seq)
    print(seq)
    bubble_sort(seq)
    print(seq)

    assert seq == list(range(10))
