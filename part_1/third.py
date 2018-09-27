def removed_duplicates(string: str) -> str:
    string = list(string)
    cnt, first = 0, 0
    for c1 in range(len(string)):
        first = c1
        for c2 in range(c1 + 1, len(string)):
            if string[c1] == string[c2]:
                cnt += 1
                continue
            else:
                first += 1
                string[first] = string[c2]
    return string[:len(string) - cnt]


def main():
    print(removed_duplicates('abcdee'))


if __name__ == '__main__':
    main()
