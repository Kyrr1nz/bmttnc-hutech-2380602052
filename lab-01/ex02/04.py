def tim_cac_so():
    return [so for so in range(2000, 3201) if so % 7 == 0 and so % 5 != 0]


def main():
    print(",".join(map(str, tim_cac_so())))


if __name__ == "__main__":
    main()
