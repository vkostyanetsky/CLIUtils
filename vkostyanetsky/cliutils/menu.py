"""
A few classes intended to make a simple console menu which are easily to override.
"""

from vkostyanetsky.cliutils import prompt


class MenuBorders:
    """
    Class stores Unicode drawing characters to draw a menu.
    """

    @property
    def top_left_corner(self) -> str:
        """
        The character a top left corner of the menu.
        """
        return "\u250C"  # ┌

    @property
    def top_right_corner(self) -> str:
        """
        The character a top right corner of the menu.
        """
        return "\u2510"  # ┐

    @property
    def bottom_left_corner(self) -> str:
        """
        The character an outer, bottom left corner of the menu.
        """
        return "\u2514"  # └

    @property
    def bottom_right_corner(self) -> str:
        """
        The character an outer, bottom right corner of the menu.
        """
        return "\u2518"  # ┘

    @property
    def inner_horizontal(self) -> str:
        """
        The character for inner horizontal section lines
        (inside the menu box).
        """
        return "\u2500"  # ─

    @property
    def outer_horizontal(self) -> str:
        """
        The character for outer horizontal lines
        (the top and bottom lines of the menu).
        """
        return "\u2500"  # ─

    @property
    def outer_vertical(self) -> str:
        """
        The character for an outer vertical line of the menu
        (the left and right sides of the menu).
        """
        return "\u2502"  # │

    @property
    def outer_vertical_inner_right(self) -> str:
        """
        The character for an outer vertical line,
        with a protruding inner line to the right.
        """
        return "\u251C"  # ├

    @property
    def outer_vertical_inner_left(self) -> str:
        """
        The character for an outer vertical line,
        with a protruding inner line to the left.
        """
        return "\u2524"  # ┤


class Menu:
    """
    A class that displays a menu and allows the user to select an option.
    """

    _texts: list[str]
    _items: list

    @property
    def _left_margin(self) -> str:
        """
        A number of spaces from the left side of the screen to the menu.
        """
        return " " * 2

    @property
    def _borders(self) -> MenuBorders:
        """
        A MenuBorders() class instance with characters to draw menu borders.
        """
        return MenuBorders()

    @property
    def _prompt(self) -> str:
        """
        A string with prompt. Usually being draw right below the menu.
        """
        return ">> "

    @property
    def _width(self) -> int:
        """
        A menu box width.
        """
        return 75

    @property
    def _plug(self) -> str:
        """
        A small piece of text to show if a line doesn't fit instead of a cut part.
        """
        return " (...)"

    def __init__(self, texts: list[str] | None = None):
        if texts is None:
            texts = []

        self._texts = texts
        self._items = []

    def _top_border(self) -> str:
        """
        Returns the top border with corners at the ends.
        """
        left_margin = self._left_margin
        left_border = self._borders.top_left_corner
        horizontals = self._outer_horizontals()
        right_border = self._borders.top_right_corner

        return f"{left_margin}{left_border}{horizontals}{right_border}"

    def _empty_line(self) -> str:
        return self._text_line("")

    def _text_line(self, text: str, tab_size: int = 4) -> str:
        """
        Returns the text with verticals at the ends.
        """
        left_margin = self._left_margin
        padding = " " * tab_size
        border = self._borders.outer_vertical

        right_space_length = self._width - len(text) - tab_size * 2
        right_space = " " * right_space_length

        if right_space_length < 0:
            text_index = right_space_length - len(self._plug)
            text = f"{text[0:text_index]}{self._plug}"

        return f"{left_margin}{border}{padding}{text}{right_space}{padding}{border}"

    def _inner_border(self) -> str:
        """
        Returns the inner border with verticals at the ends.
        """
        left_margin = self._left_margin
        left_border = self._borders.outer_vertical_inner_right
        horizontals = self._inner_horizontals()
        right_border = self._borders.outer_vertical_inner_left

        return f"{left_margin}{left_border}{horizontals}{right_border}"

    def _bottom_border(self) -> str:
        """
        Returns the bottom border with corners at the ends.
        """
        left_margin = self._left_margin
        left_border = self._borders.bottom_left_corner
        horizontals = self._inner_horizontals()
        right_border = self._borders.bottom_right_corner

        return f"{left_margin}{left_border}{horizontals}{right_border}"

    def _get_choices_to_print(self) -> list:
        """
        Returns the numerated list of strings for possible choices.
        """
        result = []

        for _, item in enumerate(self._items):
            choice = (
                f"{item['character']} - {item['title']}"
                if item["character"] is not None
                else item["title"]
            )
            result.append(choice)

        return result

    def _outer_horizontals(self, number: int = None) -> str:
        """
        Returns an outer horizontal line with a specified length that can be used
        as a top border or a bottom border.
        """
        if number is None:
            number = self._width

        return self._borders.outer_horizontal * number

    def _inner_horizontals(self, number: int = None) -> str:
        """
        Returns an inner horizontal line with a specified length that can be used
        as a bottom border.
        """
        if number is None:
            number = self._width

        return self._borders.inner_horizontal * number

    @staticmethod
    def get_item(title: str) -> dict:
        """
        Returns template for a new menu item.
        """

        return {
            "title": title,
            "method": None,
            "params": None,
            "character": None,
        }

    def add_item_separator(self, title: str = "") -> None:
        """
        Add a menu items separator (an empty line).
        """

        item = self.get_item(title)
        self._items.append(item)

    def add_item(
        self, title: str, method, params=None, character: str | None = None
    ) -> None:
        """
        Adds a new menu item.
        """

        if character is None:
            character = str(
                len([item for item in self._items if item["character"] is not None]) + 1
            )

        item = self.get_item(title)

        item["method"] = method
        item["params"] = params
        item["character"] = character

        self._items.append(item)

    def print(self) -> None:
        """
        Draws the menu.
        """
        print(self._top_border())

        if self._texts is not None:
            for text in self._texts:
                text_lines = text.split("\n")
                for text_line in text_lines:
                    print(self._text_line(text_line, 2))
                print(self._inner_border())

        print(self._empty_line())

        for choice in self._get_choices_to_print():
            print(self._text_line(text=choice))

        print(self._empty_line())
        print(self._bottom_border())

        print(self._prompt, end="")

    def choose(self) -> object:
        """
        Draws a menu an offers a user to choose from the provided options.
        Redraws the menu if a selected option is inappropriate.
        """
        choice = ""
        method = None

        while choice == "":
            prompt.clear_terminal()

            self.print()

            choice = input().strip()

            menu_items = list(
                filter(
                    lambda menu_item_1: menu_item_1["character"] is not None
                    and menu_item_1["character"].upper() == choice.upper(),
                    self._items,
                )
            )
            menu_item = menu_items[0] if menu_items else None

            if menu_item is not None:
                prompt.clear_terminal()

                method = menu_item["method"]
                params = menu_item["params"]

                if params is None:
                    method()
                else:
                    method(params)

                break

            choice = ""
            continue

        return method
