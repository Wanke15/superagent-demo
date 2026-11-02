"""Automated tests for add.py.

Run from the repository root with::

    python -m unittest -v
"""

import subprocess
import sys
import unittest
from decimal import Decimal
from pathlib import Path

import add

ADD_SCRIPT = Path(__file__).with_name("add.py")


def run_cli(*args):
    """Run add.py as a subprocess and return the completed process."""
    return subprocess.run(
        [sys.executable, str(ADD_SCRIPT), *args],
        capture_output=True,
        text=True,
        check=False,
    )


class AddFunctionTests(unittest.TestCase):
    """Unit tests for the add() helper."""

    def test_adds_integers(self):
        self.assertEqual(add.add(Decimal("2"), Decimal("3")), Decimal("5"))

    def test_adds_decimals_without_binary_artifacts(self):
        self.assertEqual(add.add(Decimal("0.1"), Decimal("0.2")), Decimal("0.3"))

    def test_adds_negative_numbers(self):
        self.assertEqual(add.add(Decimal("-2.5"), Decimal("1")), Decimal("-1.5"))


class AddCliTests(unittest.TestCase):
    """End-to-end tests for the command-line interface."""

    def assert_cli_output(self, args, expected):
        result = run_cli(*args)
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertEqual(result.stdout.strip(), expected)

    def test_integers(self):
        self.assert_cli_output(["2", "3"], "5")

    def test_floats(self):
        self.assert_cli_output(["1.5", "2.25"], "3.75")

    def test_mixed_integer_and_float(self):
        self.assert_cli_output(["1", "0.5"], "1.5")

    def test_negative_operands(self):
        self.assert_cli_output(["-4", "1.5"], "-2.5")

    def test_large_integers_are_exact(self):
        self.assert_cli_output(
            ["12345678901234567890", "1"], "12345678901234567891"
        )

    def test_invalid_number_is_rejected(self):
        result = run_cli("abc", "1")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("abc", result.stderr)

    def test_missing_operand_is_rejected(self):
        result = run_cli("1")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("usage", result.stderr.lower())

    def test_help_flag(self):
        result = run_cli("--help")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("usage", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
