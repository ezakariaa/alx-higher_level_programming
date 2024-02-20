#!/usr/bin/python3
""" class inheriting from the built-in list class. """


class MyList(list):
"""Class inheriting from the built-in list."""
	def print_sorted(self):
	"""Prints sorted list in ascending order."""
	print(sorted(self.copy()))
