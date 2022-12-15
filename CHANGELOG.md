# Changelog

<!-- ## [Unreleased] -->

### Added

- Now it is possible to pass arguments to a function which represents menu item.
- The menu class received `texts` parameters intended to be shown above items.
- Option to set a letter as a menu item trigger (instead of a digit).
- A menu is able to cut a text line if is doesn't fit in its box.
- The `ask_for_enter` function now returns the input string.

## 0.2.0 - 2022-08-20

### Added

- Added a new `title_and_value` function.
- The `enter_to_continue` function renamed to `ask_for_enter`.
- The `prompt_for_yes_or_no` function renamed to `ask_for_yes_or_no`.

## 0.1.0 - 2022-08-17

### Added

- A few classes intended to make a console menu.
- A function to clear a terminal.
- A function which prompts a user to enter `y` or `n`.
- A function kindly asking a user to press Enter to continue.