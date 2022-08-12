from menu_borders import *
from prompt import clear_screen


class Menu:
    _borders: MenuBorders = LightMenuBorders()
    _margin: str = " " * 2
    _prompt: str = ">> "
    _width: int = 75
    _items: list = []

    def __init__(self, items: list, borders: MenuBorders = None) -> None:

        self._items = items

        if borders is not None:
            self._borders = borders

    def _top_border(self) -> str:

        return "{left_margin}{left_vertical}{horizontal}{right_vertical}".format(
            left_margin=self._margin,
            left_vertical=self._borders.top_left_corner,
            horizontal=self._outer_horizontals(),
            right_vertical=self._borders.top_right_corner,
        )

    def _inner_text(self, text: str = "", tab_size: int = 4) -> str:

        content = "{tab}{text}".format(tab=" " * tab_size, text=text)

        content = "{content}{inner_right_margin}".format(
            content=content, inner_right_margin=" " * (self._width - len(content))
        )

        return "{left_margin}{vertical}{content}{vertical}".format(
            left_margin=self._margin,
            vertical=self._borders.outer_vertical,
            content=content,
        )

    def _inner_border(self) -> str:

        return "{left_margin}{left_vertical}{horizontal}{right_vertical}".format(
            left_margin=self._margin,
            left_vertical=self._borders.outer_vertical_inner_right,
            horizontal=self._inner_horizontals(),
            right_vertical=self._borders.outer_vertical_inner_left,
        )

    def _bottom_border(self) -> str:

        return "{left_margin}{left_vertical}{horizontal}{right_vertical}".format(
            left_margin=self._margin,
            left_vertical=self._borders.bottom_left_corner,
            right_vertical=self._borders.bottom_right_corner,
            horizontal=self._outer_horizontals(),
        )

    def _get_choices_to_print(self) -> list:

        result = []

        for index, item in enumerate(self._items):

            choice = "{number} - {title}".format(number=index + 1, title=item.__doc__)

            result.append(choice)

        return result

    def _outer_horizontals(self, number: int = None) -> str:

        if number is None:
            number = self._width

        return self._borders.outer_horizontal * number

    def _inner_horizontals(self, number: int = None) -> str:

        if number is None:
            number = self._width

        return self._borders.inner_horizontal * number

    def print(self) -> None:

        print(self._top_border())
        print(self._inner_text())

        for choice in self._get_choices_to_print():
            print(self._inner_text(text=choice))

        print(self._inner_text())
        print(self._bottom_border())

        print(self._prompt, end="")

    def choose(self) -> object:

        choice = 0
        method = None

        while choice < 1 or choice > len(self._items):

            clear_screen()

            self.print()

            choice = input()

            if choice.isdigit():

                choice = int(choice)

                method = self._items[choice - 1]
                method()

                break

            else:
                choice = 0

        return method


class LM(Menu):

    def print(self) -> None:

        print(self._top_border())
        print(self._inner_text("TITLE"))
        print(self._inner_border())
        print(self._inner_text())

        for choice in self._get_choices_to_print():
            print(self._inner_text(text=choice))

        print(self._inner_text())
        print(self._bottom_border())

        print(self._prompt, end="")


def do_1():
    """Start New Fast"""
    print("i1")


def do_2():
    """Fasts Browser"""
    print("i2")


def do_3():
    """Statistics"""
    print("i3")


def do_4():
    """Exit"""
    print("i4")


menu = LM([do_1, do_2, do_3, do_4], LightMenuBorders())
menu.print()
print()

menu = LM([do_1, do_2, do_3, do_4], AsciiMenuBorders())
menu.print()
print()

menu = LM([do_1, do_2, do_3, do_4], DoubleLineBorderStyle())
menu.print()
print()


