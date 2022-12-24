from CharacterGenerator import CharacterGenerator


def print_hi():
    CharacterGenerator.generate_character(CharacterGenerator()).print_char_sheet()


if __name__ == '__main__':
    print_hi()
