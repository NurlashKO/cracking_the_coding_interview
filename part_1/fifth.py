def replace_spaces(string: str) -> str:
    string = list(string)
    return string.replace(' ', '%20')


def main():
    print(replace_spaces('abcde kvlfd vfdvd'))


if __name__ == '__main__':
    main()
