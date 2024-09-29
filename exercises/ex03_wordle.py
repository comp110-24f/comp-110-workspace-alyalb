"""Creating a program similar to Wordle"""

__author__ = "730655780"


def input_guess(secret_word_len: int) -> str:
    while True:
        guess: str = input(f"Enter a {secret_word_len} character word: ")
        if len(guess) != secret_word_len:
            print(f"That wasn't {secret_word_len} chars! Try again: {guess}")
            # f string, background lesson
        else:
            return guess
        # with return in else block, will only return answer IF it is valid


def contains_char(secret_word: str, letter_guess: str) -> bool:
    """checks instances of letter in an inputted word regardless of word length by
    checking each index with loop"""
    assert len(letter_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if letter_guess == secret_word[index]:
            return True
        index += 1
    else:
        return False


def emojified(user_guess: str, secret_word: str) -> str:
    """returns emojis of varying colors to compare the guess to the secret word"""
    assert len(user_guess) == len(secret_word)
    index: int = 0
    copy: str = ""
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    while index < len(secret_word):
        if user_guess[index] == secret_word[index]:
            copy += green_box
        elif contains_char(secret_word=secret_word, letter_guess=user_guess[index]):
            copy += yellow_box
            # can just call contains_char to evaluate, don't need 'user_guess[index]
            # ==contains_char'
        else:
            copy += white_box
        index += 1
    return copy


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1

    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        emoji: str = emojified(guess, secret)
        print(emoji)
        # these must go within the while loop, guess prompts new guess and emoji
        # evaluates new string according to new guess
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            return
        # return statement forces exit. does not prompt for a guess after win
        else:
            turns += 1

    print("X/6 - Sorry, try again tomorrow!")
    # don't need if statement here since turns will already exceed 6 at this point of
    #  function


if __name__ == "__main__":
    main(secret="codes")
