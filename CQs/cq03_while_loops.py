__author__ = "730655780"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase) - 1:
        if phrase[index] == search_char:
            count += 1
        index = index + 1
    return count


# make memory diagram to see what is happening here!
