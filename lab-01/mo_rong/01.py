from itertools import permutations


def liet_ke_hoan_vi():
    return list(permutations([1, 2, 3]))


def main():
    for hoan_vi in liet_ke_hoan_vi():
        print(hoan_vi)


if __name__ == "__main__":
    main()
