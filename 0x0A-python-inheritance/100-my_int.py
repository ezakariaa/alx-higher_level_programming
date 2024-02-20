#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    """Class that inherits from int with inverted == and != operators."""

    def __eq__(self, other):
        """Overrides the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the inequality operator."""
        return super().__eq__(other)
