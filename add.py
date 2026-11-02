#!/usr/bin/env python3
"""Command-line addition tool: print the sum of two numbers.

Both integers and floating-point decimals are supported. Decimal arithmetic
is used so that common inputs keep exact results (for example ``0.1 + 0.2``
prints ``0.3`` instead of ``0.30000000000000004``).
"""

import argparse
import sys
from decimal import Decimal, InvalidOperation


def parse_number(raw):
    """Parse a command-line token as a finite decimal number."""
    try:
        value = Decimal(raw)
    except InvalidOperation:
        raise argparse.ArgumentTypeError(f"not a valid number: {raw!r}") from None
    if not value.is_finite():
        raise argparse.ArgumentTypeError(f"not a finite number: {raw!r}")
    return value


def add(a, b):
    """Return the sum of two Decimal numbers."""
    return a + b


def format_number(value):
    """Render a Decimal without exponent notation."""
    return format(value, "f")


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="add.py",
        description="Print the sum of two numbers (integers or decimals).",
    )
    parser.add_argument("a", type=parse_number, metavar="A", help="first number")
    parser.add_argument("b", type=parse_number, metavar="B", help="second number")
    args = parser.parse_args(argv)

    print(format_number(add(args.a, args.b)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
