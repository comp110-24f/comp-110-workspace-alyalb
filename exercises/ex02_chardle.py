"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730655780"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return word


# when else, don't need to put != because guidelines listed in 'if'


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character")
        exit()
        return letter
        # when exit, skips any new lines, hence why 'return' is gray


def contains_char(input_word: str, input_letter: str) -> None:
    print("Searching for " + input_letter + " in " + input_word)
    if input_letter == input_word[0]:
        print(input_letter + " found at index 0")
    if input_letter == input_word[1]:
        print(input_letter + " found at index 1")
    if input_letter == input_word[2]:
        print(input_letter + " found at index 2")
    if input_letter == input_word[3]:
        print(input_letter + " found at index 3")
    if input_letter == input_word[4]:
        print(input_letter + " found at index 4")
    # checking instances begins here
    instance: int = 0
    if input_letter == input_word[0]:
        instance = instance + 1
    if input_letter == input_word[1]:
        instance += 1
    if input_letter == input_word[2]:
        instance += 1
    if input_letter == input_word[3]:
        instance += 1
    if input_letter == input_word[4]:
        instance += 1
    # each must be new if, otherwise if one instance proved true, would continue to
    # next line of code
    if instance > 1:
        print(
            str(instance) + " instances of " + input_letter + " found in " + input_word
        )
    elif instance == 1:
        print(
            str(instance) + " instance of " + input_letter + " found in " + input_word
        )
    else:
        print("No instances of " + input_letter + " found in " + input_word)
    # increase instance with each encounter, print statement based on returned instances


def main() -> None:
    contains_char(input_word(), input_letter())


# this releases no output

if __name__ == "__main__":
    main()
# but this does, reason TBA
