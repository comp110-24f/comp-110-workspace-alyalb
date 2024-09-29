"""practicing scope"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed"""
    copy: str = ""  # sets up empty str to copy values over
    index: int = 0  # local variables, exist within context of function
    while index < len(msg):
        if msg[index] != char:
            # or if not(msg[index])
            copy += msg[index]
            # copy = copy +msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    word: str = "yoyo"  # global variable, outside function

    # remove_chars ("football", "o") -> ftball
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))
