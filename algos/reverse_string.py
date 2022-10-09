def reverse1(s: str) -> str:
    return s[::-1]


def reverse2(s: str) -> str:
    return "".join(reversed(s))


def reverse3(s: str) -> str:
    size = len(s)
    ls = list(s)
    for i in range(size // 2):
        ls[i], ls[size - 1 - i] = ls[size - 1 - i], ls[i]

    return "".join(ls)


if __name__ == '__main__':
    print(reverse1("abcde"))
    print(reverse2("abcde"))
    print(reverse3("abcde"))

    print(reverse1(""))
    print(reverse2(""))
    print(reverse3(""))

    print(reverse1("abcd"))
    print(reverse2("abcd"))
    print(reverse3("abcd"))
