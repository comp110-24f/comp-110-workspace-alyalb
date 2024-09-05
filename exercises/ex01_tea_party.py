"""Let's have a tea party"""

__author__: str = "730655780"


def main_planner(guests: int) -> None:
    """entry point of program"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print(
        "Cost: "
        + "$"
        + str(cost(treat_count=(treats(guests)), tea_count=(tea_bags(guests))))
    )


# calling function in reference to the number of guests


def tea_bags(people: int) -> int:
    """number of guests attending"""
    return people * 2


def treats(people: int) -> int:
    """number of treats per guest"""
    return int((tea_bags(people=people) * 1.5))


# work from inside out, set people to people because people is input&keyword argument
# at the same time
# call back to tea_bags


def cost(tea_count: int, treat_count: int) -> float:
    """the cost of treats and tea combined"""
    return tea_count * 0.5 + treat_count * 0.75


# no parentheses for simple math without calling other function

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending?")))
