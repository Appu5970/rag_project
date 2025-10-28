"""Generate a centered pyramid pattern.

Usage examples:
  python pyramid.py 4
  python pyramid.py 5 '#'
  python pyramid.py --test

The script prints a centered pyramid of the given height. Non-positive
heights are treated as no output.
"""

import sys
from typing import List, Iterable


def generate_pyramid_lines(height: int, char: str = '*') -> List[str]:
	"""Return a list of lines representing a centered pyramid.

	Each level i (1..height) has (2*i - 1) characters 'char' centered with spaces.
	"""
	if height <= 0:
		return []
	lines: List[str] = []
	for i in range(1, height + 1):
		spaces = height - i
		stars = 2 * i - 1
		lines.append(' ' * spaces + char * stars)
	return lines


def print_pyramid(height: int, char: str = '*') -> None:
	for line in generate_pyramid_lines(height, char):
		print(line)


def _run_self_tests() -> None:
	# Basic shape tests
	assert generate_pyramid_lines(0) == []
	assert generate_pyramid_lines(1) == ['*']
	assert generate_pyramid_lines(2) == [' *', '***']
	assert generate_pyramid_lines(3) == ['  *', ' ***', '*****']
	# custom char
	assert generate_pyramid_lines(3, '#') == ['  #', ' ###', '#####']
	# ensure join and printing doesn't crash
	for h in range(1, 6):
		lines = generate_pyramid_lines(h)
		assert len(lines) == h

	print("pyramid.py: self-tests passed")


def main(argv: list[str] | None = None) -> int:
	argv = list(argv or sys.argv[1:])
	if not argv:
		# interactive prompt
		try:
			s = input("Enter pyramid height (integer): ")
		except EOFError:
			return 0
		if not s.strip():
			print("No height provided.")
			return 0
		argv = [s]

	if argv[0] in ("--test", "-t"):
		_run_self
		_tests()
		return 0

	# parse height
	try:
		height = int(argv[0])
	except ValueError:
		print(f"Invalid height: {argv[0]!r}. Must be an integer.")
		return 2

	char = argv[1] if len(argv) > 1 else '*'
	if len(char) != 1:
		print("Character should be a single character. Using first character.")
		char = char[0] if char else '*'

	print_pyramid(height, char)
	return 0


if __name__ == '__main__':
	raise SystemExit(main())

