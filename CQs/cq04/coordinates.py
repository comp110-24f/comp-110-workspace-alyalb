"""Importing practice"""

__author__ = "730655780"


def get_coords(xs: str, ys: str) -> None:
    index_x: int = 0
    while index_x < len(xs):
        index_y: int = 0
        while index_y < len(ys):
            print(f"({xs[index_x]},{ys[index_y]})")
            index_y += 1
        index_x += 1
