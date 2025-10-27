"""Simple palindrome checker script.

Usage:
  - Run interactively: python test1.py
  - Pass text as arguments: python test1.py "A man, a plan, a canal: Panama"
  - Run quick self-tests: python test1.py --test

The checker ignores non-alphanumeric characters and is case-insensitive.
"""

import re
import sys
from typing import Iterable


def is_palindrome(s: str) -> bool:
	"""Return True if string s is a palindrome.

	The function normalizes the input by removing any non-alphanumeric
	characters and comparing in lowercase.

	Examples:
		is_palindrome('A man, a plan, a canal: Panama') -> True
		is_palindrome('hello') -> False
	"""
	filtered = re.sub(r'[^A-Za-z0-9]', '', s).lower()
	return filtered == filtered[::-1]


def check_lines(lines: Iterable[str]) -> None:
	"""Check each line and print whether it's a palindrome."""
	for line in lines:
		line = line.rstrip('\n')
		if not line:
			continue
		print(f"{line!r} -> {'Palindrome' if is_palindrome(line) else 'Not a palindrome'}")


def _run_self_tests() -> None:
	tests = {
		"": True,  # empty string is a palindrome
		"a": True,
		"Aa": True,
		"racecar": True,
		"A man, a plan, a canal: Panama": True,
		"No 'x' in Nixon": True,
		"hello": False,
		"ab": False,
	}
	for inp, expected in tests.items():
		got = is_palindrome(inp)
		assert got == expected, f"is_palindrome({inp!r}) -> {got}, expected {expected}"
	print("All self-tests passed.")


def main(argv: list[str] | None = None) -> int:
	argv = list(argv or sys.argv[1:])
	if not argv:
		# interactive mode: prompt the user
		try:
			user = input("Enter text to check palindrome (or Ctrl-D to exit): ")
		except EOFError:
			return 0
		if not user:
			print("No input provided.")
			return 0
		print("Palindrome" if is_palindrome(user) else "Not a palindrome")
		return 0

	if argv and argv[0] in ("--test", "-t", "self-test"):
		_run_self_tests()
		return 0

	# Treat remaining args as the text to check (join them)
	text = " ".join(argv)
	print("Palindrome" if is_palindrome(text) else "Not a palindrome")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())

