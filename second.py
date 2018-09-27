def reversed_c_string(c_string: str) -> str:
    res = str()
    for c in range(len(c_string) - 1):
        res += c_string[len(c_string) - 1 - c - 1]
    res += '\0'
    return res


def main():
    print(reversed_c_string('abcde\0'))


if __name__ == '__main__':
    main()
