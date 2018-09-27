characters = []
for i in range(256):
    characters.append(False)


def string_has_unique_characters_with_array(string: str):
    for character in string:
        if characters[int(ord(character))]:
            return False
        else:
            characters[int(ord(character))] = True
    return True


def string_has_unique_characters_without_array(string: str):
    string = list(string)
    string.sort()
    for index in range(1, len(string)):
        if string[index] == string[index - 1]:
            return False
    return True


def main():
    assert string_has_unique_characters_with_array('abcde') is True
    assert string_has_unique_characters_with_array('abcdd') is False
    assert string_has_unique_characters_without_array('abcde') is True
    assert string_has_unique_characters_without_array('abcdd') is False


if __name__ == '__main__':
    main()
