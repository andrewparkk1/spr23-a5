#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
# Checks that the program outputs "3" for an input of "1 + 2"
assert run("85 + 15").output == "100"
# Checks that the program outputs "8" for an input of "2 * 4"
assert run("9 * 2").output == "18"
# Checks that the program exists successfully (no error) for input "2 * 4"
assert run("4 / 2").output == "2"
# Checks that the program fails (correctly errors) for input "2 @ 3"
assert run("5 @ 3").exit_status != 0

print("All tests passed!")