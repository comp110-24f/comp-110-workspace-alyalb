"""Practicing conditionals"""


def less_than_10(num: int) -> None:
    """Tell us if num < 10"""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


# less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off"""
    if alarm:
        return "Wake up!"
    else:
        return "Keep sleeping!"


def check_first_letter(word: str, letter: str) -> str:
    """Checks if a letter is the first character of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


# print(check_first_letter(word="happy", letter="s"))

"""weather practice with conditionals"""


def get_weather_report() -> str:
    """weather, no input type and return as string"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
