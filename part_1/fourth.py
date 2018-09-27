def are_anagrams(first: str, second: str) -> bool:
    return sorted(first) == sorted(second)


def main():
    assert print(are_anagrams('abcde', 'bcdae')) == 0


if __name__ == '__main__':
    main()
